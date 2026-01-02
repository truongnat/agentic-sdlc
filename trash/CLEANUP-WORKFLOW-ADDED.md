# Cleanup Workflow Implementation Complete ✅

**Date:** January 2, 2026  
**Feature:** `/cleanup` workflow for moving legacy files to trash

## What Was Added

### 1. Workflow Definition
**File:** `.agent/workflows/cleanup.md`

Comprehensive workflow for identifying and moving unused, old, or legacy files:
- **Phase 1:** Analysis - Scan for completion docs, duplicates, legacy artifacts
- **Phase 2:** Categorization - Sort into Safe/Review/Keep categories
- **Phase 3:** User Confirmation - Present findings and get approval
- **Phase 4:** Execution - Move files to trash with summary
- **Phase 5:** Verification - Check for broken links and verify project works

### 2. Steering File
**File:** `.kiro/steering/workflow-cleanup.md`

Quick reference guide for Kiro IDE integration:
- Command syntax and options
- Cleanup categories
- Process overview
- Recovery instructions
- Integration with other workflows

### 3. Updated Documentation

**Updated Files:**
- `.agent/workflows/housekeeping.md` - Added reference to `/cleanup` workflow
- `.kiro/steering/workflow-routing.md` - Added cleanup to decision tree
- `.kiro/steering/workflow-enhancements.md` - Added cleanup command

## Usage

### Basic Cleanup
```bash
@ORCHESTRATOR /cleanup
```

### With Options
```bash
@ORCHESTRATOR /cleanup --dry-run         # Preview without moving
@ORCHESTRATOR /cleanup --aggressive      # Include review-needed files
@ORCHESTRATOR /cleanup --category docs   # Specific category only
```

### From Any Role
```bash
@DEV /cleanup
@REPORTER /cleanup
@ORCHESTRATOR /cleanup
```

## Cleanup Categories

### Category A: Safe to Move (Auto)
- Completion documents (`-COMPLETE.md`, `-SUMMARY.md`)
- Old test results (> 30 days)
- Empty or duplicate files
- Deprecated scripts with replacements
- Migration/reorganization reports

### Category B: Review Needed (User Confirmation)
- Old sprint artifacts (> 3 sprints)
- Legacy configuration files
- Demo/example projects
- Outdated documentation

### Category C: Keep (Never Move)
- Active documentation
- Current configuration
- Active code
- Recent artifacts (< 1 sprint)
- Knowledge base entries

## Cleanup Patterns

The workflow recognizes these patterns:

1. **Completion Documents**
   - Files ending in `-COMPLETE.md`
   - Files with "Implementation Complete" in title
   - Migration/reorganization summaries

2. **Duplicate Files**
   - Multiple versions: `file.md`, `file-v2.md`, `file-improved.md`
   - Backup files: `file.bak`, `file.old`
   - Empty files with same name as populated file

3. **Old Sprint Artifacts**
   - Sprint folders > 3 sprints old
   - No recent modifications (> 30 days)
   - Marked as "archived" or "completed"

4. **Legacy Scripts**
   - Scripts with "old", "legacy", "deprecated" in name
   - Scripts replaced by newer versions
   - Scripts not referenced in package.json or docs

5. **Test Results**
   - Files ending in `-RESULTS.md`, `-REPORT.md`
   - Old test output files
   - Benchmark results > 30 days old

## Output

When cleanup runs, it creates:

1. **Trash Folder** - `trash/` at project root
2. **Cleanup Summary** - `trash/CLEANUP-SUMMARY.md`
3. **Updated Documentation** - Fixed broken links
4. **Cleanup Report** - Added to KB if significant

## Recovery

All files are preserved in trash folder:

```bash
# List files in trash
dir trash/

# Recover specific file
move trash/[filename] [original-location]/

# Recover all files
move trash/* ./
```

## Integration

### With `/housekeeping`
- `/housekeeping` includes cleanup as one step
- `/cleanup` is focused cleanup only
- Can be run independently or as part of housekeeping

### With `/compound`
- Document cleanup patterns in KB
- Track time saved by cleanup
- Build cleanup automation

### With `/cycle`
- Run cleanup at end of cycle
- Keep workspace clean between tasks

## Workflow Decision Tree

```
Is workspace cluttered with legacy files?
├─ YES → /cleanup (focused file cleanup)
└─ NO → Continue

Need full maintenance (archive + drift + index)?
├─ YES → /housekeeping (includes cleanup)
└─ NO → Continue
```

## Example Scenarios

### Scenario 1: After Major Reorganization
```
@ORCHESTRATOR /cleanup
# Moves all completion documents to trash
# Creates cleanup summary
# Fixes broken links
```

### Scenario 2: Before Release
```
@ORCHESTRATOR /housekeeping
# Includes cleanup as part of full maintenance
# Archives old sprints
# Updates documentation
# Rebuilds indexes
```

### Scenario 3: Weekly Maintenance
```
@DEV /cleanup --dry-run
# Preview what would be cleaned
# Review findings
# Run actual cleanup if needed
```

## Metrics

Track cleanup effectiveness:
- **Files Moved:** Count of files moved to trash
- **Space Saved:** Disk space freed
- **Time Saved:** Time saved by cleaner workspace
- **Cleanup Frequency:** How often cleanup is needed

## Best Practices

1. **Always create trash folder** - Don't delete permanently
2. **Document what was moved** - Create cleanup summary
3. **Get user confirmation** - For Category B files
4. **Verify after cleanup** - Run health checks
5. **Update documentation** - Fix broken links
6. **Keep recent artifacts** - Don't move files < 1 sprint old

## Automation Opportunities

Future enhancements:
- Auto-cleanup triggers (after sprint, before release)
- Smart detection using file modification dates
- Git history analysis
- File reference tracking
- Usage pattern analysis

## Related Workflows

- `/housekeeping` - Comprehensive maintenance
- `/compound` - Document cleanup patterns
- `/audit` - Verify project health after cleanup
- `/cycle` - Include cleanup at end of task

## Success Criteria

✅ Workflow definition created  
✅ Steering file added  
✅ Documentation updated  
✅ Integration with housekeeping  
✅ Decision tree updated  
✅ Example usage documented  
✅ Recovery process documented  

## Next Steps

1. Test the workflow on a real cleanup scenario
2. Document cleanup patterns in KB
3. Add automation triggers
4. Create cleanup metrics dashboard
5. Build smart detection algorithms

---

**Status:** ✅ Implementation Complete  
**Files Created:** 2  
**Files Updated:** 3  
**Ready for Use:** Yes

#cleanup #workflow #maintenance #trash #legacy

