# Setup Utilities

Utility scripts for setting up and configuring the Agentic SDLC system.

## Overview

This directory contains setup scripts that help configure the TeamLifecycle workflow, research agents, and other system components.

## Scripts

### `setup_research_hooks.sh`
**Purpose:** Setup Kiro IDE hooks for automatic research agent execution

**Platform:** Linux, macOS, Git Bash

**Features:**
- Creates research hooks in `.kiro/hooks/`
- Configures auto-research triggers
- Sets up hook permissions
- Validates hook configuration

**Usage:**
```bash
bash tools/setup/setup_research_hooks.sh
```

**What it does:**
1. Creates `.kiro/hooks/` directory
2. Generates hook configuration files:
   - `research-before-planning.json`
   - `research-before-development.json`
   - `research-before-bug-fix.json`
   - `research-on-demand.json`
3. Sets executable permissions
4. Validates configuration

**Hook Triggers:**
- **Before Planning** - When @PM is mentioned
- **Before Development** - When @DEV starts work
- **Before Bug Fix** - When @TESTER investigates bugs
- **On Demand** - When `/research` command is used

**Example Hook Configuration:**
```json
{
  "name": "research-before-planning",
  "trigger": "on_message",
  "condition": "message contains '@PM'",
  "action": {
    "type": "command",
    "command": "python tools/research/research_agent.py --task \"${message}\" --type general"
  }
}
```

### `standardize_filenames.ps1`
**Purpose:** Standardize filenames across the project

**Platform:** Windows PowerShell

**Features:**
- Converts filenames to consistent format
- Removes special characters
- Applies naming conventions
- Creates backup before changes

**Usage:**
```powershell
.\tools\setup\standardize_filenames.ps1
.\tools\setup\standardize_filenames.ps1 -Path "docs/sprints"
.\tools\setup\standardize_filenames.ps1 -DryRun
```

**Options:**
- `-Path` - Target directory (default: current)
- `-DryRun` - Preview changes without applying
- `-Backup` - Create backup before changes
- `-Recursive` - Process subdirectories

**Naming Conventions:**
- Lowercase with hyphens: `my-file-name.md`
- Remove special characters: `file@name!.md` → `file-name.md`
- Consistent date format: `YYYY-MM-DD`
- KB entries: `KB-YYYY-MM-DD-###-title.md`

**Example:**
```powershell
PS> .\tools\setup\standardize_filenames.ps1 -Path "docs" -DryRun

🔍 Scanning: docs/
📝 Would rename:
  • Project Plan V1.md → project-plan-v1.md
  • Design_Document.md → design-document.md
  • Test Report (Final).md → test-report-final.md

ℹ️  Run without -DryRun to apply changes
```

## Setup Workflows

### Initial Project Setup

```bash
# 1. Clone repository
git clone <repo-url>
cd agentic-sdlc

# 2. Install dependencies
npm install
pip install -r tools/requirements.txt

# 3. Setup research hooks (optional)
bash tools/setup/setup_research_hooks.sh

# 4. Configure environment
cp .env.template .env
# Edit .env with your credentials

# 5. Initialize knowledge base
node bin/agentic-sdlc/cli.js init-kb

# 6. Verify setup
./bin/kb/kb stats
```

### IDE Integration Setup

```bash
# Setup for specific IDE
node bin/agentic-sdlc/cli.js ide cursor
node bin/agentic-sdlc/cli.js ide copilot
node bin/agentic-sdlc/cli.js ide windsurf

# Setup for all IDEs
node bin/agentic-sdlc/cli.js ide all
```

### Research Agent Setup

```bash
# 1. Setup hooks
bash tools/setup/setup_research_hooks.sh

# 2. Test research agent
python tools/research/research_agent.py --task "test" --type general

# 3. Verify hooks
ls -la .kiro/hooks/

# 4. Test hook trigger
# In Kiro IDE, mention @PM and verify research runs
```

## Configuration Files

### Research Hooks
**Location:** `.kiro/hooks/`

**Files:**
- `research-before-planning.json`
- `research-before-development.json`
- `research-before-bug-fix.json`
- `research-on-demand.json`

### Environment Variables
**Location:** `.env`

**Required:**
```bash
# GitHub (optional)
GITHUB_TOKEN=your_token
GITHUB_REPO=username/repo

# Neo4j (optional)
NEO4J_URI=neo4j+s://instance.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password

# Research APIs (optional)
TAVILY_API_KEY=your_key
BRAVE_API_KEY=your_key
```

## Platform-Specific Notes

### Linux/macOS

**Make scripts executable:**
```bash
chmod +x tools/setup/setup_research_hooks.sh
```

**Run scripts:**
```bash
bash tools/setup/setup_research_hooks.sh
```

### Windows

**PowerShell execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Run scripts:**
```powershell
.\tools\setup\standardize_filenames.ps1
```

**Git Bash:**
```bash
bash tools/setup/setup_research_hooks.sh
```

## Troubleshooting

### Permission Denied (Linux/macOS)
```bash
chmod +x tools/setup/setup_research_hooks.sh
```

### PowerShell Script Won't Run
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Hooks Not Triggering
1. Check hook files exist: `ls .kiro/hooks/`
2. Verify hook configuration syntax
3. Check Kiro IDE hook settings
4. Review hook logs

### Research Agent Not Found
```bash
# Verify Python path
which python3

# Check script exists
ls tools/research/research_agent.py

# Test directly
python tools/research/research_agent.py --help
```

## Adding New Setup Scripts

### Script Template

**Bash:**
```bash
#!/bin/bash
# Script: setup_feature.sh
# Purpose: Setup feature X

set -e  # Exit on error

echo "🔧 Setting up Feature X..."

# Setup logic here

echo "✅ Setup complete!"
```

**PowerShell:**
```powershell
# Script: Setup-Feature.ps1
# Purpose: Setup feature X

[CmdletBinding()]
param(
    [switch]$DryRun
)

Write-Host "🔧 Setting up Feature X..." -ForegroundColor Cyan

# Setup logic here

Write-Host "✅ Setup complete!" -ForegroundColor Green
```

### Best Practices

1. **Idempotent** - Safe to run multiple times
2. **Dry-run mode** - Preview changes first
3. **Validation** - Check prerequisites
4. **Error handling** - Graceful failures
5. **Documentation** - Clear usage instructions
6. **Cross-platform** - Support Windows, Linux, macOS

## Integration with Other Tools

### Called by bin/ CLI
```javascript
// bin/agentic-sdlc/commands/install.js
import { execSync } from 'child_process';

export async function install() {
  // Run setup scripts
  execSync('bash tools/setup/setup_research_hooks.sh');
}
```

### Called by .agent/ Workflows
```markdown
## @PM Workflow

### Step 0: Setup
```bash
bash tools/setup/setup_research_hooks.sh
```
```

## Future Enhancements

- [ ] Automated dependency installation
- [ ] Configuration wizard
- [ ] Health check script
- [ ] Uninstall/cleanup script
- [ ] Migration scripts
- [ ] Docker setup
- [ ] CI/CD integration

## Related Documentation

- **Research Agent:** `../research/README.md`
- **CLI Guide:** `../../docs/CLI-GUIDE.md`
- **Workflow Guide:** `../../.agent/workflows/README.md`

---

**Version:** 1.0.0  
**Created:** 2026-01-02  
**Platform:** Windows, Linux, macOS
