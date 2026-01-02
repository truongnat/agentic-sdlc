---
inclusion: manual
keywords: ["@BRAIN", "brain", "master", "orchestrate all"]
source: .agent/roles/role-brain.md
---

# @BRAIN - Master Orchestrator & Flow Controller

**Source:** `.agent/roles/role-brain.md`

This is a reference file. Full documentation is maintained in `.agent/roles/role-brain.md`.

## Quick Commands

- `@BRAIN /status` - Show current workflow state
- `@BRAIN /validate` - Validate phase completion  
- `@BRAIN /auto-execute` - Full automation mode
- `@BRAIN /rollback [STATE]` - Rollback to previous state
- `@BRAIN /force-transition [REASON]` - Emergency bypass

## Workflow States

IDLE → PLANNING → PLAN_APPROVAL → DESIGNING → DESIGN_REVIEW → DEVELOPMENT → TESTING → BUG_FIXING → DEPLOYMENT → REPORTING → FINAL_REVIEW → FINAL_APPROVAL → COMPLETE

## Critical Rules

1. **NEVER skip phases** - Follow diagram strictly
2. **ALWAYS validate** - Check prerequisites before transitions
3. **ENFORCE approvals** - Block without explicit user approval
4. **TRACK everything** - Maintain complete state history
5. **FAIL safely** - Rollback on errors, never corrupt state

For complete documentation, see `.agent/roles/role-brain.md`

#brain #master-orchestrator #workflow-controller
