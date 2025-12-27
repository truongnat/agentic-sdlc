# 📚 TeamLifecycle Instructions - Usage Guide

> **Version:** 1.0  
> **Last Updated:** 2025-12-23

---

## 🎯 Overview

This instruction set simulates a **complete Software Development Lifecycle (SDLC)** with specialized roles. When you invoke a role using `@tag`, Gemini will act as that role and perform tasks according to the defined workflow.

---

## 📁 Directory Structure

```
.gemini/instructions/
├── global.md                    # Global rules (mandatory)
├── roles/                       # Team roles
│   ├── pm.md                    # Project Manager
│   ├── po.md                    # Product Owner
│   ├── sa.md                    # Solution Architect
│   ├── designer.md              # UI/UX Designer
│   ├── qa.md                    # Quality Assurance
│   ├── seca.md                  # Security Analyst
│   ├── dev.md                   # Developer
│   ├── devops.md                # DevOps Engineer
│   ├── tester.md                # Tester
│   ├── reporter.md              # Reporter
│   └── stakeholder.md           # Stakeholder
└── templates/                   # Document templates
    ├── Project-Plan-Template.md
    ├── Product-Backlog-Template.md
    ├── Backend-Design-Spec-Template.md
    ├── Design-Verification-Report-Template.md
    ├── Security-Review-Report-Template.md
    ├── Development-Log-Template.md
    ├── DevOps-Plan-Template.md
    ├── Test-Report-Template.md
    ├── Phase-Report-Template.md
    ├── Final-Approval-Report-Template.md
    ├── definition-of-done.md
    └── incident-response.md
```

---

## 🚀 Getting Started

### Step 1: Start a Project

Invoke **PM** to begin planning:

```
@PM - I want to build a wedding website with:
- Couple introduction page
- Countdown timer
- Photo gallery
- RSVP form
```

PM will create `Project-Plan-v1.md` and wait for your approval.

### Step 2: Approval

After reviewing the plan, respond with:
- ✅ **"Approved"** - Proceed to next phase
- 🔄 **Provide feedback** - PM will revise and create a new version

### Step 3: Automatic Workflow

Once approved, roles are triggered automatically in sequence:

```
PM → SA + UIUX + PO → QA + SecA → DEV + DevOps → TESTER → REPORTER → STAKEHOLDER
```

---

## 📋 Roles & Tags

| Role | Tag | Responsibility |
|------|-----|----------------|
| **Project Manager** | `@PM` | Planning, scope management, team coordination |
| **Product Owner** | `@PO` | Backlog management, feature prioritization |
| **Solution Architect** | `@SA` | Backend architecture, database, API design |
| **UI/UX Designer** | `@UIUX` | Interface design, user experience |
| **QA Analyst** | `@QA` | Design review, quality assurance |
| **Security Analyst** | `@SECA` | Security assessment |
| **Developer** | `@DEV` | Code implementation |
| **DevOps** | `@DEVOPS` | CI/CD, deployment, infrastructure |
| **Tester** | `@TESTER` | Functional testing, bug detection |
| **Reporter** | `@REPORTER` | Progress reports, documentation |
| **Stakeholder** | `@STAKEHOLDER` | Final approval |

---

## 🏷️ Important Tags

### Phase Tags
| Tag | Description |
|-----|-------------|
| `#planning` | Planning phase |
| `#designing` | Design phase |
| `#development` | Development phase |
| `#testing` | Testing phase |
| `#reporting` | Reporting phase |

### Bug Priority Tags
| Tag | Severity |
|-----|----------|
| `#fixbug-critical` | Breaks core functionality |
| `#fixbug-high` | Major feature broken |
| `#fixbug-medium` | Works but incorrect behavior |
| `#fixbug-low` | Cosmetic issues |

### Special Tags
| Tag | Description |
|-----|-------------|
| `#blocked` | Blocked, needs support |
| `#hotfix` | Emergency fix |
| `#rollback` | Needs rollback |
| `#deployed-staging` | Deployed to staging |
| `#deployed-production` | Deployed to production |

---

## 📄 Generated Artifacts

Artifacts are organized by type in the `docs/` folder:

| Folder | Artifacts | Owner |
|--------|-----------|-------|
| `docs/plans/` | Project-Plan-v*.md, Product-Backlog-v*.md | PM, PO |
| `docs/designs/` | Backend-Design-Spec-v*.md, UIUX-Design-Spec-v*.md | SA, UIUX |
| `docs/reviews/` | Design-Verification-Report-v*.md, Security-Review-Report-v*.md | QA, SecA |
| `docs/logs/` | Development-Log-v*.md, DevOps-Plan-and-Log-v*.md | DEV, DevOps |
| `docs/tests/` | Test-Report-v*.md | TESTER |
| `docs/reports/` | Phase-Report-*.md, Final-Project-Report.md, Final-Approval-Report.md | REPORTER, STAKEHOLDER |

> ⚠️ **CRITICAL:** All artifacts are in `docs/`, NEVER in `.gemini/`

---

## 💡 Usage Examples

### Request new design
```
@UIUX - Design a gallery page with lightbox effect
```

### Request bug fix
```
@DEV - Fix BUG-001: Countdown not displaying correctly on mobile
```

### Request security review
```
@SECA - Review RSVP form for XSS vulnerabilities
```

### Check progress
```
@REPORTER - Summarize current project progress
```

### Request deployment
```
@DEVOPS - Deploy current version to staging
```

---

## ⚠️ Important Rules

### ✅ DO:
- Start with `@PM` for new projects
- Provide clear approval before phase transitions
- Use correct tags to invoke roles
- Review generated artifacts
- **Create and save the required report file after completing any task**

### ❌ DON'T:
- Skip phases (e.g., coding before design approval)
- Add features not in approved plan
- Bypass security review

---

## 🔄 Changing Scope

1. Invoke `@PM` with change request
2. PM creates new plan version
3. Wait for re-approval
4. Continue workflow

---

## 📞 Need Help?

If unsure which role to invoke:
```
@PM - I need help with [describe issue], who should I contact?
```

PM will direct you to the right person.

---

#instructions #usage-guide
