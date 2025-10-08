# Bài Tập An Toàn Mạng

## Phần 1: Digital Certificates & Cryptography

### Câu 1: Digital Certificate X.509

**Chức năng chính của một Digital Certificate (Chứng thư số) theo chuẩn X.509 là gì?**

- [ ] A. Mã hóa dữ liệu truyền trên mạng
- [ ] B. Lưu trữ khóa bí mật của người dùng một cách an toàn
- [ ] C. Tạo ra các cặp khóa công khai/bí mật cho người dùng
- [x] **D. Ràng buộc một định danh (identity) với một khóa công khai (public key) thông qua chữ ký của một bên thứ ba tin cậy (CA)**

!!! success "Giải thích" 
    Digital Certificate X.509 có chức năng cốt lõi là ràng buộc định danh (identity) với khóa công khai thông qua chữ ký số của Certificate Authority (CA). Đây là nền tảng của PKI (Public Key Infrastructure).

---

### Câu 2: Security Goals

**Một hệ thống ngân hàng trực tuyến sử dụng kết hợp Diffie-Hellman để thiết lập một khóa phiên, sau đó dùng khóa này với AES-256-CBC để mã hóa dữ liệu giao dịch. Họ cũng dùng HMAC-SHA256 để đảm bảo tính toàn vẹn của tin nhắn. Quy trình này được thiết kế để đảm bảo các mục tiêu an ninh nào?**

- [ ] A. Chỉ Confidentiality (Bảo mật)
- [x] **B. Confidentiality (Bảo mật), Integrity (Toàn vẹn) và Authenticity (Xác thực)**
- [ ] C. Chỉ Integrity (Toàn vẹn) và Authenticity (Xác thực)
- [ ] D. Chỉ Availability (Sẵn sàng)

!!! success "Giải thích" 
    - **Diffie-Hellman + AES-256-CBC**: Đảm bảo Confidentiality (bảo mật) 
    - **HMAC-SHA256**: Đảm bảo Integrity (toàn vẹn) và Authenticity (xác thực) - Kết hợp cả 3 mục tiêu: CIA (Confidentiality, Integrity, Authenticity)

---

### Câu 3: Fail-Safe Defaults

**Phân tích đoạn mã sau:**

```c
if (dwRet == ERROR_ACCESS_DENIED) {
    // fail
} else {
    // success
}
```

**Lỗi bảo mật của đoạn mã này là gì khi xét theo nguyên tắc "fail-safe defaults"?**

- [ ] A. Biến dwRet có thể bị tấn công tràn số
- [ ] B. Nó không ghi lại nhật ký khi truy cập bị từ chối
- [ ] C. Nó không thông báo cho quản trị viên khi có lỗi
- [x] **D. Nó mặc định cho phép truy cập (success) trong mọi trường hợp khác ngoài trường hợp bị từ chối rõ ràng (ERROR_ACCESS_DENIED), bao gồm cả các trường hợp lỗi không lường trước**

!!! danger "Lỗi bảo mật nghiêm trọng" 
    Code này vi phạm nguyên tắc **fail-safe defaults**. Nếu `dwRet` trả về bất kỳ giá trị nào khác (lỗi hệ thống, timeout, NULL...), code sẽ mặc định cho phép truy cập. Đúng ra phải **mặc định từ chối** (deny by default).

---

### Câu 4: File Integrity

**Để bảo vệ tính toàn vẹn (Integrity) của một file phần mềm tải về từ trên mạng, người dùng nên làm gì?**

- [ ] A. Chỉ tải từ các trang web có HTTPS
- [ ] B. Dùng phần mềm diệt virus để quét file đó
- [x] **C. Tính giá trị hash (ví dụ: SHA-256) của file đã tải về và so sánh nó với giá trị hash do nhà cung cấp công bố**
- [ ] D. Giải nén file trong một môi trường sandbox

!!! tip "Best Practice" 
    Checksum/hash verification là phương pháp hiệu quả nhất để xác minh tính toàn vẹn. HTTPS chỉ bảo vệ trong quá trình truyền tải, không đảm bảo file trên server đã bị thay đổi hay chưa.

---

