# Bin & Tools Reorganization Plan

## ⚠️ IMPORTANT: Python/Shell Only - No JavaScript

**Technology Stack:**
- ✅ Python 3.7+ (primary language)
- ✅ Shell scripts (.sh for Linux/macOS)
- ✅ PowerShell scripts (.ps1 for Windows)
- ❌ NO JavaScript/Node.js

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│              PROJECT STRUCTURE (Python/Shell)                │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   ┌─────────┐          ┌─────────┐          ┌─────────┐
   │   bin/  │          │ tools/  │          │ .agent/ │
   │   CLI   │◄─────────│ Support │─────────►│Workflows│
   │ Python  │          │ Scripts │          │   KB    │
   └─────────┘          └─────────┘          └─────────┘
```

### Separation of Concerns

1. **`bin/`** = **CLI Tools Only (Python)**
   - Python KB CLI (kb)
   - Shell/PowerShell entry points
   - User-facing command-line interfaces
   - Cross-platform support

2. **`tools/`** = **Support Scripts (Python/Shell)**
   - Support both `bin/` CLI and `.agent/` workflows
   - GitHub integration (Python)
   - Neo4j brain integration (Python)
   - Research agent system (Python)
   - Setup utilities (Shell/PowerShell)
   - Backend automation scripts

3. **`.agent/`** = **TeamLifecycle System**
   - Workflow scripts (Python)
   - Role templates (Markdown)
   - Knowledge base entries (Markdown)
   - Templates and rules

## Current State Analysis

### `bin/` Directory
**Purpose:** Command-line interfaces ONLY (Python)
**Current Structure:**
```
bin/
├── commands/          # ❌ Node.js CLI commands (TO BE REMOVED)
├── lib/              # ✅ Python KB library modules
├── utils/            # ❌ Node.js utilities (TO BE REMOVED)
├── cli.js            # ❌ Node.js main CLI (TO BE REMOVED)
├── kb                # ✅ Bash entry point for KB CLI
├── kb.bat            # ✅ Windows entry point for KB CLI
├── kb_cli.py         # ✅ Python KB CLI main
└── kb.ps1            # ⚠️  Legacy PowerShell KB CLI
```

**Issues:**
- ❌ Contains Node.js files (cli.js, commands/, utils/)
- ❌ Node.js should be completely removed
- ✅ Python KB CLI is good
- ⚠️  Legacy PowerShell scripts still present

### `tools/` Directory
**Purpose:** Support scripts for bin/ CLI and .agent/ workflows (Python/Shell)
**Current Structure:**
```
tools/
├── github/           # ✅ Python - GitHub sync scripts
├── neo4j/            # ✅ Python - Neo4j integration scripts
├── research/         # ✅ Python - Research agent system
└── setup/            # ✅ Shell/PowerShell - Setup scripts
```

**Status:**
- ✅ All Python/Shell - correct!
- ✅ Well-organized by function
- ✅ Correctly supports both bin/ and .agent/

### `.agent/scripts/` Directory
**Purpose:** Workflow automation scripts (Python)
**Current Structure:**
```
.agent/scripts/
├── kb/               # ✅ Python - KB management
├── utils/            # ✅ Python - Common utilities
├── validation/       # ✅ Python - Health checks
├── workflows/        # ✅ Python - Workflow scripts
├── run.py           # ✅ Python - Main runner
├── run.sh           # ✅ Shell - Linux/macOS entry
└── run.bat          # ✅ Batch - Windows entry
```

**Status:**
- ✅ All Python - perfect!
- ✅ Cross-platform entry points

## Reorganization Strategy

### Recommended Structure (Python/Shell Only)

```
bin/                           # CLI TOOLS (Python only)
├── kb/                        # Python KB CLI
│   ├── lib/                  # KB library modules
│   │   ├── __init__.py
│   │   ├── kb_common.py
│   │   ├── kb_search.py
│   │   ├── kb_add.py
│   │   ├── kb_index.py
│   │   ├── kb_stats.py
│   │   ├── kb_list.py
│   │   └── kb_compound.py
│   ├── kb                    # Bash entry
│   ├── kb.bat                # Windows batch entry
│   ├── kb_cli.py            # Main CLI
│   └── README.md
│
└── README.md                 # Overview

tools/                        # SUPPORT SCRIPTS (Python/Shell)
├── github/                   # GitHub integration (Python)
│   ├── sync_github.py
│   ├── requirements.txt
│   └── README.md
│
├── neo4j/                    # Neo4j brain integration (Python)
│   ├── sync_skills_to_neo4j.py
│   ├── query_skills_neo4j.py
│   ├── graph_brain.py
│   ├── requirements.txt
│   └── README.md
│
├── research/                 # Research agent system (Python)
│   ├── research_agent.py
│   ├── research_mcp.py
│   ├── research_mcp_extended.py
│   └── README.md
│
├── setup/                    # Setup utilities (Shell/PowerShell)
│   ├── setup_research_hooks.sh
│   ├── standardize_filenames.ps1
│   └── README.md
│
└── requirements.txt          # Master requirements

