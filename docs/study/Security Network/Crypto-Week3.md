# NT140 - Network Security: Cryptography


## 1. Tổng quan về Cryptography

### Cryptography có thể làm gì?

Mật mã học (Cryptography) là khoa học về việc bảo vệ thông tin thông qua các kỹ thuật mã hóa. Nó giúp:

- 🔒 **Bảo mật nội dung** (Confidentiality)
- ✅ **Đảm bảo tính toàn vẹn** (Integrity)
- 🔑 **Xác thực người dùng** (Authentication)
- 🚫 **Chống chối bỏ** (Non-repudiation)

### Nguyên tắc thiết kế mở (Kerckhoff's Principle)

> "Phương pháp mã hóa không cần phải bí mật, và có thể rơi vào tay kẻ thù mà không gây bất tiện."

**Ý nghĩa hiện đại:**
- Tất cả thuật toán phải được công khai
- "Security through obscurity" (bảo mật qua che giấu) hầu như không bao giờ hiệu quả
- Bảo mật phụ thuộc vào **độ mạnh của thuật toán** và **tính bí mật của khóa**

---

## 2. CIA Triad - Ba mục tiêu bảo mật

### 🔐 Confidentiality (Tính bảo mật)
- Tránh việc tiết lộ thông tin không được phép
- Chỉ người có quyền mới được xem thông tin

### ✔️ Integrity (Tính toàn vẹn)
- Tránh việc chỉnh sửa thông tin không được phép
- Đảm bảo dữ liệu không bị thay đổi

### ⚡ Availability (Tính khả dụng)
- Đảm bảo thông tin và hệ thống sẵn sàng khi cần
- Không thể giải quyết chỉ bằng mã hóa thông tin

---

## 3. Threat Model - Mô hình đe dọa

### Kẻ tấn công biết gì?
- ✅ Thuật toán mã hóa (công khai)
- ✅ Hành vi người dùng thông thường
- ✅ Ngôn ngữ của tin nhắn (ví dụ: tiếng Anh)
- ✅ Các cụm từ phổ biến (email headers, chữ ký...)

### Kẻ tấn công có thể làm gì?
- **Passive attack**: Nghe lén nội dung giao tiếp
- **Active attack**: Can thiệp, chỉnh sửa nội dung
- **Computing power**: Sức mạnh tính toán (giới hạn bởi thời gian đa thức)

### Điều bí mật duy nhất
**🔑 KHÓA (KEY) phải được giữ bí mật!**

---

## 4. Mã hóa đối xứng (Symmetric Encryption)

### Đặc điểm
- Cùng một khóa để **mã hóa** và **giải mã** (hoặc khóa rất giống nhau)
- Còn gọi là **Secret-Key Ciphers**

### ⚡ Ưu điểm
- **Rất nhanh!** (5-10 Gbps với AES-NI)
- Phù hợp cho mã hóa dữ liệu lớn

### ⚠️ Nhược điểm
- **Quản lý khóa khó khăn**
- Cần chia sẻ khóa bí mật trước khi giao tiếp
- Làm sao gửi khóa an toàn cho người lạ?

---

### 4.1. Block Cipher - Mã khối

#### Khái niệm
- Mã hóa từng **khối dữ liệu cố định** (block size)
- Input phải đủ một block đầy đủ

#### Thông số thiết kế
- **Block size**: Số bit được mã hóa trong một lần
- **Key size**: Kích thước khóa (k-bit → |K| = 2^k khả năng)

---

### 4.2. AES - Advanced Encryption Standard

#### Thông tin chung
- 🏆 **Chuẩn mã hóa hiện đại nhất**
- Không có tấn công thực tế nào thành công trong 20 năm
- Được chấp thuận bảo vệ thông tin mật

#### Kích thước khóa
- **128-bit**: Cho thông tin SECRET
- **192-bit hoặc 256-bit**: Cho thông tin TOP SECRET

#### Hiệu suất
- Hoạt động trên đơn vị byte/word → hiệu quả trong phần mềm
- Có hướng dẫn CPU đặc biệt (Intel AES-NI): **>10 Gbps trên 1 core**
- Hardware đặc biệt: **30+ Gbps**

---

### 4.3. Block Cipher Modes - Chế độ mã khối

#### 🚫 ECB Mode (Electronic Codebook) - **KHÔNG NÊN DÙNG**

**Cách hoạt động:**
```
Cj = E(K, Pj) cho mỗi block j
```

**Vấn đề:**
- Không che giấu các khối lặp lại
- Chỉ dùng cho tin nhắn ngắn hơn 1 block
- **Không an toàn cho tin nhắn dài!**

---

#### ✅ CBC Mode (Cipher Block Chaining) - **AN TOÀN**

**Cách hoạt động:**
```
C1 = E(K, [P1 ⊕ IV])
Cj = E(K, [Pj ⊕ Cj-1]) với j=2...N
```

**Đặc điểm:**
- ✅ IV phải **ngẫu nhiên** (được truyền cùng ciphertext)
- ✅ Phá vỡ pattern lặp lại
- ✅ Thay đổi 1 block ảnh hưởng tất cả block sau
- ⚠️ Không thể song song hóa (parallelization)
- ⚠️ Cần padding cho block cuối

---

#### ⚡ CTR Mode (Counter) - **NHANH VÀ SONG SONG**

**Cách hoạt động:**
```
Cj = Pj ⊕ E(K, Counter + j)
```

