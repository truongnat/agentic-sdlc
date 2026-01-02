# Kiro IDE Integration Guide

## Overview

Kiro IDE integration is handled through the `.kiro/steering/` directory, which contains lightweight reference files that point to the source documentation in `.agent/`.

## Architecture

```
User (Kiro IDE)
    ↓
.kiro/steering/          # Lightweight references (auto-loaded)
    ↓
.agent/                  # Source of truth
    ├── roles/           # Full role documentation
    ├── workflows/       # Workflow implementations
    └── knowledge-base/  # Compound learning system
```

## File Structure

### Kiro Steering Files
```
.kiro/steering/
├── README.md                    # Steering guide
├── 00-teamlifecycle-overview.md # Always loaded
├── global-rules.md              # Always loaded
├── critical-patterns.md         # Always loaded
├── compound-learning.md         # Always loaded
├── workflow-enhancements.md     # Always loaded
├── workflow-routing.md          # Always loaded
├── role-brain.md               # @BRAIN reference
├── role-pm.md                  # @PM reference
├── role-po.md                  # @PO reference
├── role-sa.md                  # @SA reference
├── role-uiux.md                # @UIUX reference
├── role-qa.md                  # @QA reference
├── role-seca.md                # @SECA reference
├── role-dev.md                 # @DEV reference
├── role-devops.md              # @DEVOPS reference
├── role-tester.md              # @TESTER reference
├── role-reporter.md            # @REPORTER reference
├── role-stakeholder.md         # @STAKEHOLDER reference
└── role-orchestrator.md        # @ORCHESTRATOR reference
```

### Source Files
```
.agent/roles/
├── role-brain.md               # Full BRAIN documentation
├── role-pm.md                  # Full PM documentation
├── role-po.md                  # Full PO documentation
├── role-sa.md                  # Full SA documentation
├── role-uiux.md                # Full UIUX documentation
├── role-qa.md                  # Full QA documentation
├── role-seca.md                # Full SECA documentation
├── role-dev.md                 # Full DEV documentation
├── role-devops.md              # Full DEVOPS documentation
├── role-tester.md              # Full TESTER documentation
├── role-reporter.md            # Full REPORTER documentation
├── role-stakeholder.md         # Full STAKEHOLDER documentation
└── role-orchestrator.md        # Full ORCHESTRATOR documentation
```

## How It Works

### 1. Automatic Loading
Kiro IDE automatically loads all files in `.kiro/steering/` based on their frontmatter:

```yaml
---
inclusion: always    # Loaded in every conversation
---
```

```yaml
---
inclusion: manual    # Loaded when keywords mentioned
keywords: ["@PM", "project manager", "planning"]
---
```

### 2. Reference Pattern
Each role file in `.kiro/steering/` is a lightweight reference:

```markdown
---
inclusion: manual
keywords: ["@PM", "project manager"]
source: .agent/roles/role-pm.md
---

# @PM - Project Manager

**Source:** `.agent/roles/role-pm.md`

## Quick Reference
[Brief overview and commands]

For complete documentation, see `.agent/roles/role-pm.md`
```

### 3. Source of Truth
Full documentation lives in `.agent/roles/`:

```markdown
---
title: "@PM - Project Manager"
version: 1.0.0
category: role
priority: high
---

# Project Manager (PM) Role

[Complete documentation with all details]
```

## Usage in Kiro IDE

### Activating Roles

Simply mention the role in your message:

```
@PM - Build a todo app with React
```

Kiro will:
1. Detect the `@PM` keyword
2. Load `.kiro/steering/role-pm.md`
3. Reference `.agent/roles/role-pm.md` for full context
4. Execute the PM role

### Using BRAIN Master Orchestrator

```
@BRAIN - Build a todo app

@BRAIN /status

@BRAIN /validate

@BRAIN /auto-execute
```

### Using Enhanced Workflows

```
@DEV /cycle - Fix login button on mobile

@SA /explore - Real-time notification architecture

@DEV /compound - Document React hydration fix

@DEV /emergency - P0: Payment gateway down

@ORCHESTRATOR /housekeeping
```

### Using Full Automation

```
@ORCHESTRATOR --mode=full-auto
Build a complete authentication system with OAuth
```

## Available Commands

### BRAIN Commands
- `@BRAIN /status` - Show current workflow state
- `@BRAIN /validate` - Validate phase completion
- `@BRAIN /auto-execute` - Full automation mode
- `@BRAIN /rollback [STATE]` - Rollback to previous state
- `@BRAIN /force-transition [REASON]` - Emergency bypass

### Role Mentions
- `@PM` - Project Manager
- `@PO` - Product Owner
- `@SA` - System Analyst
- `@UIUX` - UI/UX Designer
- `@QA` - Quality Assurance
- `@SECA` - Security Analyst
- `@DEV` - Developer
- `@DEVOPS` - DevOps Engineer
- `@TESTER` - Tester
- `@REPORTER` - Reporter
- `@STAKEHOLDER` - Stakeholder
- `@ORCHESTRATOR` - Orchestrator

### Enhanced Workflows
- `/cycle` - Complete task lifecycle (< 4 hours)
- `/explore` - Deep investigation
- `/compound` - Capture knowledge
- `/emergency` - Critical incident response
- `/housekeeping` - Cleanup and maintenance
- `/route` - Intelligent workflow selection

