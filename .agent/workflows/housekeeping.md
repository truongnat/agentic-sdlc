---
description: [Support] Housekeeping - Cleanup and Maintenance
---

# /housekeeping - System Maintenance Workflow

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
1. **RUN REGULARLY:** Execute at least once per sprint.
2. **VERIFY HEALTH:** Ensure all indexes are updated.
3. **ARCHIVE OLD DATA:** Move completed sprint data to archive.

## Quick Command

```bash
python tools/workflows/housekeeping.py
```

## Workflow Steps

### Step 1: Archive Old Sprints
- Identifies completed sprints
- Moves to `docs/archive/sprint-[N]/`
- Preserves reference copies

### Step 2: Fix Documentation Drift
- Checks for stale references
- Identifies broken links
- Reports outdated documentation

### Step 3: Update Indexes
```bash
# Updates KB index
python bin/kb_cli.py update-index
```
- Regenerates `.agent/knowledge-base/INDEX.md`
- Ensures all entries are indexed
- Updates statistics

### Step 4: Verify System Health
Reports:
- Total KB entries
- Number of categories
- Current sprint status
- System health status

## Expected Output

```
============================================================
Housekeeping Workflow
============================================================

[INFO] Run housekeeping tasks? (Y/n): y

============================================================
Step 1: Archive Old Sprints
============================================================
[INFO] Checking for completed sprints...
[OK] No sprints to archive

============================================================
Step 2: Fix Documentation Drift
============================================================
[INFO] Checking for documentation drift...
[OK] No drift detected

============================================================
Step 3: Update Indexes
============================================================
[INFO] Updating knowledge base index...
[OK] KB index updated

============================================================
Step 4: Verify System Health
============================================================
[INFO] Total KB entries: 12
[INFO] Categories: 6
[INFO] Current sprint: sprint-6
[OK] System health check passed

🎉 Housekeeping completed successfully!
```

## When to Run

- **Weekly:** During sprint (recommended)
- **End of Sprint:** Before closing sprint
- **After Major Changes:** After bulk KB entries or documentation updates
- **Before Release:** Ensure clean state

## Related Workflows

- **/brain** - For syncing Neo4j and LEANN
- **/validate** - For checking workflow tool references
- **/metrics** - For generating project statistics
- **/sprint close** - Triggers housekeeping automatically

#housekeeping #maintenance #cleanup #health-check