**Đặc điểm:**
- ✅ **Hoàn toàn song song hóa được**
- ✅ Giống như XOR với "random noise"
- ✅ Tương tự One-Time Pad với pseudo-random pad
- ⚠️ **Malleable**: Kẻ tấn công có thể flip bits tùy ý
- ⚠️ Cần thêm integrity protection

---

#### 🔧 Padding Techniques

**Kỹ thuật 1 - Bit Padding:**
```
Luôn thêm bit '1', sau đó thêm '0' để đủ block
Ví dụ (8-bit blocks): 10111010 110 → 10111010 11010000
```

**Kỹ thuật 2 - PKCS#7 / PKCS#5:**
```
Đếm số byte cần padding (c), thêm c bytes có giá trị c
Ví dụ (32-bit blocks): 42 1a 49 c3 21 → 42 1a 49 c3 21 03 03 03
```

---

### 4.4. One-Time Pad (OTP)

#### Đặc điểm
- **Perfect confidentiality** (bảo mật hoàn hảo)
- Khóa phải dài bằng tin nhắn
- Mỗi khóa chỉ dùng một lần

#### ⚠️ Vấn đề
- 🔴 **Malleable cipher**: Kẻ tấn công có thể thay đổi ciphertext và dự đoán được thay đổi trong plaintext
- 🔴 Phân phối khóa cực kỳ khó khăn (khóa dài bằng tin nhắn!)
- 🔴 **Yếu về tính toàn vẹn** (integrity)

> ⚡ **Kết luận**: OTP có perfect confidentiality nhưng rất khó sử dụng và yếu về integrity.

---

## 5. Mã hóa bất đối xứng (Public-Key Cryptography)

### Tại sao cần Public-Key?

**Vấn đề với Symmetric:**
- Làm sao gửi thẻ tín dụng an toàn cho cửa hàng lần đầu?
- Chưa bao giờ giao tiếp → không có khóa chung!
- Giải pháp KDC (Key Distribution Center)? → Cần tin tưởng tuyệt đối!

---

### 5.1. Khái niệm cơ bản

#### Đặc điểm
- **Khóa khác nhau** để mã hóa và giải mã
- Còn gọi là **Asymmetric Ciphers**

#### Hai loại khóa
- **Public Key (PU)**: Công khai, ai cũng có thể dùng để mã hóa
- **Private Key (PR)**: Bí mật, chỉ chủ sở hữu có để giải mã

---

### 5.2. Ứng dụng

#### 🔐 Cho Confidentiality (Bảo mật)
```
Mã hóa bằng Public Key → Giải mã bằng Private Key
```
- Bất kỳ ai cũng có thể mã hóa tin nhắn gửi cho Bob
- Chỉ Bob (có Private Key) mới giải mã được

#### ✍️ Cho Integrity (Chữ ký số)
```
Ký bằng Private Key → Verify bằng Public Key
```
- Chỉ Alice (có Private Key) mới ký được
- Bất kỳ ai (có Public Key) đều verify được

---

### 5.3. Cơ sở toán học

#### Key Pair Generator
```
KPG(R) → (PU, PR)
```

**Yêu cầu:**
1. Tính toán hiệu quả (polynomial time)
2. D(PR, E(PU, M)) = M (giải mã hoạt động đúng)
3. Tính PR từ PU là **không khả thi về mặt tính toán**

**Ví dụ RSA:**
- R tạo ra 2 số nguyên tố lớn
- PU là tích của chúng
- PR là thông tin chỉ biết khi có phân tích thừa số

---

### 5.4. RSA Algorithm

#### Cơ sở toán học
- Dựa trên **độ khó của phân tích thừa số**
- Key size thông thường: **2048 bits**

#### Đặc điểm
- ✅ Có thể dùng cho cả mã hóa và chữ ký
- ⚠️ Chậm hơn symmetric nhiều
- ⚠️ Cần khóa lớn để an toàn

---

### 5.5. Diffie-Hellman Key Exchange

#### Mục đích
Hai bên chia sẻ một **khóa bí mật chung** qua kênh không an toàn

#### Cách hoạt động

**Tham số công khai:** p (số nguyên tố), g (primitive root của p)

**Alice:**
```
Private key: a (ngẫu nhiên từ {1...p-1})
Public key: A = g^a mod p
Gửi A cho Bob
Tính khóa chung: KA = B^a mod p = g^(ab) mod p
```

**Bob:**
```
Private key: b (ngẫu nhiên từ {1...p-1})
Public key: B = g^b mod p
Gửi B cho Alice
Tính khóa chung: KB = A^b mod p = g^(ab) mod p
```

**Kết quả:** KA = KB = g^(ab) mod p

---

#### 🔐 Bảo mật

**Eve biết:** g, p, A, B

**Để tìm khóa chung, Eve cần:**
- Tìm a = dlog_g,p(A), hoặc
- Tìm b = dlog_g,p(B)

→ **Phải giải bài toán Discrete Logarithm** (rất khó!)

---

### 5.6. Discrete Log Problem

#### Định nghĩa
Với số nguyên tố p, tồn tại primitive root g sao cho:
```
g^1, g^2, g^3, ..., g^(p-1) (mod p)
```
là tất cả các giá trị khác nhau từ 1 đến p-1.

#### Ví dụ
g=3 là primitive root của p=17:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|-----|
| 3^i mod 17 | 3 | 9 | 10 | 13 | 5 | 15 | 11 | 16 | 14 | 8 | 7 | 4 | 12 | 2 | 6 | 1 |

#### Độ khó
- f(i) = g^i mod p: **dễ tính** (modular powering)
- f^(-1)(x) = dlog(x): **khó tính** (discrete log)

---

### 5.7. Thuật toán Public-Key phổ biến

