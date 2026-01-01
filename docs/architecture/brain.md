# 🧠 The Project Brain: Hybrid Memory & Reasoning

This project uses a **Hybrid Brain Architecture** combining **LEANN** (Vector Memory) and **Neo4j Aura** (Reasoning Graph).

## 🚀 Two Layers of Intelligence

### 1. LEANN (Semantic Knowledge)
- **Primary Use:** Finding similar code patterns and semantic context.
- **Why:** Ultra-fast, AST-aware search with 97% storage savings.
- **Operation:** Local (runs via WSL2 or local Python).

### 2. Neo4j Cloud (Reasoning Graph)
- **Primary Use:** Understanding relationships between requirements, code, and bugs.
- **Why:** Allows agents to perform deep reasoning paths: *"This bug in File X is related to Requirement Y implemented in Sprint Z."*
- **Operation:** Cloud-based (Neo4j AuraDB).

## 🛠️ How to Use

### 1. Semantic Search
Use `/brain [query]` or run:
```bash
leann search "your query"
```

### 2. Reasoning Update
To sync the latest project structure and relationships to the Cloud Brain:
```bash
python bin/graph_brain.py
```

## 📋 Best Practices
- **Update Frequently:** Run the ingestion script after merging any major feature.
- **Hybrid Queries:** When solving a complex bug, ask the AI to check both LEANN for code context and Neo4j for relationship history.

---
*Powered by [LEANN](https://github.com/yichuan-w/LEANN) and [Neo4j Aura](https://neo4j.com/aura/)*
