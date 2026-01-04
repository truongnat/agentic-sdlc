# Workflow Decision Tree

> **Logic for selecting the correct Agentic SDLC workflow.**

**Last Updated:** 2026-01-03

## 🌳 Interactive Decision Path

Start at **Node 1** and follow the usage patterns.

### 1. Is this a production emergency?
- **YES** (System down, critical bug) → [`/emergency`](process/emergency.md)
- **NO** → Go to **2**

### 2. Is this a full project or major feature?
- **YES** (Requires planning, design, dev, test) → [`/orchestrator`](process/orchestrator.md)
- **NO** → Go to **3**

### 3. Is this a single, well-defined task?
- **YES** (e.g. "Add login button") → [`/cycle`](process/cycle.md)
- **NO** → Go to **4**

### 4. Are you performing a specific role's duty?
- **Project Manager** (Planning, Reporting) → [`/pm`](../skills/role-pm.md)
- **Business Analyst** (Requirements) → [`/ba`](../skills/role-ba.md)
- **System Analyst** (Architecture) → [`/sa`](../skills/role-sa.md)
- **UI/UX Designer** (Design) → [`/uiux`](../skills/role-uiux.md)
- **Developer** (Code) → [`/dev`](../skills/role-dev.md)
- **Tester** (QA) → [`/tester`](../skills/role-tester.md)
- **Security** (Audit) → [`/seca`](../skills/role-seca.md)
- **DevOps** (Deploy) → [`/devops`](../skills/role-devops.md)
- **NO** → Go to **5**

### 5. Are you performing maintenance or support?
- **Brain Sync** (Update AI memory) → [`/brain`](support/brain.md)
- **Knowledge Capture** (After task) → [`/compound`](support/compound.md)
- **Cleanup** (Files/Folders) → [`/housekeeping`](support/housekeeping.md)
- **Validation** (Check sanity) → [`/validate`](utilities/validate.md)
- **Metrics** (Check stats) → [`/metrics`](utilities/metrics.md)
- **Release** (Versioning) → [`/release`](support/release.md)
- **NO** → Go to **6**

### 6. Do you need to investigate or decide?
- **Deep Analysis** → [`/explore`](process/explore.md)
- **Routing Help** → [`/route`](support/route.md)

---

## 📊 Visual Matrix

| Objective | High Urgency | Normal Urgency | Low Urgency |
|-----------|--------------|----------------|-------------|
| **Fix Bug** | `/emergency` | `/dev` | `/cycle` |
| **New Feature** | - | `/orchestrator` | `/cycle` |
| **Question** | - | `/explore` | `/brain` |
| **Maintenance** | - | `/housekeeping` | `/validate` |

---

## 🔄 Lifecycle Hooks

Workflows often call each other. Here is the standard flow:

1. **Planning:** `/pm` → `/ba` → `/sa`
2. **Execution:** `/dev` ↔ `/tester`
3. **Closure:** `/devops` → `/compound` → `/brain`

## Tags

`#decision-tree` `#guide` `#workflows`
