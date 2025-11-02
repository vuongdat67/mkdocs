---
title: Mermaid Diagrams & Math Guide
---

# 📊 Mermaid Diagrams & Math in MkDocs

Complete guide to using Mermaid diagrams and mathematical formulas in MkDocs Material.

---

## 🎨 Mermaid Diagrams

### 1. Flowchart / Graph

Biểu đồ luồng để mô tả quy trình, thuật toán.

=== "Vertical (TB)"
    ```mermaid
    graph TB
        A[Start] --> B{Is it raining?}
        B -->|Yes| C[Take umbrella]
        B -->|No| D[No umbrella needed]
        C --> E[Go outside]
        D --> E
        E --> F[End]
        
        style A fill:#28a745,color:#fff
        style F fill:#dc3545,color:#fff
        style B fill:#ffc107,color:#000
    ```

=== "Horizontal (LR)"
    ```mermaid
    graph LR
        A[Input] --> B[Process 1]
        B --> C[Process 2]
        C --> D[Process 3]
        D --> E[Output]
        
        style A fill:#667eea,color:#fff
        style E fill:#764ba2,color:#fff
    ```

=== "Syntax"
    ````markdown
    ```mermaid
    graph TB
        A[Square] --> B(Round edges)
        B --> C{Diamond}
        C -->|Label 1| D[Result 1]
        C -->|Label 2| E[Result 2]
        
        style A fill:#color,color:#textcolor
    ```
    ````

**Node Shapes:**
- `[Text]` - Square
- `(Text)` - Rounded
- `{Text}` - Diamond
- `((Text))` - Circle
- `>Text]` - Asymmetric
- `[[Text]]` - Subroutine

**Arrow Types:**
- `-->` - Solid arrow
- `-.->` - Dotted arrow
- `==>` - Thick arrow
- `--text-->` - Arrow with label

---

### 2. Sequence Diagram

Biểu đồ tuần tự cho tương tác giữa các đối tượng.

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant Server
    participant Database
    
    User->>Browser: Enter URL
    Browser->>Server: HTTP Request
    activate Server
    Server->>Database: Query data
    activate Database
    Database-->>Server: Return data
    deactivate Database
    Server-->>Browser: HTTP Response
    deactivate Server
    Browser-->>User: Display page
    
    Note over User,Browser: User sees the page
    Note right of Database: Data is cached
