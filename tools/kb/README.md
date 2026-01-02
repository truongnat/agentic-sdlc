# Knowledge Base Management Scripts

Manage the compound learning system.

## Available Scripts

### `search.py` - Search Knowledge Base
Search for patterns, solutions, and knowledge entries.

**Usage:**
```bash
# Search by query
python tools/kb/search.py --query "authentication"

# Search by category
python tools/kb/search.py --category "security"

# Search by priority
python tools/kb/search.py --priority "critical"
```

**Features:**
- Full-text search
- YAML frontmatter filtering
- Category-based search
- Tag-based search
- Related pattern discovery

---

### `update-index.py` - Update KB Index
Rebuild the searchable knowledge base index.

**Usage:**
```bash
# Update full index
python tools/kb/update-index.py

# Update specific category
python tools/kb/update-index.py --category "bugs"
```

**Tasks:**
- Scan all KB entries
- Extract YAML frontmatter
- Build searchable index
- Generate cross-references
- Validate entry structure

---

### `stats.py` - Generate KB Statistics
Generate compound system health metrics.

**Usage:**
```bash
# Full statistics
python tools/kb/stats.py

# Weekly report
python tools/kb/stats.py --period "week"
```

**Metrics:**
- Total entries
- Entries by category
- Time saved
- Reuse rate
- Coverage percentage
- Top patterns

---

## Knowledge Base Structure

```
.agent/knowledge-base/
├── INDEX.md                 # Searchable index
├── bugs/                    # Bug patterns
│   ├── critical/
│   ├── high/
│   ├── medium/
│   └── low/
├── features/                # Feature implementations
├── architecture/            # Architecture decisions
├── security/                # Security fixes
├── performance/             # Optimizations
└── platform-specific/       # Platform issues
```

## Entry Format

All entries use YAML frontmatter:

```yaml
---
title: "Brief descriptive title"
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
Clear description

## Root Cause
What caused it

## Solution
Step-by-step fix

## Prevention
How to avoid

## Related Patterns
Links to similar issues
```

## Integration

Called by:
- **Kiro IDE** - `/compound` command
- **CLI** - `kb` commands
- **Workflows** - All roles (search-first)

## Dependencies

```bash
pip install pyyaml
```

## See Also

- **KB Documentation:** `.agent/knowledge-base/README.md`
- **Compound Learning:** `.kiro/steering/compound-learning.md`
- **Tools Overview:** `tools/README.md`