#### Mã hóa & Key Exchange

| Thuật toán | Cơ sở toán học | Độ khó | Key size |
|------------|----------------|--------|----------|
| **RSA** | Factoring | Semi-hard | 2048 bits |
| **El Gamal** | Discrete Log (mod p) | Semi-hard | 2048 bits |
| **EC ElGamal** | Discrete Log (EC) | Hard | 224 bits |
| **Diffie-Hellman** | Discrete Log (mod p) | Semi-hard | 2048 bits |
| **EC-DHE** | Discrete Log (EC) | Hard | 224 bits |

---

### 5.8. So sánh Key Size

**Độ an toàn tương đương:**

| Symmetric | FFC (RSA, DH) | ECC |
|-----------|---------------|-----|
| 80 bits | 1024 bits | 160 bits |
| 112 bits | 2048 bits | 224 bits |
| 128 bits | 3072 bits | 256 bits |
| 192 bits | 7680 bits | 384 bits |
| 256 bits | 15360 bits | 521 bits |

**→ ECC hiệu quả hơn nhiều về kích thước khóa!**

---

### 5.9. So sánh Symmetric vs Public-Key

| Tiêu chí | Symmetric | Public-Key |
|----------|-----------|------------|
| **Tốc độ** | ⚡⚡⚡ Rất nhanh | 🐌 Chậm (100-1000x) |
| **Quản lý khóa** | ❌ Khó (cần chia sẻ trước) | ✅ Dễ (giao tiếp với người lạ) |
| **Tấn công** | Brute-force | Math tricks |
| **Key size** | Nhỏ (128-256 bit) | Lớn (2048+ bit) |
| **Ứng dụng** | Mã hóa data lớn | Key exchange, chữ ký |

---

### 5.10. Hybrid Encryption - Giải pháp tối ưu

#### Ý tưởng
Kết hợp **ưu điểm của cả hai**:
1. Dùng **Public-Key** để mã hóa "session key" ngẫu nhiên
2. Dùng **Symmetric** với session key để mã hóa tin nhắn thực

#### Quy trình
```
[Public-Key Encryption]
    Receiver's Public Key + Random Session Key
    → Encrypted Session Key

[Symmetric Encryption]
    Session Key + Message (có thể rất lớn!)
    → Ciphertext
```

#### Ưu điểm
- ✅ Giao tiếp với người lạ (key management)
- ✅ Nhanh cho tin nhắn lớn
- ⚠️ Code phức tạp hơn (2 thuật toán)

---

## 6. Bảo vệ tính toàn vẹn (Integrity Protection)

### 6.1. Khái niệm

#### Authenticator/Tag
- Được tính từ message
- **Ngắn** (ví dụ: 20 bytes cho file 4GB)
- Nếu message hoặc tag bị thay đổi → không khớp

#### Ba phương pháp

| Phương pháp | Cần khóa? | Kiểm tra |
|-------------|-----------|----------|
| **Hash Function** | ❌ Không | Tính lại để verify |
| **MAC** | ✅ Shared secret | Tính lại để verify |
| **Digital Signature** | ✅ Keypair | Không tính lại được! |

---

### 6.2. Hash Functions - Hàm băm

#### Định nghĩa
```
H: {0,1}* → {0,1}^n
```
Ánh xạ từ chuỗi bit bất kỳ → chuỗi bit độ dài cố định

---

#### Tính chất mật mã học

**1. One-way (Preimage resistance)**
- Cho h, không tìm được x sao cho H(x) = h

**2. Weak collision resistance (Second preimage resistance)**
- Cho x, không tìm được y ≠ x sao cho H(x) = H(y)

**3. Strong collision resistance (Collision resistance)**
- Không tìm được bất kỳ x, y nào mà x ≠ y và H(x) = H(y)

---

#### Họ SHA (Secure Hash Algorithms)

| Thuật toán | Năm | Output size | Trạng thái |
|------------|-----|-------------|------------|
| **SHA-0** | 1993 | - | 🔴 Deprecated |
| **SHA-1** | 1995 | 160 bits | 🔴 Không dùng |
| **SHA-2** | 2002 | 224, 256, 384, 512 bits | ✅ An toàn |
| **SHA-3** | 2015 | 224, 256, 384, 512 bits | ✅ An toàn |
| **MD5** | - | 128 bits | 🔴 Không dùng |

**→ Nên dùng: SHA-256 hoặc SHA-3**

---

#### ⚠️ Vấn đề với Hash đơn thuần

**Kịch bản:**
```
Message: "Send army to X at 10:30am"
Hash: 7c91ad850b513
```

Kẻ tấn công có thể:
1. Thay đổi message
2. Tính hash mới
3. Thay cả message và hash

**→ Không an toàn nếu không có khóa bí mật!**

---

### 6.3. MAC (Message Authentication Code)

#### Định nghĩa
```
MAC(K, M) → tag
```
- K: Khóa bí mật (shared secret)
- M: Message
- tag: Authenticator

#### Đặc điểm
- ✅ Cả sender và receiver biết khóa K
- ✅ Chỉ ai có K mới tính được MAC
- ⚠️ **Không dùng H(K || M)** → dễ bị extension attack!

---

#### Thuật toán MAC phổ biến

**HMAC** (Hash-based MAC)
- Phổ biến nhất
- An toàn với SHA-256

**CMAC** (Cipher-based MAC)
- Dựa trên block cipher (AES)

**GCM** (Galois/Counter Mode)
- Kết hợp encryption + MAC

---

### 6.4. Digital Signatures - Chữ ký số

