---
description: [Process] Sprint Management Workflow
---

# /sprint - Sprint Lifecycle Management

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
1. **SPRINT START:** Create folder structure and archive previous sprint.
2. **SPRINT STATUS:** Monitor progress during sprint.
3. **SPRINT CLOSE:** Generate review and retrospective templates.

## Quick Commands

```bash
# Start a new sprint
python tools/workflows/sprint.py start 6

# Check current sprint status
python tools/workflows/sprint.py status

# Close a sprint
python tools/workflows/sprint.py close 5
```

## Sprint Start

### What It Does
1. **Archives previous sprint** (copies to `docs/archive/sprint-[N-1]/`)
2. **Creates new sprint folder structure:**
   ```
   docs/sprints/sprint-[N]/
   ├── plans/        # Sprint planning docs
   ├── designs/      # Technical designs
   ├── logs/         # Daily logs and notes
   ├── reviews/      # Code review records
   └── reports/      # Sprint reports
   ```
3. **Creates sprint README.md** with goals template
4. **Updates current sprint** in project config

### Usage
```bash
python tools/workflows/sprint.py start 6
```

### Next Steps After Start
1. Run `@PM /planning` to create sprint plan
2. Sync backlog with GitHub Issues
3. Announce sprint start to team

## Sprint Status

### What It Shows
- Current sprint name
- Sprint directory existence
- File counts per folder
- README presence

### Usage
```bash
python tools/workflows/sprint.py status
```

## Sprint Close

### What It Does
1. **Generates Sprint Review template** (`reports/Sprint-Review-[N].md`)
   - Accomplishments section
   - Metrics placeholders
   - Demo highlights
   - Stakeholder feedback

2. **Generates Retrospective template** (`reports/Retrospective-[N].md`)
   - What went well
   - What didn't go well
   - What we learned
   - Action items for next sprint

### Usage
```bash
python tools/workflows/sprint.py close 5
```

### Next Steps After Close
1. Fill in Sprint Review with accomplishments
2. Complete Retrospective with team
3. Start next sprint: `python tools/workflows/sprint.py start 6`

## Sprint Folder Structure

```
docs/sprints/sprint-[N]/
├── README.md           # Sprint overview and goals
├── plans/
│   ├── Project-Plan-Sprint-[N]-v*.md
│   └── Product-Backlog-Sprint-[N]-v*.md
├── designs/
│   ├── Backend-Design-Spec-Sprint-[N]-v*.md
│   └── UIUX-Design-Spec-Sprint-[N]-v*.md
├── logs/
│   ├── Development-Log-Sprint-[N]-v*.md
│   └── Incident-Report-*.json
├── reviews/
│   ├── Design-Verification-Report-Sprint-[N].md
│   └── Security-Review-Report-Sprint-[N].md
└── reports/
    ├── Sprint-Review-[N].md
    └── Retrospective-[N].md
```

## Integration with Other Workflows

- **@PM** uses sprint folders for planning artifacts
- **@DEV** logs progress in `Development-Log.md`
- **/emergency** creates incident reports in `logs/`
- **/release** references sprint in changelog

#sprint #agile #lifecycle #planning #retrospective