```

=== "Advanced Features"
    ```mermaid
    sequenceDiagram
        autonumber
        Alice->>+John: Hello John, how are you?
        Alice->>+John: John, can you hear me?
        John-->>-Alice: Hi Alice, I can hear you!
        John-->>-Alice: I feel great!
        
        rect rgb(191, 223, 255)
        note right of Alice: Alice thinks
        Alice->>John: What about you?
        John->>Alice: Doing well!
        end
        
        loop Every minute
            John-->Alice: Great!
        end
        
        alt is sick
            John->>Alice: Not so good :(
        else is well
            John->>Alice: Feeling fresh like a daisy
        end
    ```

**Key Syntax:**
- `->>` - Solid line
- `-->>` - Dotted line
- `->>+` - Activate
- `-->>-` - Deactivate
- `autonumber` - Auto-number messages
- `loop...end` - Loop block
- `alt...else...end` - Alternative paths

---

### 3. Class Diagram

Biểu đồ lớp cho OOP design.

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound() String
        +eat() void
        -sleep() void
    }
    
    class Dog {
        +String breed
        +bark() String
        +wagTail() void
    }
    
    class Cat {
        +String color
        +meow() String
        +purr() void
    }
    
    Animal <|-- Dog
    Animal <|-- Cat
    Dog --> Owner : belongs to
    Cat --> Owner : belongs to
    
    class Owner {
        +String name
        +List~Animal~ pets
        +adoptPet(Animal) void
    }
    
    class Veterinarian {
        +String name
        +treat(Animal) void
    }
    
    Owner ..> Veterinarian : consults
```

**Visibility:**
- `+` Public
- `-` Private
- `#` Protected
- `~` Package/Internal

**Relationships:**
- `<|--` Inheritance
- `*--` Composition
- `o--` Aggregation
- `-->` Association
- `..>` Dependency
- `..|>` Realization

---

### 4. State Diagram

Biểu đồ trạng thái cho vòng đời đối tượng.

```mermaid
stateDiagram-v2
    [*] --> Idle
    
    Idle --> Processing: Start
    Processing --> Success: Complete
    Processing --> Failed: Error
    
    Success --> [*]
    Failed --> Retry: Retry
    Retry --> Processing
    Failed --> [*]: Give up
    
    state Processing {
        [*] --> Loading
        Loading --> Validating
        Validating --> Saving
        Saving --> [*]
    }
    
    note right of Success
        Operation completed
        successfully
    end note
    
    note left of Failed
        An error occurred
        during processing
    end note
```

=== "User Authentication Flow"
    ```mermaid
    stateDiagram-v2
        [*] --> LoggedOut
        
        LoggedOut --> LoggingIn: Enter credentials
        LoggingIn --> LoggedIn: Valid credentials
        LoggingIn --> LoggedOut: Invalid credentials
        
        LoggedIn --> ViewingProfile: View profile
        LoggedIn --> EditingProfile: Edit profile
        LoggedIn --> LoggedOut: Logout
        
        ViewingProfile --> LoggedIn: Back
        EditingProfile --> LoggedIn: Save changes
        
        LoggedIn --> [*]: Session expired
    ```

---

### 5. Entity Relationship Diagram (ERD)

Biểu đồ thực thể quan hệ cho database design.

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string customer_id PK
        string name
        string email
        string phone
    }
    
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER {
        string order_id PK
        string customer_id FK
        date order_date
        string status
    }
    
    ORDER_ITEM }o--|| PRODUCT : references
    ORDER_ITEM {
        string order_id FK
        string product_id FK
        int quantity
        decimal price
    }
    
    PRODUCT {
        string product_id PK
        string name
        decimal price
        int stock
    }
    
    CATEGORY ||--o{ PRODUCT : contains
    CATEGORY {
        string category_id PK
        string name
        string description
    }
```

**Cardinality:**
- `||--||` One to one
- `||--o{` One to many
- `}o--o{` Many to many
- `||--|{` One to exactly many

---

### 6. Gantt Chart

Biểu đồ Gantt cho project timeline.

```mermaid
gantt
    title Project Development Timeline
    dateFormat YYYY-MM-DD
    
    section Planning
    Requirements gathering    :done, req, 2024-01-01, 2024-01-15
    System design            :done, design, after req, 15d
    
    section Development
    Backend API              :active, backend, 2024-02-01, 30d
    Frontend UI              :frontend, after backend, 25d
    Database setup           :crit, db, 2024-02-01, 10d
    
    section Testing
    Unit testing             :testing, after frontend, 10d
    Integration testing      :after testing, 7d
    UAT                      :crit, after testing, 5d
    
    section Deployment
    Production deploy        :milestone, deploy, after testing, 1d
    Monitoring setup         :after deploy, 3d
```

**Keywords:**
- `:done` - Completed
- `:active` - In progress
- `:crit` - Critical task
- `:milestone` - Milestone marker

---

### 7. Pie Chart

Biểu đồ tròn cho phân bổ phần trăm.

```mermaid
pie title Programming Languages Used
    "Python" : 35
    "JavaScript" : 28
    "Java" : 15
    "C++" : 12
    "Go" : 6
    "Others" : 4
```

=== "Project Time Distribution"
    ```mermaid
    pie title Time Spent on Project Phases
        "Development" : 45
        "Testing" : 20
        "Planning" : 15
        "Deployment" : 10
        "Maintenance" : 10
    ```

---

### 8. Git Graph

Biểu đồ Git branches và commits.

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Add features"
    
    branch develop
    checkout develop
    commit id: "Dev work 1"
    commit id: "Dev work 2"
    
    branch feature-login
    checkout feature-login
    commit id: "Add login page"
    commit id: "Add auth logic"
    
    checkout develop
    merge feature-login
    
    checkout main
    merge develop tag: "v1.0"
    
    checkout develop
    commit id: "Bug fixes"
    
    checkout main
    merge develop tag: "v1.1"
```

---

### 9. User Journey

Biểu đồ hành trình người dùng.

```mermaid
journey
    title User Shopping Experience
    section Browse
      Visit website: 5: User
      Search product: 4: User
      View details: 5: User
    section Purchase
      Add to cart: 4: User
      Checkout: 3: User, System
      Payment: 2: User, PaymentGateway
    section Post-purchase
      Confirmation: 5: System
      Track order: 4: User, System
      Receive product: 5: User
```

---

### 10. Timeline

Biểu đồ timeline cho sự kiện theo thời gian.

```mermaid
timeline
    title History of Web Development
    section 1990s
        1991 : HTML invented
        1995 : JavaScript created
             : PHP released
        1996 : CSS introduced
    section 2000s
        2004 : Web 2.0 era begins
        2006 : jQuery released
        2009 : Node.js launched
    section 2010s
        2010 : AngularJS released
        2013 : React.js released
        2014 : Vue.js released
        2015 : ES6 standardized
    section 2020s
        2020 : Deno 1.0 released
        2023 : AI-assisted coding mainstream
```

---

## 🧮 Mathematical Formulas (KaTeX)

MkDocs Material sử dụng KaTeX để render công thức toán học.

### Inline Math

Sử dụng `$...$` cho công thức inline:

The formula $E = mc^2$ is Einstein's mass-energy equivalence.

The quadratic formula is $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

### Display Math

Sử dụng `$$...$$` cho công thức block:

$$
\int_{a}^{b} f(x) dx = F(b) - F(a)
$$

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

### Common Mathematical Symbols

=== "Greek Letters"
    | Symbol | Code | Symbol | Code |
    |--------|------|--------|------|
    | $\alpha$ | `\alpha` | $\beta$ | `\beta` |
    | $\gamma$ | `\gamma` | $\delta$ | `\delta` |
    | $\theta$ | `\theta` | $\lambda$ | `\lambda` |
    | $\mu$ | `\mu` | $\pi$ | `\pi` |
    | $\sigma$ | `\sigma` | $\omega$ | `\omega` |

=== "Operators"
    | Symbol | Code | Symbol | Code |
    |--------|------|--------|------|
    | $\times$ | `\times` | $\div$ | `\div` |
    | $\pm$ | `\pm` | $\mp$ | `\mp` |
    | $\leq$ | `\leq` | $\geq$ | `\geq` |
    | $\neq$ | `\neq` | $\approx$ | `\approx` |
    | $\sum$ | `\sum` | $\prod$ | `\prod` |
    | $\int$ | `\int` | $\infty$ | `\infty` |

=== "Arrows & Sets"
    | Symbol | Code | Symbol | Code |
    |--------|------|--------|------|
    | $\rightarrow$ | `\rightarrow` | $\Rightarrow$ | `\Rightarrow` |
    | $\leftarrow$ | `\leftarrow` | $\Leftarrow$ | `\Leftarrow` |
    | $\in$ | `\in` | $\notin$ | `\notin` |
    | $\subset$ | `\subset` | $\subseteq$ | `\subseteq` |
    | $\cup$ | `\cup` | $\cap$ | `\cap` |
    | $\emptyset$ | `\emptyset` | $\forall$ | `\forall` |

### Advanced Examples

#### Calculus

**Derivative:**
$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$

**Integration by parts:**
$$
\int u \, dv = uv - \int v \, du
$$

**Taylor Series:**
$$
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots
$$

#### Linear Algebra

**Matrix:**
$$
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

**Determinant:**
$$
\det(A) = \begin{vmatrix}
a & b \\
c & d
\end{vmatrix} = ad - bc
$$

**Eigenvalue equation:**
$$
Av = \lambda v
$$

#### Statistics

**Mean:**
$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

**Variance:**
$$
\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

**Normal Distribution:**
$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

#### Algorithm Complexity

**Big O Notation:**
- $O(1)$ - Constant time
- $O(\log n)$ - Logarithmic time
- $O(n)$ - Linear time
- $O(n \log n)$ - Linearithmic time
- $O(n^2)$ - Quadratic time
- $O(2^n)$ - Exponential time

**Master Theorem:**
$$
T(n) = aT\left(\frac{n}{b}\right) + f(n)
$$

#### Probability

**Bayes' Theorem:**
$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

**Expected Value:**
$$
E[X] = \sum_{i=1}^{n} x_i \cdot P(x_i)
$$

---

## 🎨 Styling Mermaid Diagrams

### Using `style` keyword

```mermaid
graph LR
    A[Success] --> B[Processing]
    B --> C[Error]
    B --> D[Warning]
    
    style A fill:#28a745,stroke:#1e7e34,color:#fff
    style C fill:#dc3545,stroke:#c82333,color:#fff
    style D fill:#ffc107,stroke:#e0a800,color:#000
    style B fill:#667eea,stroke:#5568d3,color:#fff
```

### Using `classDef`

```mermaid
graph TB
    A[Start]:::successClass --> B[Process]:::processClass
    B --> C{Check}:::decisionClass
    C -->|Pass| D[Success]:::successClass
    C -->|Fail| E[Error]:::errorClass
    
    classDef successClass fill:#28a745,stroke:#1e7e34,color:#fff
    classDef errorClass fill:#dc3545,stroke:#c82333,color:#fff
    classDef processClass fill:#007bff,stroke:#0056b3,color:#fff
    classDef decisionClass fill:#ffc107,stroke:#e0a800,color:#000
```

---

## 📝 Complete Example: System Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        A[Web Browser]
        B[Mobile App]
    end
    
    subgraph "Load Balancer"
        LB[Nginx Load Balancer]
    end
    
    subgraph "Application Layer"
        API1[API Server 1]
        API2[API Server 2]
        API3[API Server 3]
    end
    
    subgraph "Cache Layer"
        REDIS[Redis Cache]
    end
    
    subgraph "Database Layer"
        DB[(PostgreSQL)]
        REPLICA[(Read Replica)]
    end
    
    subgraph "Storage Layer"
        S3[AWS S3]
    end
    
    A --> LB
    B --> LB
    LB --> API1
    LB --> API2
    LB --> API3
    
    API1 --> REDIS
    API2 --> REDIS
    API3 --> REDIS
    
    API1 --> DB
    API2 --> DB
    API3 --> DB
    
    API1 --> REPLICA
    API2 --> REPLICA
    API3 --> REPLICA
    
    DB -.-> REPLICA
    
    API1 --> S3
    API2 --> S3
    API3 --> S3
    
    style A fill:#667eea,color:#fff
    style B fill:#667eea,color:#fff
    style LB fill:#764ba2,color:#fff
    style REDIS fill:#dc3545,color:#fff
    style DB fill:#28a745,color:#fff
    style REPLICA fill:#28a745,color:#fff
    style S3 fill:#ff9900,color:#fff
```

---

## 🎯 Best Practices

!!! tip "Mermaid Tips"
    1. Keep diagrams simple and focused
    2. Use subgraphs to organize complex diagrams
    3. Apply consistent styling across similar diagrams
    4. Add notes for important information
    5. Test diagrams in live editor first: [Mermaid Live Editor](https://mermaid.live/)

!!! tip "Math Tips"
    1. Use `\text{}` for text inside math: $\text{speed} = \frac{\text{distance}}{\text{time}}$
    2. Use `\,` for small space, `\quad` for medium, `\qquad` for large
    3. Align equations with `align` environment
    4. Number equations for reference

---

## 📚 Resources

- [Mermaid Official Docs](https://mermaid.js.org/)
- [Mermaid Live Editor](https://mermaid.live/)
- [KaTeX Supported Functions](https://katex.org/docs/supported.html)
- [LaTeX Math Symbols](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols)

---

**Happy diagramming! 🎨**