### Câu 5: Security Concepts

**Một trang web yêu cầu người dùng nhập thông tin thẻ tín dụng nhưng lại truyền dữ liệu qua giao thức HTTP thay vì HTTPS. Đây là một ví dụ về:**

- [ ] A. Một cuộc tấn công (Attack)
- [ ] B. Một rủi ro (Risk)
- [ ] C. Một mối đe dọa (Threat)
- [x] **D. Một lỗ hổng (Vulnerability)**

!!! info "Phân biệt khái niệm" 
    - **Vulnerability**: Điểm yếu trong thiết kế/cấu hình hệ thống 
    - **Threat**: Nguồn gây hại tiềm tàng 
    - **Attack**: Hành động khai thác lỗ hổng 
    - **Risk**: Vulnerability × Threat

---

## Phần 2: Malware

### Câu 6: Slammer Worm

**Sâu Slammer (2003) có tốc độ lây lan cực kỳ nhanh, gây tắc nghẽn mạng toàn cầu chỉ trong vài phút. Yếu tố kỹ thuật chính nào đã góp phần vào tốc độ kinh hoàng này?**

- [ ] A. Nó lây lan qua email Outlook
- [ ] B. Nó khai thác lỗ hổng trong giao thức HTTP
- [ ] C. Kích thước của nó rất nhỏ
- [x] **D. Nó sử dụng giao thức UDP không cần kết nối (connectionless) để gửi các gói tin lây nhiễm**

!!! warning "Slammer Worm Analysis" 
    - **Kích thước**: Chỉ 376 bytes 
    - **Giao thức**: UDP (không cần handshake như TCP) 
    - **Tốc độ**: Lây nhiễm 75,000 máy chủ trong 10 phút 
    - **Khai thác**: SQL Server buffer overflow (MS02-039)

---

### Câu 7: Rootkit

**Mục đích chính của một Rootkit là gì?**

- [ ] A. Biến máy tính thành một phần của botnet
- [ ] B. Mã hóa dữ liệu và đòi tiền chuộc
- [x] **C. Che giấu sự tồn tại của chính nó và các phần mềm độc hại khác khỏi người dùng và hệ điều hành**
- [ ] D. Đánh cắp thông tin cá nhân của người dùng

!!! info "Rootkit Characteristics" 
    Rootkit hoạt động ở kernel-level hoặc user-level để: 
    - Ẩn processes, files, registry keys 
    - Hook system calls 
    - Bypass security software 
    - Maintain persistent access

---

### Câu 8: APT vs Malware

**Một Advanced Persistent Threat (APT) khác với một cuộc tấn công malware thông thường ở điểm nào?**

- [ ] A. APT luôn sử dụng các malware chưa từng được biết đến
- [ ] B. APT chỉ nhắm vào các cá nhân, không nhắm vào tổ chức
- [x] **C. APT là một chiến dịch tấn công có chủ đích, dai dẳng, được tài trợ tốt và nhắm vào một mục tiêu cụ thể, thay vì là một cuộc tấn công cơ hội, ngẫu nhiên**
- [ ] D. APT không bao giờ sử dụng các kỹ thuật social engineering

!!! example "APT Characteristics" 
    - **Advanced**: Sử dụng kỹ thuật tinh vi, có thể dùng zero-day 
    - **Persistent**: Duy trì truy cập lâu dài (tháng/năm) 
    - **Threat**: Được tài trợ bởi nation-state hoặc tổ chức lớn 
    - **Targeted**: Nhắm mục tiêu cụ thể (chính phủ, doanh nghiệp)

---

### Câu 9: Malware Types

**Một phần mềm diệt virus phát hiện một file đáng ngờ vì nó đang cố gắng sửa đổi MBR (Master Boot Record) của ổ cứng. Hành vi này đặc trưng cho loại malware nào?**

- [x] **A. Boot Sector Virus**
- [ ] B. Spyware
- [ ] C. Macro Virus
- [ ] D. Ransomware

!!! danger "Boot Sector Virus" 
    - Lây nhiễm vào MBR hoặc boot sector của ổ đĩa 
    - Kích hoạt trước khi OS khởi động 
    - Rất khó phát hiện và loại bỏ 
    - Ví dụ: Brain, Michelangelo

