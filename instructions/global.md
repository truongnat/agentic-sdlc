# TeamLifecycle Global Rules & Conventions
(Version 1.1 – Strict IT SDLC Simulation for Google Antigravity)

**Last Updated:** 2025-12-23  
**Maintainer:** Project Team

---

## Purpose
This document defines the mandatory rules, conventions, and lifecycle flow that EVERY agent in the TeamLifecycle workflow MUST follow without exception.  
It ensures strict compliance, full traceability, auto-communication, and professional software development process.

---

## Strict SDLC Flow (NO SKIPPING PHASES – EVER)

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐
│ 1. Planning     │───▶│ 2. Plan Approval│───▶│ 3. Designing            │
│    (PM)         │    │    (User)       │    │    (SA + UIUX + PO)     │
└─────────────────┘    └─────────────────┘    └───────────┬─────────────┘
                                                          │
                                                          ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐
│ 6. Testing      │◀───│ 5. Development  │◀───│ 4. Design Verification  │
│    (TESTER)     │    │   (DEV + Ops)   │    │    (QA + SecA)          │
└────────┬────────┘    └─────────────────┘    └─────────────────────────┘
         │
         ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐
│ 7. Bug Fixing   │───▶│ 8. Deployment   │───▶│ 9. Reporting            │
│   (DEV + Ops)   │    │    (DevOps)     │    │    (REPORTER)           │
└─────────────────┘    └─────────────────┘    └───────────┬─────────────┘
                                                          │
                                                          ▼
                       ┌─────────────────┐    ┌─────────────────────────┐
                       │ ↩ Cycle Repeat  │◀───│ 10. Final Review        │
                       │   (if rejected) │    │    (STAKEHOLDER)        │
                       └─────────────────┘    └───────────┬─────────────┘
                                                          │ ✅ Approved
                                                          ▼
                                              ┌─────────────────────────┐
                                              │ 11. Completion          │
                                              └─────────────────────────┘
```

### Phase Details:
1. **Planning** (PM) – Gather requirements, create project plan
2. **Plan Approval** (User) – Explicit user sign-off required
3. **Designing** (SA + UIUX + PO in parallel) – Architecture, UI/UX, backlog prioritization
4. **Design Verification** (QA + SecA in parallel) – Quality and security review
5. **Development** (DEV + DevOps in parallel) – Implementation
6. **Testing** (TESTER) – Functional, integration, E2E testing
7. **Bug Fixing** (DEVs + DevOps) – Address identified issues
8. **Deployment Prep** (DevOps) – CI/CD, staging, production readiness
9. **Reporting & Documentation** (REPORTER) – Comprehensive documentation
10. **Final Review** (STAKEHOLDER) – Business approval
11. **Repeat Cycle** (if needed) or **Completion**

---

## Cross-Role Dependencies

```
                              ┌──────┐
                              │  PM  │
                              └──┬───┘
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
                ┌──────┐    ┌──────┐     ┌──────┐
                │  SA  │    │ UIUX │     │  PO  │ ← (provides clarifications)
                └──┬───┘    └──┬───┘     └──────┘
                   └─────┬─────┘
            ┌────────────┴────────────┐
            ▼                         ▼
        ┌──────┐                  ┌──────┐
        │  QA  │                  │ SecA │
        └──┬───┘                  └──┬───┘
           └────────────┬────────────┘
             ┌─────────┴─────────┐
             ▼                   ▼
         ┌──────┐           ┌────────┐
         │ DEV  │           │ DevOps │
         └──┬───┘           └───┬────┘
            └─────────┬─────────┘
                       ▼
                  ┌────────┐
                  │ TESTER │
                  └───┬────┘
                      ▼
                 ┌──────────┐
                 │ REPORTER │
                 └────┬─────┘
                      ▼
              ┌─────────────┐
              │ STAKEHOLDER │
              └──────┬──────┘
         ┌───────────┴───────────┐
         ▼                       ▼
    ✅ Complete            ↩ Rejected → PM
