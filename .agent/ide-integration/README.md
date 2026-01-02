# IDE Integration Guide

This folder contains integration documentation for TeamLifecycle SDLC workflow with BRAIN orchestrator.

## Supported IDEs

This project officially supports:
- **Kiro IDE** - Primary integration with automatic steering file loading
- **Antigravity** - Compound engineering plugin integration

## Architecture

TeamLifecycle uses a layered architecture:
- **`.agent/`** - Source of truth (roles, workflows, knowledge base)
- **`.kiro/steering/`** - Kiro IDE integration (lightweight references)
- **`.agent/ide-integration/`** - Integration documentation (this folder)

---

## 📁 Files

| File | Purpose | Description |
|------|---------|-------------|
| `README.md` | Overview | This file - integration overview |
| `KIRO-IDE.md` | Kiro IDE | Complete integration guide for Kiro IDE |
| `INTEGRATION-SUMMARY.md` | Summary | Integration architecture summary |

---

## 🚀 Kiro IDE Integration

### Built-in Support

Kiro IDE has **native integration** through `.kiro/steering/` files that are automatically loaded.

**No setup required!** Just start using:

```
@BRAIN - Build a todo app
@PM - Create project plan
@DEV /cycle - Fix login button
@ORCHESTRATOR --mode=full-auto
```

### How It Works

1. **Automatic Loading** - Kiro loads all `.kiro/steering/*.md` files
2. **Keyword Activation** - Mention `@ROLE` to activate that role
3. **Reference Pattern** - Steering files reference full docs in `.agent/`
4. **Source of Truth** - All documentation maintained in `.agent/`

### Documentation

See **`KIRO-IDE.md`** for complete integration guide including:
- Architecture details
- File structure
- Usage examples
- Available commands
- Workflow states
- Troubleshooting

---

## 🔄 Antigravity Integration

### Compound Engineering Plugin

Antigravity's compound engineering plugin integrates with the knowledge base system.

**Integration Points:**
- `.agent/knowledge-base/` - Shared knowledge repository
- YAML frontmatter - Searchable metadata
- Compound loop - Problem → Solution → Document → Reuse

### Knowledge Base Structure

```
.agent/knowledge-base/
├── INDEX.md                    # Searchable index
├── bugs/                       # Bug patterns by priority
│   ├── critical/
│   ├── high/
│   ├── medium/
│   └── low/
├── features/                   # Feature implementations
│   ├── authentication/
│   ├── performance/
│   └── integration/
├── architecture/               # Architecture decisions
├── security/                   # Security fixes
├── performance/                # Optimizations
└── platform-specific/          # Platform issues
```

### Compound Learning Workflow

**Before ANY complex work:**
1. Search `.agent/knowledge-base/INDEX.md`
2. Check related categories
3. Review similar patterns
4. Apply learned solutions
5. Document new insights

**Auto-Compounding Triggers:**
- Bug marked `#fixbug-critical` or `#fixbug-high`
- Security vulnerabilities found
- Performance improvement > 20%
- Architecture decisions documented
- Platform-specific issues resolved

---

## 🎯 Available Commands

### BRAIN Master Orchestrator
```
@BRAIN - Build a todo app
@BRAIN /status - Show workflow state
@BRAIN /validate - Validate phase completion
@BRAIN /auto-execute - Full automation mode
@BRAIN /rollback [STATE] - Rollback to previous state
```

### Core Roles
```
@PM - Project Manager (Planning & Scope)
@PO - Product Owner (Backlog & Prioritization)
@SA - System Analyst (Architecture & API Design)
@UIUX - UI/UX Designer (Interface Design)
@QA - Quality Assurance (Design Review)
@SECA - Security Analyst (Security Assessment)
@DEV - Developer (Implementation)
@DEVOPS - DevOps Engineer (Infrastructure & Deployment)
@TESTER - Tester (Testing & Bug Detection)
@REPORTER - Reporter (Documentation & Reporting)
@STAKEHOLDER - Stakeholder (Final Review)
@ORCHESTRATOR - Orchestrator (Workflow Automation)
```

### Enhanced Workflows
```
/cycle - Complete task lifecycle (< 4 hours)
/explore - Deep investigation for complex features
/compound - Capture knowledge after solving problems
/emergency - Critical incident response
/housekeeping - Cleanup and maintenance
/route - Intelligent workflow selection
```

---

## 💡 Usage Examples

### Using BRAIN Master Orchestrator
```
@BRAIN - Build a todo app with React

BRAIN will:
1. Initialize workflow state (IDLE → PLANNING)
2. Activate @PM for planning
3. Enforce approval gates
4. Manage all phase transitions
5. Validate artifacts at each step
6. Track complete state history
```

### Check Workflow Status
```
@BRAIN /status

Shows:
- Current state (e.g., DESIGNING)
- Completed phases
- In-progress work
- Next steps
- Approval gates
```

