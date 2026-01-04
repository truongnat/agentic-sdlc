---
description: [Process] Orchestrator - Full Automation Workflow
---

# Orchestrator Workflow

> **Master Controller:** [View @BRAIN Skill](../../skills/role-brain.md)
> 
> **⚠️ Supervised by @BRAIN.** Report status on each phase transition.

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
All phases must be executed in order. No skipping.

## State Machine Integration
This workflow follows the state machine defined in `@BRAIN`. Before each phase transition:
1. Run `agentic-sdlc brain validate` to check prerequisites
2. Run `agentic-sdlc brain transition <NEW_STATE>` to update state
3. Artifacts required per state are validated automatically

### 0.0 **Team Communication (MANDATORY):**
   - **Announce:** `agentic-sdlc run tools/communication/cli.py send --channel general --thread "SDLC-Flow" --role ORCHESTRATOR --content "Starting Full SDLC Automation."`

### 0.1 **Initialize State (If New Sprint):**
```bash
agentic-sdlc brain init <SPRINT_NUMBER>
```

## SDLC Flow (State Transitions)

### Phase 1: Planning (@PM)
- Research, create Project Plan, wait for User approval.

### Phase 2: Requirements (@BA)
- Create User Stories with Gherkin acceptance criteria.

### Phase 3: Design (@SA + @UIUX)
- Create Backend and UI/UX design specs.

### Phase 4: Design Verification (@TESTER + @SECA)
- Review designs for quality and security.

### Phase 5: Development (@DEV + @DEVOPS)
- Feature branch, atomic commits, PRs, GitHub issues.

### Phase 6: Testing (@TESTER)
- E2E testing, provide `#testing-passed`.

### Phase 7: Bug Fixing (@DEV)
- Fix bugs, update KB.

### Phase 8: Deployment (@DEVOPS)
- Merge to main, deploy to staging/production.

### Phase 9-10: Reporting & Closure (@PM)
- Update CHANGELOG, Final Review.

### Phase 11: Self-Learning
- Run: `agentic-sdlc kb compound sync`
- Run: `agentic-sdlc learn --record-success`

#orchestrator #automation #sdlc
---
## ⚠️ ENFORCEMENT REMINDER
Before executing this workflow, agent MUST:
1. Have completed /preflight checks
2. Searched knowledge base for similar tasks
3. Checked current brain state
Failure to complete pre-flight = workflow violation.
