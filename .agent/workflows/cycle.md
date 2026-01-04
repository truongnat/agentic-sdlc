---
description: [Process] Complete Task Lifecycle - Plan → Work → Review → Compound
---

# /cycle - Complete Task Lifecycle

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
1. **NO SKIPPING:** Every step is MANDATORY.
2. **TEAM COMMUNICATION FIRST:** Announce start and check history.
3. **GIT FLOW:** Feature branch, atomic commits, PR.
4. **SELF-LEARNING:** After completion, update Neo4j.

### 0.0 **Team Communication (MANDATORY):**
   - **Check History:** `python tools/communication/cli.py history --channel general --limit 10`
   - **Announce Start:** `python tools/communication/cli.py send --channel general --thread "SDLC-Flow" --role AGENT --content "Starting /cycle for [Task]."`

## Workflow Steps

### 1. Research Phase (MANDATORY)
```bash
python tools/research/research_agent.py --feature "[task]" --type feature
```
- [ ] Search KB for similar implementations.
- [ ] Check GitHub issues for context.

### 2. Planning
- Define acceptance criteria.
- Add task to `Development-Log.md`.

### 3. Feature Branch
```bash
git checkout -b feat/TASK-ID-name
git push -u origin feat/TASK-ID-name
```

### 4. Implementation
- Code according to plan.
- Atomic commits: `git commit -m "[TASK-ID] feat: description"`

### 5. Verification
- Run local tests.
- Create PR, tag @TESTER.

### 6. Merge
- Wait for `#testing-passed`.
- Merge via @DEVOPS or @SA.

### 7. Self-Learning (MANDATORY)
```bash
python tools/neo4j/sync_skills_to_neo4j.py
python tools/neo4j/learning_engine.py --record-success "TASK-ID" --task-type "feature"
```
- Update `CHANGELOG.md`.

#cycle #workflow #git-flow #self-learning