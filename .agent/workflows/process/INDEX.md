# Process Workflows Index

> **End-to-end process automation workflows.**

**Last Updated:** 2026-01-03

## Overview

Process workflows orchestrate multi-phase operations, coordinating between roles to complete complex SDLC processes from start to finish.

## Workflows

| Command | Description | Status |
|---------|-------------|--------|
| `/cycle` | Complete Task Lifecycle - Plan → Work → Review → Compound | ✅ Active |
| `/orchestrator` | Full Automation Workflow - All SDLC Phases | ✅ Active |
| `/explore` | Deep Investigation - Multi-order analysis before planning | ✅ Active |
| `/emergency` | Hotfix Response - Critical incidents & production fixes | ✅ Active |
| `/sprint` | Sprint Management - Planning, tracking, retrospective | ✅ Active |

## Workflow Details

### `/cycle` - Complete Task Lifecycle
- **File:** `cycle.md`
- **Purpose:** Single task from research to completion
- **Flow:** Research → Planning → Feature Branch → Implementation → Verification → Merge → Self-Learning
- **Git Convention:** Feature branch, atomic commits, PR workflow
- **Outputs:** Updated `Development-Log.md`, `CHANGELOG.md`

### `/orchestrator` - Full SDLC Automation
- **File:** `orchestrator.md`
- **Purpose:** Complete project from requirements to deployment
- **Flow:** 
  1. Phase 1: Planning (@PM)
  2. Phase 2: Requirements (@BA)
  3. Phase 3: Design (@SA + @UIUX)
  4. Phase 4: Design Verification (@TESTER + @SECA)
  5. Phase 5: Development (@DEV + @DEVOPS)
  6. Phase 6: Testing (@TESTER)
  7. Phase 7: Bug Fixing (@DEV)
  8. Phase 8: Deployment (@DEVOPS)
  9. Phase 9-10: Reporting & Closure (@PM)
  10. Phase 11: Self-Learning

### `/explore` - Deep Investigation ⚠️
- **File:** `explore.md`
- **Status:** ✅ Active - Manual workflow
- **Purpose:** 4th-order analysis before major planning decisions
- **Use Case:** Complex features, architectural decisions

### `/emergency` - Hotfix Response ⚠️
- **File:** `emergency.md`
- **Status:** ✅ Active - Tool-backed
- **Purpose:** Critical production incident response
- **Use Case:** P0 bugs, security incidents

### `/sprint` - Sprint Management ⚠️
- **File:** `sprint.md`
- **Status:** ✅ Active - Tool-backed
- **Purpose:** Agile sprint lifecycle management
- **Use Case:** Sprint planning, daily standups, retrospectives

## Usage Examples

```bash
# Complete a single task
/cycle Implement user authentication

# Full project automation
/orchestrator Build a REST API for user management
```

## Tags

`#process` `#automation` `#lifecycle` `#sdlc`