#### Đặc điểm

| | MAC | Digital Signature |
|---|-----|-------------------|
| **Khóa** | Shared secret | Public/Private keypair |
| **Ký** | Cả hai bên | Chỉ người có Private Key |
| **Verify** | Cả hai bên | Bất kỳ ai có Public Key |
| **Tốc độ** | ⚡ Nhanh | 🐌 Chậm |
| **Key mgmt** | ❌ Khó | ✅ Dễ |

---

#### Quy trình

**Ký:**
```
1. Hash message: h = H(M)
2. Sign hash: sig = Sign(PR, h)
3. Gửi (M, sig)
```

**Verify:**
```
1. Hash message: h = H(M)
2. Verify: Verify(PU, h, sig) → true/false
```

**→ Tại sao hash trước khi ký?**
- Tốc độ: Không chạy toàn bộ message qua hàm chậm
- An toàn: Collision resistance đảm bảo message/hash liên kết chặt

---

#### Thuật toán Digital Signature

| Thuật toán | Cơ sở toán học | Key size | Signature size |
|------------|----------------|----------|----------------|
| **RSA** | Factoring | 2048 bits | 2048 bits |
| **DSA** | Discrete Log (mod p) | 2048 bits | 448 bits |
| **EC-DSA** | Discrete Log (EC) | 224 bits | 448 bits |

**→ EC-DSA hiệu quả nhất!**

---

### 6.5. Vấn đề với Digital Signatures

#### Câu hỏi quan trọng
**Signature verification nói gì?**
- "Chỉ người có private key tương ứng mới tạo được chữ ký này"

**Bạn muốn nó nói gì?**
- "Alice đã ký cái này"

#### ⚠️ Vấn đề
**Làm sao biết public key đó thực sự là của Alice?**

→ Cần **Digital Certificates**!

---

## 7. Chứng chỉ số (Digital Certificates)

### 7.1. Mục đích

**Giải quyết bài toán:**
- Làm sao tin tưởng một public key thuộc về đúng người?
- Làm sao không bị tấn công Man-in-the-Middle?

---

### 7.2. Cấu trúc Certificate

```
Identity: Joe Smith
Public key: 9f66159c13e...
Expires: March 31, 2020
Signature: c9f9abffae98b...
```

**Thành phần:**
- Thông tin định danh (tên, tổ chức...)
- Public key
- Thời hạn hiệu lực
- **Chữ ký của Certificate Authority (CA)**

---

### 7.3. Certificate Authority (CA)

#### Vai trò
- **Trusted Third Party (TTP)**
- Xác minh định danh và khóa
- Ký certificate với private key của CA

#### Chicken-and-egg problem?
- Cần public key của CA để verify
- Giải pháp: Thay vì hàng triệu website → chỉ vài chục CA
- CA's public key được **cài sẵn** trong OS/browser

---

### 7.4. Chuỗi tin cậy (Chain of Trust)

```
Root CA
  ↓ signs
Intermediate CA
  ↓ signs
End-entity Certificate (website)
```

- Root CA tự ký (self-signed)
- Intermediate CA được Root CA ký
- Website certificate được Intermediate CA ký

---

## 8. Tóm tắt và So sánh

### 8.1. Các chức năng mật mã cơ bản

| Chức năng | Mục đích | Ví dụ | Ưu điểm |
|-----------|----------|-------|---------|
| **Symmetric Encryption** | Confidentiality | AES | ⚡ Nhanh |
| **Public-Key Encryption** | Confidentiality | RSA, ECC | 🔑 Linh hoạt |
| **Hash Functions** | Integrity | SHA-256 | ⚡ Nhanh, không cần khóa |
| **MAC** | Integrity | HMAC | ⚡ Nhanh, cần shared key |
| **Digital Signatures** | Integrity + Non-repudiation | RSA, DSA, EC-DSA | 🔑 Linh hoạt |
| **Certificates** | Trust | X.509 | 👤 Biết ai đang giao tiếp |

---

### 8.2. Khi nào dùng cái gì?

#### Confidentiality (Bảo mật)

**Symmetric (AES):**
- ✅ Cả hai bên đã có shared secret
- ✅ Cần mã hóa data lớn
- ✅ Cần tốc độ cao

**Public-Key (RSA/ECC):**
- ✅ Giao tiếp lần đầu (chưa có shared secret)
- ✅ Key exchange
- ⚠️ Không dùng trực tiếp cho data lớn

**Hybrid (Best practice):**
- ✅ PK để trao đổi session key
- ✅ Symmetric để mã hóa data

---

#### Integrity (Toàn vẹn)

**Hash Function:**
- ✅ Chỉ cần phát hiện thay đổi (không có kẻ tấn công chủ động)
- ✅ Checksum, file verification

**MAC:**
- ✅ Có shared secret
- ✅ Cần xác thực giữa hai bên tin tưởng
- ✅ Nhanh

**Digital Signature:**
- ✅ Cần chống chối bỏ (non-repudiation)
- ✅ Nhiều người verify
- ✅ Không có shared secret trước

---

### 8.3. Bảng cheat sheet

#### 🎯 Mục tiêu → Giải pháp

| Tôi muốn... | Dùng... |
|-------------|---------|
| Mã hóa file lớn nhanh | AES-256 (CBC/CTR) |
| Gửi tin nhắn bí mật cho người lạ | RSA hoặc Hybrid |
| Đảm bảo file không bị sửa | SHA-256 hash |
| Xác thực tin nhắn từ đối tác | HMAC-SHA256 |
| Ký tài liệu chính thức | RSA/EC-DSA signature |
| Trao đổi khóa an toàn | Diffie-Hellman / ECDHE |
| Tin tưởng public key | Certificate từ CA |

