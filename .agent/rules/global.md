# TeamLifecycle Global Rules & Conventions
(Version 1.4 – Strict IT SDLC Simulation for Google Antigravity)

**Last Updated:** 2026-01-01  
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
9. **Reporting & Documentation** (REPORTER) – Update CHANGELOG.md and create comprehensive reports
10. **Final Review** (STAKEHOLDER) – Business approval
11. **Repeat Cycle** (if needed) or **Completion**

---

## Cross-Role Dependencies

(See Role Descriptions for specific handoffs)

---

## Specialized Rule Sets

**You MUST refer to these additional rule files for specific domains:**

1. **Artifacts & Naming:** `.agent/rules/artifacts.md`
   - Covers: Naming conventions, folder structure, forbidden locations.
2. **Git & Task Workflow:** `.agent/rules/git-workflow.md`
   - Covers: Jira-style task tracking, atomic commits, Definition of Done.
3. **Knowledge Base:** `.agent/rules/knowledge-base.md`
   - Covers: When and how to create knowledge entries.
4. **Auto-Learning System:** `.agent/rules/auto-learning.md`
   - Covers: Automatic knowledge capture from tasks, issues, and bug fixes.

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
- **Available roles:** @ORCHESTRATOR, @PM, @PO, @SA, @UIUX, @QA, @SECA, @DEV, @DEVOPS, @TESTER, @REPORTER, @STAKEHOLDER
- Example: `### Next Step: @SA - Start designing` or `@TESTER - Please test`
- **Orchestrator mode:** Add `--mode=full-auto` or `--mode=semi-auto` to enable automation

### 3. No Scope Creep
- No new features or changes outside approved Project Plan
- Any change requires PM + PO to revise plan and get user re-approval

### 4. Bug Priority Classification
| Priority | Tag | Criteria |
|----------|-----|----------|
| **Critical** | `#fixbug-critical` | Breaks core functionality, data loss, security exploit |
| **High** | `#fixbug-high` | Major feature broken, serious UX issue |
| **Medium** | `#fixbug-medium` | Works but with wrong behavior or poor UX |
| **Low** | `#fixbug-low` | Cosmetic, minor inconsistency |

### 5. Cycle Repeat Triggers
Handled by REPORTER or STAKEHOLDER when:
- ❌ Unresolved critical/high bugs
- ❌ Rejected design or security review
- ❌ Stakeholder rejection
- ❌ Incomplete requirements coverage

**Action:** Tag `@PM` with reason → PM engages user → New plan version

### 6. Transparency & Evidence
- Use screenshots, recordings, or browser artifacts for proof
- All agents must produce verifiable artifacts (logs, reports, diagrams)

### 7. Global Handoff Template

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
| 1.4 | 2026-01-01 | Split large rules into artifacts.md, git-workflow.md, knowledge-base.md |
| 1.3 | 2026-01-01 | Added Task Management & Atomic Git Commit Rules |
| 1.2 | 2026-01-01 | Migrated to Native Agent structure (.agent/). Updated paths. |
| 1.1 | 2025-12-23 | Added PO role, new tags (#product-owner, #backlog, #blocked, #hotfix, #rollback, #deployed-*), Definition of Done, Cross-Role Dependencies diagram, Incident/Hotfix workflow, Changelog |
| 1.0 | Initial | Initial release with 10 roles and core SDLC flow |