```

---

## Core Rules Every Agent MUST Obey

### 1. Approval Gates
Critical phases require explicit approval:
| Gate | Approver | Artifact |
|------|----------|----------|
| Project Plan | User | Project-Plan-v*.md |
| Design | QA + SecA | Design-Verification-Report, Security-Review-Report |
| Final Delivery | STAKEHOLDER | Final-Approval-Report.md |

### 2. Auto-Communication via @Tags
Always use @role tags to notify next agents.
- **Available roles:** @PM, @PO, @SA, @UIUX, @QA, @SECA, @DEV, @DEVOPS, @TESTER, @REPORTER, @STAKEHOLDER
- Example: `### Next Step: @SA - Start designing` or `@TESTER - Please test`

### 3. Mandatory Documentation Tags
Every action must be tagged with appropriate hashtags:

| Category | Tags |
|----------|------|
| **Planning** | `#planning`, `#product-owner`, `#backlog` |
| **Design** | `#designing`, `#uiux-design` |
| **Verification** | `#verify-design`, `#security-review` |
| **Development** | `#development`, `#devops` |
| **Testing** | `#testing` |
| **Bug Fixes** | `#fixbug-critical`, `#fixbug-high`, `#fixbug-medium`, `#fixbug-low` |
| **Status** | `#blocked`, `#hotfix`, `#rollback` |
| **Deployment** | `#deployed-staging`, `#deployed-production` |
| **Research** | `#searching` |
| **Reporting** | `#reporting`, `#stakeholder-review` |

### 4. No Scope Creep
- No new features or changes outside approved Project Plan
- Any change requires PM + PO to revise plan and get user re-approval

### 5. Artifact Naming Convention
Use versioned names attached to the current Sprint:
| Artifact | Owner |
|----------|-------|
| `Project-Plan-Sprint-[N]-v*.md` | PM |
| `Product-Backlog-Sprint-[N]-v*.md` | PO |
| `UIUX-Design-Spec-Sprint-[N]-v*.md` | UIUX |
| `Backend-Design-Spec-Sprint-[N]-v*.md` | SA |
| `Design-Verification-Report-Sprint-[N]-v*.md` | QA |
| `Security-Review-Report-Sprint-[N]-v*.md` | SecA |
| `Development-Log-Sprint-[N]-v*.md` | DEV |
| `DevOps-Plan-and-Log-Sprint-[N]-v*.md` | DevOps |
| `Test-Report-Sprint-[N]-v*.md` | TESTER |
| `Phase-Report-Sprint-[N]-v*.md` | REPORTER |
| `Master-Documentation.md` | REPORTER |
| `Final-Project-Report.md` | REPORTER |
| `Final-Approval-Report.md` | STAKEHOLDER |

⚠️ **CRITICAL LOCATION RULE:**  
ALL project artifacts MUST be created in the project workspace with organized structure based on **Sprint**:

**Base Directory:** `docs/sprints/sprint-[N]/`

| Category | Folder Path | Content Example | Owner |
|----------|-------------|-----------------|-------|
| Plans | `docs/sprints/sprint-[N]/plans/` | `Project-Plan-Sprint-[N]-v*.md`, `Product-Backlog-Sprint-[N]-v*.md` | PM, PO |
| Designs | `docs/sprints/sprint-[N]/designs/` | `Backend-Design-Spec-Sprint-[N]-v*.md`, `UIUX-Design-Spec-Sprint-[N]-v*.md` | SA, UIUX |
| Reviews | `docs/sprints/sprint-[N]/reviews/` | `Design-Verification-Report-Sprint-[N]-v*.md`, `Security-Review-Report-Sprint-[N]-v*.md` | QA, SecA |
| Logs | `docs/sprints/sprint-[N]/logs/` | `Development-Log-Sprint-[N]-v*.md`, `DevOps-Plan-and-Log-Sprint-[N]-v*.md` | DEV, DevOps |
| Tests | `docs/sprints/sprint-[N]/tests/` | `Test-Report-Sprint-[N]-v*.md` | TESTER |
| Reports | `docs/sprints/sprint-[N]/reports/` | `Phase-Report-Sprint-[N]-v*.md` | REPORTER |
| Global | `docs/global/reports/` | `Final-Project-Report.md`, `Final-Approval-Report.md` | REPORTER, STAKEHOLDER |
| Global | `docs/global/` | `Master-Documentation.md` | REPORTER |

**FORBIDDEN:** `.gemini/` directory (reserved for instructions only)