---

#### ⚠️ KHÔNG nên dùng

| ❌ Đừng dùng | ✅ Thay bằng | Lý do |
|-------------|-------------|-------|
| MD5 | SHA-256 | Collision attacks |
| SHA-1 | SHA-256/SHA-3 | Collision attacks |
| ECB mode | CBC/CTR | Không che giấu pattern |
| RSA < 2048 bit | RSA 2048+ | Dễ phá |
| H(K \|\| M) cho MAC | HMAC | Extension attack |
| OTP thực tế | AES-CTR + HMAC | Key distribution khó |

---

### 8.4. Độ mạnh khóa cần thiết (2025)

#### Khuyến nghị tối thiểu

| Loại | Thuật toán | Key size |
|------|------------|----------|
| **Symmetric** | AES | 128 bits |
| **Hash** | SHA-2 | 256 bits |
| **RSA** | RSA | 2048 bits |
| **DH** | Diffie-Hellman | 2048 bits |
| **ECC** | EC-DSA, ECDHE | 224 bits |

#### Khuyến nghị cho tương lai (5-10 năm)

| Loại | Key size |
|------|----------|
| **Symmetric** | 256 bits |
| **RSA/DH** | 3072 bits |
| **ECC** | 256 bits |

---

## 9. Ứng dụng thực tế

### 9.1. HTTPS/TLS - Bảo mật web

#### Quy trình TLS Handshake (đơn giản hóa)

```
1. Client Hello: Hỗ trợ cipher suites nào?
2. Server Hello: Chọn cipher suite
3. Server Certificate: Gửi certificate (chứa public key)
4. Client verify certificate: Kiểm tra chữ ký CA
5. Key Exchange: ECDHE để tạo session key
6. Finished: Bắt đầu dùng symmetric encryption (AES)
```

**Kết hợp:**
- ✅ Certificate → Trust (biết đang nói chuyện với ai)
- ✅ ECDHE → Key exchange (tạo shared secret)
- ✅ AES-GCM → Encryption + MAC (confidentiality + integrity)
- ✅ Digital signature → Authentication

---

### 9.2. SSH - Secure Shell

#### Thành phần
- **Host key**: RSA/ECDSA key của server
- **User authentication**: Password hoặc public key
- **Session encryption**: AES với key từ DH

#### Quy trình
```
1. Client kết nối server
2. Server gửi host public key
3. DH key exchange → session key
4. User authentication (password/key)
5. Encrypted session với AES
```

---

### 9.3. PGP/GPG - Email encryption

#### Tính năng
- Mã hóa email
- Ký email
- Web of trust (thay vì CA)

#### Quy trình gửi email mã hóa
```
1. Tạo random session key
2. Mã hóa email bằng AES + session key
3. Mã hóa session key bằng recipient's RSA public key
4. Ký toàn bộ bằng sender's private key
5. Gửi: encrypted_email + encrypted_session_key + signature
```

---

### 9.4. VPN - Virtual Private Network

#### IPsec
- **Authentication Header (AH)**: Integrity
- **Encapsulating Security Payload (ESP)**: Confidentiality + Integrity
- **IKE (Internet Key Exchange)**: Dùng DH để tạo keys

#### Quy trình
```
1. IKE Phase 1: Authenticate và tạo secure channel
2. IKE Phase 2: Negotiate cipher suites và keys
3. Data transfer: Encrypted với agreed cipher (AES)
```

---

## 10. Các tấn công phổ biến và phòng thủ

### 10.1. Brute Force Attack

#### Mô tả
Thử tất cả khóa có thể cho đến khi tìm được đúng

#### Độ phức tạp
- k-bit key → trung bình cần ½ × 2^k lần thử

#### Phòng thủ
- ✅ Dùng key đủ lớn (AES-256, RSA-2048)
- ✅ Rate limiting (giới hạn số lần thử)
- ✅ Key stretching (PBKDF2, bcrypt)

---

### 10.2. Man-in-the-Middle (MITM)

#### Mô tả
Kẻ tấn công đứng giữa hai bên giao tiếp

**Kịch bản:**
```
Alice → Eve → Bob
Alice nghĩ đang nói với Bob
Bob nghĩ đang nói với Alice
Thực tế cả hai đang nói với Eve!
```

#### Phòng thủ
- ✅ Dùng certificates để xác thực
- ✅ Certificate pinning
- ✅ Out-of-band verification

---

### 10.3. Replay Attack

#### Mô tả
Kẻ tấn công ghi lại message hợp lệ và gửi lại sau

**Ví dụ:**
```
Alice → Bank: "Transfer $100 to Bob" + signature
Eve ghi lại và gửi lại 10 lần
→ $1000 được chuyển!
```

#### Phòng thủ
- ✅ Timestamps trong message
- ✅ Nonce (number used once)
- ✅ Sequence numbers

---

### 10.4. Padding Oracle Attack

#### Mô tả
Tấn công vào implementation của padding trong CBC mode

#### Phòng thủ
- ✅ Dùng authenticated encryption (GCM)
- ✅ Constant-time operations
- ✅ Không leak thông tin về padding errors

---

### 10.5. Timing Attack

#### Mô tả
Phân tích thời gian xử lý để suy ra thông tin bí mật

**Ví dụ:**
```
if (password == stored_password)  // So sánh từng ký tự
    return true;

→ Thời gian khác nhau cho biết bao nhiêu ký tự đúng!
```

