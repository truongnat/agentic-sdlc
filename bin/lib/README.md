# Knowledge Base CLI Library

This directory contains the Python library modules for the **Knowledge Base CLI**.

## Overview

The KB CLI is a cross-platform command-line tool for managing the TeamLifecycle knowledge base with optional Neo4j brain integration.

## Architecture

```
kb_cli.py                    # Main CLI entry point
    │
    ├── kb_common.py        # Common utilities
    ├── kb_search.py        # Search functionality
    ├── kb_add.py           # Add entries
    ├── kb_index.py         # Index generation
    ├── kb_stats.py         # Statistics
    ├── kb_list.py          # List entries
    └── kb_compound.py      # Neo4j integration
```

## Modules

### `kb_common.py`
**Purpose:** Common utilities and shared functions

**Exports:**
- `get_kb_path()` - Get knowledge base directory path
- `parse_yaml_frontmatter()` - Parse YAML frontmatter from markdown
- `format_date()` - Format dates consistently
- `get_editor()` - Get platform-specific default editor
- `Colors` - ANSI color codes class

**Usage:**
```python
from kb_common import get_kb_path, Colors

kb_path = get_kb_path()
print(f"{Colors.GREEN}Success!{Colors.RESET}")
```

### `kb_search.py`
**Purpose:** Search knowledge base entries

**Exports:**
- `search_kb(term: str)` - Search for entries matching term

**Features:**
- Searches INDEX.md first
- Falls back to full file search
- Shows context around matches
- Displays metadata

**Usage:**
```python
from kb_search import search_kb

search_kb("react hydration")
```

### `kb_add.py`
**Purpose:** Add new knowledge base entries

**Exports:**
- `add_entry()` - Interactive entry creation wizard

**Features:**
- Interactive prompts
- YAML frontmatter generation
- Unique filename generation
- Auto-open in editor
- Category/priority selection

**Usage:**
```python
from kb_add import add_entry

add_entry()  # Interactive wizard
```

### `kb_index.py`
**Purpose:** Generate and update INDEX.md

**Exports:**
- `update_index()` - Scan entries and regenerate INDEX.md

**Features:**
- Scans all KB entries
- Extracts metadata
- Groups by category, priority, date
- Generates searchable index
- Shows statistics

**Usage:**
```python
from kb_index import update_index

update_index()
```

### `kb_stats.py`
**Purpose:** Display knowledge base statistics

**Exports:**
- `show_stats()` - Calculate and display KB metrics

**Features:**
- Total entries count
- Breakdown by category
- Breakdown by priority
- Total attempts
- Time saved calculations
- Growth trends

**Usage:**
```python
from kb_stats import show_stats

show_stats()
```

### `kb_list.py`
**Purpose:** List knowledge base entries

**Exports:**
- `list_entries(category: str = None, recent: int = None)` - List entries

**Features:**
- List all entries
- Filter by category
- Show recent entries
- Display metadata

**Usage:**
```python
from kb_list import list_entries

list_entries()              # All entries
list_entries("bugs")        # Bugs only
list_entries(recent=10)     # Last 10 entries
```

### `kb_compound.py`
**Purpose:** Neo4j brain integration

**Exports:**
- `compound_operation(action: str, term: str = None)` - Execute compound operations

**Actions:**
- `search` - Search file system + Neo4j
- `add` - Add entry + sync to Neo4j
- `sync` - Full sync to Neo4j
- `query` - Intelligent Neo4j queries
- `stats` - Compound system health

**Features:**
- Neo4j connection management
- Graceful fallback if Neo4j unavailable
- Cross-platform subprocess handling
- Relationship mapping

**Usage:**
```python
from kb_compound import compound_operation

compound_operation("search", "authentication")
compound_operation("sync")
compound_operation("stats")
```

## Dependencies

### Required
- Python 3.7+
- Standard library modules:
  - `os`, `sys`, `pathlib`
  - `json`, `yaml`
  - `datetime`, `re`
  - `subprocess`

### Optional
- `neo4j` - For Neo4j brain integration
- `python-dotenv` - For environment variables

Install optional dependencies:
```bash
pip install neo4j python-dotenv
```

## Configuration

### Environment Variables
Create `.env` file in project root:
```bash
# Neo4j Configuration (optional)
NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
NEO4J_DATABASE=neo4j
```

### Knowledge Base Path
Default: `.agent/knowledge-base/`

Override with environment variable:
```bash
KB_PATH=/custom/path/to/kb
```

## Entry Format

All KB entries use YAML frontmatter:

