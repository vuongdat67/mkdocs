# Project Documentation Template

<style>
.doc-container { max-width: 1100px; margin: 20px auto; }
.template-selector { display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0; }
.template-card { flex: 1; min-width: 200px; padding: 20px; background: var(--md-code-bg-color); border-radius: 8px; cursor: pointer; border: 2px solid transparent; transition: all 0.3s; }
.template-card:hover { border-color: var(--md-primary-fg-color); transform: translateY(-3px); }
.template-card.active { border-color: var(--md-primary-fg-color); background: var(--md-accent-fg-color--transparent); }
.template-icon { font-size: 2em; margin-bottom: 10px; }
.template-title { font-weight: 600; font-size: 1.1em; }
.template-desc { font-size: 0.9em; opacity: 0.7; margin-top: 5px; }
.doc-editor { display: none; margin: 20px 0; }
.doc-editor.active { display: block; }
.editor-toolbar { display: flex; gap: 10px; margin-bottom: 15px; flex-wrap: wrap; }
.toolbar-btn { padding: 8px 15px; border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px; background: var(--md-code-bg-color); color: var(--md-default-fg-color); cursor: pointer; font-weight: 500; transition: all 0.2s; }
.toolbar-btn:hover { background: var(--md-primary-fg-color); color: white; }
.template-content { padding: 20px; background: var(--md-code-bg-color); border-radius: 6px; white-space: pre-wrap; font-family: 'Consolas', monospace; font-size: 0.9em; line-height: 1.6; max-height: 600px; overflow-y: auto; }
.section-nav { position: sticky; top: 20px; padding: 15px; background: var(--md-code-bg-color); border-radius: 6px; margin-bottom: 20px; }
.section-nav a { display: block; padding: 8px 12px; margin: 5px 0; border-radius: 4px; color: var(--md-default-fg-color); text-decoration: none; transition: all 0.2s; }
.section-nav a:hover { background: var(--md-accent-fg-color--transparent); }
.workflow-diagram { padding: 20px; background: var(--md-code-bg-color); border-radius: 6px; margin: 20px 0; text-align: center; }
.phase-box { display: inline-block; padding: 15px 25px; margin: 10px; background: var(--md-primary-fg-color); color: white; border-radius: 6px; font-weight: 600; }
.arrow { display: inline-block; margin: 0 10px; font-size: 1.5em; }
</style>

<div class="doc-container">
  <h2>Select Project Template</h2>
  
  <div class="template-selector">
    <div class="template-card active" onclick="selectTemplate('sdl')">
      <div class="template-icon">🔒</div>
      <div class="template-title">SDL Workflow</div>
      <div class="template-desc">Security Development Lifecycle</div>
    </div>
    
    <div class="template-card" onclick="selectTemplate('agile')">
      <div class="template-icon">⚡</div>
      <div class="template-title">Agile Sprint</div>
      <div class="template-desc">Sprint planning & retrospective</div>
    </div>
    
    <div class="template-card" onclick="selectTemplate('threat')">
      <div class="template-icon">🛡️</div>
      <div class="template-title">Threat Model</div>
      <div class="template-desc">STRIDE threat modeling</div>
    </div>
    
    <div class="template-card" onclick="selectTemplate('adr')">
      <div class="template-icon">📋</div>
      <div class="template-title">ADR</div>
      <div class="template-desc">Architecture Decision Record</div>
    </div>
  </div>

  <!-- SDL Template -->
  <div class="doc-editor active" id="sdl">
    <div class="editor-toolbar">
      <button class="toolbar-btn" onclick="copyTemplate('sdl')">📋 Copy Template</button>
      <button class="toolbar-btn" onclick="downloadTemplate('sdl', 'SDL_Workflow')">💾 Download</button>
    </div>
    
    <div class="workflow-diagram">
      <div class="phase-box">Requirements</div>
      <span class="arrow">→</span>
      <div class="phase-box">Design</div>
      <span class="arrow">→</span>
      <div class="phase-box">Implementation</div>
      <span class="arrow">→</span>
      <div class="phase-box">Verification</div>
      <span class="arrow">→</span>
      <div class="phase-box">Release</div>
    </div>
    
    <div class="template-content" id="sdl-content"># Security Development Lifecycle (SDL)