.agent/                       # TEAMLIFECYCLE SYSTEM
├── scripts/                  # Workflow scripts (Python)
│   ├── kb/                  # KB management
│   ├── utils/               # Common utilities
│   ├── validation/          # Health checks
│   ├── workflows/           # Workflow automation
│   ├── run.py              # Main runner
│   ├── run.sh              # Shell entry
│   └── run.bat             # Batch entry
│
├── workflows/                # Workflow definitions (Markdown)
├── roles/                    # Role templates (Markdown)
├── knowledge-base/           # KB entries (Markdown)
├── templates/                # Document templates
└── rules/                    # Global rules
```

### Key Principles

1. **bin/** = Python CLI tools only
   - Direct user interaction
   - Command-line interfaces
   - Python + Shell/Batch entry points

2. **tools/** = Python/Shell support scripts
   - Called by bin/ CLI
   - Called by .agent/ workflows
   - Automation and integration
   - No direct user interaction

3. **NO JavaScript/Node.js**
   - Remove all .js files
   - Remove node_modules/
   - Remove package.json (or keep minimal for npm scripts only)
   - Use Python for all logic

## Recommended Changes

### Phase 1: Remove Node.js / Keep Python Only

**Goal:** Remove all JavaScript/Node.js files

**Actions:**
1. **Remove Node.js files:**
   ```bash
   # Remove Node.js CLI
   rm -rf bin/commands/
   rm -rf bin/utils/
   rm bin/cli.js
   
   # Remove Node.js dependencies
   rm -rf node_modules/
   rm package-lock.json
   ```

2. **Update package.json (optional - keep for npm scripts only):**
   ```json
   {
     "name": "agentic-sdlc",
     "version": "1.0.1",
     "description": "Simulating SDLC with AI Agents (Python)",
     "scripts": {
       "workflow:cycle": "python .agent/scripts/workflows/cycle.py",
       "workflow:housekeeping": "python .agent/scripts/workflows/housekeeping.py",
       "kb:search": "./bin/kb search",
       "kb:stats": "./bin/kb stats",
       "health": "python .agent/scripts/validation/health-check.py",
       "agent": "python .agent/scripts/run.py"
     }
   }
   ```

3. **Or remove package.json entirely:**
   ```bash
   rm package.json
   ```

### Phase 2: Organize bin/ (Python CLI Only)

**Goal:** Clean Python-only CLI structure

**Current:**
```
bin/
├── cli.js, commands/, utils/     # ❌ Node.js (remove)
├── kb_cli.py, lib/, kb, kb.bat  # ✅ Python (keep)
└── kb.ps1                        # ⚠️  Legacy (archive)
```

**Target:**
```
bin/
├── kb/                           # Python KB CLI (grouped)
│   ├── lib/
│   ├── kb, kb.bat
│   ├── kb_cli.py
│   └── README.md
└── README.md                     # Overview
```

**Actions:**
1. Create `bin/kb/` subdirectory
2. Move Python files: `kb_cli.py`, `lib/`, `kb`, `kb.bat`
3. Archive legacy: `kb.ps1` → `bin/legacy/` or delete
4. Update entry scripts paths
5. Add README files

### Phase 3: Enhance tools/ (Python/Shell Support)

**Goal:** Better documentation and organization

**Current:**
```
tools/
├── github/      # ✅ Python - has README
├── neo4j/       # ✅ Python - has README
├── research/    # ✅ Python - has README
└── setup/       # ✅ Shell/PS - has README
```

**Target:**
```
tools/
├── github/
│   ├── sync_github.py
│   ├── requirements.txt
│   └── README.md              ✓ Exists
├── neo4j/
│   ├── *.py
│   ├── requirements.txt
│   └── README.md              ✓ Exists
├── research/
│   ├── *.py
│   └── README.md              ✓ Exists
├── setup/
│   ├── *.sh, *.ps1
│   └── README.md              ✓ Exists
├── requirements.txt           ✓ Exists (master)
└── README.md                  ✓ Exists
```

**Actions:**
1. ✅ All README files already created
2. ✅ Master requirements.txt already created
3. Verify all scripts are Python/Shell only

### Phase 4: Documentation

**Goal:** Update documentation to reflect Python-only architecture

**New Documentation:**
1. Update `README.md` - Remove Node.js references
2. Update `docs/` - Python/Shell only
3. Create `docs/PYTHON-ARCHITECTURE.md` - Python architecture guide
4. Update all examples to use Python/Shell

**Content:**
- Remove all Node.js/npm references
- Update installation instructions (pip only)
- Update usage examples (Python/Shell only)
- Add Python best practices

## Implementation Plan

### Step 1: Backup Current State
```bash
git add -A
git commit -m "backup: before removing Node.js and reorganizing"
```

### Step 2: Remove Node.js Files

**2.1 Remove Node.js CLI:**
```bash
# Remove Node.js files
rm -rf bin/commands/
rm -rf bin/utils/
rm bin/cli.js

