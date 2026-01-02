# Workflow Automation Scripts

Execute TeamLifecycle workflow commands.

## Available Workflows

### `cycle.py` - Complete Task Lifecycle
Execute the full task lifecycle: Plan → Work → Review → Compound

**Usage:**
```bash
python tools/workflows/cycle.py --task "Add user avatar upload"
```

**Called by:**
- Kiro IDE: `/cycle` command
- CLI: `agentic-sdlc cycle`

**Flow:**
1. Search KB for similar patterns
2. Plan implementation
3. Execute work
4. Review and test
5. Compound knowledge

---

### `housekeeping.py` - Maintenance & Cleanup
Regular maintenance and cleanup tasks.

**Usage:**
```bash
python tools/workflows/housekeeping.py --sprint 3
```

**Called by:**
- Kiro IDE: `/housekeeping` command
- CLI: `agentic-sdlc housekeeping`

**Tasks:**
- Archive completed sprints
- Fix documentation drift
- Update KB index
- Verify artifact placement
- Clean up temporary files

---

### `emergency.py` - Critical Incident Response
Handle production emergencies and critical bugs.

**Usage:**
```bash
python tools/workflows/emergency.py --issue "Payment gateway down"
```

**Called by:**
- Kiro IDE: `/emergency` command
- CLI: `agentic-sdlc emergency`

**Flow:**
1. Assess severity
2. Implement hotfix
3. Deploy to production
4. Create postmortem
5. Compound learnings

---

## Integration

These workflows are called by:
- **Kiro IDE** - Via `/workflow` commands
- **CLI** - Via `bin/agentic-sdlc` commands
- **Hooks** - Automated triggers

## Dependencies

```bash
pip install -r tools/requirements.txt
```

## See Also

- **Workflow Documentation:** `.agent/workflows/`
- **Tools Overview:** `tools/README.md`
- **Knowledge Base:** `.agent/knowledge-base/`