### 6. Bug Priority Classification
| Priority | Tag | Criteria |
|----------|-----|----------|
| **Critical** | `#fixbug-critical` | Breaks core functionality, data loss, security exploit |
| **High** | `#fixbug-high` | Major feature broken, serious UX issue |
| **Medium** | `#fixbug-medium` | Works but with wrong behavior or poor UX |
| **Low** | `#fixbug-low` | Cosmetic, minor inconsistency |

### 7. Cycle Repeat Triggers
Handled by REPORTER or STAKEHOLDER when:
- ❌ Unresolved critical/high bugs
- ❌ Rejected design or security review
- ❌ Stakeholder rejection
- ❌ Incomplete requirements coverage

**Action:** Tag `@PM` with reason → PM engages user → New plan version

### 8. Transparency & Evidence
- Use screenshots, recordings, or browser artifacts for proof
- All agents must produce verifiable artifacts (logs, reports, diagrams)

### 10. Mandatory Reporting
After completing any task or phase, the role **MUST** create the corresponding report file as specified in the Artifact Naming Convention. This ensures full traceability and audit trail.

- **No task is considered complete without its artifact.**
- Artifacts must be placed in the exact folder structure: `docs/sprints/sprint-[N]/[category]/`
- Use version numbers (v1, v2, etc.) for revisions.

### 11. Completion Criteria
- ✅ STAKEHOLDER approves
- ✅ No critical/high bugs remain
- ✅ All Must-Have features delivered and verified
- ✅ REPORTER creates Final-Project-Report.md
- ✅ User is notified

---

## Definition of Done (DoD)

A feature/task is "Done" when ALL of the following are true:

### For Development Tasks:
- [ ] Code implemented according to approved design specs
- [ ] Code follows project coding standards
- [ ] Local testing passed
- [ ] Evidence captured (screenshots/logs)
- [ ] Tagged with `#development`
- [ ] Handoff to TESTER completed

### For Testing:
- [ ] All test cases executed
- [ ] No critical/high bugs open
- [ ] Evidence documented in Test-Report
- [ ] Tagged with `#testing`

### For Deployment:
- [ ] CI/CD pipeline passing
- [ ] Staging environment verified
- [ ] Security checklist completed
- [ ] Tagged with `#deployed-staging` or `#deployed-production`

### For Project Completion:
- [ ] All Must-Have features verified
- [ ] STAKEHOLDER approved
- [ ] Final documentation complete
- [ ] User notified

---

## Incident / Hotfix Workflow

For **critical production issues** that require bypassing the normal cycle:

```
🚨 Incident     ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
   Detected ───▶│   Triage    │───▶│   Hotfix    │───▶│ Quick Test  │
                │ (PM+DevOps) │    │   (DEV)     │    │  (TESTER)   │
                └─────────────┘    └─────────────┘    └──────┬──────┘
                                                             │
                ┌─────────────┐    ┌─────────────┐           │
                │  Postmortem │◀───│   Deploy    │◀──────────┘
                │ (REPORTER)  │    │  (DevOps)   │
                └─────────────┘    └─────────────┘
```

**Rules:**
1. Tag with `#hotfix` and `#fixbug-critical`
2. PM must approve hotfix scope (no feature additions)
3. Minimal testing required (smoke test only)
4. Full regression testing in next regular cycle
5. REPORTER must document incident in Phase-Report

**Rollback:** If hotfix fails, tag `#rollback` and revert immediately

---

## Global Handoff Template

Use this at the end of **every artifact**:

```markdown
### Next Step:
- [List of @tags and actions]
- [Clear status: ready for next phase / awaiting approval / cycle repeat]

#[appropriate-tags]
```

---

## Final Note

> ⚠️ **ALL AGENTS MUST STRICTLY ADHERE TO THESE RULES.**  
> Any deviation will break the workflow.  
> If unsure, tag `@PM` for clarification.

#global-rules #reporting

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.1 | 2025-12-23 | Added PO role, new tags (#product-owner, #backlog, #blocked, #hotfix, #rollback, #deployed-*), Definition of Done, Cross-Role Dependencies diagram, Incident/Hotfix workflow, Changelog |
| 1.0 | Initial | Initial release with 10 roles and core SDLC flow |