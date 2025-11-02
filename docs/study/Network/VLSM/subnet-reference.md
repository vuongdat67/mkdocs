# 🌐 Subnet Mask & VLSM - Complete Reference

## 📊 Bảng Subnet Mask đầy đủ (IPv4)

### Class A (1.0.0.0 - 126.0.0.0)

| CIDR | Subnet Mask | Wildcard Mask | # Subnets | # Hosts/Subnet | Total Hosts |
|------|-------------|---------------|-----------|----------------|-------------|
| /8 | 255.0.0.0 | 0.255.255.255 | 1 | 16,777,214 | 16,777,214 |
| /9 | 255.128.0.0 | 0.127.255.255 | 2 | 8,388,606 | 16,777,212 |
| /10 | 255.192.0.0 | 0.63.255.255 | 4 | 4,194,302 | 16,777,208 |
| /11 | 255.224.0.0 | 0.31.255.255 | 8 | 2,097,150 | 16,777,200 |
| /12 | 255.240.0.0 | 0.15.255.255 | 16 | 1,048,574 | 16,777,184 |
| /13 | 255.248.0.0 | 0.7.255.255 | 32 | 524,286 | 16,777,152 |
| /14 | 255.252.0.0 | 0.3.255.255 | 64 | 262,142 | 16,777,088 |
| /15 | 255.254.0.0 | 0.1.255.255 | 128 | 131,070 | 16,776,960 |

### Class B (128.0.0.0 - 191.255.0.0)

| CIDR | Subnet Mask | Wildcard Mask | # Subnets | # Hosts/Subnet | Total Hosts |
|------|-------------|---------------|-----------|----------------|-------------|
| /16 | 255.255.0.0 | 0.0.255.255 | 1 | 65,534 | 65,534 |
| /17 | 255.255.128.0 | 0.0.127.255 | 2 | 32,766 | 65,532 |
| /18 | 255.255.192.0 | 0.0.63.255 | 4 | 16,382 | 65,528 |
| /19 | 255.255.224.0 | 0.0.31.255 | 8 | 8,190 | 65,520 |
| /20 | 255.255.240.0 | 0.0.15.255 | 16 | 4,094 | 65,504 |
| /21 | 255.255.248.0 | 0.0.7.255 | 32 | 2,046 | 65,472 |
| /22 | 255.255.252.0 | 0.0.3.255 | 64 | 1,022 | 65,408 |
| /23 | 255.255.254.0 | 0.0.1.255 | 128 | 510 | 65,280 |

### Class C (192.0.0.0 - 223.255.255.0)

| CIDR | Subnet Mask | Wildcard Mask | # Subnets | # Hosts/Subnet | Total Hosts |
|------|-------------|---------------|-----------|----------------|-------------|
| /24 | 255.255.255.0 | 0.0.0.255 | 1 | 254 | 254 |
| /25 | 255.255.255.128 | 0.0.0.127 | 2 | 126 | 252 |
| /26 | 255.255.255.192 | 0.0.0.63 | 4 | 62 | 248 |
| /27 | 255.255.255.224 | 0.0.0.31 | 8 | 30 | 240 |
| /28 | 255.255.255.240 | 0.0.0.15 | 16 | 14 | 224 |
| /29 | 255.255.255.248 | 0.0.0.7 | 32 | 6 | 192 |
| /30 | 255.255.255.252 | 0.0.0.3 | 64 | 2 | 128 |
| /31 | 255.255.255.254 | 0.0.0.1 | 128 | 2* | 256 |
| /32 | 255.255.255.255 | 0.0.0.0 | 256 | 1 | 256 |

**/31**: Point-to-point links (RFC 3021), không có network/broadcast address

---

## 📐 Công thức tính Subnetting

### 1. Số Subnets
```
Số Subnets = 2^n
```
Trong đó `n` = số bits mượn

**Ví dụ**: 192.168.1.0/24 chia thành /26
- Bits mượn: 26 - 24 = 2 bits
- Số subnets: 2^2 = 4 subnets

### 2. Số Hosts mỗi Subnet
```
Số Hosts = 2^h - 2
```
Trong đó `h` = số host bits (32 - prefix length)

**Ví dụ**: /26
- Host bits: 32 - 26 = 6 bits
- Số hosts: 2^6 - 2 = 62 hosts

**-2 vì**:
- 1 địa chỉ Network (all host bits = 0)
- 1 địa chỉ Broadcast (all host bits = 1)

### 3. Block Size (Khoảng cách giữa các subnet)
```
Block Size = 256 - Octet cuối của Subnet Mask
```

