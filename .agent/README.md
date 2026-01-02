# .agent Directory - Source of Truth

This directory contains the **source of truth** for all TeamLifecycle SDLC workflow documentation, roles, workflows, and knowledge base.

## Directory Structure

```
.agent/
├── README.md                    # This file
├── CONFIG.md                    # Configuration guide
├── USAGE.md                     # Usage instructions
├── roles/                       # Role definitions (source of truth)
│   ├── role-brain.md           # Master orchestrator
│   ├── role-pm.md              # Project Manager
│   ├── role-sa.md              # System Analyst
│   └── ...                     # Other roles
├── workflows/                   # Workflow implementations
│   ├── cycle.md                # Complete task lifecycle
│   ├── explore.md              # Deep investigation
│   ├── emergency.md            # Critical incident response
│   └── ...                     # Other workflows
├── knowledge-base/              # Compound learning system
│   ├── INDEX.md                # Searchable index
│   ├── bugs/                   # Bug patterns
│   ├── features/               # Feature implementations
│   ├── architecture/           # Architecture decisions
│   ├── security/               # Security fixes
│   └── ...                     # Other categories
├── templates/                   # Document templates
│   ├── project-plan.md
│   ├── architecture-spec.md
│   └── ...
├── rules/                       # Global rules
│   ├── global-rules.md
│   ├── critical-patterns.md
│   └── ...
└── ide-integration/             # IDE-specific integration
    └── kiro/                    # Kiro IDE integration
        └── steering/            # References to .agent files
```

**Note:** All executable scripts are in `tools/` directory. See `tools/README.md` for details.

## Integration with Kiro IDE

The `.kiro/steering/` directory contains **reference files** that point to the source documentation in `.agent/`:

```
.kiro/steering/role-brain.md  →  .agent/roles/role-brain.md
.kiro/steering/role-pm.md     →  .agent/roles/role-pm.md
...
```

This approach provides:
- **Single source of truth** - All documentation in `.agent/`
- **IDE integration** - Kiro steering files reference `.agent/`
- **Portability** - `.agent/` can work with any IDE
- **Maintainability** - Update once in `.agent/`, reference everywhere

## Why This Structure?

### 1. IDE Agnostic
The `.agent/` directory is not tied to any specific IDE. It can be used with:
- Kiro IDE (via `.kiro/steering/` references)
- Cursor IDE (via `.cursorrules` references)
- Any other AI-powered IDE
- Command-line tools
- CI/CD pipelines

### 2. Single Source of Truth
All documentation lives in `.agent/`. IDE-specific files are just lightweight references:

```markdown
---
source: .agent/roles/role-brain.md
---

# @BRAIN

**Source:** `.agent/roles/role-brain.md`

[Quick reference content here]

For complete documentation, see `.agent/roles/role-brain.md`
```

### 3. Easy Maintenance
Update documentation once in `.agent/`, and all IDE integrations automatically reference the latest version.

### 4. Version Control Friendly
- Core documentation in `.agent/` is always committed
- IDE-specific files in `.kiro/`, `.cursor/`, etc. can be gitignored if needed
- Team members can use different IDEs with same workflow

## File Organization

### Roles (`roles/`)
Complete role definitions with:
- Identity and responsibilities
- Commands and workflows
- Integration with other roles
- Examples and templates

### Workflows (`workflows/`)
Detailed workflow implementations:
- Step-by-step procedures
- Decision trees
- Error handling
- Success criteria

### Knowledge Base (`knowledge-base/`)
Compound learning system:
- Searchable index
- Categorized entries
- YAML frontmatter for metadata
- Cross-references

### Templates (`templates/`)
Document templates for:
- Project plans
- Design specifications
- Test reports
- Final deliverables

### Rules (`rules/`)
Global rules and patterns:
- SDLC flow rules
- Critical patterns (antibodies)
- Compound learning principles
- Best practices

## Executable Scripts

**All executable scripts are in `tools/` directory:**
- `tools/workflows/` - Workflow automation
- `tools/kb/` - Knowledge base management
- `tools/validation/` - Health checks
- `tools/utils/` - Shared utilities
- `tools/github/` - GitHub integration
- `tools/neo4j/` - Neo4j integration
- `tools/research/` - Research agent
- `tools/setup/` - Setup utilities

See `tools/README.md` for complete documentation.

## How to Use

### For Kiro IDE Users
1. Kiro automatically loads `.kiro/steering/` files
2. These files reference `.agent/` for full documentation
3. Use `@ROLE` mentions to activate roles
4. Use `/workflow` commands for enhanced workflows

### For Other IDE Users
1. Reference `.agent/` files directly in your IDE configuration
2. Use the same role and workflow structure
3. Adapt integration layer for your IDE

### For CLI/Automation
1. Parse `.agent/` files directly
2. Use YAML frontmatter for metadata
3. Follow workflow state machines
4. Integrate with CI/CD pipelines

## Adding New Content

### Adding a New Role
1. Create `.agent/roles/role-[name].md` with full documentation
2. Create `.kiro/steering/role-[name].md` as a reference file
3. Update `.agent/CONFIG.md` with role information
4. Add role to workflow diagrams

### Adding a New Workflow
1. Create `.agent/workflows/[workflow-name].md`
2. Document workflow steps and decision points
3. Add workflow to `.agent/USAGE.md`
4. Update workflow routing guide

### Adding Knowledge Base Entry
1. Create entry in appropriate `.agent/knowledge-base/` category
2. Use YAML frontmatter for metadata
3. Update `.agent/knowledge-base/INDEX.md`
4. Cross-reference related entries

## Benefits

✅ **Portable** - Works with any IDE or tool
✅ **Maintainable** - Single source of truth
✅ **Scalable** - Easy to add new roles/workflows
✅ **Searchable** - YAML frontmatter + index
✅ **Versionable** - Git-friendly structure
✅ **Composable** - Mix and match roles/workflows
✅ **Testable** - Clear success criteria
✅ **Documentable** - Self-documenting structure

## Philosophy

> "The `.agent/` directory is the brain. IDE integrations are just the interface."

By keeping the core logic in `.agent/` and using lightweight references in IDE-specific directories, we create a system that is:
- Easy to understand
- Easy to maintain
- Easy to extend
- Easy to port to new tools

## Learn More

- **Configuration:** `.agent/CONFIG.md`
- **Usage Guide:** `.agent/USAGE.md`
- **Workflows:** `.agent/workflows/README.md`
- **Knowledge Base:** `.agent/knowledge-base/README.md`
- **Kiro Integration:** `.kiro/steering/README.md`

---

**Version:** 1.0.0
**Created:** 2026-01-02
**Philosophy:** Single source of truth, IDE agnostic, compound learning

