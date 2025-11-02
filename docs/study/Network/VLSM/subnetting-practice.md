# 🎓 Bài tập Subnetting & VLSM

Bộ bài tập thực hành từ cơ bản đến nâng cao với đáp án chi tiết.

---

## 📚 Phần 1: Subnetting cơ bản

### Bài 1: Tính subnet mask
**Đề**: Bạn có network 192.168.10.0/24 và cần chia thành 4 subnets bằng nhau. Hãy tính:
- Subnet mask mới
- Số hosts mỗi subnet
- Các network addresses

<details>
<summary>💡 Hints</summary>

- Cần bao nhiêu bits để tạo 4 subnets?
- Formula: 2^n = số subnets
</details>

<details>
<summary>✅ Đáp án</summary>

**Giải**:
1. Số subnets cần: 4 → 2^n = 4 → n = 2 bits
2. Subnet mask mới: /24 + 2 = **/26**
3. Subnet mask decimal: **255.255.255.192**
4. Block size: 256 - 192 = **64**
5. Số hosts/subnet: 2^6 - 2 = **62 hosts**

**Các subnets**:
| Subnet | Network | Range | Broadcast |
|--------|---------|-------|-----------|
| 1 | 192.168.10.0/26 | .1 - .62 | 192.168.10.63 |
| 2 | 192.168.10.64/26 | .65 - .126 | 192.168.10.127 |
| 3 | 192.168.10.128/26 | .129 - .190 | 192.168.10.191 |
| 4 | 192.168.10.192/26 | .193 - .254 | 192.168.10.255 |
</details>

---

### Bài 2: Xác định subnet
**Đề**: IP 172.16.45.120/20 thuộc subnet nào? Tìm:
- Network address
- Broadcast address
- First & Last host
- Số usable hosts

<details>
<summary>💡 Hints</summary>

- /20 = 255.255.240.0
- Magic number = 256 - 240 = 16
- Áp dụng vào octet thứ 3
</details>

<details>
<summary>✅ Đáp án</summary>

**Giải**:
1. Subnet mask: /20 = **255.255.240.0**
2. Octet thứ 3: 45
3. Block size: 256 - 240 = **16**
4. Subnet: 45 ÷ 16 = 2 (bỏ dư) → 2 × 16 = **32**

**Kết quả**:
- Network: **172.16.32.0/20**
- First host: **172.16.32.1**
- Last host: **172.16.47.254**
- Broadcast: **172.16.47.255**
- Usable hosts: 2^12 - 2 = **4094 hosts**

**Giải thích**: Octet 3 từ 32 đến 47 (16 giá trị)
</details>

---

### Bài 3: Subnet trong các class
**Đề**: Cho các IP sau, xác định class và default subnet mask:
- a) 10.52.36.90
- b) 172.31.200.10
- c) 192.168.100.50
- d) 224.0.0.5
- e) 126.255.255.255

<details>
<summary>✅ Đáp án</summary>

| IP | Class | Default Mask | Private? |
|----|-------|--------------|----------|
| 10.52.36.90 | A | 255.0.0.0 (/8) | ✅ Yes |
| 172.31.200.10 | B | 255.255.0.0 (/16) | ✅ Yes |
| 192.168.100.50 | C | 255.255.255.0 (/24) | ✅ Yes |
| 224.0.0.5 | D | N/A (Multicast) | ❌ No |
| 126.255.255.255 | A | 255.0.0.0 (/8) | ❌ No |

**Note**: 
- Class A: 1-126 (127 reserved for loopback)
- Class B: 128-191
- Class C: 192-223
- Class D: 224-239 (Multicast)
- Class E: 240-255 (Reserved)
</details>

---

### Bài 4: Point-to-Point links
**Đề**: Bạn có 5 routers cần kết nối point-to-point. Dùng network 192.168.50.0/24, hãy chia subnet cho các links.

<details>
<summary>💡 Hints</summary>

- Mỗi P2P link cần 2 hosts
- Dùng /30 (2 usable hosts)
- 5 routers → 4 links (tính số links: n routers = n-1 links nếu kết nối tuần tự)
</details>

<details>
<summary>✅ Đáp án</summary>

**P2P link cần /30** (2 usable hosts)
- Block size: 4
- Mỗi link chiếm 4 địa chỉ

**Chia subnet**:
| Link | Network | Router 1 | Router 2 | Broadcast |
|------|---------|----------|----------|-----------|
| R1-R2 | 192.168.50.0/30 | .1 | .2 | .3 |
| R2-R3 | 192.168.50.4/30 | .5 | .6 | .7 |
| R3-R4 | 192.168.50.8/30 | .9 | .10 | .11 |
| R4-R5 | 192.168.50.12/30 | .13 | .14 | .15 |