**Ví dụ**: 255.255.255.192 (/26)
- Block size: 256 - 192 = 64
- Subnets: 0, 64, 128, 192

### 4. Wildcard Mask
```
Wildcard Mask = 255.255.255.255 - Subnet Mask
```

**Ví dụ**: Subnet mask 255.255.255.192
- Wildcard: 0.0.0.63

---

## 🎯 VLSM (Variable Length Subnet Mask)

### Nguyên tắc VLSM

1. **Sắp xếp theo thứ tự giảm dần** số hosts cần
2. **Tính subnet mask** cho từng yêu cầu
3. **Gán địa chỉ** từ lớn đến nhỏ
4. **Không overlap** các subnet

### Ví dụ VLSM

**Đề bài**: Chia 192.168.1.0/24 cho:
- LAN A: 100 hosts
- LAN B: 50 hosts  
- LAN C: 20 hosts
- LAN D: 10 hosts
- 2 Point-to-Point links: 2 hosts mỗi link

**Giải**:

#### 1. Sắp xếp theo thứ tự giảm dần
```
1. LAN A: 100 hosts
2. LAN B: 50 hosts
3. LAN C: 20 hosts
4. LAN D: 10 hosts
5. Link 1: 2 hosts
6. Link 2: 2 hosts
```

#### 2. Tính subnet mask

**LAN A (100 hosts)**:
- Cần: 2^h - 2 ≥ 100 → h = 7 (2^7 - 2 = 126)
- Subnet mask: /25 (32 - 7 = 25)
- Block size: 128
- **Subnet**: 192.168.1.0/25
  - Network: 192.168.1.0
  - First host: 192.168.1.1
  - Last host: 192.168.1.126
  - Broadcast: 192.168.1.127

**LAN B (50 hosts)**:
- Cần: 2^h - 2 ≥ 50 → h = 6 (2^6 - 2 = 62)
- Subnet mask: /26
- Block size: 64
- **Subnet**: 192.168.1.128/26
  - Network: 192.168.1.128
  - First host: 192.168.1.129
  - Last host: 192.168.1.190
  - Broadcast: 192.168.1.191

**LAN C (20 hosts)**:
- Cần: 2^h - 2 ≥ 20 → h = 5 (2^5 - 2 = 30)
- Subnet mask: /27
- Block size: 32
- **Subnet**: 192.168.1.192/27
  - Network: 192.168.1.192
  - First host: 192.168.1.193
  - Last host: 192.168.1.222
  - Broadcast: 192.168.1.223

**LAN D (10 hosts)**:
- Cần: 2^h - 2 ≥ 10 → h = 4 (2^4 - 2 = 14)
- Subnet mask: /28
- Block size: 16
- **Subnet**: 192.168.1.224/28
  - Network: 192.168.1.224
  - First host: 192.168.1.225
  - Last host: 192.168.1.238
  - Broadcast: 192.168.1.239

**Link 1 (2 hosts)**:
- Cần: 2^h - 2 ≥ 2 → h = 2 (2^2 - 2 = 2)
- Subnet mask: /30
- Block size: 4
- **Subnet**: 192.168.1.240/30
  - Network: 192.168.1.240
  - First host: 192.168.1.241
  - Last host: 192.168.1.242
  - Broadcast: 192.168.1.243

**Link 2 (2 hosts)**:
- **Subnet**: 192.168.1.244/30
  - Network: 192.168.1.244
  - First host: 192.168.1.245
  - Last host: 192.168.1.246
  - Broadcast: 192.168.1.247

#### 3. Tổng kết VLSM

| Network | Hosts | CIDR | Network Address | Range | Broadcast |
|---------|-------|------|-----------------|-------|-----------|
| LAN A | 100 | /25 | 192.168.1.0 | .1 - .126 | 192.168.1.127 |
| LAN B | 50 | /26 | 192.168.1.128 | .129 - .190 | 192.168.1.191 |
| LAN C | 20 | /27 | 192.168.1.192 | .193 - .222 | 192.168.1.223 |
| LAN D | 10 | /28 | 192.168.1.224 | .225 - .238 | 192.168.1.239 |
| Link 1 | 2 | /30 | 192.168.1.240 | .241 - .242 | 192.168.1.243 |
| Link 2 | 2 | /30 | 192.168.1.244 | .245 - .246 | 192.168.1.247 |

**Địa chỉ còn lại**: 192.168.1.248/29 - 192.168.1.255/32 (dự phòng)

---

## 🔢 Bảng Quick Reference - Powers of 2

