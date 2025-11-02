# 🎓 VLSM - Variable Length Subnet Mask Tutorial

Hướng dẫn chi tiết về VLSM từ cơ bản đến nâng cao với ví dụ thực tế.

---

## 📚 Mục lục

1. [VLSM là gì?](#vlsm-là-gì)
2. [Tại sao cần VLSM?](#tại-sao-cần-vlsm)
3. [Quy trình VLSM](#quy-trình-vlsm)
4. [Ví dụ chi tiết](#ví-dụ-chi-tiết)
5. [Best Practices](#best-practices)
6. [Common Mistakes](#common-mistakes)
7. [Advanced Topics](#advanced-topics)

---

## 🤔 VLSM là gì?

**VLSM** (Variable Length Subnet Mask) là kỹ thuật chia subnet với **độ dài mask khác nhau** trong cùng một network để tối ưu sử dụng địa chỉ IP.

### So sánh: Fixed-Length vs VLSM

#### Fixed-Length Subnetting (Cũ)
```
Network: 192.168.1.0/24
Chia thành 4 subnets bằng nhau (/26):

Subnet 1: 192.168.1.0/26    → 62 hosts
Subnet 2: 192.168.1.64/26   → 62 hosts
Subnet 3: 192.168.1.128/26  → 62 hosts
Subnet 4: 192.168.1.192/26  → 62 hosts
```

**Vấn đề**: 
- Nếu Subnet 1 cần 100 hosts → Không đủ! ❌
- Nếu Subnet 4 chỉ cần 2 hosts → Lãng phí 60 addresses! ❌

#### VLSM (Mới - Tối ưu)
```
Network: 192.168.1.0/24
Chia theo nhu cầu:

Subnet 1: 192.168.1.0/25    → 126 hosts (cho 100 hosts)
Subnet 2: 192.168.1.128/26  → 62 hosts (cho 50 hosts)
Subnet 3: 192.168.1.192/27  → 30 hosts (cho 20 hosts)
Subnet 4: 192.168.1.224/30  → 2 hosts (cho P2P link)
```

**Lợi ích**:
- ✅ Đáp ứng đủ nhu cầu
- ✅ Tiết kiệm địa chỉ IP
- ✅ Linh hoạt mở rộng

---

## 💡 Tại sao cần VLSM?

### 1. **Tiết kiệm địa chỉ IP**

**Ví dụ**: Công ty có 4 LANs
- LAN A: 100 users
- LAN B: 50 users
- LAN C: 20 users
- WAN Link: 2 routers

**Không VLSM** (Fixed /26):
```
Total: 4 × 62 = 248 addresses
Lãng phí: 248 - 172 = 76 addresses (31%)
```

**Có VLSM**:
```
/25 (126) + /26 (62) + /27 (30) + /30 (2) = 220 addresses
Lãng phí: 220 - 172 = 48 addresses (22%)
Tiết kiệm: 28 addresses!
```

### 2. **Flexibility trong thiết kế**

- Subnet lớn cho departments
- Subnet vừa cho labs
- Subnet nhỏ cho management
- /30 cho WAN links

### 3. **Summarization hiệu quả**

VLSM cho phép tổng hợp routes tốt hơn → giảm routing table size.

### 4. **Growth planning**

Dễ dàng mở rộng từng subnet riêng lẻ mà không ảnh hưởng toàn bộ network.

---

## 📋 Quy trình VLSM - 6 Bước

### Bước 1: **Liệt kê Requirements**

Xác định tất cả subnets cần và số hosts mỗi subnet.

**Ví dụ**:
```
LAN A: 100 hosts
LAN B: 50 hosts
LAN C: 20 hosts
Server Farm: 10 servers
Management: 5 devices
WAN Link 1: 2 routers
WAN Link 2: 2 routers
```

### Bước 2: **Sắp xếp giảm dần**

Sắp xếp theo số hosts từ **lớn nhất → nhỏ nhất**.

```
1. LAN A: 100 hosts
2. LAN B: 50 hosts
3. LAN C: 20 hosts
4. Server Farm: 10 servers
5. Management: 5 devices
6. WAN Link 1: 2 routers
7. WAN Link 2: 2 routers
```

### Bước 3: **Tính CIDR cho từng subnet**

Dùng công thức: **2^h - 2 ≥ hosts cần**

| Requirement | Hosts cần | 2^h - 2 | h | CIDR | Usable |
|-------------|-----------|---------|---|------|--------|
| LAN A | 100 | 2^7-2=126 | 7 | /25 | 126 |
| LAN B | 50 | 2^6-2=62 | 6 | /26 | 62 |
| LAN C | 20 | 2^5-2=30 | 5 | /27 | 30 |
| Server Farm | 10 | 2^4-2=14 | 4 | /28 | 14 |
| Management | 5 | 2^3-2=6 | 3 | /29 | 6 |
| WAN 1,2 | 2 | 2^2-2=2 | 2 | /30 | 2 |

**Chú ý**: CIDR = 32 - h

### Bước 4: **Gán địa chỉ subnet**

Bắt đầu từ network address gốc, gán **từ lớn đến nhỏ**.

**Base network**: 192.168.1.0/24

#### LAN A (/25):
- Block size: 2^7 = 128
- Network: **192.168.1.0/25**
- Range: 192.168.1.1 - 192.168.1.126
- Broadcast: 192.168.1.127
- **Next available**: 192.168.1.128

#### LAN B (/26):
- Block size: 2^6 = 64
- Start from: 192.168.1.128
- Network: **192.168.1.128/26**
- Range: 192.168.1.129 - 192.168.1.190
- Broadcast: 192.168.1.191
- **Next available**: 192.168.1.192

#### LAN C (/27):
- Block size: 2^5 = 32
- Start from: 192.168.1.192
- Network: **192.168.1.192/27**
- Range: 192.168.1.193 - 192.168.1.222
- Broadcast: 192.168.1.223
- **Next available**: 192.168.1.224

#### Server Farm (/28):
- Block size: 2^4 = 16
- Network: **192.168.1.224/28**
- Range: 192.168.1.225 - 192.168.1.238
- Broadcast: 192.168.1.239
- **Next available**: 192.168.1.240

#### Management (/29):
- Block size: 2^3 = 8
- Network: **192.168.1.240/29**
- Range: 192.168.1.241 - 192.168.1.246
- Broadcast: 192.168.1.247
- **Next available**: 192.168.1.248

#### WAN Link 1 (/30):
- Block size: 2^2 = 4
- Network: **192.168.1.248/30**
- Range: 192.168.1.249 - 192.168.1.250
- Broadcast: 192.168.1.251
- **Next available**: 192.168.1.252

#### WAN Link 2 (/30):
- Network: **192.168.1.252/30**
- Range: 192.168.1.253 - 192.168.1.254
- Broadcast: 192.168.1.255

### Bước 5: **Vẽ sơ đồ**

```
                    Internet
                        |
                   [Router]
                        |
        +---------------+---------------+
        |               |               |
    [Switch]        [Switch]        [Switch]
    LAN A           LAN B           LAN C
   /25 (126)       /26 (62)        /27 (30)
```

### Bước 6: **Verification (Kiểm tra)**

Checklist:
- [ ] Tất cả subnets đủ hosts?
- [ ] Không có overlap?
- [ ] Căn chỉnh block size đúng?
- [ ] Còn địa chỉ dự phòng?

---

## 🎯 Ví dụ chi tiết: Thiết kế Enterprise Network

### Đề bài

**Công ty XYZ** có network **10.50.0.0/16** cần chia cho:

**Headquarters**:
- Sales Department: 500 employees
- Engineering: 300 employees
- HR: 100 employees
- Finance: 50 employees
- Datacenter: 30 servers
- Printers: 20 devices
- Management: 10 switches

**Branch Offices**:
- Branch A: 200 employees
- Branch B: 150 employees
- Branch C: 100 employees

**Infrastructure**:
- 5 WAN links (HQ ↔ Branches)
- DMZ: 10 public servers

### Giải pháp

#### Bước 1: List & Sort

```
1. Sales: 500 → need 510 (2^9-2=510) → /23
2. Engineering: 300 → need 510 → /23
3. Branch A: 200 → need 254 (2^8-2=254) → /24
4. Branch B: 150 → need 254 → /24
5. HR: 100 → need 126 (2^7-2=126) → /25
6. Branch C: 100 → need 126 → /25
7. Finance: 50 → need 62 (2^6-2=62) → /26
8. Datacenter: 30 → need 30 (2^5-2=30) → /27
9. Printers: 20 → need 30 → /27
10. DMZ: 10 → need 14 (2^4-2=14) → /28
11. Management: 10 → need 14 → /28
12. WAN 1-5: 2 each → /30
```

#### Bước 2: VLSM Table

| Network | Hosts | CIDR | Network Address | First Host | Last Host | Broadcast | Subnet Mask |
|---------|-------|------|-----------------|------------|-----------|-----------|-------------|
| Sales | 500 | /23 | 10.50.0.0 | 10.50.0.1 | 10.50.1.254 | 10.50.1.255 | 255.255.254.0 |
| Engineering | 300 | /23 | 10.50.2.0 | 10.50.2.1 | 10.50.3.254 | 10.50.3.255 | 255.255.254.0 |
| Branch A | 200 | /24 | 10.50.4.0 | 10.50.4.1 | 10.50.4.254 | 10.50.4.255 | 255.255.255.0 |
| Branch B | 150 | /24 | 10.50.5.0 | 10.50.5.1 | 10.50.5.254 | 10.50.5.255 | 255.255.255.0 |
| HR | 100 | /25 | 10.50.6.0 | 10.50.6.1 | 10.50.6.126 | 10.50.6.127 | 255.255.255.128 |
| Branch C | 100 | /25 | 10.50.6.128 | 10.50.6.129 | 10.50.6.254 | 10.50.6.255 | 255.255.255.128 |
| Finance | 50 | /26 | 10.50.7.0 | 10.50.7.1 | 10.50.7.62 | 10.50.7.63 | 255.255.255.192 |
| Datacenter | 30 | /27 | 10.50.7.64 | 10.50.7.65 | 10.50.7.94 | 10.50.7.95 | 255.255.255.224 |
| Printers | 20 | /27 | 10.50.7.96 | 10.50.7.97 | 10.50.7.126 | 10.50.7.127 | 255.255.255.224 |
| DMZ | 10 | /28 | 10.50.7.128 | 10.50.7.129 | 10.50.7.142 | 10.50.7.143 | 255.255.255.240 |
| Management | 10 | /28 | 10.50.7.144 | 10.50.7.145 | 10.50.7.158 | 10.50.7.159 | 255.255.255.240 |
| WAN 1 | 2 | /30 | 10.50.7.160 | 10.50.7.161 | 10.50.7.162 | 10.50.7.163 | 255.255.255.252 |
| WAN 2 | 2 | /30 | 10.50.7.164 | 10.50.7.165 | 10.50.7.166 | 10.50.7.167 | 255.255.255.252 |
| WAN 3 | 2 | /30 | 10.50.7.168 | 10.50.7.169 | 10.50.7.170 | 10.50.7.171 | 255.255.255.252 |
| WAN 4 | 2 | /30 | 10.50.7.172 | 10.50.7.173 | 10.50.7.174 | 10.50.7.175 | 255.255.255.252 |
| WAN 5 | 2 | /30 | 10.50.7.176 | 10.50.7.177 | 10.50.7.178 | 10.50.7.179 | 255.255.255.252 |

#### Bước 3: Summarization

**HQ Subnets** (10.50.0.0 - 10.50.7.159):
- Summary: **10.50.0.0/20** covers 10.50.0.0 - 10.50.15.255

**Branch Subnets** (10.50.4.0/24, 10.50.5.0/24, 10.50.6.128/25):
- Can be summarized: **10.50.4.0/22** covers 10.50.4.0 - 10.50.7.255

**WAN Links** (10.50.7.160 - 10.50.7.179):
- Summary: **10.50.7.160/27**

#### Bước 4: Routing Table (Optimized)

```
# Core Router
10.50.0.0/20     → HQ (all departments)
10.50.4.0/22     → Branches
10.50.7.160/27   → WAN links

# Total routes: 3 (instead of 17!)
```

#### Bước 5: Tổng kết

**Sử dụng**:
- Addresses used: ~2,100 / 65,536 ≈ **3.2%**
- Available for growth: **96.8%**
- Routing entries: **3 summary routes**
- Subnets created: **17**

**Còn lại cho mở rộng**:
- 10.50.8.0 - 10.50.255.255 (available)

---

## 💎 Best Practices

### 1. **Planning trước khi implement**

```
Bad Practice ❌:
- Chia subnet rồi mới design
- Không xem xét mở rộng

Good Practice ✅:
- Survey nhu cầu hiện tại + dự kiến 3-5 năm
- Document đầy đủ
- Review với team
```

### 2. **Reserved space cho growth**

```
Rule of thumb:
- Small networks: +50% capacity
- Medium: +100%
- Enterprise: +200%

Ví dụ: Cần 100 hosts
→ Plan cho 200-300 hosts
→ Chọn /23 (510) thay vì /25 (126)
```

### 3. **Consistent numbering scheme**

```
Good Scheme ✅:
10.0.0.0/16   → HQ
10.1.0.0/16   → Branch 1
10.2.0.0/16   → Branch 2
...
10.10.0.0/16  → Remote sites
10.20.0.0/16  → WAN links
```

### 4. **Document everything**

```
Minimum documentation:
- Network diagram
- IP addressing table
- VLAN assignments
- Gateway addresses
- DNS/DHCP ranges
- Change log
```

### 5. **Use private IP ranges properly**

```
Large networks:   10.0.0.0/8
Medium:           172.16.0.0/12
Small/Home:       192.168.0.0/16

Don't mix randomly!
```

### 6. **Align to block boundaries**

```
Bad ❌:
192.168.1.17/28  (misaligned)

Good ✅:
192.168.1.16/28  (aligned to block of 16)
```

---

## ⚠️ Common Mistakes

### Mistake 1: **Không sắp xếp theo size**

```
❌ Wrong:
LAN A (20 hosts): 192.168.1.0/27
LAN B (100 hosts): 192.168.1.32/25  → Overlap!

✅ Correct:
LAN B (100): 192.168.1.0/25
LAN A (20): 192.168.1.128/27
```

### Mistake 2: **Quên -2 hosts**

```
❌ Wrong:
Need 30 hosts → /27 gives 32 addresses → OK

✅ Correct:
Need 30 hosts → /27 gives 2^5-2=30 usable → OK
Need 32 hosts → /27 gives 30 → NOT enough!
                → Need /26 (62 hosts)
```

### Mistake 3: **Overlap subnets**

```
❌ Wrong:
Subnet 1: 10.0.0.0/24
Subnet 2: 10.0.0.128/25  → Inside Subnet 1!

✅ Correct:
Subnet 1: 10.0.0.0/24
Subnet 2: 10.0.1.0/25    → No overlap
```

### Mistake 4: **Không dự phòng**

```
❌ Wrong:
Need 100 hosts → Give /25 (126) → Only 26 spare

✅ Better:
Need 100 hosts → Give /24 (254) → 154 spare (growth)
```

### Mistake 5: **Lãng phí /30**

```
❌ Wrong:
P2P link cần 2 hosts → Dùng /29 (6 hosts) → Waste!

✅ Correct:
P2P link → Dùng /30 (2 hosts) → Perfect!
Or /31 (RFC 3021) for point-to-point
```

---

## 🚀 Advanced Topics

### 1. **Summarization & Supernetting**

**VLSM cho phép summarization hiệu quả**:

```
Original subnets:
192.168.16.0/24
192.168.17.0/24
192.168.18.0/24
192.168.19.0/24

Binary:
192.168.00010000.0  /24
192.168.00010001.0  /24
192.168.00010010.0  /24
192.168.00010011.0  /24

Common bits: 00010xxx (5 bits)
Summary: 192.168.16.0/21 ✅
```

### 2. **Classless Inter-Domain Routing (CIDR)**

VLSM là một phần của CIDR:
- Không phụ thuộc vào class
- Flexible prefix length
- Efficient aggregation

### 3. **VLSM với IPv6**

IPv6 cũng dùng VLSM:
```
2001:db8::/32  → Organization
2001:db8:1::/48  → Site
2001:db8:1:1::/64  → Subnet
```

### 4. **Hierarchical Design**

```
Layer 1 (Core):     10.0.0.0/8
Layer 2 (Regional): 10.X.0.0/16
Layer 3 (Site):     10.X.Y.0/24
Layer 4 (Subnet):   10.X.Y.Z/varying
```

### 5. **Automation Tools**

```bash
# Python example
import ipaddress

def vlsm(network, requirements):
    net = ipaddress.IPv4Network(network)
    subnets = []
    
    # Sort by size descending
    requirements.sort(key=lambda x: x[1], reverse=True)
    
    current = net.network_address
    
    for name, hosts in requirements:
        # Calculate prefix
        prefix = 32 - (hosts + 2).bit_length()
        subnet = ipaddress.IPv4Network(f"{current}/{prefix}")
        
        subnets.append((name, subnet))
        current = subnet.broadcast_address + 1
    
    return subnets
```

---

## 🎯 Practice Scenarios

### Scenario 1: Multi-site company

```
Network: 172.30.0.0/16
Sites:
- HQ: 1000 users
- Branch 1-5: 200 users each
- Remote: 20 sites, 10 users each
- WAN: 25 links

→ Design VLSM scheme
```

### Scenario 2: ISP allocation

```
Network: 203.0.113.0/24 (Public)
Customers:
- Customer A: /28 (14 hosts)
- Customer B: /29 (6 hosts)
- Customer C: /30 (2 hosts)
- ...

→ Allocate efficiently
```

### Scenario 3: Campus network

```
Network: 10.10.0.0/16
Buildings:
- Building A: 500 devices, 3 floors
- Building B: 300 devices, 2 floors
- Building C: 200 devices, 2 floors
- Datacenter: 100 servers
- WiFi: 1000 concurrent users

→ VLSM + VLAN design
```

---

## 📖 Summary

### Key Takeaways

1. **VLSM = Flexibility**: Khác subnet khác size
2. **Process**: List → Sort → Calculate → Assign → Verify
3. **Formula**: 2^h - 2 ≥ hosts needed
4. **Always**: Document & plan for growth
5. **Avoid**: Overlap, misalignment, no reserves

### When to use VLSM?

✅ Use VLSM when:
- Diverse network sizes
- IP conservation needed
- Hierarchical design
- Want to summarize routes

❌ Maybe not when:
- Very small network (< 50 devices)
- All subnets same size
- Simple flat design

---

## 🔗 Resources

- [🌐 VLSM Calculator](../index.md#vlsm) - Interactive tool
- [📊 Subnet Reference](subnet-reference.md) - Quick lookup
- [🎓 Practice Problems](subnetting-practice.md) - Exercises
- [RFC 1878](https://tools.ietf.org/html/rfc1878) - VLSM tables

---

## 🎓 Next Steps

1. **Practice**: Làm ít nhất 10 bài VLSM
2. **Use calculator**: Verify kết quả với tool
3. **Real design**: Thử thiết kế cho network thật
4. **Study**: Routing protocols (OSPF, EIGRP) hỗ trợ VLSM

---

**Happy subnetting! 🚀** [Try VLSM Calculator →](../index.md#vlsm)