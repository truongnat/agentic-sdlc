# TeamLifecycle Steering Files for Kiro IDE

This directory contains **lightweight reference files** that point to the source documentation in `.agent/`.

## Architecture

```
.agent/                          # SOURCE OF TRUTH
├── roles/                       # Full role documentation
├── workflows/                   # Workflow implementations
└── knowledge-base/              # Compound learning system

.kiro/steering/                  # REFERENCES ONLY
├── role-*.md                    # Lightweight role references
├── workflow-*.md                # Workflow guides
└── *.md                         # Core rules and patterns
```

## What are Steering Files?

Steering files provide context and instructions to Kiro IDE. They can be:
- **Always included** - Loaded automatically in every conversation
- **Manually included** - Activated when user mentions specific keywords
- **File-matched** - Loaded when working with specific file types

**Note:** Role files in this directory are lightweight references. Full documentation is in `.agent/roles/`.

## Available Steering Files

### Core Workflow (Always Loaded)
- `00-teamlifecycle-overview.md` - Overview of all roles and workflow
- `global-rules.md` - Core rules for all roles
- `critical-patterns.md` - Antibodies against recurring mistakes
- `compound-learning.md` - Self-improving knowledge system
- `workflow-enhancements.md` - Enhanced workflow commands
- `workflow-routing.md` - Workflow selection guide

### Role-Specific (Manual Activation)
Activate by mentioning the role in your message. These are lightweight references to `.agent/roles/`:

- `role-brain.md` - Master Orchestrator (@BRAIN) → `.agent/roles/role-brain.md`
- `role-pm.md` - Project Manager (@PM) → `.agent/roles/role-pm.md`
- `role-po.md` - Product Owner (@PO) → `.agent/roles/role-po.md`
- `role-sa.md` - System Analyst (@SA) → `.agent/roles/role-sa.md`
- `role-uiux.md` - UI/UX Designer (@UIUX) → `.agent/roles/role-uiux.md`
- `role-qa.md` - Quality Assurance (@QA) → `.agent/roles/role-qa.md`
- `role-seca.md` - Security Analyst (@SECA) → `.agent/roles/role-seca.md`
- `role-dev.md` - Developer (@DEV) → `.agent/roles/role-dev.md`
- `role-devops.md` - DevOps Engineer (@DEVOPS) → `.agent/roles/role-devops.md`
- `role-tester.md` - Tester (@TESTER) → `.agent/roles/role-tester.md`
- `role-reporter.md` - Reporter (@REPORTER) → `.agent/roles/role-reporter.md`
- `role-stakeholder.md` - Stakeholder (@STAKEHOLDER) → `.agent/roles/role-stakeholder.md`
- `role-orchestrator.md` - Orchestrator (@ORCHESTRATOR) → `.agent/roles/role-orchestrator.md`

### Supporting Files (Manual Activation)
- `git-workflow.md` - Git commit rules and conventions
- `knowledge-base.md` - Knowledge base management guidelines
- `documentation-updates.md` - Documentation update procedures

## How to Use

### 1. Activate a Role
Simply mention the role in your message:
```
@PM - Please create a project plan for a todo app
```

### 2. Use Enhanced Workflows
Use slash commands for compound engineering workflows:
```
@DEV /cycle - Add user profile avatar upload
@SA /explore - Real-time notification system architecture
@DEV /compound - Document the React hydration fix
@DEV /emergency - P0: Payment gateway down
@ORCHESTRATOR /housekeeping
```

### 3. Auto-Execute Workflow
Use the orchestrator for automated execution:
```
@ORCHESTRATOR --mode=full-auto
Build a todo app with React and Node.js
```

### 4. Route Unclear Tasks
Let the system choose the best workflow:
```
@ORCHESTRATOR /route - Need to add payment processing
```

## Workflow Phases

### Standard SDLC Flow
1. **Planning** (@PM) → User Approval
2. **Design** (@SA + @UIUX + @PO in parallel)
3. **Design Review** (@QA + @SECA in parallel)
4. **Development** (@DEV + @DEVOPS in parallel)
5. **Testing** (@TESTER)
6. **Reporting** (@REPORTER)
7. **Final Review** (@STAKEHOLDER) → User Approval

### Enhanced Workflows
- **`/cycle`** - Complete task lifecycle (< 4 hours)
- **`/explore`** - Deep investigation for complex features
- **`/compound`** - Capture knowledge after solving problems
- **`/emergency`** - Critical incident response
- **`/housekeeping`** - Regular maintenance and cleanup
- **`/route`** - Intelligent workflow selection

## Artifact Structure

All deliverables are organized in:
```
docs/sprints/sprint-[N]/
├── plans/          # Project plans, backlogs
├── designs/        # Architecture, UI/UX specs
├── reviews/        # QA and security reports
├── logs/           # Dev, DevOps, orchestration logs
├── tests/          # Test reports
└── reports/        # Final reports
```

## Knowledge Base Integration