## Project Information
- **Project Name:** [Your Project]
- **Version:** 1.0.0
- **SDL Phase:** Requirements
- **Security Lead:** [Name]
- **Date:** 2025-11-02

---

## Phase 1: Requirements

### Security Requirements
- [ ] Authentication mechanism defined
- [ ] Authorization model designed
- [ ] Data classification completed
- [ ] Compliance requirements identified (GDPR, HIPAA, etc.)
- [ ] Privacy requirements documented

### Security Training
- [ ] Team completed secure coding training
- [ ] Threat modeling workshop conducted
- [ ] Security tools training completed

### Key Deliverables
- Security requirements document
- Compliance checklist
- Privacy impact assessment

---

## Phase 2: Design

### Threat Modeling
- **Methodology:** STRIDE
- **Assets Identified:** 
  - User credentials
  - Personal data
  - API keys
  
- **Threats Identified:**
  1. SQL Injection on login form
  2. XSS in user profile
  3. CSRF on state-changing operations
  
### Security Design Review
- [ ] Architecture reviewed for security flaws
- [ ] Attack surface analyzed
- [ ] Security controls designed
- [ ] Cryptographic requirements defined

### Design Patterns
- **Authentication:** JWT with refresh tokens
- **Authorization:** RBAC (Role-Based Access Control)
- **Data Protection:** AES-256 encryption at rest, TLS 1.3 in transit

---

## Phase 3: Implementation

### Secure Coding Standards
- [ ] OWASP Top 10 guidelines followed
- [ ] Input validation implemented
- [ ] Output encoding applied
- [ ] Parameterized queries used
- [ ] Secrets management configured

### Code Review Checklist
- [ ] No hardcoded credentials
- [ ] Error messages don't leak sensitive info
- [ ] Proper exception handling
- [ ] Secure random number generation
- [ ] Session management secure

### Security Tools
- **SAST:** SonarQube, Checkmarx
- **Dependency Check:** OWASP Dependency-Check
- **Secrets Scanner:** GitGuardian, TruffleHog

---

## Phase 4: Verification

### Security Testing
- [ ] Penetration testing completed
- [ ] Vulnerability scanning performed
- [ ] Fuzzing tests executed
- [ ] Security regression tests passed

### Test Results
| Test Type | Date | Result | Critical Issues |
|-----------|------|--------|-----------------|
| SAST | 2025-10-15 | Pass | 0 |
| DAST | 2025-10-20 | Pass | 0 |
| Pen Test | 2025-10-25 | Pass | 0 |

### Findings & Mitigations
1. **Finding:** Weak password policy
   - **Risk:** Medium
   - **Mitigation:** Enforce 12+ chars, complexity requirements
   - **Status:** Fixed

---

## Phase 5: Release

### Security Sign-off
- [ ] All critical/high vulnerabilities resolved
- [ ] Security testing completed
- [ ] Incident response plan ready
- [ ] Security documentation updated

### Post-Release
- [ ] Security monitoring enabled
- [ ] Incident response team briefed
- [ ] Bug bounty program launched (if applicable)
- [ ] Security patch process defined

### Continuous Security
- Regular security updates
- Quarterly security reviews
- Annual penetration testing
- Security awareness training

---

## Metrics & KPIs
- **Vulnerabilities Found:** 12 (0 Critical, 2 High, 10 Low)
- **Mean Time to Remediate:** 3.5 days
- **Security Test Coverage:** 85%
- **Code Review Coverage:** 100%

---

