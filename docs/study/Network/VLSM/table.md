# 🧮 Subnet Masks Table

Bảng dưới đây liệt kê các subnet phổ biến cùng với prefix, số địa chỉ và subnet mask tương ứng.  
> **Gợi ý:** Mỗi lần giảm prefix (/n → /n-1) thì số địa chỉ tăng gấp đôi.

<style>
.md-typeset table {
  margin-left: auto;
  margin-right: auto;
  width: fit-content;
  display: table;
}
.md-typeset th, .md-typeset td {
  text-align: center;
  padding: 6px 12px;
}
.md-typeset th {
  background-color: #f4f4f4;
}
</style>

| Number of Addresses | Number of Bits | Prefix | Subnet Mask        |
|:-------------------:|:--------------:|:------:|:-------------------|
| 1        | 0  | /32 | 255.255.255.255 |
| 2        | 1  | /31 | 255.255.255.254 |
| 4        | 2  | /30 | 255.255.255.252 |
| 8        | 3  | /29 | 255.255.255.248 |
| 16       | 4  | /28 | 255.255.255.240 |
| 32       | 5  | /27 | 255.255.255.224 |
| 64       | 6  | /26 | 255.255.255.192 |
| 128      | 7  | /25 | 255.255.255.128 |
| 256      | 8  | /24 | 255.255.255.0   |
| 512      | 9  | /23 | 255.255.254.0   |
| 1,024    | 10 | /22 | 255.255.252.0   |
| 2,048    | 11 | /21 | 255.255.248.0   |
| 4,096    | 12 | /20 | 255.255.240.0   |
| 8,192    | 13 | /19 | 255.255.224.0   |
| 16,384   | 14 | /18 | 255.255.192.0   |
| 32,768   | 15 | /17 | 255.255.128.0   |
| 65,536   | 16 | /16 | 255.255.0.0     |
| 131,072  | 17 | /15 | 255.254.0.0     |
| 262,144  | 18 | /14 | 255.252.0.0     |
| 524,288  | 19 | /13 | 255.248.0.0     |
| 1,048,576| 20 | /12 | 255.240.0.0     |
| 2,097,152| 21 | /11 | 255.224.0.0     |
| 4,194,304| 22 | /10 | 255.192.0.0     |
| 8,388,608| 23 | /9  | 255.128.0.0     |
| 16,777,216|24 | /8  | 255.0.0.0       |

---

✅ **Ghi chú:**
- “Number of Addresses” bao gồm cả network & broadcast.
- “Usable Hosts” = (Number of Addresses) − 2 (trừ network & broadcast).
- CIDR /32 thường dùng cho địa chỉ host đơn, /24 là subnet phổ biến cho mạng LAN.

---

> Muốn mở rộng thêm phần tính toán động (nhập prefix → hiện kết quả)?  
> Có thể chèn thêm JS vào file này bằng cách:
> ```yaml
> extra_javascript:
>   - assets/js/subnet.js
> ```
> rồi dùng form HTML trong markdown như ví dụ trước.