**Còn lại**: 192.168.50.16/28 đến 192.168.50.255/32
</details>

---

## 📊 Phần 2: VLSM - Variable Length Subnet Mask

### Bài 5: VLSM cơ bản
**Đề**: Chia network 172.20.0.0/16 cho các yêu cầu sau:
- Department A: 1000 hosts
- Department B: 500 hosts
- Department C: 250 hosts
- Department D: 100 hosts
- 3 P2P links

<details>
<summary>💡 Hints</summary>

1. Sắp xếp giảm dần
2. Tính CIDR: 2^h - 2 ≥ hosts cần
3. Gán từ lớn đến nhỏ
</details>

<details>
<summary>✅ Đáp án</summary>

**Sắp xếp requirements**:
1. Dept A: 1000 hosts → /22 (1022 hosts)
2. Dept B: 500 hosts → /23 (510 hosts)
3. Dept C: 250 hosts → /24 (254 hosts)
4. Dept D: 100 hosts → /25 (126 hosts)
5. Link 1-3: 2 hosts → /30 (2 hosts)

**VLSM Table**:
| Network | Hosts | CIDR | Network Address | Range | Broadcast |
|---------|-------|------|-----------------|-------|-----------|
| Dept A | 1000 | /22 | 172.20.0.0 | .0.1 - .3.254 | 172.20.3.255 |
| Dept B | 500 | /23 | 172.20.4.0 | .4.1 - .5.254 | 172.20.5.255 |
| Dept C | 250 | /24 | 172.20.6.0 | .6.1 - .6.254 | 172.20.6.255 |
| Dept D | 100 | /25 | 172.20.7.0 | .7.1 - .7.126 | 172.20.7.127 |
| Link 1 | 2 | /30 | 172.20.7.128 | .128-.129 | 172.20.7.131 |
| Link 2 | 2 | /30 | 172.20.7.132 | .132-.133 | 172.20.7.135 |
| Link 3 | 2 | /30 | 172.20.7.136 | .136-.137 | 172.20.7.139 |

**Tổng sử dụng**: ~1876 hosts
**Còn lại**: 172.20.7.140 → 172.20.255.255
</details>

---

### Bài 6: VLSM phức tạp
**Đề**: Công ty có network 10.10.0.0/16. Chia cho:
- HQ: 8000 hosts
- Branch 1: 4000 hosts
- Branch 2: 2000 hosts
- Branch 3: 1000 hosts
- Branch 4: 500 hosts
- Remote offices: 10 sites, 50 hosts mỗi site
- WAN links: 15 links

<details>
<summary>✅ Đáp án</summary>

**VLSM Solution**:

| Network | Hosts | CIDR | Network | First | Last | Broadcast |
|---------|-------|------|---------|-------|------|-----------|
| HQ | 8000 | /19 | 10.10.0.0 | .0.1 | .31.254 | 10.10.31.255 |
| Branch 1 | 4000 | /20 | 10.10.32.0 | .32.1 | .47.254 | 10.10.47.255 |
| Branch 2 | 2000 | /21 | 10.10.48.0 | .48.1 | .55.254 | 10.10.55.255 |
| Branch 3 | 1000 | /22 | 10.10.56.0 | .56.1 | .59.254 | 10.10.59.255 |
| Branch 4 | 500 | /23 | 10.10.60.0 | .60.1 | .61.254 | 10.10.61.255 |
| Remote 1-10 | 50 | /26 | 10.10.62.0-62.192 | Varies | Varies | Varies |
| WAN 1-15 | 2 | /30 | 10.10.63.0-63.56 | Varies | Varies | Varies |

**Chi tiết Remote Offices** (10 sites × /26):
- Each /26 = 62 hosts
- 10.10.62.0/26, 10.10.62.64/26, ..., 10.10.62.192/26

**Chi tiết WAN Links** (15 links × /30):
- Each /30 = 2 hosts
- 10.10.63.0/30, 10.10.63.4/30, ..., 10.10.63.56/30

**Tổng kết**:
- Đã dùng: ~16,000 addresses
- Còn lại: 10.10.63.60 → 10.10.255.255
- % used: ~25% of /16
</details>

---

## 🔥 Phần 3: Bài tập nâng cao

### Bài 7: Tìm lỗi Subnet
**Đề**: Tìm lỗi trong các thiết kế subnet sau:

**Scenario A**:
```
Network: 192.168.1.0/24
Subnet 1: 192.168.1.0/26 (0-63)
Subnet 2: 192.168.1.60/26 (60-123)
Subnet 3: 192.168.1.128/26 (128-191)
```

