# TeamLifecycle Architecture Overview

## System Architecture

The TeamLifecycle SDLC workflow system is organized with a clear separation between source documentation and IDE integration.

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTION                          │
│                   (Kiro IDE / Chat)                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              .kiro/steering/                                 │
│         (Lightweight References)                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ role-brain.md    → .agent/roles/role-brain.md        │  │
│  │ role-pm.md       → .agent/roles/role-pm.md           │  │
│  │ role-dev.md      → .agent/roles/role-dev.md          │  │
│  │ ... (all roles)                                       │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              .agent/                                         │
│         (SOURCE OF TRUTH)                                    │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ roles/           - Full role documentation           │  │
│  │ workflows/       - Workflow implementations          │  │
│  │ knowledge-base/  - Compound learning system          │  │
│  │ templates/       - Document templates                │  │
│  │ rules/           - Global rules                      │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              docs/                                           │
│         (Generated Artifacts)                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ sprints/sprint-N/                                     │  │
│  │   ├── plans/      - Project plans                    │  │
│  │   ├── designs/    - Design specs                     │  │
│  │   ├── reviews/    - QA/Security reports              │  │
│  │   ├── logs/       - Dev/DevOps logs                  │  │
│  │   └── reports/    - Final reports                    │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Directory Structure

### `.agent/` - Source of Truth
All core documentation, roles, workflows, and knowledge base.

```
.agent/
├── README.md                    # Architecture explanation
├── CONFIG.md                    # Configuration guide
├── USAGE.md                     # Usage instructions
├── roles/                       # Full role documentation
│   ├── role-brain.md           # Master orchestrator
│   ├── role-pm.md              # Project Manager
│   ├── role-po.md              # Product Owner
│   ├── role-sa.md              # System Analyst
│   ├── role-uiux.md            # UI/UX Designer
│   ├── role-qa.md              # Quality Assurance
│   ├── role-seca.md            # Security Analyst
│   ├── role-dev.md             # Developer
│   ├── role-devops.md          # DevOps Engineer
│   ├── role-tester.md          # Tester
│   ├── role-reporter.md        # Reporter
│   ├── role-stakeholder.md     # Stakeholder
│   └── role-orchestrator.md    # Orchestrator
├── workflows/                   # Workflow implementations
│   ├── cycle.md                # Complete task lifecycle
│   ├── explore.md              # Deep investigation
│   ├── compound.md             # Knowledge capture
│   ├── emergency.md            # Critical incident response
│   ├── housekeeping.md         # Cleanup and maintenance
│   └── route.md                # Workflow selection
├── knowledge-base/              # Compound learning system
│   ├── INDEX.md                # Searchable index
│   ├── bugs/                   # Bug patterns
│   ├── features/               # Feature implementations
│   ├── architecture/           # Architecture decisions
│   ├── security/               # Security fixes
│   └── performance/            # Optimizations
├── templates/                   # Document templates
│   ├── project-plan.md
│   ├── architecture-spec.md
│   ├── uiux-spec.md
│   └── ...
└── rules/                       # Global rules
    ├── global-rules.md
    ├── critical-patterns.md
    └── compound-learning.md
```

### `.kiro/steering/` - IDE Integration
Lightweight reference files that point to `.agent/` source.

```
.kiro/steering/
├── README.md                    # Steering guide
├── 00-teamlifecycle-overview.md # Always loaded
├── global-rules.md              # Always loaded
├── critical-patterns.md         # Always loaded
├── compound-learning.md         # Always loaded
├── workflow-enhancements.md     # Always loaded
├── workflow-routing.md          # Always loaded
├── role-brain.md               # Reference → .agent/roles/
├── role-pm.md                  # Reference → .agent/roles/
├── role-po.md                  # Reference → .agent/roles/
├── role-sa.md                  # Reference → .agent/roles/
├── role-uiux.md                # Reference → .agent/roles/
├── role-qa.md                  # Reference → .agent/roles/
├── role-seca.md                # Reference → .agent/roles/
├── role-dev.md                 # Reference → .agent/roles/
├── role-devops.md              # Reference → .agent/roles/
├── role-tester.md              # Reference → .agent/roles/
├── role-reporter.md            # Reference → .agent/roles/
├── role-stakeholder.md         # Reference → .agent/roles/
└── role-orchestrator.md        # Reference → .agent/roles/
```

### `docs/` - Generated Artifacts
Sprint-specific deliverables and documentation.

```
docs/
├── SDLC-Diagram.md             # Mermaid workflow diagrams
├── BRAIN-ARCHITECTURE.md       # BRAIN technical docs
├── ARCHITECTURE-OVERVIEW.md    # This file
└── sprints/
    └── sprint-N/
        ├── plans/              # PM, PO artifacts
        ├── designs/            # SA, UIUX artifacts
        ├── reviews/            # QA, SECA artifacts
        ├── logs/               # DEV, DEVOPS, TESTER artifacts
        └── reports/            # REPORTER, STAKEHOLDER artifacts
```

## Component Roles

### 🧠 BRAIN - Master Orchestrator
- **Location:** `.agent/roles/role-brain.md`
- **Purpose:** Root-level controller that strictly manages all workflow execution
- **Commands:** `/status`, `/validate`, `/auto-execute`, `/rollback`, `/force-transition`
- **States:** 13 workflow states from IDLE to COMPLETE
- **Enforcement:** No phase skipping, approval gates, artifact validation

