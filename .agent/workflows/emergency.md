---
description: [Process] Emergency/Hotfix Response Workflow
---

# /emergency - Critical Incident Response

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
1. **IMMEDIATE ACTION:** This workflow takes priority over all other tasks.
2. **TIME-BOXED ASSESSMENT:** Max 5 minutes for initial assessment.
3. **MITIGATION FIRST:** Stop the bleeding before fixing root cause.
4. **COMPOUND LEARNING:** Create KB entry after resolution (MANDATORY).

### 0.0 **Declare Incident:**
```bash
python tools/workflows/emergency.py --severity P0 --issue "[issue description]"
```

## Severity Levels

| Level | Response Time | Examples |
|-------|--------------|----------|
| **P0** | < 15 min | Production down, data loss, security breach |
| **P1** | < 1 hour | Major feature broken, significant user impact |
| **P2** | < 4 hours | Minor feature broken, workaround available |

## Workflow Steps

### 1. Declare Incident (Minute 0)
- Assign incident ID: `INCIDENT-YYYYMMDDHHMMSS`
- Create incident channel/thread
- Notify stakeholders
- Assign incident commander

### 2. Rapid Assessment (5 min max)
```bash
# Search KB for similar incidents
python tools/research/research_agent.py --task "[issue]" --type bug
```
**Quick Checks:**
- [ ] Check monitoring/logs
- [ ] Verify deployment timeline
- [ ] Check external dependencies
- [ ] Review recent commits

### 3. Immediate Mitigation

**Options (fastest first):**
1. **Rollback** - Revert to last known good (~2 min)
2. **Feature Flag** - Disable broken feature (~1 min)
3. **Traffic** - Route around problem (~5 min)
4. **Scale Up** - Add resources if capacity issue (~10 min)

### 4. Root Cause Analysis
While mitigation deploys:
- Review error logs
- Check monitoring dashboards
- Reproduce in staging

### 5. Hotfix Development (Fast Track)
**Skip for speed:**
- ❌ Full design review (document after)
- ❌ Full test suite (critical path only)
- ✅ Single reviewer approval

```bash
git checkout -b hotfix/INCIDENT-ID
# Make minimal fix
git commit -m "hotfix: description (#INCIDENT-ID)"
```

### 6. Verify Resolution
- [ ] Error rate returned to normal
- [ ] Key metrics recovered
- [ ] User reports stopped
- [ ] No new issues introduced

### 7. Compound Learning (MANDATORY)
```bash
# Create KB entry automatically
python tools/workflows/emergency.py --severity P0 --issue "[issue]"

# Or manually update Neo4j
python tools/neo4j/sync_skills_to_neo4j.py
python tools/neo4j/learning_engine.py --record-error "ErrorType" "description" --resolution "fix"
```

### 8. Post-Incident
- [ ] Schedule postmortem (within 24 hours)
- [ ] Review and assign action items
- [ ] Update runbooks if needed
- [ ] Notify stakeholders of resolution

## CLI Usage

```bash
# Interactive workflow
python tools/workflows/emergency.py -s P0 -i "Payment gateway 500 errors"

# Non-interactive (for automation)
python tools/workflows/emergency.py -s P1 -i "API timeout" --non-interactive
```

## Output Artifacts
- `docs/sprints/sprint-[N]/logs/Incident-Report-[ID].json`
- KB entry in `.agent/knowledge-base/bugs/`

#emergency #hotfix #incident #production #p0
