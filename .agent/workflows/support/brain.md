---
description: [Support] LEANN AI Brain - Automated Project Memory
---

# Brain Workflow

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
All steps are mandatory for proper brain synchronization.

// turbo-all

## Quick Sync
```bash
python tools/neo4j/brain_parallel.py --sync
```

## Full Sync (All Operations)
```bash
python tools/neo4j/brain_parallel.py --full
```

## Manual Steps

### 1. Index Project (LEANN)
```bash
leann index --path . --update
```

### 2. Sync to Neo4j
```bash
python tools/neo4j/sync_skills_to_neo4j.py
python tools/neo4j/document_sync.py --all
```

### 3. Update KB Index
```bash
python bin/kb_cli.py update-index
```

### 4. Get Recommendations
```bash
python tools/neo4j/brain_parallel.py --recommend "[task description]"
```

#brain #leann #neo4j #self-learning