## References
- [OWASP SDL](https://owasp.org)
- [Microsoft SDL](https://www.microsoft.com/en-us/securityengineering/sdl)
- [NIST Secure SDLC](https://csrc.nist.gov)</div>
  </div>

  <!-- Agile Sprint Template -->
  <div class="doc-editor" id="agile">
    <div class="editor-toolbar">
      <button class="toolbar-btn" onclick="copyTemplate('agile')">📋 Copy Template</button>
      <button class="toolbar-btn" onclick="downloadTemplate('agile', 'Agile_Sprint')">💾 Download</button>
    </div>
    
    <div class="template-content" id="agile-content"># Agile Sprint Planning

## Sprint Information
- **Sprint Number:** Sprint 12
- **Duration:** 2 weeks
- **Start Date:** 2025-11-02
- **End Date:** 2025-11-15
- **Sprint Goal:** Implement authentication module with OAuth2

---

## Sprint Planning

### Team Capacity
| Team Member | Capacity (hours) | Available |
|-------------|------------------|-----------|
| Developer 1 | 80 | 70 (vacation) |
| Developer 2 | 80 | 80 |
| Tester | 40 | 40 |
| **Total** | **200** | **190** |

### Sprint Backlog

#### User Stories

**US-101: As a user, I want to login with Google OAuth**
- **Priority:** High
- **Estimate:** 13 points
- **Acceptance Criteria:**
  - Google OAuth integration working
  - User profile created on first login
  - Session management implemented
- **Tasks:**
  - [ ] Setup OAuth credentials (2h)
  - [ ] Implement OAuth flow (8h)
  - [ ] Create user profile service (5h)
  - [ ] Write tests (3h)

**US-102: As an admin, I want to manage user roles**
- **Priority:** Medium
- **Estimate:** 8 points
- **Acceptance Criteria:**
  - CRUD operations for roles
  - Role assignment to users
  - Permission checking middleware
- **Tasks:**
  - [ ] Design role schema (1h)
  - [ ] Implement role CRUD (5h)
  - [ ] Create middleware (3h)
  - [ ] Testing (3h)

### Technical Debt
- [ ] Refactor authentication service (5h)
- [ ] Update deprecated dependencies (2h)
- [ ] Improve error logging (3h)

---

## Daily Standup Notes

### Day 1 (2025-11-02)
**Developer 1:**
- Yesterday: Sprint planning
- Today: OAuth setup
- Blockers: None

**Developer 2:**
- Yesterday: Sprint planning
- Today: Database schema
- Blockers: None

### Day 5 (2025-11-06)
**Key Updates:**
- OAuth integration 80% complete
- Performance issue found in role query - optimizing
- Need security review for OAuth implementation

---

## Sprint Review

### Completed Stories
- ✅ US-101: OAuth login (13 points)
- ✅ US-102: Role management (8 points)
- **Total Completed:** 21 points

### Demo Checklist
- [ ] OAuth login flow
- [ ] Role management UI
- [ ] Security testing results
- [ ] Performance metrics

### Stakeholder Feedback
- OAuth UX is smooth
- Request: Add GitHub OAuth support
- Performance: Response times good (<200ms)

---

## Sprint Retrospective

### What Went Well ✅
- Good collaboration on OAuth implementation
- Early security review caught issues
- Clear acceptance criteria helped testing

### What Didn't Go Well ❌
- Underestimated OAuth complexity
- Late discovery of rate limiting needs
- Test coverage lower than expected (75%)

### Action Items 🎯
1. Add buffer time for security features
2. Include rate limiting in planning checklist
3. Set test coverage goal at 85%
4. Schedule security review earlier in sprint

### Team Health
- **Velocity:** 21 points (target: 20)
- **Quality:** 2 bugs found in production
- **Morale:** High (8/10)

---

## Sprint Metrics

### Burndown
- Day 1: 21 points remaining
- Day 5: 12 points remaining
- Day 10: 0 points remaining

### Velocity Trend
| Sprint | Committed | Completed |
|--------|-----------|-----------|
| Sprint 10 | 18 | 16 |
| Sprint 11 | 20 | 20 |
| Sprint 12 | 21 | 21 |

### Defects
- Found: 3
- Fixed: 3
- Escaped to Production: 0

---

## Next Sprint Preview
- GitHub OAuth support
- MFA implementation
- Session timeout configuration</div>
  </div>

  <!-- Threat Model Template -->
  <div class="doc-editor" id="threat">
    <div class="editor-toolbar">
      <button class="toolbar-btn" onclick="copyTemplate('threat')">📋 Copy Template</button>
      <button class="toolbar-btn" onclick="downloadTemplate('threat', 'Threat_Model')">💾 Download</button>
    </div>
    
    <div class="template-content" id="threat-content"># Threat Modeling - STRIDE Methodology

## System Overview
- **System Name:** E-Commerce Platform
- **Version:** 2.0
- **Date:** 2025-11-02
- **Team:** Security, DevOps, Backend

---

## System Description

### Components
1. **Web Application** (React)
2. **API Gateway** (Node.js)
3. **Authentication Service** (JWT)
4. **Database** (PostgreSQL)
5. **Payment Gateway** (Stripe)
6. **Email Service** (SendGrid)

### Data Flow
```
User → Web App → API Gateway → Auth Service → Database
                             → Payment Gateway
                             → Email Service
```

### Trust Boundaries
- Internet ↔ Web Application
- Web Application ↔ API Gateway
- API Gateway ↔ Internal Services
- Application ↔ Database

---

## STRIDE Analysis

### S - Spoofing

**Threat: Attacker impersonates legitimate user**
- **Component:** Authentication Service
- **Attack Vector:** Stolen JWT tokens
- **Impact:** High - Unauthorized access to user account
- **Likelihood:** Medium
- **Risk Score:** 8/10

**Mitigations:**
- ✅ Implement JWT with short expiry (15 min)
- ✅ Add refresh token rotation
- ✅ Enable MFA for sensitive operations
- ⚠️ Add device fingerprinting
- ❌ Implement anomaly detection (planned)

---

### T - Tampering

**Threat: SQL Injection in user input**
- **Component:** API Gateway → Database
- **Attack Vector:** Malicious input in search queries
- **Impact:** Critical - Data breach
- **Likelihood:** Low (with mitigations)
- **Risk Score:** 6/10

**Mitigations:**
- ✅ Use parameterized queries
- ✅ Input validation on all endpoints
- ✅ ORM usage (prevents direct SQL)
- ✅ Web Application Firewall (WAF)

**Threat: Man-in-the-Middle attack**
- **Component:** All network communications
- **Attack Vector:** Intercepted HTTP traffic
- **Impact:** High - Credential theft
- **Likelihood:** Low
- **Risk Score:** 5/10

**Mitigations:**
- ✅ TLS 1.3 enforced
- ✅ HSTS enabled
- ✅ Certificate pinning on mobile app

---

### R - Repudiation

**Threat: User denies making transaction**
- **Component:** Payment processing
- **Attack Vector:** Lack of audit trail
- **Impact:** Medium - Financial dispute
- **Likelihood:** Medium
- **Risk Score:** 5/10

**Mitigations:**
- ✅ Comprehensive logging (all transactions)
- ✅ Immutable audit trail
- ✅ Email confirmation for all orders
- ✅ Two-factor authentication for payments

---

### I - Information Disclosure

**Threat: Sensitive data exposed in logs**
- **Component:** Logging system
- **Attack Vector:** Debug logs containing PII
- **Impact:** High - Privacy violation
- **Likelihood:** Medium
- **Risk Score:** 7/10

**Mitigations:**
- ✅ Sanitize logs (no PII, credentials)
- ✅ Encrypted log storage
- ✅ Access control on log systems
- ⚠️ Regular log reviews (quarterly)

**Threat: Database backup exposed**
- **Component:** Database
- **Attack Vector:** Misconfigured S3 bucket
- **Impact:** Critical - Full data breach
- **Likelihood:** Low
- **Risk Score:** 6/10

**Mitigations:**
- ✅ Encrypted backups (AES-256)
- ✅ Private S3 buckets
- ✅ IAM least privilege
- ✅ Regular access audits

---

### D - Denial of Service

**Threat: API rate limiting bypass**
- **Component:** API Gateway
- **Attack Vector:** Distributed requests
- **Impact:** High - Service unavailable
- **Likelihood:** Medium
- **Risk Score:** 7/10

**Mitigations:**
- ✅ Rate limiting (100 req/min per IP)
- ✅ CDN with DDoS protection (Cloudflare)
- ✅ Auto-scaling infrastructure
- ⚠️ Implement CAPTCHA on sensitive endpoints

---

### E - Elevation of Privilege

**Threat: Privilege escalation via IDOR**
- **Component:** Authorization checks
- **Attack Vector:** Manipulating user IDs in requests
- **Impact:** Critical - Access to other user data
- **Likelihood:** Medium
- **Risk Score:** 8/10

**Mitigations:**
- ✅ Object-level authorization checks
- ✅ User context validation on every request
- ✅ Role-based access control (RBAC)
- ✅ Regular penetration testing

**Threat: JWT role claim manipulation**
- **Component:** JWT verification
- **Attack Vector:** Modified JWT payload
- **Impact:** Critical - Admin access
- **Likelihood:** Low
- **Risk Score:** 6/10

**Mitigations:**
- ✅ JWT signature verification
- ✅ Strong secret key (256-bit)
- ✅ Claims validation
- ✅ Regular key rotation

---

## Risk Summary

| Threat Category | Critical | High | Medium | Low |
|-----------------|----------|------|--------|-----|
| Spoofing | 0 | 1 | 0 | 0 |
| Tampering | 1 | 1 | 0 | 0 |
| Repudiation | 0 | 0 | 1 | 0 |
| Info Disclosure | 1 | 1 | 0 | 0 |
| DoS | 0 | 1 | 0 | 0 |
| Elevation | 2 | 0 | 0 | 0 |
| **Total** | **4** | **4** | **1** | **0** |

---

## Action Plan

### Immediate (Sprint 1-2)
1. Implement device fingerprinting
2. Add CAPTCHA on login/register
3. Complete anomaly detection system

### Short-term (Sprint 3-6)
1. Automated security testing in CI/CD
2. Penetration testing
3. Security training for developers

### Long-term (Q1 2026)
1. Bug bounty program
2. Security incident response plan
3. SOC 2 compliance

---

## Review Schedule
- **Next Review:** 2025-12-02
- **Frequency:** Monthly
- **Reviewers:** Security Team, Architecture Team</div>
  </div>

  <!-- ADR Template -->
  <div class="doc-editor" id="adr">
    <div class="editor-toolbar">
      <button class="toolbar-btn" onclick="copyTemplate('adr')">📋 Copy Template</button>
      <button class="toolbar-btn" onclick="downloadTemplate('adr', 'ADR')">💾 Download</button>
    </div>
    
    <div class="template-content" id="adr-content"># Architecture Decision Record (ADR)

## ADR-001: Use JWT for Authentication

### Status
**Accepted** | ~~Proposed~~ | ~~Deprecated~~ | ~~Superseded~~

### Date
2025-11-02

---

## Context

Our e-commerce platform needs a scalable authentication mechanism that:
- Supports microservices architecture
- Works across multiple domains (web, mobile, API)
- Minimizes database queries for auth checks
- Enables stateless authentication
- Integrates with existing OAuth providers

Current situation:
- Session-based auth with Redis
- Session store becoming bottleneck
- Mobile app requires separate auth mechanism
- Planning to add 5 new microservices

---

## Decision

We will use **JSON Web Tokens (JWT)** for authentication with the following approach:

### Implementation Details
- **Access Token:** Short-lived JWT (15 minutes)
- **Refresh Token:** Long-lived, stored in database (7 days)
- **Algorithm:** RS256 (asymmetric)
- **Claims:** user_id, email, roles, exp, iat
- **Storage:** 
  - Access token: Memory (httpOnly cookie for web)
  - Refresh token: Database + httpOnly cookie

### Token Structure
```json
{
  "sub": "user_123",
  "email": "user@example.com",
  "roles": ["user", "premium"],
  "iat": 1699000000,
  "exp": 1699000900
}
```

---

## Alternatives Considered

### 1. Session-based Authentication (Current)
**Pros:**
- Simple to implement
- Easy to revoke
- Familiar to team

**Cons:**
- Requires stateful server
- Redis becomes single point of failure
- Difficult to scale across microservices
- Poor mobile app support

**Why rejected:** Doesn't meet scalability requirements

### 2. OAuth 2.0 Only
**Pros:**
- Industry standard
- Delegates auth to providers
- Good for SSO

**Cons:**
- Overkill for our use case
- Dependency on external providers
- Complex implementation
- Still need internal user management

**Why rejected:** Too complex, external dependencies

### 3. Opaque Tokens
**Pros:**
- More secure (can't decode)
- Easy to revoke

**Cons:**
- Requires database lookup on every request
- Network latency
- Doesn't solve stateless requirement

**Why rejected:** Performance concerns

---

## Consequences

### Positive ✅
- **Stateless:** No server-side session storage needed
- **Scalable:** Works across all microservices
- **Performance:** No database lookup for auth
- **Mobile-friendly:** Works seamlessly on mobile apps
- **Decoupled:** Services can verify tokens independently

### Negative ❌
- **Token Revocation:** Hard to revoke before expiry
  - *Mitigation:* Short expiry + refresh token rotation
- **Token Size:** JWTs larger than session IDs
  - *Mitigation:* Minimal claims, gzip compression
- **Complexity:** More complex than sessions
  - *Mitigation:* Use battle-tested library (jsonwebtoken)
- **Secret Management:** Need secure key storage
  - *Mitigation:* Use secrets manager (AWS Secrets Manager)

### Security Considerations
- ✅ Use RS256 (not HS256) for better security
- ✅ Short expiry times (15 min)
- ✅ Implement refresh token rotation
- ✅ Store refresh tokens hashed in database
- ✅ Add rate limiting on token endpoints
- ⚠️ Monitor for token leakage
- ⚠️ Implement anomaly detection

---

## Implementation Plan

### Phase 1: Foundation (Week 1-2)
- [ ] Setup JWT library
- [ ] Create signing keys
- [ ] Implement token generation
- [ ] Create verification middleware

### Phase 2: Integration (Week 3-4)
- [ ] Migrate login endpoint
- [ ] Add refresh token flow
- [ ] Update all protected routes
- [ ] Mobile app integration

### Phase 3: Migration (Week 5-6)
- [ ] Gradual rollout (10% → 50% → 100%)
- [ ] Monitor error rates
- [ ] Dual-support (JWT + sessions)
- [ ] Deprecate sessions

### Phase 4: Optimization (Week 7-8)
- [ ] Performance testing
- [ ] Security audit
- [ ] Documentation
- [ ] Team training

---

## Success Metrics

| Metric | Target | Current | Post-Implementation |
|--------|--------|---------|---------------------|
| Auth latency | <50ms | 120ms | 30ms |
| Session store load | N/A | High | None |
| Horizontal scaling | Easy | Hard | Easy |
| Mobile auth issues | <1% | 5% | <1% |

---

## Related ADRs
- ADR-002: Microservices Architecture
- ADR-005: API Gateway Design
- ADR-008: Secrets Management

---

## References
- [JWT Best Practices](https://tools.ietf.org/html/rfc8725)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org)
- [Auth0 JWT Handbook](https://auth0.com/resources/ebooks/jwt-handbook)

---

## Notes
- Review this decision in 6 months
- Consider adding JWE (encrypted JWT) for sensitive claims
- Plan for key rotation strategy</div>
  </div>
</div>

<script>
function selectTemplate(name) {
  document.querySelectorAll('.template-card').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('.doc-editor').forEach(e => e.classList.remove('active'));
  event.target.closest('.template-card').classList.add('active');
  document.getElementById(name).classList.add('active');
}

function copyTemplate(name) {
  const content = document.getElementById(name + '-content').textContent;
  navigator.clipboard.writeText(content).then(() => {
    alert('✓ Template copied to clipboard!');
  });
}

function downloadTemplate(name, filename) {
  const content = document.getElementById(name + '-content').textContent;
  const blob = new Blob([content], { type: 'text/markdown' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename + '.md';
  a.click();
  URL.revokeObjectURL(url);
}
</script>