---

### Câu 10: Worm Propagation

**Theo mô hình lây lan dịch tễ học (S-curve) được trình bày trong bài giảng, giai đoạn "Fast spread phase" (lây lan nhanh) xảy ra khi nào?**

- [ ] A. Ngay khi worm bắt đầu lây nhiễm
- [x] **B. Khi số lượng máy chủ bị nhiễm đủ lớn để tạo ra hiệu ứng lây lan theo cấp số nhân**
- [ ] C. Khi hầu hết các máy chủ có lỗ hổng đã bị nhiễm
- [ ] D. Khi các chuyên gia bảo mật bắt đầu phân tích worm

!!! info "S-Curve Propagation Model" 
    1. **Slow start**: Ít máy bị nhiễm ban đầu 
    2. **Fast spread**: Lây lan theo cấp số nhân (exponential growth) 
    3. **Saturation**: Hết máy dễ bị tấn công, tốc độ giảm

---

### Câu 11: Logic Bomb

**Một nhân viên bị sa thải đã cài một đoạn mã vào hệ thống của công ty. Đoạn mã này sẽ xóa toàn bộ cơ sở dữ liệu nếu tên của anh ta bị xóa khỏi danh sách nhân viên. Đây là một ví dụ điển hình của:**

- [x] **A. Logic-bomb**
- [ ] B. Backdoor
- [ ] C. Ransomware
- [ ] D. Time-bomb

!!! warning "Logic Bomb vs Time Bomb" 
    - **Logic Bomb**: Kích hoạt khi điều kiện logic được thỏa mãn (tên bị xóa, transaction cụ thể...) 
    - **Time Bomb**: Kích hoạt vào thời điểm cụ thể (ngày, giờ)

---

### Câu 12: Virus vs Worm

**Sự khác biệt cơ bản nhất giữa Virus và Worm là gì?**

- [ ] A. Virus gây hại cho dữ liệu, còn Worm chỉ gây tắc nghẽn mạng
- [ ] B. Virus chỉ lây lan qua email, còn Worm lây lan qua lỗ hổng hệ thống
- [ ] C. Virus được viết bằng hợp ngữ, còn Worm được viết bằng ngôn ngữ kịch bản
- [x] **D. Virus cần một vật chủ (file thực thi, boot sector) và thường cần sự tương tác của người dùng để lây lan, trong khi Worm là một chương trình độc lập và có thể tự lây lan qua mạng**

!!! info "Key Differences" 
    | Đặc điểm | Virus | Worm | 
    |----------|-------|------| 
    | Vật chủ | Cần (file, boot sector) | Không cần (standalone) | 
    | Lây lan | Cần user interaction | Tự động qua mạng | 
    | Tốc độ | Chậm | Rất nhanh | 
    | Ví dụ | Melissa, ILOVEYOU | Code Red, Slammer |

---

### Câu 13: Trojan Horse

**Một người dùng tải về một phần mềm crack từ trên mạng. Sau khi cài đặt, máy tính của họ hoạt động bình thường, nhưng một thời gian sau họ phát hiện tài khoản ngân hàng bị đánh cắp. Phần mềm độc hại này có khả năng cao nhất là một:**

- [x] **A. Trojan Horse (Ngựa Troia)**
- [ ] B. Virus
- [ ] C. Worm (Sâu)
- [ ] D. Adware

!!! danger "Trojan Horse" 
    - Ngụy trang là phần mềm hợp pháp (game, crack, tool...) 
    - Không tự lây lan 
    - Thực hiện hành động độc hại ngầm (keylogger, backdoor, info stealer) 
    - Ví dụ: ZeuS, Emotet, Remote Access Trojans (RATs)

---

### Câu 14: Stuxnet

**Stuxnet được coi là một cột mốc trong lịch sử malware vì nó khác biệt cơ bản so với các worm trước đó như Code Red hay Slammer. Sự khác biệt cốt lõi đó là gì?**