### 👥 Roles (12 Total)
Each role has:
- **Full documentation** in `.agent/roles/role-[name].md`
- **Lightweight reference** in `.kiro/steering/role-[name].md`
- **Clear responsibilities** and artifact requirements
- **Strict rules** and communication templates

### 🔄 Workflows (6 Enhanced)
- **`/cycle`** - Complete task lifecycle (< 4 hours)
- **`/explore`** - Deep investigation for complex features
- **`/compound`** - Capture knowledge after solving problems
- **`/emergency`** - Critical incident response
- **`/housekeeping`** - Cleanup and maintenance
- **`/route`** - Intelligent workflow selection

### 📚 Knowledge Base
- **Location:** `.agent/knowledge-base/`
- **Purpose:** Compound learning system
- **Structure:** YAML frontmatter + categorized entries
- **Integration:** Search-first workflow, auto-compounding

## Workflow Execution

### Standard SDLC Flow
```
IDLE
  ↓
PLANNING (@PM)
  ↓
PLAN_APPROVAL (User Gate 🚪)
  ↓
DESIGNING (@SA + @UIUX + @PO in parallel)
  ↓
DESIGN_REVIEW (@QA + @SECA in parallel)
  ↓
DEVELOPMENT (@DEV + @DEVOPS in parallel)
  ↓
TESTING (@TESTER)
  ↓
BUG_FIXING (@DEV) ←→ TESTING (if bugs found)
  ↓
DEPLOYMENT (@DEVOPS)
  ↓
REPORTING (@REPORTER)
  ↓
FINAL_REVIEW (@STAKEHOLDER)
  ↓
FINAL_APPROVAL (User Gate 🚪)
  ↓
COMPLETE ✅
```

### Approval Gates
1. **Gate 1:** Project Plan Approval (after PLANNING)
2. **Gate 2:** Design Approval (after DESIGN_REVIEW, if issues found)
3. **Gate 3:** Final Delivery Approval (after FINAL_REVIEW)

### Parallel Execution
- **Design Phase:** @SA + @UIUX + @PO work simultaneously
- **Review Phase:** @QA + @SECA work simultaneously
- **Development Phase:** @DEV + @DEVOPS work simultaneously

## Key Principles

### 1. Single Source of Truth
- All documentation in `.agent/`
- IDE files are lightweight references
- Update once, reference everywhere

### 2. Strict Workflow Enforcement
- BRAIN enforces diagram flow
- No phase skipping allowed
- Approval gates are mandatory
- Artifact validation required

### 3. Compound Learning
- Every solution becomes knowledge
- Search-first workflow
- Auto-compounding triggers
- Metrics tracking

### 4. IDE Agnostic
- Core logic in `.agent/`
- Works with any IDE
- Portable and maintainable
- Easy to extend

## Usage Examples

### Example 1: Start New Project
```
User: @BRAIN - Build a todo app with React

🧠 BRAIN: Initializing workflow...
State: IDLE → PLANNING
Activating @PM...
```

### Example 2: Check Status
```
User: @BRAIN /status

📊 Workflow Status
Current State: DESIGNING
Progress: 3/12 (25%)
Next Gate: Design Approval
```

### Example 3: Small Task
```
User: @DEV /cycle - Fix login button on mobile

Executing cycle workflow:
1. Search KB for similar issues
2. Plan fix
3. Implement
4. Test
5. Compound knowledge
```

### Example 4: Full Automation
```
User: @ORCHESTRATOR --mode=full-auto
Build authentication system

Executing full SDLC workflow...
Will pause at approval gates.
```

## Benefits

✅ **Strict Enforcement** - No shortcuts or rule violations
✅ **Complete Traceability** - Full history of all transitions
✅ **Error Recovery** - Safe rollback mechanisms
✅ **Parallel Optimization** - Automatic parallel execution
✅ **Quality Gates** - Mandatory validation at each phase
✅ **Compound Learning** - Automatic knowledge capture
✅ **IDE Agnostic** - Works with any tool
✅ **Maintainable** - Single source of truth

## Integration Points

### With Kiro IDE
- Steering files auto-loaded
- Role activation via `@ROLE` mentions
- Workflow commands via `/command`
- MCP tools integration

### With Git
- Atomic commits per task
- Conventional commit format
- GitHub Issue references
- Branch management

### With MCP Tools
- GitHub MCP - Issue tracking
- Playwright - E2E testing
- Browser - UI verification
- Memory - Knowledge persistence

## Metrics & Monitoring

### Workflow Metrics
- Phase durations
- Approval gate status
- Iteration counts
- Efficiency scores

### Compound Metrics
- Total KB entries
- Time saved
- Reuse rate
- Coverage percentage

### Quality Metrics
- Bug counts by priority
- Test coverage
- Security issues
- Performance improvements

## Future Enhancements

1. **AI-Powered Predictions** - Predict phase durations
2. **Auto-Recovery** - Automatic error recovery
3. **Workflow Templates** - Pre-configured workflows
4. **Real-time Dashboard** - Visual progress tracking
5. **Integration APIs** - External tool integration
6. **Custom Rules** - User-defined validation

---

**Version:** 1.0.0
**Created:** 2026-01-02
**Status:** Active
**Philosophy:** Single source of truth, strict enforcement, compound learning

