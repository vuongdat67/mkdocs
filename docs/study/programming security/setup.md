---
date:
  created: 2025-10-31
  updated: 2025-10-31
categories:
  - programing
tags:
  - setup
authors:
  - vuongdat67
readtime: 
draft: true
---

# Setup ubuntu


``` bash title="update" linenums="1" 
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y
```

**Công cụ cơ bản:**

``` bash title="tool" linenums="1" hl_lines="1"
sudo apt install -y git curl wget vim nano unzip zip tar htop net-tools build-essential software-properties-common ca-certificates lsb-release gnupg
```

!!! note "Chức năng:"

    - build-essential: biên dịch C/C++
    - net-tools: ifconfig, netstat
    - htop: giám sát CPU, RAM
    - curl/wget/git: tải và quản lý code
    













<!-- more -->