- [ ] A. Nó khai thác nhiều lỗ hổng zero-day cùng lúc
- [x] **B. Payload của nó được thiết kế để gây ra thiệt hại vật lý có chủ đích cho các hệ thống điều khiển công nghiệp**
- [ ] C. Nó lây lan nhanh hơn bất kỳ worm nào trước đây
- [ ] D. Nó có khả năng lây lan qua cả mạng và USB

!!! example "Stuxnet - First Cyber Weapon" 
    - **Mục tiêu**: Phá hoại chương trình hạt nhân Iran (centrifuges làm giàu uranium) 
    - **Payload**: Thay đổi tốc độ động cơ ly tâm → hư hỏng vật lý 
    - **Zero-days**: Khai thác 4 lỗ hổng zero-day 
    - **Năm**: 2010 
    - **Significance**: Đầu tiên gây thiệt hại vật lý trong thế giới thực từ cyber attack

---

## Phần 3: Cryptography Advanced

### Câu 15: Collision Resistance

**Một hàm băm mật mã (cryptographic hash function) được cho là có thuộc tính "Collision Resistance" mạnh khi nào?**

- [ ] A. Khi không thể tìm ra x từ giá trị h = H(x)
- [ ] B. Khi cho trước x, không thể tìm ra y ≠ x sao cho H(x) = H(y)
- [x] **C. Khi không thể tìm được bất kỳ cặp (x, y) nào sao cho x ≠ y và H(x) = H(y)**
- [ ] D. Khi hàm băm luôn tạo ra output có độ dài cố định

!!! info "Hash Function Properties" 
    - **Pre-image resistance** (A): Cho H(x), khó tìm x (one-way) 
    - **Second pre-image resistance** (B): Cho x, khó tìm y≠x với H(x)=H(y) 
    - **Collision resistance** (C): Khó tìm BẤT KỲ cặp (x,y) với H(x)=H(y)

```
Collision resistance mạnh nhất và khó đạt được nhất.
```

---

### Câu 16: Diffie-Hellman Security

**Trong giao thức trao đổi khóa Diffie-Hellman, Eve đứng ở giữa và thấy được g, p, A = g^a mod p, và B = g^b mod p. Để tính được khóa chung K = g^(ab) mod p, Eve phải giải quyết bài toán khó nào?**

- [x] **A. Logarit rời rạc (Discrete Logarithm)**
- [ ] B. Phân tích thừa số nguyên tố
- [ ] C. Bài toán ba lô (Knapsack problem)
- [ ] D. Bài toán đường đi ngắn nhất (Shortest path problem)

!!! info "Diffie-Hellman Security" 
    - **DLP (Discrete Logarithm Problem)**: Cho g^a mod p, tìm a 
    - Nếu Eve tính được a từ A = g^a mod p, có thể tính K = B^a mod p 
    - DLP là bài toán khó với số lớn (2048+ bits) 
    - Lưu ý: DH dễ bị MITM nếu không xác thực

---

### Câu 17: Public Key Encryption

**Alice muốn gửi một tin nhắn bí mật cho Bob. Trong mô hình mã hóa khóa công khai, Alice sẽ sử dụng khóa nào để mã hóa tin nhắn?**

- [ ] A. Khóa bí mật của Alice
- [ ] B. Khóa công khai của Alice
- [x] **C. Khóa công khai của Bob**
- [ ] D. Khóa bí mật của Bob

