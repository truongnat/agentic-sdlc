# 🧠 AI Self-Learning: Neo4j Reasoning Dashboard

These Cypher queries are designed to help the AI (and you) extract "wisdom" from the project graph. Run these in your [Neo4j Aura Console](https://console.neo4j.io/).

## 1. 📂 Project Heatmap (Risk Analysis)
Find files that are frequently linked to bugs. These are your "high-risk" areas that require more testing.
```cypher
MATCH (f:File)<-[:RELATES_TO_FILE]-(i:Issue)-[:HAS_LABEL]->(l:Label {name: 'type:bug'})
RETURN f.path AS FilePath, count(i) AS BugCount
ORDER BY BugCount DESC
LIMIT 10
```

## 2. 🕵️ Feature Lineage
Trace a specific feature requirement to the exact files that implement it and the issues encountered during development.
```cypher
MATCH (f:File)<-[:RELATES_TO_FILE]-(i:Issue)
WHERE i.title CONTAINS 'Feature Name'  // Replace with your feature
RETURN i.number AS Issue, i.title AS Title, f.path AS AffectedFile
```

## 3. 🚦 Skill Capability Map
See which roles (labels) are managing which parts of the codebase. This helps in understanding "Who owns what?"
```cypher
MATCH (f:File)<-[:RELATES_TO_FILE]-(i:Issue)-[:HAS_LABEL]->(l:Label)
WHERE l.name STARTS WITH 'role:'
RETURN l.name AS Role, f.path AS FilePath, count(i) AS ContributionLevel
ORDER BY ContributionLevel DESC
```

## 4. 🧠 The "Lessons Learned" Path
Find the reasoning body for completed tasks to help the AI implement similar features in the future.
```cypher
MATCH (i:Issue {state: 'closed'})-[:RELATES_TO_FILE]->(f:File)
RETURN i.title AS TaskSummary, i.body AS TechnicalReasoning, f.path AS ReferenceFile
ORDER BY i.number DESC
LIMIT 5
```

## 🧹 Maintenance Query: Clean Up Unlinked Files
Find files that don't have any issue coverage yet (potentially dark code).
```cypher
MATCH (f:File)
WHERE NOT (f)<-[:RELATES_TO_FILE]-(:Issue)
RETURN f.path AS UntrackedFile
```

---
*Query these regularly to improve the AI's "Intuition" about the codebase.*
