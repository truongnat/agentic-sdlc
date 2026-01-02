# Knowledge Base Scripts (Python Only)

**Cross-Platform CLI** - Works on Windows, Linux, and macOS

Python-based CLI for managing the TeamLifecycle knowledge base with Neo4j brain integration.

## 🐍 Technology Stack

- ✅ **Python 3.7+** - Primary language
- ✅ **Shell scripts** - Linux/macOS entry points
- ✅ **Batch/PowerShell** - Windows entry points
- ❌ **NO JavaScript/Node.js**

## 🌍 Cross-Platform Support

The KB CLI supports all major platforms:

- **Windows** - CMD, PowerShell, Git Bash
- **Linux** - Bash, Zsh, Fish
- **macOS** - Bash, Zsh

### Quick Start

**Windows:**
```cmd
bin\kb\kb.bat help
```

**Linux/macOS:**
```bash
./bin/kb/kb help
```

**See:** `kb/CROSS-PLATFORM-CLI.md` for complete cross-platform guide

## Overview

The compound learning system combines file-based storage with Neo4j graph database to create an intelligent knowledge system:

- **File System** - Stores full markdown content from `.agent/knowledge-base/` and `docs/`
- **Neo4j Brain** - Maps relationships between skills, technologies, and entries
- **Compound Scripts** - Seamless integration between both
- **Cross-Platform** - Python-based CLI works everywhere
- **Unified Search** - Search across KB entries + all project documentation (46+ entries)

### Knowledge Sources

The system indexes knowledge from two locations:

1. **`.agent/knowledge-base/`** - KB entries (bugs, features, architecture)
2. **`docs/`** - All project documentation (guides, reports, architecture docs)

This provides **7x more searchable knowledge** than KB entries alone!

## Available Scripts

### Cross-Platform CLI

**Entry Points:**
- `kb` - Bash script (Linux/macOS/Git Bash)
- `kb.bat` - Windows batch script
- `kb_cli.py` - Python CLI (all platforms)

**Library Modules:**
- `lib/kb_common.py` - Common utilities
- `lib/kb_search.py` - Search functionality
- `lib/kb_add.py` - Add entries
- `lib/kb_index.py` - Index generation
- `lib/kb_stats.py` - Statistics
- `lib/kb_list.py` - List entries
- `lib/kb_compound.py` - Neo4j integration

## 📚 Available Scripts

### 1. `kb` / `kb.bat` - Main Interface
Central command-line interface for all KB operations.

**Windows:**
```cmd
bin\kb.bat [command] [args]
```

**Linux/macOS:**
```bash
./bin/kb [command] [args]
```

## 🔍 Commands

### 1. Search Knowledge Base

Search for entries by keyword:

```powershell
# Search for a term
.\bin\kb.ps1 search "react hydration"

# Search in specific category
.\bin\kb-search.ps1 "oauth" -Category "features"

# Filter by priority
.\bin\kb-search.ps1 "bug" -Priority "critical"
```

**What it does:**
- Searches INDEX.md first
- Then searches all KB entry files
- Shows matching entries with context
- Displays file paths and metadata

### 2. Add New Entry

Interactive wizard to create a new KB entry:

```powershell
.\bin\kb.ps1 add
```

**What it does:**
- Prompts for title, category, priority, tags
- Generates unique filename with date and ID
- Creates entry from template
- Places in correct folder
- Opens file in default editor

**Categories:**
1. bug - Bug fixes
2. feature - Complex features
3. architecture - Architecture decisions
4. security - Security fixes
5. performance - Performance optimizations
6. platform - Platform-specific issues

**Priorities:**
1. critical - System breaking
2. high - Major issues
3. medium - Moderate issues
4. low - Minor issues

### 3. Update Index

Regenerate INDEX.md with all entries:

```powershell
.\bin\kb.ps1 index
```

**What it does:**
- Scans all KB entries
- Extracts metadata (title, category, priority, tags)
- Groups by category, priority, and date
- Generates searchable INDEX.md
- Shows statistics

**Run this after:**
- Adding new entries
- Updating existing entries
- Reorganizing KB structure

