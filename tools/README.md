# Tools - Support Scripts

Support scripts for both `bin/` CLI and `.agent/` workflows.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    TOOLS LAYER                               │
│         Support Scripts for CLI and Workflows                │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   ┌─────────┐          ┌─────────┐          ┌─────────┐
   │  bin/   │          │ tools/  │          │ .agent/ │
   │   CLI   │◄─────────│ Scripts │─────────►│Workflows│
   └─────────┘          └─────────┘          └─────────┘
```

## Purpose

The `tools/` directory contains backend support scripts that:
- ✅ Support `bin/` CLI commands
- ✅ Support `.agent/` workflow automation
- ✅ Provide integration with external services
- ✅ Enable automation and orchestration

**Key Principle:** Tools are called by CLI or workflows, not directly by users.

## Directory Structure

```
tools/
├── workflows/                # Workflow automation (from .agent/scripts/)
│   ├── cycle.py             # Complete task lifecycle
│   ├── housekeeping.py      # Maintenance and cleanup
│   └── emergency.py         # Critical incident response
│
├── kb/                       # Knowledge base management (from .agent/scripts/)
│   ├── search.py            # Search knowledge base
│   ├── update-index.py      # Update KB index
│   └── stats.py             # Generate KB statistics
│
├── validation/               # Health checks (from .agent/scripts/)
│   └── health-check.py      # System health monitoring
│
├── utils/                    # Shared utilities (from .agent/scripts/)
│   ├── common.py            # Common utilities
│   ├── artifact_manager.py  # Artifact management
│   └── kb_manager.py        # KB management utilities
│
├── github/                   # GitHub integration
│   ├── sync_github.py       # Sync artifacts to GitHub
│   └── README.md
│
├── neo4j/                    # Neo4j brain integration
│   ├── sync_skills_to_neo4j.py
│   ├── query_skills_neo4j.py
│   ├── graph_brain.py
│   ├── test_neo4j_connection.py
│   ├── verify_neo4j.py
│   ├── requirements.txt
│   └── README.md
│
├── research/                 # Research agent system
│   ├── research_agent.py
│   ├── research_mcp.py
│   ├── research_mcp_extended.py
│   └── README.md
│
├── setup/                    # Setup utilities
│   ├── setup_research_hooks.sh
│   ├── standardize_filenames.ps1
│   └── README.md
│
├── run.sh                    # Cross-platform runner (Unix)
├── run.py                    # Cross-platform runner (Python)
├── run.bat                   # Cross-platform runner (Windows)
├── requirements.txt          # Master requirements
└── README.md                 # This file
```

## Tools Overview

### 1. Workflow Automation (`workflows/`)
**Purpose:** Execute TeamLifecycle workflow commands

**Features:**
- Complete task lifecycle (`/cycle`)
- Maintenance and cleanup (`/housekeeping`)
- Critical incident response (`/emergency`)
- Workflow orchestration

**Called by:**
- Kiro IDE: `/cycle`, `/housekeeping`, `/emergency` commands
- `.agent/` workflows: All workflow commands
- `bin/` CLI: Workflow execution

**Usage:**
```bash
python tools/workflows/cycle.py --task "Add user avatar"
python tools/workflows/housekeeping.py --sprint 3
```

---

### 2. Knowledge Base Management (`kb/`)
**Purpose:** Manage compound learning system

**Features:**
- Search knowledge base
- Update searchable index
- Generate statistics
- Validate entries

**Called by:**
- Kiro IDE: `/compound` command
- `.agent/` workflows: All roles (knowledge search)
- `bin/` CLI: `kb` commands

**Usage:**
```bash
python tools/kb/search.py --query "authentication"
python tools/kb/update-index.py
python tools/kb/stats.py
```

---

### 3. Validation & Health Checks (`validation/`)
**Purpose:** System health monitoring

**Features:**
- Verify artifact placement
- Check documentation drift
- Validate YAML frontmatter
- Monitor system health

**Called by:**
- Kiro IDE: `/housekeeping` command
- `.agent/` workflows: Automated health checks
- `bin/` CLI: Health monitoring

**Usage:**
```bash
python tools/validation/health-check.py
```

---

### 4. Shared Utilities (`utils/`)
**Purpose:** Common utilities for all tools

**Features:**
- Artifact management
- KB management helpers
- Common functions
- Cross-tool utilities

**Called by:**
- All other tools
- Workflows
- CLI commands

**Usage:**
```python
from tools.utils.common import load_config
from tools.utils.kb_manager import search_kb
from tools.utils.artifact_manager import create_artifact
```

---

### 5. GitHub Integration (`github/`)
**Purpose:** Sync TeamLifecycle artifacts with GitHub

**Features:**
- Create issues from sprint tasks
- Manage milestones
- Apply labels
- Track progress

**Called by:**
- `bin/` CLI: `agentic-sdlc sync-github`
- `.agent/` workflows: PM, REPORTER

**Usage:**
```bash
python tools/github/sync_github.py --sprint 3
```

**Documentation:** [github/README.md](github/README.md)

---

### 2. Neo4j Integration (`neo4j/`)
**Purpose:** Knowledge graph and brain integration

**Features:**
- Sync KB entries to Neo4j
- Query knowledge graph
- Map relationships
- Track skills and technologies

**Called by:**
- `bin/` CLI: `kb compound` commands
- `.agent/` workflows: All roles (knowledge search)

**Usage:**
```bash
python tools/neo4j/sync_skills_to_neo4j.py
python tools/neo4j/query_skills_neo4j.py --all-skills
```

**Documentation:** [neo4j/README.md](neo4j/README.md)

---

### 3. Research Agent (`research/`)
**Purpose:** Automated knowledge research before tasks

**Features:**
- Search knowledge base
- Query Neo4j graph
- Search GitHub issues
- External API integration

**Called by:**
- `bin/` CLI: `agentic-sdlc research`
- `.agent/` workflows: PM, DEV, TESTER (before work)
- Kiro hooks: Auto-trigger on @role mentions

**Usage:**
```bash
python tools/research/research_agent.py --task "authentication" --type feature
```

**Documentation:** [research/README.md](research/README.md)

---

### 4. Setup Utilities (`setup/`)
**Purpose:** System setup and configuration

**Features:**
- Setup research hooks
- Standardize filenames
- Configure integrations

**Called by:**
- `bin/` CLI: `agentic-sdlc install`
- Manual setup: Initial project configuration

**Usage:**
```bash
bash tools/setup/setup_research_hooks.sh
.\tools\setup\standardize_filenames.ps1
```

**Documentation:** [setup/README.md](setup/README.md)

---

## Installation

### Install All Dependencies

```bash
# Install all tool dependencies
pip install -r tools/requirements.txt
```

### Install Specific Tool Dependencies

```bash
# GitHub integration
pip install PyGithub python-dotenv