```yaml
---
title: "Entry Title"
category: bug|feature|architecture|security|performance|platform
priority: critical|high|medium|low
sprint: sprint-N
date: YYYY-MM-DD
tags: [tag1, tag2, tag3]
related_files: [path/to/file1, path/to/file2]
attempts: 3
time_saved: "2 hours"
---

## Problem
Description of the issue

## Solution
How it was solved

## Prevention
How to avoid in future
```

## File Naming Convention

Format: `KB-YYYY-MM-DD-###-title-slug.md`

Example: `KB-2026-01-02-001-react-hydration-error.md`

Components:
- `YYYY-MM-DD` - Creation date
- `###` - Sequential ID for that day (001, 002, etc.)
- `title-slug` - URL-friendly title

## Directory Structure

```
.agent/knowledge-base/
├── INDEX.md                    # Generated index
├── bugs/
│   ├── critical/
│   ├── high/
│   ├── medium/
│   └── low/
├── features/
│   ├── authentication/
│   ├── performance/
│   ├── integration/
│   └── ui-ux/
├── architecture/
├── security/
├── performance/
└── platform-specific/
    ├── web/
    ├── mobile/
    ├── desktop/
    └── cli/
```

## Error Handling

All modules use consistent error handling:

```python
try:
    # Operation
    pass
except FileNotFoundError:
    print(f"{Colors.RED}❌ File not found{Colors.RESET}")
except PermissionError:
    print(f"{Colors.RED}❌ Permission denied{Colors.RESET}")
except Exception as e:
    print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
    import traceback
    traceback.print_exc()
```

## Color Support

Cross-platform ANSI color support:

```python
from kb_common import Colors

print(f"{Colors.GREEN}✅ Success{Colors.RESET}")
print(f"{Colors.RED}❌ Error{Colors.RESET}")
print(f"{Colors.YELLOW}⚠️  Warning{Colors.RESET}")
print(f"{Colors.CYAN}ℹ️  Info{Colors.RESET}")
```

Colors automatically enabled on Windows 10+.

## Testing

### Unit Tests
```bash
# Test individual modules
python -c "from kb_search import search_kb; search_kb('test')"
python -c "from kb_stats import show_stats; show_stats()"
```

### Integration Tests
```bash
# Test full workflow
./bin/kb search test
./bin/kb add
./bin/kb index
./bin/kb stats
```

## Adding New Modules

1. Create new file: `kb_newfeature.py`
2. Follow module structure:
   ```python
   #!/usr/bin/env python3
   """
   Module description
   """
   from kb_common import Colors, get_kb_path
   
   def new_feature():
       """Feature implementation"""
       pass
   ```
3. Import in `kb_cli.py`
4. Add command handler
5. Update this README

## Platform Support

### Windows
- ✅ Command Prompt
- ✅ PowerShell
- ✅ Git Bash
- ✅ ANSI colors (Windows 10+)

### Linux
- ✅ Bash
- ✅ Zsh
- ✅ Fish
- ✅ Full ANSI colors

### macOS
- ✅ Bash
- ✅ Zsh
- ✅ Full ANSI colors

## Performance

- **Startup:** ~100-200ms
- **Search:** ~50-100ms for 100 entries
- **Index:** ~200-500ms for 100 entries
- **Neo4j:** +100-300ms for queries

## Troubleshooting

### Import Errors
```bash
# Ensure lib directory is in Python path
export PYTHONPATH="${PYTHONPATH}:/path/to/bin/lib"
```

### Permission Errors
```bash
# Make scripts executable (Linux/macOS)
chmod +x bin/kb
chmod +x bin/kb_cli.py
```

### Neo4j Connection Issues
```bash
# Test connection
python -c "from neo4j import GraphDatabase; print('Neo4j available')"

# Check .env file
cat .env | grep NEO4J
```

## Related Files

- `../kb` - Bash entry point
- `../kb.bat` - Windows entry point
- `../kb_cli.py` - Main CLI
- `../../tools/neo4j/` - Neo4j integration scripts
- `../../.agent/knowledge-base/` - KB entries

## Documentation

- **Main README:** `../README.md`
- **Cross-Platform Guide:** `../CROSS-PLATFORM-CLI.md`
- **KB Guide:** `../../docs/KNOWLEDGE-BASE-GUIDE.md`
- **Neo4j Integration:** `../../docs/NEO4J-COMPOUND-INTEGRATION.md`

---

**Note:** This is the **Python KB CLI library**. For the Node.js project CLI, see `../commands/README.md`.