# Remove Node.js dependencies
rm -rf node_modules/
rm package-lock.json
```

**2.2 Update or remove package.json:**

**Option A: Keep minimal package.json for npm scripts:**
```json
{
  "name": "agentic-sdlc",
  "version": "1.0.1",
  "description": "SDLC with AI Agents (Python)",
  "scripts": {
    "workflow:cycle": "python .agent/scripts/workflows/cycle.py",
    "workflow:housekeeping": "python .agent/scripts/workflows/housekeeping.py",
    "kb:search": "./bin/kb search",
    "kb:stats": "./bin/kb stats",
    "health": "python .agent/scripts/validation/health-check.py"
  },
  "keywords": ["sdlc", "ai", "agent", "python"],
  "author": "truongnat",
  "license": "MIT"
}
```

**Option B: Remove package.json entirely:**
```bash
rm package.json
```

### Step 3: Reorganize bin/ (Python CLI Only)

**3.1 Create subdirectories:**
```bash
mkdir -p bin/kb
mkdir -p bin/legacy
```

**3.2 Move Python KB CLI files:**
```bash
# Move to bin/kb/
mv bin/kb_cli.py bin/kb/
mv bin/lib bin/kb/
mv bin/kb bin/kb/
mv bin/kb.bat bin/kb/
mv bin/CROSS-PLATFORM-CLI.md bin/kb/
```

**3.3 Archive legacy files:**
```bash
mv bin/kb.ps1 bin/legacy/
# Or delete: rm bin/kb.ps1
```

**3.4 Update entry scripts:**

**bin/kb/kb (Bash):**
```bash
#!/bin/bash
# KB CLI entry point for Linux/macOS

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/kb_cli.py" "$@"
```

**bin/kb/kb.bat (Windows):**
```batch
@echo off
REM KB CLI entry point for Windows

set SCRIPT_DIR=%~dp0
python "%SCRIPT_DIR%kb_cli.py" %*
```

**3.5 Make executable:**
```bash
chmod +x bin/kb/kb
```

### Step 4: Update Documentation

**4.1 Update bin/README.md:**
```markdown
# bin/ - CLI Tools (Python Only)

Python-based command-line tools.

## KB CLI
Knowledge Base management CLI

Usage:
  ./bin/kb/kb help
  ./bin/kb/kb search "term"
  ./bin/kb/kb compound search "term"
```

**4.2 Update main README.md:**
- Remove Node.js installation instructions
- Remove npm references
- Update to Python/pip only
- Update usage examples

**4.3 Update all documentation:**
- Remove JavaScript/Node.js references
- Update installation: `pip install -r tools/requirements.txt`
- Update examples to use Python/Shell

### Step 5: Test Everything

**5.1 Test Python KB CLI:**
```bash
# Linux/macOS
./bin/kb/kb help
./bin/kb/kb search test
./bin/kb/kb stats

# Windows
bin\kb\kb.bat help
bin\kb\kb.bat search test
```

**5.2 Test tools scripts:**
```bash
python tools/neo4j/test_neo4j_connection.py
python tools/research/research_agent.py --task "test"
python .agent/scripts/validation/health-check.py
```

**5.3 Test workflows:**
```bash
python .agent/scripts/workflows/cycle.py
python .agent/scripts/workflows/housekeeping.py
```

**5.4 Verify no Node.js dependencies:**
```bash
# Should not find any .js files in bin/
find bin/ -name "*.js"

# Should not find node_modules
ls node_modules  # Should not exist
```

## Benefits

### Clarity
- ✅ Clear separation of concerns
- ✅ Easy to understand structure
- ✅ Better onboarding for new users

### Maintainability
- ✅ Easier to update individual components
- ✅ Clear ownership of files
- ✅ Better testing isolation

### Usability
- ✅ Clear documentation
- ✅ Consistent naming
- ✅ Platform-specific guidance

## Migration Guide

### For Users

**Old:**
```bash
node bin/cli.js install
./bin/kb search "term"
```

**New:**
```bash
node bin/agentic-cli.js install
# OR if installed globally:
agentic-sdlc install

./bin/kb search "term"
# (unchanged)
```

### For Developers

**Old structure:**
```
bin/cli.js              # Main CLI
bin/commands/help.js    # Command
```

**New structure:**
```
bin/agentic-cli.js      # Main CLI (renamed)
bin/commands/help.js    # Command (unchanged)
```

## Timeline

- **Phase 1:** 1-2 hours (immediate improvements)
- **Phase 2:** 2-3 hours (tools enhancement)
- **Phase 3:** 2-3 hours (documentation)
- **Total:** 5-8 hours

## Success Criteria

- [ ] Clear separation between Node.js and Python CLIs
- [ ] All directories have README files
- [ ] Legacy files archived or removed
- [ ] Documentation updated
- [ ] All tests passing
- [ ] No breaking changes for users

---

**Status:** Draft  
**Created:** 2026-01-02  
**Priority:** Medium  
**Effort:** 5-8 hours