### 4. Show Statistics

Display KB statistics and metrics:

```powershell
.\bin\kb.ps1 stats
```

**What it shows:**
- Total entries
- Breakdown by category
- Breakdown by priority
- Total attempts
- Time saved
- Recent activity
- Growth trend

### 5. List Entries

List all entries or filter by category:

```powershell
# List all entries
.\bin\kb.ps1 list

# List by category
.\bin\kb.ps1 list bugs
.\bin\kb.ps1 list features
.\bin\kb.ps1 list architecture
```

### 6. Show Recent Entries

Display recently added/modified entries:

```powershell
# Show last 10 entries (default)
.\bin\kb.ps1 recent

# Show last 5 entries
.\bin\kb.ps1 recent 5
```

### 7. Compound Mode (Neo4j Integration)

Enhanced commands that integrate file system with Neo4j brain:

```powershell
# Compound search (file + Neo4j)
.\bin\kb.ps1 compound search "authentication"

# Compound add (create + sync to Neo4j)
.\bin\kb.ps1 compound add

# Compound sync (full sync to Neo4j)
.\bin\kb.ps1 compound sync

# Compound query (intelligent Neo4j queries)
.\bin\kb.ps1 compound query "React"

# Compound stats (system health)
.\bin\kb.ps1 compound stats
```

**What compound mode does:**
- Searches both file system AND Neo4j graph
- Automatically syncs entries to Neo4j brain
- Maps relationships between skills and technologies
- Provides intelligent contextual queries
- Shows compound system health

**See:** `docs/NEO4J-COMPOUND-INTEGRATION.md` for complete guide

### 8. Help

Show help and usage:

```powershell
.\bin\kb.ps1 help
```

## 🚀 Quick Start Workflow

### Before Solving a Problem

```powershell
# 1. Compound search (file + Neo4j brain)
.\bin\kb.ps1 compound search "your problem"

# 2. If found, read the solution
# 3. If not found, solve it yourself
```

### After Solving a Hard Problem

```powershell
# 1. Add entry with compound mode (auto-syncs to Neo4j)
.\bin\kb.ps1 compound add

# 2. Fill in the details in the opened file

# 3. Entry is automatically synced to Neo4j brain
```

### Weekly Maintenance

```powershell
# Check compound system health
.\bin\kb.ps1 compound stats

# Full sync to Neo4j
.\bin\kb.ps1 compound sync

# Review recent entries
.\bin\kb.ps1 recent 20
```

## 📊 Example Usage

### Scenario 1: React Hydration Error

```powershell
# Search first
PS> .\bin\kb.ps1 search "react hydration"

🔍 Searching Knowledge Base for: 'react hydration'

✅ Found in INDEX:
  KB-2026-01-01-001-react-hydration-error.md

✅ Found: React Hydration Mismatch Error
   File: .agent/knowledge-base/bugs/high/KB-2026-01-01-001-react-hydration-error.md
   Category: bug | Priority: high
   Context:
     ## Problem
     React shows "Hydration failed" error in production
     
📊 Search Results: 1 entries found
```

### Scenario 2: Add OAuth Implementation

```powershell
# Add new entry
PS> .\bin\kb.ps1 add

📝 Knowledge Base - Add New Entry

Title: OAuth 2.0 Implementation with Google
Category (1-6): 2
Priority (1-4): 2
Tags: oauth, google, authentication
Attempts: 4
Time saved: 3 hours

✅ Entry Created Successfully!

📄 File: .agent/knowledge-base/features/KB-2026-01-02-001-oauth-google.md

# Update index
PS> .\bin\kb.ps1 index

✅ INDEX.md Updated Successfully!
📊 Total Entries: 15
```

### Scenario 3: Check KB Health

