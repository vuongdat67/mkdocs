``` mermaid
%%{init: {'theme':'dark', 'themeVariables': { 'primaryColor': '#1f2937', 'edgeLabelBackground':'#333', 'fontSize':'14px'}}}%%
graph TD
    A["🧩 Ansible Controller<br>(WSL2 Ubuntu)"]:::ansible
    B["🐳 Docker Desktop<br>(Windows)"]:::docker
    A -->|"SSH 2223–2228"| B

    subgraph Docker_Env
        W1["🌐 Web1 :8088<br>Apache + PHP + WordPress"]:::wp
        W2["🌐 Web2 :8089<br>Apache + PHP + WordPress"]:::wp
        H["⚖️ HAProxy :8090<br>Load Balancer"]:::proxy
        D["🗄️ MariaDB :3307"]:::db
        R["💾 Redis :6380"]:::cache
        Bk["📦 Backup<br>cron + rsync"]:::backup
        H --> W1
        H --> W2
        H --> D
        H --> R
        H --> Bk
    end

  

```