#### Phòng thủ
- ✅ Constant-time comparison
- ✅ Dùng cryptographic comparison functions

---

### 10.6. Collision Attack trên Hash

#### Mô tả
Tìm hai messages khác nhau có cùng hash

**Ví dụ với MD5/SHA-1:**
- Đã tìm được collision thực tế
- Có thể tạo hai PDFs khác nhau cùng hash

#### Phòng thủ
- ✅ Dùng SHA-256 hoặc SHA-3
- ❌ Không dùng MD5, SHA-1

---

### 10.7. Quantum Computing Threat

#### Mô tả
Máy tính lượng tử có thể phá:
- 🔴 RSA (Shor's algorithm)
- 🔴 ECC (Shor's algorithm)
- 🔴 Diffie-Hellman

#### Không phá được
- ✅ AES (với key lớn hơn: 256-bit)
- ✅ SHA-256/SHA-3

#### Phòng thủ tương lai
- Post-Quantum Cryptography (PQC)
- NIST đang chuẩn hóa các thuật toán mới

---

## 11. Best Practices - Thực hành tốt nhất

### 11.1. Chọn thuật toán

#### ✅ NÊN dùng (2025)
- **Symmetric**: AES-256
- **Hash**: SHA-256, SHA-3
- **Public-Key Encryption**: RSA-2048+, ECC (P-256)
- **Key Exchange**: ECDHE (Curve25519)
- **Signature**: EC-DSA, Ed25519
- **MAC**: HMAC-SHA256
- **Authenticated Encryption**: AES-GCM, ChaCha20-Poly1305

#### ❌ TRÁNH
- DES, 3DES, RC4
- MD5, SHA-1
- RSA < 2048 bit
- Custom crypto ("roll your own")

---

### 11.2. Quản lý khóa

#### Sinh khóa
- ✅ Dùng cryptographically secure random number generator
- ❌ Không dùng random() thông thường
- ❌ Không dùng timestamp, user input làm seed

#### Lưu trữ khóa
- ✅ Hardware Security Module (HSM) cho production
- ✅ Key derivation functions (PBKDF2, Argon2) cho passwords
- ✅ Encrypt keys at rest
- ❌ Không hardcode keys trong code
- ❌ Không lưu plaintext trong database

#### Phân phối khóa
- ✅ Dùng secure channels (TLS)
- ✅ Key rotation định kỳ
- ✅ Separate keys cho mỗi mục đích

---

### 11.3. Implementation

#### Nguyên tắc chung
- ✅ Dùng thư viện crypto uy tín (OpenSSL, libsodium, cryptography)
- ❌ **ĐỪNG tự implement crypto!**
- ✅ Update thư viện thường xuyên
- ✅ Follow security advisories

#### Chi tiết kỹ thuật
- ✅ Constant-time operations
- ✅ Clear sensitive data từ memory
- ✅ Use authenticated encryption (GCM mode)
- ✅ Random IV/nonce cho mỗi encryption

---

### 11.4. Testing & Validation

#### Checklist
- ✅ Test với vectors chuẩn
- ✅ Fuzz testing
- ✅ Penetration testing
- ✅ Code review bởi security experts
- ✅ Static analysis tools

---

## 12. Bài tập thực hành

### 12.1. Bài toán: Hệ thống chat an toàn

**Đề bài (từ đề thi):**

Bob muốn trò chuyện an toàn với Alice qua Internet. Eve (người yêu cũ) và Michael (bố Alice) cố theo dõi và ngăn cản. Thiết kế hệ thống đảm bảo:

1. **Confidentiality**: Nội dung có thể rất dài (tâm sự, hình ảnh, video). Cần mã hóa an toàn, nhanh, và giữ kín khóa.
2. **Integrity**: Tin nhắn phải từ người gửi thật, không bị chỉnh sửa hoặc mất mát.

---

#### 💡 Giải pháp đề xuất

**Phần 1: Confidentiality (Bảo mật)**

```
Sử dụng Hybrid Encryption:

1. Initialization (chỉ một lần):
   - Bob và Alice mỗi người tạo EC keypair (Curve25519)
   - Bob: (PU_Bob, PR_Bob)
   - Alice: (PU_Alice, PR_Alice)
   - Trao đổi public keys qua certificate hoặc verify out-of-band

2. Key Exchange (mỗi session):
   - Dùng ECDHE để tạo shared secret
   - Perfect Forward Secrecy: mỗi session một ephemeral key mới
   - Derive session key: K_session = KDF(ECDHE_secret)

3. Message Encryption (mỗi tin nhắn):
   - Encrypt với AES-256-GCM
   - Input: K_session, plaintext, random nonce
   - Output: ciphertext + authentication tag
```

**Tại sao chọn này?**
- ✅ **ECDHE**: Tạo shared secret mà không gửi qua mạng
- ✅ **AES-256**: Nhanh cho data lớn (video, hình ảnh)
- ✅ **GCM mode**: Vừa encrypt vừa authenticate
- ✅ **Perfect Forward Secrecy**: Nếu khóa bị lộ, tin cũ vẫn an toàn

---

**Phần 2: Integrity & Authentication (Toàn vẹn)**

```
Sử dụng Digital Signatures + MAC:

1. Mỗi tin nhắn:
   - Message M
   - Sign: sig = Sign(PR_sender, H(M))
   - MAC: tag = HMAC(K_session, M || sig)
   
2. Gửi: (M_encrypted, sig, tag)

3. Nhận và verify:
   - Decrypt: M = Decrypt(K_session, M_encrypted)
   - Verify MAC: HMAC(K_session, M || sig) == tag
   - Verify Signature: Verify(PU_sender, H(M), sig)
```

**Tại sao cần cả hai?**
- ✅ **Digital Signature**: Chứng minh người gửi (non-repudiation)
- ✅ **MAC**: Nhanh, phát hiện tampering ngay lập tức
- ✅ **Kết hợp**: Bảo vệ toàn diện

---

**Phần 3: Thông số cụ thể (2025)**

| Thành phần | Thuật toán | Key Size | Lý do |
|------------|------------|----------|-------|
| Key Exchange | ECDHE (Curve25519) | 256-bit | Nhanh, an toàn, PFS |
| Symmetric | AES-256-GCM | 256-bit | Nhanh nhất, authenticated |
| Hash | SHA-256 | 256-bit | Chuẩn, an toàn |
| Signature | Ed25519 | 256-bit | Nhanh hơn EC-DSA |
| MAC | HMAC-SHA256 | 256-bit | Chuẩn, an toàn |
| KDF | HKDF-SHA256 | - | Derive keys an toàn |

---

**Phần 4: Quy trình đầy đủ**

```
SETUP PHASE (chỉ một lần):
1. Bob và Alice mỗi người:
   - Tạo long-term keypair: (PU, PR)
   - Trao đổi và verify public keys

SESSION ESTABLISHMENT:
1. Bob tạo ephemeral keypair: (ePU_Bob, ePR_Bob)
2. Bob → Alice: ePU_Bob
3. Alice tạo ephemeral keypair: (ePU_Alice, ePR_Alice)
4. Alice → Bob: ePU_Alice
5. Cả hai tính: shared_secret = ECDHE(ePR_self, ePU_other)
6. Derive keys: 
   - K_encrypt = HKDF(shared_secret, "encryption")
   - K_mac = HKDF(shared_secret, "authentication")

SENDING MESSAGE:
1. Bob:
   - plaintext = "Will you marry me? ❤️" + image.jpg
   - nonce = random(96 bits)
   - ciphertext = AES-GCM-Encrypt(K_encrypt, nonce, plaintext)
   - sig = Ed25519-Sign(PR_Bob, SHA256(ciphertext))
   - tag = HMAC(K_mac, ciphertext || sig || nonce)
   - Send: (ciphertext, sig, nonce, tag)

RECEIVING MESSAGE:
1. Alice:
   - Verify tag: HMAC(K_mac, ciphertext || sig || nonce) == tag
   - Verify sig: Ed25519-Verify(PU_Bob, SHA256(ciphertext), sig)
   - Decrypt: plaintext = AES-GCM-Decrypt(K_encrypt, nonce, ciphertext)
   - Display: "Will you marry me? ❤️" [image]
```

---

**Phần 5: Bảo vệ chống các tấn công**

| Tấn công | Cách phòng thủ |
|----------|----------------|
| **Eavesdropping** (Eve nghe lén) | AES-256-GCM encryption |
| **MITM** (Michael đứng giữa) | Digital signatures + PU verification |
| **Replay** (gửi lại tin cũ) | Nonce + sequence number |
| **Tampering** (sửa tin nhắn) | HMAC + Digital signature |
| **Key compromise** | Perfect Forward Secrecy (ECDHE) |

---

### 12.2. Bài tập tự luyện

#### Câu 1: Phân tích an ninh
Một công ty dùng `hash = MD5(password)` để lưu mật khẩu. Liệt kê các vấn đề và đề xuất giải pháp.

<details>
<summary>💡 Gợi ý trả lời</summary>

**Vấn đề:**
1. MD5 đã bị phá (collision attack)
2. Không có salt → rainbow table attack
3. MD5 nhanh → brute force dễ dàng
4. Không có key stretching

**Giải pháp:**
```
hash = Argon2id(password, salt, iterations)
```
- Argon2id: Chống GPU/ASIC attacks
- Salt: Random 128-bit cho mỗi user
- Iterations: Điều chỉnh để mất ~100ms
</details>

---

#### Câu 2: Thiết kế giao thức
Thiết kế giao thức cho IoT devices (tài nguyên hạn chế) giao tiếp an toàn với cloud server.

<details>
<summary>💡 Gợi ý trả lời</summary>

**Yêu cầu:**
- Low power
- Limited CPU
- Small memory

**Giải pháp:**
1. **Symmetric crypto only**: AES-128-CCM
2. **Pre-shared keys**: Cài đặt trong factory
3. **Key derivation**: Derive session keys từ master key
4. **Lightweight protocol**: CoAP thay vì HTTPS
5. **Batching**: Gom nhiều messages để giảm overhead
</details>

---

#### Câu 3: So sánh
So sánh CBC và GCM mode. Khi nào dùng cái nào?

<details>
<summary>💡 Gợi ý trả lời</summary>

| Tiêu chí | CBC | GCM |
|----------|-----|-----|
| **Encryption** | ✅ Yes | ✅ Yes |
| **Authentication** | ❌ No (cần thêm MAC) | ✅ Built-in |
| **Parallelizable** | ❌ No | ✅ Yes |
| **Performance** | Chậm hơn | Nhanh hơn (có hardware) |
| **Complexity** | Phức tạp (2 operations) | Đơn giản (1 operation) |

**Dùng CBC khi:**
- Compatibility với hệ thống cũ
- Không có hardware support cho GCM

**Dùng GCM khi:**
- Cần authenticated encryption
- Performance quan trọng
- Có hardware support (AES-NI)
</details>

---

## 13. Resources - Tài liệu tham khảo

### 13.1. Sách và khóa học

**Sách:**
- 📕 "Cryptography and Network Security" - William Stallings
- 📕 "Applied Cryptography" - Bruce Schneier
- 📕 "Serious Cryptography" - Jean-Philippe Aumasson
- 📕 "The Code Book" - Simon Singh (dễ đọc cho người mới)

**Khóa học online:**
- 🎓 Coursera: "Cryptography I" - Dan Boneh (Stanford)
- 🎓 Crypto101 (cryptopals.com) - thực hành tấn công
- 🎓 Khan Academy: Cryptography

---

### 13.2. Tools và Libraries

**Libraries an toàn:**
- 🔧 **libsodium**: Dễ dùng, modern, cross-platform
- 🔧 **OpenSSL**: Chuẩn công nghiệp, đầy đủ tính năng
- 🔧 **cryptography** (Python): High-level, dễ dùng
- 🔧 **Bouncy Castle**: Java/C# crypto library

**Tools:**
- 🛠️ **OpenSSL CLI**: Test và debug
- 🛠️ **Wireshark**: Phân tích traffic (TLS)
- 🛠️ **hashcat**: Password cracking (test strength)
- 🛠️ **John the Ripper**: Password auditing

---

### 13.3. Standards và Documentation

**NIST Publications:**
- 📄 NIST SP 800-57: Key Management Recommendations
- 📄 NIST SP 800-175B: Guideline for Using Crypto Standards
- 📄 FIPS 140-2/3: Security Requirements for Crypto Modules

**RFCs quan trọng:**
- 📄 RFC 5246: TLS 1.2
- 📄 RFC 8446: TLS 1.3
- 📄 RFC 7539: ChaCha20 and Poly1305
- 📄 RFC 8032: EdDSA (Ed25519)

---

### 13.4. Websites và Communities

**News và Updates:**
- 🌐 [Schneier on Security](https://www.schneier.com)
- 🌐 [Cryptography Stack Exchange](https://crypto.stackexchange.com)
- 🌐 [The Hacker News](https://thehackernews.com)
- 🌐 [DarkReading](https://www.darkreading.com)

**Research:**
- 🌐 [IACR ePrint Archive](https://eprint.iacr.org)
- 🌐 [IEEE Security & Privacy](https://www.ieee-security.org)

---

## 14. Checklist - Tự đánh giá kiến thức

### ✅ Kiến thức cơ bản

- [ ] Hiểu CIA triad và vai trò của cryptography
- [ ] Biết sự khác biệt symmetric vs public-key
- [ ] Hiểu Kerckhoff's Principle
- [ ] Biết threat model và adversary capabilities
- [ ] Phân biệt confidentiality vs integrity vs authentication

---

### ✅ Symmetric Cryptography

- [ ] Hiểu cách hoạt động của block cipher
- [ ] Biết các modes: ECB, CBC, CTR
- [ ] Hiểu tại sao ECB không an toàn
- [ ] Biết khi nào dùng padding
- [ ] Hiểu AES và key sizes

---

### ✅ Public-Key Cryptography

- [ ] Hiểu khái niệm public/private keypair
- [ ] Biết sự khác biệt giữa encryption và signing
- [ ] Hiểu RSA ở mức cao (không cần chi tiết toán)
- [ ] Hiểu Diffie-Hellman key exchange
- [ ] Biết tại sao ECC hiệu quả hơn RSA
- [ ] Hiểu hybrid encryption

---

### ✅ Integrity Protection

- [ ] Hiểu hash functions và properties
- [ ] Biết sự khác biệt: hash vs MAC vs digital signature
- [ ] Biết khi nào dùng cái nào
- [ ] Hiểu tại sao hash-then-sign là an toàn
- [ ] Biết các thuật toán: SHA-256, HMAC, RSA signature

---

### ✅ Advanced Topics

- [ ] Hiểu certificates và PKI
- [ ] Biết chain of trust
- [ ] Hiểu các tấn công phổ biến
- [ ] Biết best practices
- [ ] Có thể thiết kế hệ thống crypto đơn giản

---

## 15. Tổng kết

### 🎯 Key Takeaways

1. **Security through obscurity doesn't work**
   - Algorithms phải công khai
   - Chỉ keys cần bí mật

2. **Không tự implement crypto**
   - Dùng thư viện uy tín
   - Follow standards

3. **Layered security**
   - Kết hợp nhiều kỹ thuật
   - Defense in depth

4. **Crypto không phải silver bullet**
   - Chỉ giải quyết một phần vấn đề
   - Cần kết hợp với access control, audit, etc.

5. **Stay updated**
   - Crypto evolves
   - Theo dõi security advisories

---

### 🚀 Next Steps

**Để nâng cao:**
1. Thực hành với cryptopals challenges
2. Đọc security advisories và phân tích vulnerabilities
3. Tham gia CTF competitions
4. Đọc source code của crypto libraries
5. Học về post-quantum cryptography

**Để áp dụng:**
1. Review code của dự án để tìm crypto issues
2. Implement TLS cho ứng dụng
3. Set up proper key management
4. Audit và update crypto trong hệ thống hiện tại

---

## 📝 Ghi chú cuối

**Disclaimer:**
- Tài liệu này chỉ cho mục đích học tập
- Luôn consult security experts cho production systems
- Follow legal và ethical guidelines

**Credits:**
- Based on NT140 course materials
- References từ NIST, RFCs, và security community

---

**Last updated:** 2025-10-01
**Version:** 1.0

---

> "In cryptography, the difference between 'almost secure' and 'secure' is infinite." 
> — Bruce Schneier