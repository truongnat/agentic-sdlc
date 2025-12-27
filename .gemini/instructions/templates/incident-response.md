# Incident Response Template
**Version:** 1.0 | **Last Updated:** 2025-12-23

---

## 🚨 Incident Details

| Field | Value |
|-------|-------|
| **Incident ID** | INC-[YYYY-MM-DD]-[###] |
| **Severity** | `Critical` / `High` / `Medium` / `Low` |
| **Status** | `Detected` / `Triaging` / `Fixing` / `Deploying` / `Resolved` / `Postmortem` |
| **Detected By** | @[role] |
| **Detected At** | [datetime] |
| **Resolved At** | [datetime] |
| **Duration** | [total downtime] |

---

## Incident Summary
[Brief description of what happened]

## Impact
- **Affected Users:** [all / specific group / percentage]
- **Affected Features:** [list features]
- **Data Loss:** Yes / No
- **Security Breach:** Yes / No

---

## Response Timeline

| Time | Action | Owner | Status |
|------|--------|-------|--------|
| [time] | Incident detected | @TESTER / @DEVOPS | ✅ |
| [time] | Triage started | @PM + @DEVOPS | ✅ |
| [time] | Root cause identified | @DEV[#] | ✅ |
| [time] | Hotfix implemented | @DEV[#] | ✅ |
| [time] | Quick test passed | @TESTER | ✅ |
| [time] | Hotfix deployed | @DEVOPS | ✅ |
| [time] | Incident resolved | @PM | ✅ |

---

## Root Cause Analysis

### What Happened
[Detailed technical explanation]

### Why It Happened
[Root cause - code bug / config error / infrastructure / external dependency]

### Contributing Factors
- [ ] Missing tests
- [ ] Inadequate monitoring
- [ ] Configuration drift
- [ ] External service failure
- [ ] Human error
- [ ] Other: [specify]

---

## Hotfix Details

| Item | Details |
|------|---------|
| **Hotfix Branch** | `hotfix/INC-[id]` |
| **Files Changed** | [list files] |
| **Testing** | Smoke test only / Full regression |
| **Rollback Plan** | [describe rollback steps] |

### Hotfix Code Summary
```
[Brief description or diff summary of the fix]
```

---

## Action Items (Preventive Measures)

| # | Action | Owner | Priority | Due Date | Status |
|---|--------|-------|----------|----------|--------|
| 1 | [action] | @[role] | High | [date] | ⬜ |
| 2 | [action] | @[role] | Medium | [date] | ⬜ |
| 3 | [action] | @[role] | Low | [date] | ⬜ |

---

## Lessons Learned
1. [lesson 1]
2. [lesson 2]
3. [lesson 3]

---

## Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| PM | | | ☐ Approved |
| DevOps | | | ☐ Approved |
| REPORTER | | | ☐ Documented |

---

### Next Step:
- @REPORTER - Include in Phase-Report
- @PM - Schedule postmortem review if needed
- @DEVOPS - Add monitoring for this scenario

#hotfix #fixbug-critical #incident #reporting