| 2^n | Value | Common Use |
|-----|-------|------------|
| 2^1 | 2 | /31, /30 (P2P links) |
| 2^2 | 4 | /30 blocks |
| 2^3 | 8 | /29 (6 hosts) |
| 2^4 | 16 | /28 (14 hosts) |
| 2^5 | 32 | /27 (30 hosts) |
| 2^6 | 64 | /26 (62 hosts) |
| 2^7 | 128 | /25 (126 hosts) |
| 2^8 | 256 | /24 (254 hosts) |
| 2^9 | 512 | /23 (510 hosts) |
| 2^10 | 1,024 | /22 (1022 hosts) |
| 2^11 | 2,048 | /21 (2046 hosts) |
| 2^12 | 4,096 | /20 (4094 hosts) |
| 2^13 | 8,192 | /19 (8190 hosts) |
| 2^14 | 16,384 | /18 (16382 hosts) |
| 2^15 | 32,768 | /17 (32766 hosts) |
| 2^16 | 65,536 | /16 (65534 hosts) |

---

## 💡 Tips & Tricks

### 1. Nhớ nhanh Subnet Mask

**Binary Pattern**:
```
/24: 11111111.11111111.11111111.00000000 = 255.255.255.0
/25: 11111111.11111111.11111111.10000000 = 255.255.255.128
/26: 11111111.11111111.11111111.11000000 = 255.255.255.192
/27: 11111111.11111111.11111111.11100000 = 255.255.255.224
/28: 11111111.11111111.11111111.11110000 = 255.255.255.240
/29: 11111111.11111111.11111111.11111000 = 255.255.255.248
/30: 11111111.11111111.11111111.11111100 = 255.255.255.252
```

**Magic Numbers** (256 - subnet mask octet):
```
/25: 256 - 128 = 128 (block size)
/26: 256 - 192 = 64
/27: 256 - 224 = 32
/28: 256 - 240 = 16
/29: 256 - 248 = 8
/30: 256 - 252 = 4
```

### 2. Tìm subnet nhanh

**Công thức**:
```
Network Address = IP Address AND Subnet Mask
```

**Ví dụ**: 192.168.1.75/26
- Subnet mask: 255.255.255.192
- Octet 4: 75 AND 192
  - 75 = 01001011
  - 192 = 11000000
  - AND = 01000000 = 64
- Network: 192.168.1.64

**Shortcut**: 75 ÷ 64 = 1 (bỏ phần dư) → 1 × 64 = 64

### 3. Kiểm tra IP cùng subnet

**Cách 1**: Tính network address của cả 2, nếu bằng nhau = cùng subnet

**Cách 2**: Kiểm tra range
- IP1: 192.168.1.50/26 → Network: 192.168.1.0, Range: .1-.62
- IP2: 192.168.1.100/26 → Network: 192.168.1.64, Range: .65-.126
- **Khác subnet**

---

## 📱 Private IP Ranges (RFC 1918)

| Class | Range | Default Mask | # Networks |
|-------|-------|--------------|------------|
| A | 10.0.0.0 - 10.255.255.255 | /8 | 1 |
| B | 172.16.0.0 - 172.31.255.255 | /12 | 16 |
| C | 192.168.0.0 - 192.168.255.255 | /16 | 256 |

---

## 🎓 Bài tập thực hành

### Bài 1: Basic Subnetting
**Đề**: Chia 192.168.10.0/24 thành 4 subnets bằng nhau

<details>
<summary>Đáp án</summary>

- Cần 2 bits: 2^2 = 4 subnets
- New mask: /26
- Block size: 64

1. 192.168.10.0/26 (0-63)
2. 192.168.10.64/26 (64-127)
3. 192.168.10.128/26 (128-191)
4. 192.168.10.192/26 (192-255)
</details>

### Bài 2: VLSM
**Đề**: Chia 172.16.0.0/16 cho:
- Marketing: 500 hosts
- Sales: 250 hosts
- IT: 50 hosts
- Management: 25 hosts

<details>
<summary>Đáp án</summary>

1. Marketing: 172.16.0.0/23 (510 hosts)
2. Sales: 172.16.2.0/24 (254 hosts)
3. IT: 172.16.3.0/26 (62 hosts)
4. Management: 172.16.3.64/27 (30 hosts)
</details>

---

## 🔗 Tools & References

- [Subnet Calculator](https://www.subnet-calculator.com/)
- [RFC 1878 - Variable Length Subnet Table](https://tools.ietf.org/html/rfc1878)
- [RFC 950 - Internet Standard Subnetting Procedure](https://tools.ietf.org/html/rfc950)

---

**Next**: [Subnet Calculator Tool →](subnet-calculator.md)