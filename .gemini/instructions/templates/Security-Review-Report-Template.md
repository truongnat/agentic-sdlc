# Security Review Report - Version [X]

## Document Info
| Field | Value |
|-------|-------|
| Version | [X.0] |
| Date | [YYYY-MM-DD] |
| Author | @SECA |
| Status | Pass / Fail / Conditional Pass |

---

## 1. Scope of Review
| Area | Reviewed |
|------|----------|
| Authentication | ✅/❌ |
| Authorization | ✅/❌ |
| Data Validation | ✅/❌ |
| API Security | ✅/❌ |
| Data Storage | ✅/❌ |
| Dependencies | ✅/❌ |

## 2. Security Summary
| Severity | Count | Status |
|----------|-------|--------|
| Critical | [X] | [X] Resolved |
| High | [X] | [X] Resolved |
| Medium | [X] | [X] Resolved |
| Low | [X] | [X] Resolved |

## 3. Findings

### 3.1 Critical
| ID | Finding | OWASP Ref | Status |
|----|---------|-----------|--------|
| SEC-001 | [Description] | [A01-A10] | Open/Resolved |

### 3.2 High
| ID | Finding | OWASP Ref | Status |
|----|---------|-----------|--------|
| SEC-002 | [Description] | [A01-A10] | Open/Resolved |

### 3.3 Medium
| ID | Finding | OWASP Ref | Status |
|----|---------|-----------|--------|
| SEC-003 | [Description] | [A01-A10] | Open/Resolved |

### 3.4 Low
| ID | Finding | OWASP Ref | Status |
|----|---------|-----------|--------|
| SEC-004 | [Description] | [A01-A10] | Open/Resolved |

## 4. Security Checklist
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] CSRF protection
- [ ] Authentication tokens properly secured
- [ ] Authorization checks on all protected resources
- [ ] Sensitive data encrypted at rest
- [ ] Sensitive data encrypted in transit (HTTPS)
- [ ] No secrets in source code
- [ ] Dependency vulnerabilities addressed

## 5. Recommendations
1. [Security recommendation 1]
2. [Security recommendation 2]

## 6. Verdict
☐ **PASS** - No blocking security issues
☐ **CONDITIONAL PASS** - Proceed with noted mitigations
☐ **FAIL** - Critical/High issues must be resolved

---

### Next Step:
- @SA @DEV - Address security findings (if any)
- @DEV - Proceed with development (if approved)

#security-review
