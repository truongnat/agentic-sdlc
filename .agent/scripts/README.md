# Agent Scripts

Automation scripts to support TeamLifecycle workflows.

## Directory Structure

```
scripts/
├── workflows/          # Workflow automation scripts
├── kb/                 # Knowledge base management
├── validation/         # Validation and health checks
└── utils/              # Utility scripts
```

## Available Scripts

### Workflow Scripts
- `workflows/cycle.sh` - Execute complete task lifecycle
- `workflows/explore.sh` - Run deep investigation workflow
- `workflows/emergency.sh` - Handle critical incidents
- `workflows/housekeeping.sh` - Maintenance and cleanup
- `workflows/route.sh` - Intelligent workflow routing

### Knowledge Base Scripts
- `kb/index-update.sh` - Update KB index
- `kb/search.sh` - Search knowledge base
- `kb/validate.sh` - Validate KB entries
- `kb/stats.sh` - Generate KB statistics

### Validation Scripts
- `validation/check-artifacts.sh` - Verify artifact placement
- `validation/check-yaml.sh` - Validate YAML frontmatter
- `validation/check-drift.sh` - Detect documentation drift
- `validation/health-check.sh` - System health monitoring

### Utility Scripts
- `utils/create-sprint.sh` - Initialize new sprint structure
- `utils/archive-sprint.sh` - Archive completed sprint
- `utils/generate-report.sh` - Generate workflow reports

## Usage

### From Command Line
```bash
# Run workflow
.agent/scripts/workflows/cycle.sh "Add user avatar upload"

# Update KB index
.agent/scripts/kb/index-update.sh

# Health check
.agent/scripts/validation/health-check.sh
```

### From npm
```bash
# Run workflow
npm run workflow:cycle -- "Add user avatar upload"

# Update KB
npm run kb:update

# Health check
npm run health
```

## Integration with Workflows

These scripts are called automatically by workflow commands:
- `/cycle` → `workflows/cycle.sh`
- `/explore` → `workflows/explore.sh`
- `/emergency` → `workflows/emergency.sh`
- `/housekeeping` → `workflows/housekeeping.sh`
- `/compound` → `kb/compound.sh`

## Platform Support

All scripts are written in **Python 3.8+** for true cross-platform compatibility:
- ✅ Windows (CMD/PowerShell)
- ✅ macOS (Terminal)
- ✅ Linux (Bash/Zsh)

No shell-specific syntax - pure Python for consistency.