**Scenario B**:
```
Network: 10.0.0.0/8
LAN A: 10.0.0.0/25 (126 hosts, need 200)
LAN B: 10.0.1.0/24 (254 hosts, need 100)
```

<details>
<summary>✅ Đáp án</summary>

**Scenario A - Lỗi: OVERLAP**
- Subnet 1: 0-63
- Subnet 2: 60-123 ❌ **OVERLAP với Subnet 1 (60-63)**

**Fix**:
```
Subnet 1: 192.168.1.0/26 (0-63)
Subnet 2: 192.168.1.64/26 (64-127) ✅
Subnet 3: 192.168.1.128/26 (128-191) ✅
Subnet 4: 192.168.1.192/26 (192-255) ✅
```

**Scenario B - Lỗi: KHÔNG TỐI ƯU**
- LAN A cần 200 hosts nhưng chỉ có /25 (126 hosts) ❌
- LAN B chỉ cần 100 hosts nhưng dùng /24 (254 hosts) - lãng phí

**Fix**:
```
LAN A: 10.0.0.0/24 (254 hosts) ✅
LAN B: 10.0.1.0/25 (126 hosts) ✅
```
</details>

---

### Bài 8: Summarization
**Đề**: Summarize các routes sau thành 1 summary route:
```
192.168.16.0/24
192.168.17.0/24
192.168.18.0/24
192.168.19.0/24
192.168.20.0/24
192.168.21.0/24
192.168.22.0/24
192.168.23.0/24
```

<details>
<summary>💡 Hints</summary>

1. Convert sang binary
2. Tìm phần chung
3. Count số bits chung
</details>

<details>
<summary>✅ Đáp án</summary>

**Bước 1: Binary conversion**
```
192.168.16.0  = 11000000.10101000.00010000.00000000
192.168.17.0  = 11000000.10101000.00010001.00000000
...
192.168.23.0  = 11000000.10101000.00010111.00000000
```

**Bước 2: Tìm phần chung**
```
192.168.16-23 = octet 3 từ 16-23
Binary range:
16 = 00010000
23 = 00010111
Chung: 00010xxx (5 bits chung)
```

**Bước 3: Calculate CIDR**
- 24 bits (3 octets đầu) + 5 bits (octet 3) = 29 bits
- Nhưng phải align: 16-23 = 8 addresses
- 8 = 2^3 → cần 3 bits cho hosts
- CIDR: 24 - 3 = **21 bits**... KHÔNG!

**Đúng**:
- Range: 16-23 = 8 IPs trong octet 3
- Nhưng mỗi IP là /24, tổng = 8 × 256 = 2048 addresses
- 2048 = 2^11 → cần 11 bits
- Summary: 32 - 11 = **/21**
- Network: **192.168.16.0/21**

**Verify**:
- 192.168.16.0/21 covers 192.168.16.0 - 192.168.23.255 ✅

**Alternative method**:
- Start: 16 = 00010000
- End: 23 = 00010111
- Common bits: 00010 (5 bits)
- CIDR: 16 + 5 = 21
- Summary: **192.168.16.0/21**
</details>

---

### Bài 9: Wildcard mask
**Đề**: Convert các subnet masks sau sang wildcard masks và ngược lại:
- a) 255.255.255.0
- b) 255.255.240.0
- c) 0.0.15.255
- d) 0.0.0.31

<details>
<summary>✅ Đáp án</summary>

**Formula**: Wildcard = 255.255.255.255 - Subnet Mask

**Kết quả**:

| Subnet Mask | Wildcard Mask | CIDR |
|-------------|---------------|------|
| 255.255.255.0 | 0.0.0.255 | /24 |
| 255.255.240.0 | 0.0.15.255 | /20 |
| 255.255.248.0 ← | 0.0.7.255 → | /21 |
| 255.255.255.224 ← | 0.0.0.31 → | /27 |

**Ứng dụng**: Wildcard masks dùng trong ACL (Access Control Lists)

**Example ACL**:
```
access-list 10 permit 192.168.1.0 0.0.0.255
# Cho phép subnet 192.168.1.0/24
```
</details>

---

## 🎯 Phần 4: Tình huống thực tế

### Bài 10: Thiết kế network doanh nghiệp
**Đề**: Công ty ABC có network 172.16.0.0/16. Thiết kế VLSM cho:

**Headquarters (HQ)**:
- Sales: 600 employees
- Engineering: 400 employees
- HR: 100 employees
- Finance: 50 employees
- Servers: 30 servers
- Management: 20 devices
- Guest WiFi: 200 devices

**Branch Offices**:
- Branch A: 200 employees
- Branch B: 150 employees
- Branch C: 100 employees

