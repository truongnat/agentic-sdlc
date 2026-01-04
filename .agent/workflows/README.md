# Workflows Directory

> **Agentic SDLC Workflow Definitions**

**Last Updated:** 2026-01-03

## Overview

This directory contains all workflow definitions for the Agentic SDLC system. Workflows are organized into four categories based on their purpose.

## Directory Structure

```
workflows/
├── README.md           # This file
├── DECISION-TREE.md    # Workflow routing decision tree
│
├── process/            # Process automation (5 workflows)
│   ├── INDEX.md
│   ├── cycle.md       # Task lifecycle
│   ├── orchestrator.md # Full SDLC automation
│   ├── explore.md     # Deep investigation (stub)
│   ├── emergency.md   # Hotfix response (stub)
│   └── sprint.md      # Sprint management (stub)
│
├── support/            # Background operations (5 workflows)
│   ├── INDEX.md
│   ├── brain.md       # AI brain management
│   ├── compound.md    # Compound learning
│   ├── release.md     # Release management (stub)
│   ├── housekeeping.md # Cleanup (stub)
│   └── route.md       # Request routing (stub)
│
└── utilities/          # Helper workflows (2 workflows)
    ├── INDEX.md
    ├── validate.md    # Validation (stub)
    └── metrics.md     # Metrics (stub)
```

## Quick Reference

### Role/Skills Execution (Formerly Core Workflows)

| Command | Role | Description |
|---------|------|-------------|
| `/pm` | @PM | [Project Plan/Tasks](../skills/role-pm.md) |
| `/ba` | @BA | [Requirements/Stories](../skills/role-ba.md) |
| `/sa` | @SA | [Architecture/API](../skills/role-sa.md) |
| `/uiux` | @UIUX | [Design Specs](../skills/role-uiux.md) |
| `/dev` | @DEV | [Implementation](../skills/role-dev.md) |
| `/tester` | @TESTER | [Testing/QA](../skills/role-tester.md) |
| `/seca` | @SECA | [Security Review](../skills/role-seca.md) |
| `/devops` | @DEVOPS | [CI/CD & Deploy](../skills/role-devops.md) |

### Process Workflows

| Command | Description |
|---------|-------------|
| `/cycle` | Complete task lifecycle |
| `/orchestrator` | Full SDLC automation |
| `/explore` | Deep investigation (stub) |
| `/emergency` | Hotfix response (stub) |
| `/sprint` | Sprint management (stub) |

### Support Workflows

| Command | Description |
|---------|-------------|
| `/brain` | AI brain sync and management |
| `/compound` | Knowledge capture after tasks |
| `/release` | Release and versioning (stub) |
| `/housekeeping` | Cleanup and maintenance (stub) |
| `/route` | Request routing (stub) |

### Utility Workflows

| Command | Description |
|---------|-------------|
| `/validate` | Project validation (stub) |
| `/metrics` | Metrics collection (stub) |

## Workflow Format

All workflows follow this YAML frontmatter + markdown format:

```markdown
---
description: Brief workflow description
---

# Workflow Title

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
[Protocol rules]

### 0.0 **Team Communication (MANDATORY):**
[Communication steps]

## Key Duties / Steps

### 0. **RESEARCH FIRST (MANDATORY):**
[Research steps]

### 1. [Step Name]
[Step details]

#workflow-tags
```

## Turbo Mode

Workflows can enable auto-execution with annotations:

- `// turbo` - Auto-run the next step only
- `// turbo-all` - Auto-run all steps in the workflow

## Statistics

- **Total Workflows:** 20
- **Active Workflows:** 12
- **Stub Workflows:** 8

## See Also

- [DECISION-TREE.md](./DECISION-TREE.md) - Workflow routing logic
- [.agent/rules/global.md](../rules/global.md) - Global SDLC rules
- [.agent/skills/](../skills/) - Skill and Role definitions

## Tags

`#workflows` `#sdlc` `#automation` `#agentic`