# Neo4j integration
pip install neo4j python-dotenv

# Research agent
pip install requests python-dotenv pyyaml
```

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r tools/requirements.txt
```

## Configuration

### Environment Variables

Create `.env` file in project root:

```bash
# GitHub Integration (optional)
GITHUB_TOKEN=ghp_your_personal_access_token
GITHUB_REPO=username/repository

# Neo4j Integration (optional)
NEO4J_URI=neo4j+s://instance.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
NEO4J_DATABASE=neo4j

# Research Agent APIs (optional)
TAVILY_API_KEY=your_tavily_key
BRAVE_API_KEY=your_brave_key
STACKOVERFLOW_KEY=your_stackoverflow_key
```

### Tool-Specific Configuration

Each tool may have additional configuration:
- See individual README files for details
- Check `requirements.txt` in each subdirectory
- Review example configurations

## Usage Patterns

### Pattern 1: Called by CLI

```javascript
// bin/agentic-sdlc/commands/sync.js
import { execSync } from 'child_process';

export async function syncGitHub(sprint) {
  execSync(`python tools/github/sync_github.py --sprint ${sprint}`);
}
```

### Pattern 2: Called by Workflows

```markdown
## @PM Workflow

### Step 0: Research
```bash
python tools/research/research_agent.py --task "${task}" --type general
```

### Step 5: Sync to GitHub
```bash
python tools/github/sync_github.py --sprint ${sprint_number}
```
```

### Pattern 3: Called by Hooks

```json
{
  "name": "research-before-planning",
  "trigger": "on_message",
  "condition": "message contains '@PM'",
  "action": {
    "type": "command",
    "command": "python tools/research/research_agent.py --task \"${message}\""
  }
}
```

## Integration Examples

### Example 1: KB CLI with Neo4j

```bash
# User runs KB CLI
./bin/kb/kb compound search "authentication"

# KB CLI calls tools/neo4j/
# → tools/neo4j/query_skills_neo4j.py
# → Returns results to CLI
# → CLI displays to user
```

