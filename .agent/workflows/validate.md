---
description: [Utility] Validate - Workflow Compliance Checker
---

# /validate - Tool Reference Validator

## ⚠️ PURPOSE
Scans all workflow files for `python tools/...` commands and file path references, verifies they exist, and generates a validation report.

## Quick Commands

```bash
# Full validation
python tools/validation/validate.py

# With fix suggestions
python tools/validation/validate.py --fix

# Generate report file
python tools/validation/validate.py --report
```

## What It Checks

### 1. Tool References
Finds all `python tools/...` commands in workflow files and verifies the scripts exist.

**Example issues:**
- `python tools/research/research.py` → File not found (should be `research_agent.py`)
- `python tools/kb/update.py` → Missing script

### 2. File Path References
Checks paths like:
- `` `.agent/workflows/...` ``
- `` `tools/...` ``
- `".agent/..."` or `'.agent/...'`

### 3. Hardcoded Paths
Detects absolute paths that should be relative:
- `C:\Users\...` (Windows)
- `/home/...` (Linux)
- `/Users/...` (macOS)

## Output

### Console Output
```
============================================================
Workflow Tool Reference Validator
============================================================
[INFO] Project root: d:\dev\agentic-sdlc
[INFO] Scanning workflows for tool references...
[INFO] Checking for hardcoded paths...

============================================================
Validation Results
============================================================
  Workflows scanned: 20
  Total references:  45
  Valid references:  43
  Broken references: 2
  Hardcoded paths:   1

  Health Score: 85/100

============================================================
Issues Found
============================================================
[ERR] pm.md:25 - tools/research/research.py - File not found
[WARN] dev.md:42 - Windows absolute path
```

### Report Output (--report)
Generates `docs/reports/Validation-Report-YYYY-MM-DD.md`:

```markdown
# Validation Report

**Generated:** 2026-01-03 18:00  
**Health Score:** 85/100

## Summary
- **Workflows Scanned:** 20
- **Total References:** 45
- **Valid References:** 43
- **Broken References:** 2

## ❌ Broken Tool References
| Workflow | Line | Reference | Issue |
|----------|------|-----------|-------|
| pm.md | 25 | `tools/research/research.py` | File not found |

## ⚠️ Hardcoded Paths
- **dev.md** (line 42): Windows absolute path
```

## Health Score Calculation

- **Base Score:** `(valid_refs / total_refs) * 100`
- **Penalties:**
  - Hardcoded paths: -5 points each (max -20)

| Score | Status |
|-------|--------|
| 90-100 | ✅ Excellent |
| 70-89 | 🟡 Good |
| 50-69 | 🟠 Needs Attention |
| 0-49 | 🔴 Critical |

## Fix Suggestions (--fix)

```bash
python tools/validation/validate.py --fix
```

Outputs:
```
============================================================
Suggested Fixes
============================================================
  tools/research/research.py -> tools/research/research_agent.py
  tools/kb/update.py - No similar file found, may need to be created
```

## When to Run

- **Before commits:** Ensure no broken references
- **During CI/CD:** Automated validation
- **After refactoring:** Verify all paths updated
- **/housekeeping:** Part of maintenance routine

## Integration

Works with:
- **/housekeeping** - System maintenance
- **/brain** - Knowledge sync
- CI/CD pipelines

#validate #health-check #workflow-audit #compliance