**Infrastructure**:
- 5 WAN links (HQ ↔ Branches)
- 10 inter-VLAN routing links

**Requirements**:
1. Dự phòng 30% cho mỗi subnet
2. Optimize address usage
3. Summarization cho routing

<details>
<summary>✅ Đáp án</summary>

**Tính toán với growth 30%**:
- Sales: 600 × 1.3 = 780 → Need 1022 (/22)
- Engineering: 400 × 1.3 = 520 → Need 1022 (/22)
- Branch A: 200 × 1.3 = 260 → Need 510 (/23)
- Guest WiFi: 200 × 1.3 = 260 → Need 510 (/23)
- Branch B: 150 × 1.3 = 195 → Need 254 (/24)
- HR: 100 × 1.3 = 130 → Need 254 (/24)
- Branch C: 100 × 1.3 = 130 → Need 254 (/24)
- Finance: 50 × 1.3 = 65 → Need 126 (/25)
- Servers: 30 × 1.3 = 39 → Need 62 (/26)
- Management: 20 × 1.3 = 26 → Need 30 (/27)
- WAN (5 links): /30 each
- Inter-VLAN (10): /30 each

**VLSM Design**:

```
HQ (172.16.0.0/17 summary):
├─ Sales:        172.16.0.0/22   (1022 hosts)
├─ Engineering:  172.16.4.0/22   (1022 hosts)
├─ Guest WiFi:   172.16.8.0/23   (510 hosts)
├─ HR:           172.16.10.0/24  (254 hosts)
├─ Finance:      172.16.11.0/25  (126 hosts)
├─ Servers:      172.16.11.128/26 (62 hosts)
└─ Management:   172.16.11.192/27 (30 hosts)

Branches (172.16.128.0/18 summary):
├─ Branch A:     172.16.128.0/23 (510 hosts)
├─ Branch B:     172.16.130.0/24 (254 hosts)
└─ Branch C:     172.16.131.0/24 (254 hosts)

WAN Links (172.16.192.0/27):
├─ HQ-BranchA:   172.16.192.0/30
├─ HQ-BranchB:   172.16.192.4/30
├─ HQ-BranchC:   172.16.192.8/30
├─ Inter-links:  172.16.192.12-192.51 (/30 each)
```

**Routing Table (Summarized)**:
```
172.16.0.0/17    → HQ networks
172.16.128.0/18  → Branch networks
172.16.192.0/27  → WAN links
```

**Benefits**:
- ✅ Proper segmentation
- ✅ 30% growth capacity
- ✅ Efficient addressing
- ✅ Easy to route & manage
- ✅ Summarization reduces routing table
</details>

---

## 💪 Challenge: Speed Test

**Mục tiêu**: Tính nhanh trong 30 giây mỗi câu!

### Speed Round 1
1. 192.168.5.78/28 → Network address?
2. 10.20.30.0/22 → Số hosts?
3. 172.16.100.50/26 → Broadcast?

<details>
<summary>Đáp án</summary>

1. **192.168.5.64/28** (block 16, 78÷16=4.x → 4×16=64)
2. **1022 hosts** (32-22=10 bits → 2^10-2=1022)
3. **172.16.100.63** (block 64, 50÷64=0.x → broadcast=63)
</details>

### Speed Round 2
1. /25 = ? hosts
2. 255.255.252.0 = /?
3. 192.168.1.0/24 → /26 = ? subnets

<details>
<summary>Đáp án</summary>

1. **126 hosts** (2^7-2)
2. **/22** (count 1s: 11111111.11111111.11111100.00000000 = 22)
3. **4 subnets** (borrow 2 bits: 2^2=4)
</details>

---

## 📖 Resources & Tools

- [Interactive Subnet Calculator](../index.md#subnet-calc) - Dùng calculator để verify
- [VLSM Calculator](../index.md#vlsm) - Tính VLSM tự động
- [Subnet Reference](subnet-reference.md) - Bảng tra cứu đầy đủ

---

## 🎓 Tips học tốt Subnetting

1. **Nhớ công thức**:
   - Hosts = 2^h - 2
   - Subnets = 2^n
   - Block size = 256 - subnet octet

2. **Practice**:
   - Làm ít nhất 10 bài mỗi ngày
   - Time yourself
   - Không dùng calculator ban đầu

3. **Patterns**:
   - /24 = 254 hosts (phổ biến nhất)
   - /30 = 2 hosts (P2P links)
   - /29 = 6 hosts (small networks)
   - /26 = 62 hosts (medium networks)

4. **Binary thinking**:
   - Học đếm binary nhanh
   - Nhận diện powers of 2
   - Convert decimal ↔ binary

---

**Chúc bạn học tốt! 🚀** [← Back to Calculator](../index.md)