### Small Task with /cycle
```
@DEV /cycle - Fix login button on mobile

Executes:
1. Search KB for similar issues
2. Plan fix
3. Implement
4. Test locally
5. Commit with atomic message
6. Compound knowledge if non-obvious
```

### Complex Feature with /explore
```
@SA /explore - Real-time notification architecture

Executes:
1. Multi-order analysis
2. Research best practices
3. Evaluate trade-offs
4. Generate recommendations
5. Document findings
```

### Full Automation
```
@ORCHESTRATOR --mode=full-auto
Build authentication system with OAuth

Executes entire SDLC:
- Planning → Design → Development → Testing → Deployment
- Pauses only at approval gates
- Manages parallel execution
- Validates all transitions
```

---

## 🔄 Workflow States

BRAIN manages these workflow states:

```
IDLE → PLANNING → PLAN_APPROVAL → DESIGNING → DESIGN_REVIEW → 
DEVELOPMENT → TESTING → BUG_FIXING → DEPLOYMENT → REPORTING → 
FINAL_REVIEW → FINAL_APPROVAL → COMPLETE
```

### Approval Gates 🚪
1. **Project Plan** - After PLANNING (User approval required)
2. **Design** - After DESIGN_REVIEW (if critical issues found)
3. **Final Delivery** - After FINAL_REVIEW (User approval required)

### Parallel Execution ⚡
- **Design Phase:** @SA + @UIUX + @PO work simultaneously
- **Review Phase:** @QA + @SECA work simultaneously
- **Development Phase:** @DEV + @DEVOPS work simultaneously

---

## 📚 Documentation

### Integration Guides
- **Kiro IDE:** `KIRO-IDE.md` - Complete Kiro integration guide
- **Summary:** `INTEGRATION-SUMMARY.md` - Architecture summary

### System Documentation
- **Architecture:** `docs/ARCHITECTURE-OVERVIEW.md`
- **BRAIN Details:** `docs/BRAIN-ARCHITECTURE.md`
- **Diagrams:** `docs/SDLC-Diagram.md`
- **Setup Guide:** `docs/SETUP-COMPLETE.md`

### Source Files
- **Roles:** `.agent/roles/` - Full role documentation
- **Workflows:** `.agent/workflows/` - Workflow implementations
- **Knowledge Base:** `.agent/knowledge-base/` - Compound learning
- **Templates:** `.agent/templates/` - Document templates
- **Rules:** `.agent/rules/` - Global rules

### Kiro Integration
- **Steering Files:** `.kiro/steering/` - Kiro IDE references
- **README:** `.kiro/steering/README.md` - Steering guide

---

## 🐛 Troubleshooting

### Kiro IDE Issues

**Role Not Activating:**
- Check `.kiro/steering/role-[name].md` exists
- Check `.agent/roles/role-[name].md` exists
- Verify keywords in frontmatter
- Use exact keyword (e.g., `@PM`)

**Commands Not Working:**
- Check command syntax (e.g., `@BRAIN /status`)
- Ensure role is activated first
- Verify Kiro has project access

**Workflow Not Progressing:**
- Check BRAIN is managing workflow
- Verify approval gates are satisfied
- Ensure required artifacts exist
- Check for blocking bugs

### Knowledge Base Issues

**Search Not Finding Entries:**
- Check `.agent/knowledge-base/INDEX.md` is updated
- Verify YAML frontmatter is correct
- Check category structure
- Ensure tags are properly formatted

**Compound Not Triggering:**
- Check bug priority tags (`#fixbug-critical`, `#fixbug-high`)
- Verify solution was non-obvious (3+ attempts)
- Check auto-compound triggers
- Manually use `/compound` if needed

---

## 🤝 Philosophy

> "Each unit of engineering work should make subsequent units of work easier—not harder."

This system transforms AI agents from session-to-session amnesiacs into learning partners that compound their capabilities over time.

### Key Principles

1. **Single Source of Truth** - All documentation in `.agent/`
2. **Strict Enforcement** - BRAIN enforces workflow rules
3. **Compound Learning** - Every solution becomes knowledge
4. **IDE Agnostic** - Core logic not tied to specific IDE
5. **Maintainable** - Clear separation of concerns

---

## 📊 Metrics

### Workflow Metrics
- Phase durations
- Approval gate status
- Iteration counts
- Efficiency scores

### Compound Metrics
- Total KB entries
- Time saved by reusing solutions
- Pattern reuse rate
- Knowledge coverage percentage

### Quality Metrics
- Bug counts by priority
- Test coverage
- Security issues
- Performance improvements

---

**Version:** 1.0.0  
**Created:** 2026-01-02  
**Status:** Production Ready ✅  
**Supported IDEs:** Kiro IDE, Antigravity

#ide-integration #kiro-ide #antigravity #teamlifecycle