## Workflow States

BRAIN manages these workflow states:

```
IDLE → PLANNING → PLAN_APPROVAL → DESIGNING → DESIGN_REVIEW → 
DEVELOPMENT → TESTING → BUG_FIXING → DEPLOYMENT → REPORTING → 
FINAL_REVIEW → FINAL_APPROVAL → COMPLETE
```

### Approval Gates 🚪
1. **Project Plan** - After PLANNING
2. **Design** - After DESIGN_REVIEW (if issues)
3. **Final Delivery** - After FINAL_REVIEW

### Parallel Execution ⚡
- **Design Phase:** @SA + @UIUX + @PO work simultaneously
- **Review Phase:** @QA + @SECA work simultaneously
- **Development Phase:** @DEV + @DEVOPS work simultaneously

## Examples

### Example 1: Simple Task
```
User: @DEV /cycle - Add user avatar upload

Kiro executes:
1. Loads role-dev.md reference
2. Accesses full documentation from .agent/roles/role-dev.md
3. Executes /cycle workflow
4. Completes task with atomic commit
5. Compounds knowledge if non-obvious
```

### Example 2: Full Project with BRAIN
```
User: @BRAIN - Build a todo app with React

BRAIN:
🧠 BRAIN Initialized
State: IDLE → PLANNING
Activating @PM...

PM creates plan → User approves → BRAIN transitions to DESIGNING
@SA + @UIUX + @PO work in parallel → BRAIN validates completion
@QA + @SECA review → BRAIN checks for issues
@DEV + @DEVOPS implement → BRAIN monitors progress
@TESTER tests → BRAIN checks for bugs
@DEVOPS deploys → BRAIN validates deployment
@REPORTER documents → BRAIN reviews completeness
@STAKEHOLDER approves → BRAIN marks COMPLETE ✅
```

### Example 3: Check Status
```
User: @BRAIN /status

📊 Workflow Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current State: DESIGNING
Sprint: sprint-1
Phase Progress: 3/12 (25%)

✅ Completed:
  - PLANNING: @PM (Project-Plan-v1.md)
  - PLAN_APPROVAL: User approved

🔄 In Progress:
  - @SA: Architecture spec (80%)
  - @UIUX: UI/UX spec (60%)
  - @PO: Product backlog (90%)

⏳ Pending:
  - DESIGN_REVIEW: @QA + @SECA
  - DEVELOPMENT: @DEV + @DEVOPS
  - ... (remaining phases)

🚪 Next Gate: Design Approval (after QA + SECA review)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Customization

### Adding New Roles

1. Create full documentation in `.agent/roles/role-[name].md`
2. Create reference in `.kiro/steering/role-[name].md`:

```markdown
---
inclusion: manual
keywords: ["@NEWROLE", "new role"]
source: .agent/roles/role-[name].md
---

# @NEWROLE - New Role Name

**Source:** `.agent/roles/role-[name].md`

[Quick reference content]

For complete documentation, see `.agent/roles/role-[name].md`
```

3. Update `.kiro/steering/00-teamlifecycle-overview.md` to include new role

### Modifying Existing Roles

1. Edit the source file in `.agent/roles/role-[name].md`
2. Optionally update quick reference in `.kiro/steering/role-[name].md`
3. Kiro will automatically use the updated documentation

## Benefits

### Single Source of Truth
- All documentation in `.agent/`
- Update once, reference everywhere
- No duplication or drift

### IDE Agnostic
- Core logic not tied to Kiro
- Can port to other IDEs easily
- Maintains consistency

### Lightweight References
- Kiro loads small reference files
- Full context accessed on-demand
- Better performance

### Maintainable
- Clear separation of concerns
- Easy to update and extend
- Version control friendly

## Troubleshooting

### Role Not Activating

**Check:**
1. Reference file exists: `.kiro/steering/role-[name].md`
2. Source file exists: `.agent/roles/role-[name].md`
3. Keywords are correct in frontmatter
4. Mention exact keyword in message (e.g., `@PM`)

### Commands Not Working

**Check:**
1. Command syntax is correct (e.g., `@BRAIN /status`)
2. Role is activated before using commands
3. Kiro has access to project files

### Workflow Not Progressing

**Check:**
1. BRAIN is managing the workflow (`@BRAIN` mentioned)
2. Approval gates are satisfied
3. Required artifacts exist
4. No critical/high bugs blocking progress

## Documentation

- **Architecture:** `docs/ARCHITECTURE-OVERVIEW.md`
- **BRAIN Details:** `docs/BRAIN-ARCHITECTURE.md`
- **Diagrams:** `docs/SDLC-Diagram.md`
- **Setup Guide:** `docs/SETUP-COMPLETE.md`
- **Steering README:** `.kiro/steering/README.md`
- **Agent README:** `.agent/README.md`

## Support

For issues or questions:
1. Check documentation in `docs/`
2. Review role definitions in `.agent/roles/`
3. Check steering files in `.kiro/steering/`
4. Use `@BRAIN /status` to check workflow state

---

**Version:** 1.0.0
**Created:** 2026-01-02
**Status:** Production Ready ✅

#kiro-ide #integration #teamlifecycle
