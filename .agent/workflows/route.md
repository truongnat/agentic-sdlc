---
description: [Support] Route - Workflow Selection Helper
---

# /route - Intelligent Request Routing

## ⚠️ PURPOSE
Analyzes user requests and routes to the appropriate workflow or role. Use when unsure which workflow to invoke.

## Quick Reference

### By Request Type

| Request Type | Recommended Route |
|--------------|-------------------|
| "Build a new feature" | `/orchestrator` or `/pm` → full SDLC |
| "Fix this bug" | `/dev` or `/emergency` (if P0) |
| "Review this design" | `/tester` + `/seca` |
| "Set up infrastructure" | `/devops` |
| "Create user stories" | `/ba` |
| "Design the UI" | `/uiux` |
| "Design the API" | `/sa` |
| "How do I..." | `/explore` first, then appropriate role |

### By Urgency

| Urgency | Route |
|---------|-------|
| 🔴 Production down | `/emergency --severity P0` |
| 🟠 Major bug | `/emergency --severity P1` |
| 🟡 Normal task | `/cycle` |
| 🟢 Investigation | `/explore` |

### By Phase

| SDLC Phase | Route |
|------------|-------|
| Planning | `/pm` |
| Requirements | `/ba` |
| Design | `/sa` + `/uiux` |
| Verification | `/tester` + `/seca` |
| Implementation | `/dev` |
| Testing | `/tester` |
| Deployment | `/devops` |
| Closure | `/pm` |

## Decision Tree

```
Is this an emergency?
├── Yes → /emergency
└── No → Continue

Is this a full project/feature?
├── Yes → /orchestrator (full automation)
└── No → Continue

Is this a single task?
├── Yes → /cycle
└── No → Continue

What phase are you in?
├── Planning → /pm
├── Requirements → /ba
├── Design → /sa or /uiux
├── Review → /tester or /seca
├── Development → /dev
├── Testing → /tester
└── Deployment → /devops

Need maintenance?
├── Brain sync → /brain
├── Cleanup → /housekeeping
├── Validation → /validate
├── Metrics → /metrics
└── Release → /release
```

## Role Selection Guide

### @PM - Project Manager
**Use when:**
- Starting a new project
- Creating project plans
- Tracking sprint progress
- Generating reports

### @BA - Business Analyst
**Use when:**
- Gathering requirements
- Writing user stories
- Defining acceptance criteria

### @SA - System Analyst
**Use when:**
- Designing architecture
- Creating API specifications
- Making technical decisions

### @UIUX - UI/UX Designer
**Use when:**
- Designing interfaces
- Creating wireframes
- Ensuring accessibility

### @DEV - Developer
**Use when:**
- Implementing features
- Writing code
- Fixing bugs

### @TESTER - Tester
**Use when:**
- Reviewing designs
- Writing test plans
- Executing E2E tests

### @SECA - Security Analyst
**Use when:**
- Security review
- Threat modeling
- Compliance checking

### @DEVOPS - DevOps Engineer
**Use when:**
- Setting up CI/CD
- Managing deployments
- Merging PRs

## Common Patterns

### New Feature Request
```
/pm → /ba → /sa + /uiux → /tester + /seca → /dev → /tester → /devops
```

### Bug Fix
```
Minor: /cycle
Major: /emergency → /dev → /tester → /devops → /compound
```

### Documentation Update
```
/dev (for code docs) or /pm (for project docs)
```

### Maintenance
```
/housekeeping → /validate → /metrics → /brain
```

#route #routing #decision-tree #workflow-selection