### Example 2: PM Workflow with Research

```bash
# User: @PM Build todo app

# PM workflow calls tools/research/
# → tools/research/research_agent.py --task "todo app"
# → Searches KB, Neo4j, GitHub
# → Returns research report
# → PM uses findings in project plan
```

### Example 3: Automated GitHub Sync

```bash
# REPORTER workflow completes

# Workflow calls tools/github/
# → tools/github/sync_github.py --sprint 3
# → Creates GitHub issues
# → Applies labels
# → Links artifacts
```

## Development

### Adding New Tools

1. Create subdirectory: `tools/newtool/`
2. Add scripts: `tools/newtool/script.py`
3. Add README: `tools/newtool/README.md`
4. Add requirements: `tools/newtool/requirements.txt`
5. Update master requirements: `tools/requirements.txt`
6. Update this README

### Tool Template

```python
#!/usr/bin/env python3
"""
Tool: New Tool
Purpose: Brief description
Called by: bin/ CLI, .agent/ workflows
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment
load_dotenv()

def main():
    """Main function"""
    print("🔧 Running New Tool...")
    
    # Tool logic here
    
    print("✅ Complete!")

if __name__ == '__main__':
    main()
```

### Best Practices

1. **Idempotent** - Safe to run multiple times
2. **Error handling** - Graceful failures
3. **Logging** - Clear progress messages
4. **Configuration** - Use environment variables
5. **Documentation** - Comprehensive README
6. **Testing** - Include test scripts
7. **Cross-platform** - Support Windows, Linux, macOS

## Testing

### Test Individual Tools

```bash
# GitHub integration
python tools/github/sync_github.py --dry-run

# Neo4j integration
python tools/neo4j/test_neo4j_connection.py

# Research agent
python tools/research/research_agent.py --task "test" --type general

# Setup utilities
bash tools/setup/setup_research_hooks.sh
```

### Test Integration

```bash
# Test CLI → Tools
./bin/kb/kb compound search "test"

# Test Workflow → Tools
# Run @PM workflow and verify research runs
```

## Troubleshooting

### Import Errors

```bash
# Ensure dependencies installed
pip install -r tools/requirements.txt

# Check Python path
which python3
python3 --version
```

### Permission Errors

```bash
# Make scripts executable (Linux/macOS)
chmod +x tools/setup/*.sh
chmod +x tools/research/*.py
```

### Configuration Errors

```bash
# Check .env file exists
ls -la .env

# Verify environment variables
cat .env | grep GITHUB_TOKEN
cat .env | grep NEO4J_URI
```

### API Errors

```bash
# Test GitHub connection
python -c "from github import Github; g = Github('token'); print(g.get_user().login)"

# Test Neo4j connection
python tools/neo4j/test_neo4j_connection.py
```

## Performance

### Optimization Tips

1. **Cache results** - Avoid redundant API calls
2. **Batch operations** - Process multiple items together
3. **Async operations** - Use async/await for I/O
4. **Connection pooling** - Reuse database connections
5. **Rate limiting** - Respect API limits

### Benchmarks

- **GitHub sync:** ~2-5 seconds per sprint
- **Neo4j sync:** ~5-10 seconds for 100 entries
- **Research agent:** ~3-8 seconds per query
- **Setup scripts:** ~1-2 seconds

## Security

### Best Practices

1. **Never commit secrets** - Use .env files
2. **Use environment variables** - Not hardcoded values
3. **Validate inputs** - Sanitize user input
4. **Secure connections** - Use HTTPS/TLS
5. **Minimal permissions** - Least privilege principle

### API Token Security

```bash
# .env file (never commit!)
GITHUB_TOKEN=ghp_...
NEO4J_PASSWORD=...

# .gitignore
.env
*.env
```

## Related Documentation

- **CLI Guide:** `../docs/CLI-GUIDE.md`
- **Architecture:** `../docs/ARCHITECTURE.md`
- **Workflows:** `../.agent/workflows/README.md`
- **Knowledge Base:** `../.agent/knowledge-base/README.md`

## Support

### Questions?
- Check individual tool README files
- Review example configurations
- Test with dry-run mode first

### Issues?
- Check error logs
- Verify configuration
- Test dependencies
- Review API quotas

### Contributions?
- Follow tool template
- Add comprehensive README
- Include tests
- Update this overview

---

**Version:** 1.0.0  
**Created:** 2026-01-02  
**Purpose:** Support scripts for bin/ CLI and .agent/ workflows
