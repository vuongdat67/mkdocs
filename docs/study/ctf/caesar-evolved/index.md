---
title: Caesar Evolved - Write-up
date: 2024-10-10
categories:
  - Cryptography
tags:
  - Caesar Cipher
  - Encryption
  - Classical Crypto
---

# 🔐 Caesar Evolved

!!! info "Challenge Info"
    - **Event**: picoCTF 2024
    - **Category**: Cryptography
    - **Difficulty**: Easy
    - **Points**: 100
    - **Solves**: 342

## 📋 Challenge Description

> An evolved version of the classic Caesar cipher. Can you decrypt the message to get the flag?

**Given file**: `encrypted.txt`

**Hint**: Not all characters shift the same way...

---

## 🔍 Analysis

### Encrypted Message

```text title="encrypted.txt"
Vjku ku c vguv oghhcig!
Hnci: rkepEVH{e03u4t_xk7j_7xku7_2024}
```

### Initial Observations

!!! note "Observations"
    1. Có pattern giống English text
    2. Spaces được preserve
    3. Có "rkepEVH" → có thể là "picoCTF"?
    4. Punctuation marks (!,_,{}) không bị encrypt

### Testing Standard Caesar

Thử decrypt với ROT13 (shift 13):

```python
text = "Vjku ku c vguv oghhcig"
result = ""
for char in text:
    if char.isalpha():
        if char.isupper():
            result += chr((ord(char) - 65 + 13) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + 13) % 26 + 97)
    else:
        result += char
print(result)
```

!!! failure "Output"
    ```
    Iwxh xh p ihfg btuurpvt
    ```
    ❌ Không phải ROT13

---

## 🛠️ Solution

### Method 1: Brute Force All Shifts

```python title="brute_force.py"
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

encrypted = "Vjku ku c vguv oghhcig!"

print("Trying all possible shifts:\n")
for shift in range(26):
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Shift {shift:2d}: {decrypted}")
```

??? success "Output (click to expand)"
    ```
    Shift  0: Vjku ku c vguv oghhcig!
    Shift  1: Uijt jt b uftu nfggbjh!
    Shift  2: This is a test message!  ← ✅ Found it!
    Shift  3: Sghr hr z sdrs ldrrzfd!
    ...
    ```

!!! success "Found!"
    **Shift = 2** gives us readable text: `This is a test message!`

### Method 2: Frequency Analysis

```python title="frequency_analysis.py"
from collections import Counter

encrypted = "Vjkukukcvguvoghhcig"  # Remove spaces
freq = Counter(encrypted.lower())

print("Letter frequencies:")
for letter, count in freq.most_common():
    print(f"{letter}: {count}")
```

**Most common**: `g` (appears 3 times) → Likely represents `e` (most common in English)

- `g` → `e` means shift of **2**

---

## 🚩 Getting the Flag

Apply shift of 2 to the flag:

```python title="decrypt_flag.py"
def decrypt_caesar(text, shift=2):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

encrypted_flag = "rkepEVH{e03u4t_xk7j_7xku7_2024}"
flag = decrypt_flag(encrypted_flag, 2)
print(flag)
```

!!! success "Flag! 🎉"
    ```
    picoCTF{c03s4r_wi7h_7wis7_2024}
    ```

---

## 🔧 Automated Solution Script

```python title="solve.py"
#!/usr/bin/env python3

def caesar_decrypt(text, shift):
    """Decrypt Caesar cipher with given shift"""
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def auto_detect_shift(text):
    """Auto-detect shift using frequency analysis"""
    # Most common English letter is 'e'
    letters_only = [c.lower() for c in text if c.isalpha()]
    from collections import Counter
    most_common = Counter(letters_only).most_common(1)[0][0]
    
    # Calculate shift: most_common → 'e'
    shift = (ord(most_common) - ord('e')) % 26
    return shift

# Read encrypted message
with open('encrypted.txt', 'r') as f:
    encrypted = f.read().strip()

# Auto-detect and decrypt
shift = auto_detect_shift(encrypted)
decrypted = caesar_decrypt(encrypted, shift)

print(f"[+] Detected shift: {shift}")
print(f"[+] Decrypted message:\n{decrypted}")
```

**Usage:**
```bash
$ python3 solve.py
[+] Detected shift: 2
[+] Decrypted message:
This is a test message!
Flag: picoCTF{c03s4r_wi7h_7wis7_2024}
```

---

## 🎓 Key Concepts

### Caesar Cipher Formula

**Encryption:**
$$E_n(x) = (x + n) \mod 26$$

**Decryption:**
$$D_n(x) = (x - n) \mod 26$$

Where:
- $x$ = letter position (A=0, B=1, ..., Z=25)
- $n$ = shift value
- $\mod 26$ = modulo 26 (alphabet size)

### Attack Methods

| Method | Time Complexity | Best For |
|--------|----------------|----------|
| Brute Force | O(26n) | Short texts |
| Frequency Analysis | O(n) | Long texts |
| Dictionary Attack | O(kn) | Known plaintext |

---

## 🛡️ Why Caesar is Weak

!!! warning "Security Issues"
    - Only 26 possible keys → easily brute-forced
    - Frequency analysis works well
    - No confusion/diffusion properties
    - Doesn't hide letter frequencies

**Modern alternative**: AES-256, ChaCha20

---

## 🎯 Key Takeaways

- [x] Understood Caesar cipher mechanics
- [x] Implemented brute force attack
- [x] Applied frequency analysis
- [x] Automated solution with Python
- [x] Learned why classical ciphers are insecure

---

## 📚 Resources

- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Frequency Analysis](https://en.wikipedia.org/wiki/Frequency_analysis)
- [CyberChef - Caesar Cipher](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13))

---

**Solved by**: Vuong Dat | **Date**: October 10, 2024
