---
title: Khu vực học tập
hide:
  - navigation
  - toc
---

# 📚 Khu vực học tập chuyên ngành

Tổng hợp kiến thức IT, mạng máy tính, an toàn thông tin và các môn học chuyên ngành.

---

## 📊 Thống kê học tập

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-icon">📖</div>
    <div class="stat-number">12</div>
    <div class="stat-label">Môn học</div>
  </div>
  <div class="stat-card">
    <div class="stat-icon">📝</div>
    <div class="stat-number">156</div>
    <div class="stat-label">Bài học</div>
  </div>
  <div class="stat-card">
    <div class="stat-icon">💡</div>
    <div class="stat-number">89</div>
    <div class="stat-label">Lab thực hành</div>
  </div>
  <div class="stat-card">
    <div class="stat-icon">✅</div>
    <div class="stat-number">78%</div>
    <div class="stat-label">Hoàn thành</div>
  </div>
</div>

---

<div class="grid cards" markdown>

-   :material-network:{ .lg .middle } __Quản trị mạng và hệ thống__

    ---
    Linux System Admin, Windows Server, Active Directory, DNS, DHCP
    
    [:octicons-arrow-right-24: Network/](Network/)

-   :material-security-network:{ .lg .middle } __An toàn mạng__

    ---
    Firewall, IDS/IPS, Security Policies, Penetration Testing
    
    [:octicons-arrow-right-24: Security Network/](Security Network/)

-   :material-router-wireless:{ .lg .middle } __Cấu hình mạng__

    ---
    Cisco Routing & Switching, VLAN, STP, OSPF, BGP
    
    [:octicons-arrow-right-24: Network/](Network/)

-   :material-layers:{ .lg .middle } __Mô hình OSI & TCP/IP__

    ---
    7 tầng OSI, Protocols, Encapsulation, Troubleshooting
    
    [:octicons-arrow-right-24: Network/osi-model.md](Network/osi-model.md)

-   :material-wifi-strength-4-lock:{ .lg .middle } __Wireless Security__

    ---
    WPA2/WPA3, Wireless Attacks, Aircrack-ng
    
    [:octicons-arrow-right-24: Security Network/](Security Network/)

-   :material-bug:{ .lg .middle } __Penetration Testing__

    ---
    Metasploit, Burp Suite, SQL Injection, XSS
    
    [:octicons-arrow-right-24: Security Network/](Security Network/)

-   :material-assembly-variant:{ .lg .middle } __Assembly x86__

    ---
    Low-level programming, Reverse Engineering
    
    [:octicons-arrow-right-24: Assembly x86/](Assembly x86/)

-   :material-flag:{ .lg .middle } __CTF Challenges__

    ---
    Capture The Flag, Security challenges
    
    [:octicons-arrow-right-24: CTF/](CTF/)

-   :material-cloud-lock:{ .lg .middle } __Cloud Security__

    ---
    AWS Security, Azure Security, IAM, Encryption
    
    [:octicons-arrow-right-24: Đang cập nhật]()

-   :material-robot-outline:{ .lg .middle } __AI & ML__

    ---
    Machine Learning, Deep Learning, Neural Networks
    
    [:octicons-arrow-right-24: Đang cập nhật]()

-   :material-database:{ .lg .middle } __Database Administration__

    ---
    MySQL, PostgreSQL, MongoDB, Redis
    
    [:octicons-arrow-right-24: Đang cập nhật]()

-   :material-docker:{ .lg .middle } __DevOps & Containerization__

    ---
    Docker, Kubernetes, CI/CD, Jenkins
    
    [:octicons-arrow-right-24: Đang cập nhật]()

</div>

<style>
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin: 40px 0;
}

.stat-card {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  border: 2px solid rgba(102, 126, 234, 0.3);
  border-radius: 15px;
  padding: 25px;
  text-align: center;
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
}

.stat-icon {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #667eea;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 0.95rem;
  color: #666;
  font-weight: 500;
}

[data-md-color-scheme="slate"] .stat-label {
  color: #aaa;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

---

## 🎯 Lộ trình học tập

```mermaid
graph TB
    A[Fundamentals] --> B[Networking Basics]
    B --> C[System Administration]
    C --> D[Security Fundamentals]
    D --> E[Advanced Topics]
    
    B --> B1[OSI Model]
    B --> B2[TCP/IP]
    B --> B3[Routing & Switching]
    
    C --> C1[Linux Admin]
    C --> C2[Windows Server]
    C --> C3[Scripting]
    
    D --> D1[Firewall]
    D --> D2[IDS/IPS]
    D --> D3[Encryption]
    
    E --> E1[Penetration Testing]
    E --> E2[Cloud Security]
    E --> E3[DevSecOps]
    
    style A fill:#28a745,color:#fff
    style E fill:#dc3545,color:#fff
```