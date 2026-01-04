---
description: [Support] Compound Knowledge Capture Workflowter Tasks
---

# Compound Learning Workflow

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
This workflow MUST be executed after completing any significant task.

## When to Use
- After fixing a bug (medium+ priority)
- After completing a feature
- After resolving a complex problem (3+ hours)

## Steps

### 1. Create KB Entry
```bash
cp .agent/templates/Knowledge-Entry-Template.md \
   .agent/knowledge-base/[category]/KB-$(date +%Y-%m-%d)-###-[name].md
```

### 2. Fill Entry
- Problem/Challenge
- Solution
- Implementation details
- Learnings

### 3. Sync to Neo4j
```bash
python tools/neo4j/sync_skills_to_neo4j.py
```

### 4. Update KB Index
```bash
python bin/kb_cli.py update-index
```

### 5. Record Success (Learning Engine)
```bash
python tools/neo4j/learning_engine.py --record-success "TASK-ID" --task-type "feature"
```

#compound #learning #knowledge-base