```powershell
PS> .\bin\kb.ps1 stats

📊 Knowledge Base Statistics

📚 Total Entries: 15

📁 By Category:
   bug            : 6 entries (40%)
   ██████████████████████
   feature        : 5 entries (33.3%)
   ████████████████
   architecture   : 2 entries (13.3%)
   ██████
   security       : 2 entries (13.3%)
   ██████

⚠️  By Priority:
   🔴 critical    : 2 entries (13.3%)
   🟠 high        : 5 entries (33.3%)
   🟡 medium      : 6 entries (40%)
   🟢 low         : 2 entries (13.3%)

📈 Compound Learning Metrics:
   Total Attempts: 45
   Avg Attempts per Entry: 3.0
   Total Time Saved: ~38 hours
   Projected Time Saved (2x reuse): ~76 hours

💡 Compound Effect:
   Each entry makes future work easier!
   Keep documenting to compound your knowledge! 🚀
```

## 🎯 Best Practices

### When to Search
- ✅ Before starting any complex task
- ✅ When encountering an error
- ✅ When implementing a known pattern
- ✅ During code review

### When to Add
- ✅ Bug took 3+ attempts to fix
- ✅ Solution was non-obvious
- ✅ Issue likely to recur
- ✅ Pattern applies to multiple features
- ✅ Security vulnerability fixed
- ✅ Performance optimization achieved

### When to Update Index
- ✅ After adding new entries
- ✅ After updating existing entries
- ✅ Weekly maintenance
- ✅ Before sharing KB with team

## 🔧 Script Details

### File Naming Convention

Entries are named: `KB-YYYY-MM-DD-###-title-slug.md`

Example: `KB-2026-01-02-001-react-hydration-error.md`

- `YYYY-MM-DD` - Date created
- `###` - Sequential ID for that day
- `title-slug` - URL-friendly title

### Folder Structure

```
.agent/knowledge-base/
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

### Entry Template

Each entry includes:
- YAML frontmatter (metadata)
- Problem description
- What didn't work
- Solution that worked
- Code examples
- Prevention tips
- Related patterns

## 📚 Documentation

- **Simple Guide:** `.agent/knowledge-base/HOW-IT-WORKS.md`
- **Visual Guide:** `docs/KNOWLEDGE-BASE-GUIDE.md`
- **Quick Reference:** `docs/KNOWLEDGE-BASE-SIMPLE.md`
- **Full README:** `.agent/knowledge-base/README.md`

## 🐛 Troubleshooting

### Script Won't Run

```powershell
# Enable script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Search Not Finding Entries

- Check spelling
- Try different keywords
- Use broader terms
- Check if entry exists: `.\bin\kb.ps1 list`

### Index Not Updating

- Ensure entries have proper YAML frontmatter
- Check file naming convention
- Run: `.\bin\kb.ps1 index` manually

## 💡 Tips

1. **Search First** - Always search before solving
2. **Document Immediately** - Add entry right after solving
3. **Use Tags** - Add relevant tags for better searchability
4. **Update Index** - Run `kb.ps1 index` regularly
5. **Review Stats** - Check `kb.ps1 stats` weekly
6. **Share Knowledge** - Tell team about useful entries

## 🎓 Learning Path

### Week 1: Consumer
```powershell
.\bin\kb.ps1 search "your problem"
.\bin\kb.ps1 list
.\bin\kb.ps1 recent
```

### Week 2: Contributor
```powershell
.\bin\kb.ps1 add
.\bin\kb.ps1 index
```

### Week 3: Curator
```powershell
.\bin\kb.ps1 stats
# Update old entries
.\bin\kb.ps1 index
```

## 🚀 Advanced Usage

### Batch Operations

```powershell
# Search multiple terms
$terms = @("react", "oauth", "performance")
foreach ($term in $terms) {
    .\bin\kb.ps1 search $term
}

# List all categories
$categories = @("bugs", "features", "architecture")
foreach ($cat in $categories) {
    .\bin\kb.ps1 list $cat
}
```

### Integration with Git

```powershell
# After adding entry
.\bin\kb.ps1 add
.\bin\kb.ps1 index
git add .agent/knowledge-base/
git commit -m "docs: add KB entry for OAuth implementation"
```

---

**Version:** 1.0.0  
**Created:** 2026-01-02  
**Platform:** Windows PowerShell

#knowledge-base #scripts #automation #compound-learning