!!! tip "Public Key Encryption Rule" 
    - **Mã hóa**: Dùng public key của người NHẬN (Bob's public key) 
    - **Giải mã**: Dùng private key của người NHẬN (Bob's private key) 
    - Chỉ Bob có private key → chỉ Bob giải mã được

---

### Câu 18: Key Size Comparison

**So với mã hóa đối xứng (ví dụ: AES-128), mã hóa bất đối xứng (ví dụ: RSA-2048) đòi hỏi kích thước khóa lớn hơn nhiều để đạt được cùng một mức độ an toàn. Tại sao?**

- [x] **A. Vì an toàn của mã hóa bất đối xứng dựa trên các bài toán có cấu trúc (như phân tích thừa số nguyên tố), có thể bị phá vỡ bằng các thuật toán hiệu quả hơn brute-force**
- [ ] B. Vì mã hóa đối xứng được hỗ trợ bởi phần cứng chuyên dụng
- [ ] C. Vì mã hóa bất đối xứng yêu cầu hai khóa thay vì một
- [ ] D. Vì khóa công khai cần phải đủ dài để chứa thông tin định danh người dùng

!!! info "Key Size Comparison" 
    | Security Level | Symmetric | RSA | ECC | 
    |----------------|-----------|-----|-----| 
    | 80-bit | DES (56) | RSA-1024 | ECC-160 | 
    | 128-bit | AES-128 | RSA-3072 | ECC-256 | 
    | 256-bit | AES-256 | RSA-15360 | ECC-512 |

```
Lý do: Factorization và DLP có thuật toán sub-exponential (GNFS, Index Calculus)
```

---

### Câu 19: OTP Malleability

**Trong bối cảnh của One-Time Pad (OTP), thuộc tính "malleable" (dễ uốn nắn) có nghĩa là gì?**

- [ ] A. OTP chỉ có thể mã hóa tin nhắn một lần duy nhất
- [ ] B. Kẻ tấn công có thể dễ dàng đoán ra khóa
- [x] **C. Kẻ tấn công có thể thay đổi một bit trong ciphertext và dự đoán được sự thay đổi tương ứng trong plaintext sau khi giải mã**
- [ ] D. Khóa OTP phải dài bằng plaintext

!!! warning "OTP Malleability" 
    OTP sử dụng XOR: C = P ⊕ K

```
Nếu attacker flip bit i trong C:
- C' = C ⊕ (1 << i)
- P' = C' ⊕ K = P ⊕ (1 << i)

→ Bit i trong plaintext bị flip → **không đảm bảo integrity**
```

---

### Câu 20: Kerckhoff's Principle

**Nguyên tắc Kerckhoff's (nay là nguyên tắc Open Design) cho rằng "an toàn của một hệ mật mã không nên phụ thuộc vào việc giữ bí mật thuật toán". Điều này ngụ ý rằng:**

- [x] **A. An toàn của hệ thống phụ thuộc vào sự bí mật của khóa và sức mạnh của thuật toán đã được cộng đồng kiểm chứng**
- [ ] B. Chỉ cần giữ bí mật khóa là đủ, không cần thuật toán mạnh
- [ ] C. Thuật toán tự chế luôn tốt hơn các thuật toán công khai
- [ ] D. Mật mã bất đối xứng không tuân theo nguyên tắc này

!!! quote "Kerckhoff's Principle (1883)" 
    _"A cryptosystem should be secure even if everything about the system, except the key, is public knowledge."_

```
**Lợi ích:**
- Thuật toán công khai được kiểm chứng bởi cộng đồng
- Tránh "security through obscurity"
- Dễ thay đổi khóa hơn thay đổi thuật toán
```

---

### Câu 21: Hybrid Encryption

**Tại sao trong giao thức mã hóa Hybrid (Hybrid Encryption), người ta lại dùng mã hóa bất đối xứng (như RSA) để mã hóa khóa phiên (session key) thay vì mã hóa toàn bộ dữ liệu?**

- [ ] A. Vì khóa phiên của AES quá ngắn để tự bảo vệ
- [ ] B. Vì mã hóa đối xứng (như AES) không thể giải mã được nếu không có khóa công khai
- [x] **C. Vì mã hóa bất đối xứng rất chậm, không phù hợp cho dữ liệu lớn, nhưng lại giải quyết được bài toán trao đổi khóa an toàn**
- [ ] D. Vì RSA an toàn hơn AES

!!! tip "Hybrid Encryption Best Practice" 
    **Lý do sử dụng:** 
    - RSA: 1000-10000x chậm hơn AES 
    - RSA có giới hạn kích thước dữ liệu (< modulus size)

```
**Cách hoạt động:**
1. Tạo random session key (AES-256)
2. Mã hóa session key bằng RSA public key
3. Mã hóa data bằng AES với session key
4. Gửi: RSA(session_key) + AES(data)
```

---

## Phần 4: Block Cipher Modes & Security Concepts

### Câu 22: ECB Mode Weakness

**Một kẻ tấn công chặn được một file ảnh đã được mã hóa. Dù không giải mã được, kẻ tấn công nhận thấy các vùng lặp lại rất rõ trong ciphertext, tương ứng với các vùng màu đồng nhất trong ảnh gốc. Điểm yếu này là đặc trưng của chế độ mã hóa khối (block cipher mode) nào?**

- [ ] A. Cipher Block Chaining (CBC)
- [x] **B. Electronic Codebook (ECB)**
- [ ] C. Output Feedback (OFB)
- [ ] D. Counter (CTR)

!!! danger "ECB Mode - Never Use for Real Data" 
    **Vấn đề:** Mỗi block plaintext giống nhau → block ciphertext giống nhau

````
```
P1 = P2 → E(K, P1) = E(K, P2)
```

**Hậu quả:**
- Pattern trong plaintext bị lộ
- Dễ bị known-plaintext attack
- Không đảm bảo semantic security

**Khuyến nghị:** Dùng CBC, CTR, hoặc GCM
````

---

### Câu 23: Unauthorized Disclosure

**Tất cả những điều sau đây là ví dụ về Unauthorized Disclosure (Tiết lộ trái phép), NGOẠI TRỪ:**

- [ ] A. Intrusion (Đột nhập vào hệ thống để đọc file)
- [x] **B. Falsification (Làm giả dữ liệu trong cơ sở dữ liệu)**
- [ ] C. Interception (Nghe lén tin nhắn)
- [ ] D. Inference (Suy luận ra thông tin nhạy cảm từ các dữ liệu công khai)

!!! info "CIA Triad Classification" 
    **Unauthorized Disclosure (vi phạm Confidentiality):** 
    - Intrusion, Interception, Inference

```
**Deception (vi phạm Integrity):**
- **Falsification**, Masquerading, Repudiation

**Disruption (vi phạm Availability):**
- Incapacitation, Corruption, Obstruction
```

---

### Câu 24: Cybersecurity Skills

**Theo thống kê trong bài giảng (01), kỹ năng nào được các nhà tuyển dụng coi là quan trọng nhất đối với một ứng viên an ninh mạng?**

- [ ] A. Bằng cấp, chứng chỉ
- [ ] B. Kinh nghiệm thực tiễn
- [x] **C. Kỹ năng**
- [ ] D. Đào tạo lý thuyết chuyên sâu

!!! success "Top Cybersecurity Skills" 
    1. **Technical Skills**: Network security, penetration testing, SIEM 
    2. **Analytical Skills**: Problem-solving, critical thinking 
    3. **Communication**: Explain technical issues to non-technical stakeholders 
    4. **Continuous Learning**: Stay updated with latest threats

```
Bằng cấp quan trọng, nhưng kỹ năng thực tế là quyết định nhất.
```

---

### Câu 25: Active vs Passive Attack

**Một kẻ tấn công gửi email lừa đảo (phishing) đến một nhân viên và lừa họ tiết lộ mật khẩu. Sau đó, kẻ tấn công dùng mật khẩu này để truy cập hệ thống. Hành động của kẻ tấn công được phân loại là gì?**

- [ ] A. Inside attack (Tấn công từ bên trong)
- [ ] B. Threat consequence (Hậu quả của mối đe dọa)
- [x] **C. Active attack (Tấn công chủ động)**
- [ ] D. Passive attack (Tấn công thụ động)

!!! info "Active vs Passive Attacks" 
    **Passive Attack:** 
    - Chỉ quan sát/nghe lén 
    - Không thay đổi dữ liệu 
    - Khó phát hiện 
    - Ví dụ: Eavesdropping, traffic analysis

```
**Active Attack:**
- Thay đổi/inject dữ liệu hoặc hệ thống
- Dễ phát hiện hơn
- Ví dụ: Phishing, MITM, malware injection, DoS

Phishing + login → **Active attack**
```

---

### Câu 26: Zero-Day Market

**Một hacker phát hiện ra một lỗ hổng zero-day trong hệ điều hành iOS. Theo bài giảng, để có được mức giá cao nhất một cách hợp pháp, hacker này nên bán lỗ hổng cho ai?**

- [ ] A. Apple, để họ vá lỗi và nhận tiền thưởng bug bounty
- [ ] B. Google Project Zero, để họ công bố rộng rãi
- [ ] C. Một diễn đàn hacker trên dark web
- [x] **D. Các công ty như Zerodium, chuyên bán lại cho các khách hàng chính phủ**

!!! warning "Zero-Day Market Pricing" 
**Giá trị iOS zero-day (2024):** 
    - **Zerodium**: $2-2.5 million (RCE với persistence) 
    - **Apple Bug Bounty**: Tối đa $1 million (nhưng hiếm khi trả mức này) 
    - **Black market**: Biến động, rủi ro pháp lý cao

```
**Lưu ý:** Bán cho Zerodium hợp pháp nhưng có tranh cãi về đạo đức (exploits được bán cho government agencies).
```

---

### Câu 27: Risk Assessment

**Theo mô hình Threat + Vulnerability = Risk, việc một công ty đặt máy chủ chứa dữ liệu khách hàng nhạy cảm trong một khu vực thường xuyên xảy ra động đất được xem là gì?**

- [ ] A. Một Threat (Mối đe dọa)
- [ ] B. Một Countermeasure (Biện pháp đối phó)
- [x] **C. Một Risk (Rủi ro)**
- [ ] D. Một Vulnerability (Lỗ hổng)

!!! info "Risk = Threat × Vulnerability" 
    **Phân tích:** 
    - **Threat**: Động đất (nguồn gây hại tự nhiên) 
    - **Vulnerability**: Đặt server ở khu vực nguy hiểm (điểm yếu trong thiết kế)
    - **Risk**: Kết hợp cả hai → nguy cơ mất dữ liệu

```
**Countermeasures:**
- Chuyển data center
- Backup offsite
- Disaster recovery plan
```

---

### Câu 28: Trusting Trust

**Tư tưởng "Reflections on Trusting Trust" của Ken Thompson nêu bật vấn đề cơ bản nào trong an ninh máy tính?**

- [ ] A. Mật khẩu đăng nhập có thể bị ghi lại dễ dàng
- [x] **B. Một trình biên dịch bị xâm nhập có thể chèn backdoor vào bất kỳ chương trình nào nó biên dịch, khiến việc kiểm tra mã nguồn trở nên không đủ**
- [ ] C. Phần cứng máy tính không thể được tin cậy hoàn toàn
- [ ] D. Mọi phần mềm mã nguồn mở đều có backdoor

!!! quote "Ken Thompson (1984 Turing Award Lecture)" 
    **Vấn đề Trust Chain:**

```
1. Compiler bị nhiễm backdoor
2. Compiler tự nhân bản backdoor khi compile chính nó
3. Compiler chèn backdoor vào các chương trình khác (login, sudo...)
4. Source code sạch → binary bị nhiễm

**Kết luận:** *"You can't trust code that you did not totally create yourself."*

**Relevance:** Supply chain attacks (SolarWinds, XZ Utils backdoor)
```

---

### Câu 29: Least Privilege

**Một nhân viên IT cấu hình máy chủ web của công ty. Để tăng tính tiện dụng cho người dùng, anh ta cho phép tiến trình máy chủ chạy với quyền quản trị viên (root/administrator). Điều này vi phạm rõ ràng nhất nguyên tắc thiết kế bảo mật nào?**

- [ ] A. Economy of mechanism (Tính kinh tế của cơ chế)
- [ ] B. Fail-safe defaults (Mặc định an toàn)
- [x] **C. Least privilege (Đặc quyền tối thiểu)**
- [ ] D. Open design (Thiết kế mở)

!!! danger "Least Privilege Violation" 
    **Vấn đề:** 
    - Web server chạy với root → khi bị exploit, attacker có full control 
    - Một lỗ hổng RCE nhỏ → complete system compromise

````
**Best Practice:**
- Tạo dedicated user (www-data, nginx, apache)
- Chỉ cấp quyền đọc web files + bind port 80/443
- Sử dụng capabilities thay vì full root (Linux)
- Drop privileges sau khi bind port

**Example:**
```bash
# Bad
nginx -g "daemon off;"  # running as root

# Good
useradd -r -s /bin/false nginx
chown -R nginx:nginx /var/www
su -s /bin/sh -c "nginx" nginx
```
````

---

### Câu 30: Fail-Safe Defaults

**Một hệ thống kiểm soát truy cập file được thiết kế sao cho nếu một quy tắc (rule) không rõ ràng hoặc gây ra lỗi trong quá trình kiểm tra, quyền truy cập sẽ tự động bị từ chối. Đây là một ví dụ thực tế của nguyên tắc nào?**

- [x] **A. Fail-safe defaults (Mặc định an toàn)**
- [ ] B. Separation of privilege (Phân tách đặc quyền)
- [ ] C. Psychological acceptability (Tính chấp nhận tâm lý)
- [ ] D. Complete mediation (Kiểm duyệt toàn diện)

!!! success "Fail-Safe Defaults Implementation" 
    **Principle:** Mặc định từ chối (Deny by default), chỉ cho phép khi được explicit allow.

````
**Code Pattern:**
```python
def check_access(user, resource):
    try:
        # Check ACL rules
        if has_explicit_permission(user, resource):
            return ALLOW
        else:
            return DENY  # Default deny
    except Exception as e:
        log_error(e)
        return DENY  # Fail-safe: deny on error
```

**Real-world Examples:**
- Firewall rules: Default DROP
- SELinux/AppArmor: Default deny
- IAM policies: Explicit deny > Allow
````

---

## Tổng Kết

### Phân Bố Điểm Theo Chủ Đề

|Chủ đề|Số câu|Phần trăm|
|---|---|---|
|Cryptography|10|33.3%|
|Malware|9|30%|
|Security Principles|8|26.7%|
|Block Cipher & Misc|3|10%|

### Các Nguyên Tắc Bảo Mật Quan Trọng

!!! tip "Saltzer & Schroeder's Design Principles" 
    1. **Economy of mechanism**: Giữ thiết kế đơn giản 
    2. **Fail-safe defaults**: Mặc định từ chối 
    3. **Complete mediation**: Kiểm tra mọi lần truy cập 
    4. **Open design**: Không dựa vào bảo mật qua che giấu 
    5. **Separation of privilege**: Yêu cầu nhiều điều kiện
    6. **Least privilege**: Chỉ cấp quyền tối thiểu 
    7. **Least common mechanism**: Tối thiểu chia sẻ tài nguyên
    8. **Psychological acceptability**: Dễ sử dụng = dễ áp dụng

### Khuyến Nghị Học Tập

!!! note "Study Tips" 
    **High Priority Topics:** 
    - Digital certificates & PKI 
    - Symmetric vs Asymmetric encryption 
    - Hash functions & their properties 
    - Malware types & propagation 
    - Security design principles

```
**Hands-on Practice:**
- Sử dụng OpenSSL để test encryption modes
- Phân tích malware samples trong sandbox
- Practice writing secure code
- Thực hành với CTF challenges
```

### Tài Liệu Tham Khảo

- **Cryptography**: Applied Cryptography (Bruce Schneier)
- **Malware**: Practical Malware Analysis (Michael Sikorski)
- **Security Principles**: Computer Security: Art and Science (Matt Bishop)
- **Standards**: NIST SP 800 series, OWASP Top 10

---

**Lưu ý:** Tài liệu này dùng cho mục đích học tập. Đáp án và giải thích dựa trên kiến thức an toàn mạng chuẩn mực tính đến tháng 1/2025.. Mã hóa dữ liệu truyền trên mạng

- [ ] B. Lưu trữ khóa bí mật của người dùng một cách an toàn
- [ ] C. Tạo ra các cặp khóa công khai/bí mật cho người dùng
- [x] **D. Ràng buộc một định danh (identity) với một khóa công khai (public key) thông qua chữ ký của một bên thứ ba tin cậy (CA)**

!!! success "Giải thích" 
    Digital Certificate X.509 có chức năng cốt lõi là ràng buộc định danh (identity) với khóa công khai thông qua chữ ký số của Certificate Authority (CA). Đây là nền tảng của PKI (Public Key Infrastructure).

---