The compound learning system stores all solved problems:
```
.agent/knowledge-base/
├── INDEX.md                 # Searchable index
├── bugs/                    # Bug patterns by priority
├── features/                # Feature implementations
├── architecture/            # Architecture decisions
├── security/                # Security fixes
├── performance/             # Optimizations
└── platform-specific/       # Platform issues
```

### Search-First Workflow
**Before starting ANY complex work:**
1. Search `.agent/knowledge-base/INDEX.md`
2. Check related categories
3. Review similar patterns
4. Apply learned solutions
5. Document new insights

## Compound Learning Loop

```
Problem → Solution → Document → Search → Reuse → Compound
```

Every bug fixed, pattern discovered, and solution documented becomes permanent knowledge that compounds over time.

## Critical Patterns (Antibodies)

### Anti-Patterns to Avoid
1. ❌ **Big Bang Integration** - Commit immediately per task
2. ❌ **Approval Bypass** - Never skip design/security reviews
3. ❌ **Scope Creep** - Only implement approved features
4. ❌ **Knowledge Amnesia** - Search KB before implementing
5. ❌ **Silent Failures** - Test after each implementation
6. ❌ **Documentation Debt** - Update docs in same commit
7. ❌ **Security Afterthought** - SECA review before development
8. ❌ **Deployment Surprise** - Full staging verification required

### Positive Patterns to Follow
1. ✅ **Compound Learning** - Every solution becomes knowledge
2. ✅ **Parallel Execution** - Independent roles work simultaneously
3. ✅ **Evidence-Based Progress** - All claims backed by artifacts
4. ✅ **Atomic Tasks** - Small, verifiable units of work
5. ✅ **Fail-Fast Validation** - Early detection of issues
6. ✅ **Automated Handoffs** - Roles auto-notify next steps
7. ✅ **Health Monitoring** - Continuous system health checks
8. ✅ **Modular Skills** - Pluggable capabilities

## MCP Integration

The workflow leverages MCP tools configured in `.kiro/settings/mcp.json`:
- **GitHub MCP** - Issue tracking, milestones, labels
- **Playwright/Browser** - E2E testing, UI verification
- **Sequential Thinking** - Complex logic planning
- **Next.js DevTools** - Next.js development and debugging
- **Shadcn** - Component library integration
- **Fetch** - Web content retrieval

## Quick Start Examples

### Example 1: Small Task
```
@DEV /cycle - Fix login button not working on mobile
```
**Flow:** Search KB → Plan → Implement → Test → Compound

### Example 2: Complex Feature
```
@SA /explore - Real-time notification system with WebSocket
```
**Flow:** Multi-order analysis → Research → Recommendations

### Example 3: Production Emergency
```
@DEV /emergency - P0: Database connection pool exhausted
```
**Flow:** Assess → Mitigate → Hotfix → Deploy → Postmortem → Compound

### Example 4: Large Project
```
@PM - Build a complete authentication system with OAuth
Platform: Web (Next.js)
--mode=full-auto
```
**Flow:** Plan → Design → Develop → Test → Report → Approve

### Example 5: Maintenance
```
@ORCHESTRATOR /housekeeping - End of sprint-3 cleanup
```
**Flow:** Archive → Fix drift → Update index → Verify

## Workflow Selection Guide

Use the decision tree:
```
Production emergency?     → /emergency
Small task (< 4h)?       → /cycle
Complex investigation?   → /explore
Large project?           → /specs (via @PM)
Maintenance?             → /housekeeping
Document solution?       → /compound
Unsure?                  → /route
```

## Metrics and Health Monitoring

Track compound system effectiveness:
```
📊 Compound System Health
- Total KB Entries: [N]
- Entries This Week: [N]
- Time Saved: [N hours]
- Reuse Rate: [N%]
- Coverage: [N%]
```

## Customization

To customize the workflow:
1. Edit steering files in this directory
2. Kiro will automatically reload changes
3. Use front-matter to control inclusion behavior
4. Add new workflows in `.agent/workflows/`

## Integration with .agent Directory

The `.kiro/steering/` files work together with `.agent/`:
- **`.kiro/steering/`** - Kiro IDE integration layer
- **`.agent/workflows/`** - Detailed workflow implementations
- **`.agent/knowledge-base/`** - Shared knowledge repository
- **`.agent/templates/`** - Document templates
- **`.agent/rules/`** - Global rules

## Learn More

- **Detailed Configuration:** `.agent/CONFIG.md`
- **Usage Guide:** `.agent/USAGE.md`
- **Workflow Details:** `.agent/workflows/[workflow].md`
- **KB Guide:** `.agent/knowledge-base/README.md`
- **Original Workflows:** `.agent/workflows/README.md`

## Philosophy

> "Each unit of engineering work should make subsequent units of work easier—not harder."

This system transforms AI agents from session-to-session amnesiacs into learning partners that compound their capabilities over time. Every bug fixed, pattern discovered, and solution documented becomes permanent knowledge that makes future work faster and better.

## Credits

Inspired by:
- **Antigravity Compound Engineering Plugin** - Compound learning principles
- **TeamLifecycle Methodology** - SDLC simulation framework
- **Every Inc.** - Original compound engineering concept

#teamlifecycle #compound-engineering #kiro-ide
