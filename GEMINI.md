# GEMINI.md - Brain System Documentation

> **Universal Guide:** This document describes the `.agent/` brain system in an IDE-agnostic way. Use this guide with **any AI-powered IDE** (Cursor, Windsurf, Cline, Aider, etc.) or CLI tools.

---

## 🧠 What is the Brain System?

The **Brain** is the core of Agentic SDLC - an intelligent, self-learning knowledge management system located in the `.agent/` directory. It provides:

1. **3-Layer Architecture** - Root (Brain), Workflow, Execution layers
2. **AI Role System** - 14 specialized agents (PM, SA, Dev, QA, etc.)
3. **Workflow Automation** - 15 predefined workflows accessible via `/slash` commands
4. **Knowledge Base** - Compound learning from every task, bug, and solution
5. **Cross-IDE Compatibility** - Works with any IDE through standard markdown files
6. **Self-Learning Engine** - Automatically improves from project experience

### 3-Layer Architecture (v2.0)
```
┌─────────────────────────────────────────────────────────────┐
│              LAYER 1: ROOT (Brain)                           │
│  Observer │ Judge │ Learner │ A/B Tester │ Model Optimizer  │
│  Self-Improver                                               │
├─────────────────────────────────────────────────────────────┤
│              LAYER 2: WORKFLOW                               │
│  /orchestrator │ /cycle │ /emergency │ /sprint              │
├─────────────────────────────────────────────────────────────┤
│              LAYER 3: EXECUTION                              │
│  @PM │ @BA │ @SA │ @DEV │ @TESTER │ @DEVOPS │ Scripts       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Directory Structure

```
.agent/                          # 🧠 THE BRAIN (Source of Truth)
│
├── workflows/                   # 15 workflow definitions
│   ├── process/                # 6 Process workflows (cycle, sprint, etc.)
│   ├── support/                # 6 Support workflows (brain, route, etc.)
│   └── utilities/              # 3 Utility workflows (validate, metrics)
│
├── skills/                       # 13+ AI skill definitions
│   ├── role-pm.md              # Project Manager
│   ├── role-sa.md              # System Analyst
│   ├── role-dev.md             # Developer
│   ├── role-qa.md              # Quality Assurance
│   ├── role-seca.md            # Security Analyst
│   └── ...
│
├── knowledge-base/              # Compound learning system
│   ├── INDEX.md                # Searchable index
│   ├── bugs/                   # Bug patterns & solutions
│   ├── features/               # Feature implementations
│   ├── architecture/           # Architecture decisions
│   ├── security/               # Security fixes
│   ├── performance/            # Performance optimizations
│   └── ...
│
├── templates/                   # 17+ document templates
│   ├── project-plan.md
│   ├── architecture-spec.md
│   ├── test-report.md
│   └── ...
│
├── rules/                       # Global rules & conventions
│   ├── global.md               # Core SDLC flow
│   ├── artifacts.md            # File naming & organization
│   ├── git-workflow.md         # Git & task management
│   ├── knowledge-base.md       # KB creation rules
│   └── auto-learning.md        # Auto-learning triggers
│
├── ide-integration/             # IDE-specific configs
│   └── [generated per IDE]
│
├── README.md                    # .agent directory overview
├── CONFIG.md                    # Configuration guide
└── USAGE.md                     # Usage instructions
```

---

## 🎯 Core Components

### 1. Workflows (`.agent/workflows/`)

**What:** Step-by-step automation for SDLC tasks
**How to use:** Reference workflows in your IDE or use `/slash` commands

**Key Workflows:**

| Command | Purpose | What It Does |
|---------|---------|--------------|
| `/auto` | Full Automation | Complete SDLC from planning to deployment |
| `/cycle` | Task Lifecycle | Plan → Work → Review → Document |
| `/pm` | Project Management | Requirements gathering & planning |
| `/dev` | Development | Implementation workflow |
| `/qa` | Quality Assurance | Design review & testing strategy |
| `/brain` | Brain Management | Sync knowledge, get recommendations |
| `/kb-search` | Search KB | Find relevant knowledge entries |
| `/explore` | Deep Investigation | Multi-order analysis before planning |
| `/emergency` | Hotfix Response | Critical incidents & production fixes |

**Workflow Structure:**

```markdown
---
description: Brief workflow description
---

# Workflow Title

## Step 1: [Action]
[Detailed instructions]

## Step 2: [Action]
[Detailed instructions]

### Decision Point:
- If [condition] → Go to Step X
- Otherwise → Continue

#workflow-tag #skill-tag
```

### 2. Skills (`.agent/skills/`)

**What:** Specialized AI agent definitions for each SDLC phase
**How to use:** Reference with `@ROLE` mentions in your IDE

**Available Roles:**

```
📋 Planning & Requirements
  ├── @PM          - Project Manager (planning, backlog, reporting)
  └── @BA          - Business Analyst (requirements)

🎨 Design & Architecture
  ├── @SA          - System Analyst (architecture)
  └── @UIUX        - UI/UX Designer (interface design)

✅ Review & Quality
  ├── @SECA        - Security Analyst (security review)
  └── @TESTER      - Quality Assurance & Testing

💻 Development & Operations
  ├── @DEV         - Developer (implementation)
  └── @DEVOPS      - DevOps Engineer (CI/CD, deployment)

🤖 Automation
  └── @ORCHESTRATOR - Workflow orchestrator
```

**Role Definition Structure:**

```markdown
# @ROLE - Role Title

## Identity
[Who this role is, responsibilities]

## Commands
[Available commands and workflows]

## Integration
[How this role works with others]

## Templates Used
[Document templates this role creates]

#role-tag #skills-enabled
```

### 3. Knowledge Base (`.agent/knowledge-base/`)

**What:** Self-learning system that captures and organizes project knowledge
**How it works:** Automatically or manually create entries as you solve problems

**Categories:**

```
knowledge-base/
├── INDEX.md              # Searchable index (auto-generated)
├── bugs/                 # Bug patterns & solutions
│   └── [category]-[slug].md
├── features/             # Feature implementations
│   └── [category]-[slug].md
├── architecture/         # Architecture decisions
│   └── [topic]-[slug].md
├── security/             # Security vulnerabilities & fixes
│   └── [category]-[slug].md
├── performance/          # Performance optimizations
│   └── [optimization]-[slug].md
├── tools/               # Tool usage & integration
│   └── [tool]-[slug].md
└── workflows/           # Custom workflow modifications
    └── [workflow]-[slug].md
```

**Entry Structure (YAML Frontmatter):**

```markdown
---
category: feature-implementation
subcategory: authentication
tags: [jwt, oauth, security]
difficulty: medium
date: 2026-01-03
author: @DEV
related: [security-jwt-best-practices, bugs-jwt-expiration]
sprint: sprint-5
---

# JWT Authentication Implementation

## Problem/Challenge
[What was needed]

## Solution
[How it was solved]

## Implementation
[Code/config details]

## Learnings
[Key takeaways]

## Related Issues
- [Link to issues/PRs]

#feature #authentication #jwt
```

**When to Create KB Entries:**

- ✅ Bug fixed (priority medium+)
- ✅ New feature implemented
- ✅ Architecture decision made
- ✅ Security vulnerability fixed
- ✅ Performance optimization applied
- ✅ Complex problem solved (3+ hours)

### 4. Templates (`.agent/templates/`)

**What:** Standardized document templates for consistency
**How to use:** Roles use templates to create project artifacts

**Available Templates:**

```
Planning & Requirements:
  ├── project-plan.md
  ├── requirements-spec.md
  └── user-stories.md

Design & Architecture:
  ├── architecture-spec.md
  ├── backend-design-spec.md
  ├── uiux-design-spec.md
  └── api-design.md

Quality & Security:
  ├── design-verification-report.md
  ├── security-review-report.md
  └── test-report.md

Development & Delivery:
  ├── implementation-log.md
  ├── deployment-plan.md
  ├── final-report.md
  └── changelog-entry.md

Documentation:
  ├── technical-documentation.md
  └── user-guide.md
```

### 5. Rules (`.agent/rules/`)

**What:** Global conventions that all agents must follow
**Why:** Ensures consistency, quality, and traceability

**Rule Files:**

| File | Purpose |
|------|---------|
| `global.md` | Core SDLC flow, role dependencies, approval gates |
| `artifacts.md` | File naming, folder structure, sprint-based organization |
| `git-workflow.md` | Task tracking, atomic commits, branching strategy |
| `knowledge-base.md` | KB entry creation, YAML metadata, indexing |
| `auto-learning.md` | Automatic knowledge capture triggers |

---

## 🔧 How to Use with Any IDE

### Option 1: Cursor IDE

1. **Install Agentic SDLC:**
   ```bash
   agentic-sdlc install
   agentic-sdlc ide cursor
   ```

2. **Use in Chat:**
   ```
   @pm Build a todo app
   /cycle Implement user authentication
   ```

3. **Access Brain:**
   ```
   /brain
   /kb-search authentication
   ```

### Option 2: Windsurf IDE

1. **Install:**
   ```bash
   agentic-sdlc install
   agentic-sdlc ide windsurf
   ```

2. **Reference in Cascade:**
   - Windsurf automatically reads `.agent/` files
   - Use `@` mentions for roles
   - Use `/` commands for workflows

### Option 3: Cline / Aider / Other IDEs

1. **Install:**
   ```bash
   agentic-sdlc install
   ```

2. **Manual Integration:**
   - Point your IDE to `.agent/workflows/` directory
   - Reference skill files in `.agent/skills/`
   - Use workflows as instruction templates

3. **In Chat:**
   ```
   Read .agent/workflows/pm.md and help me plan a new feature
   Act as @DEV and follow .agent/workflows/dev.md
   ```

### Option 4: CLI / Command Line

```bash
# View workflows
ls .agent/workflows/

# Read a workflow
cat .agent/workflows/pm.md

# Search knowledge base
python bin/kb_cli.py search "authentication"

# Use brain system
python tools/neo4j/brain_parallel.py --recommend "OAuth implementation"
```

---

## 🧠 Brain Intelligence System

The brain consists of **three interconnected layers:**

### Layer 1: LEANN (Vector Search)

**What:** High-performance vector database for semantic search
**Location:** `.leann/` directory (auto-generated)

```bash
# Index project
leann index --path .

# Update index
leann index --update

# Search (used by Research Agent)
leann search "authentication patterns"
```

### Layer 2: Neo4j (Knowledge Graph)

**What:** Graph database mapping skills, technologies, and relationships
**Location:** Cloud-hosted (configured in `.env`)

**Capabilities:**
- Visualize skill relationships
- Find learning paths
- Discover related technologies
- Track team expertise
- Reason about solutions

**Configuration (`.env`):**

```bash
NEO4J_URI=neo4j+s://xxxxx.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-password
NEO4J_DATABASE=neo4j
```

**Usage:**

```bash
# Sync KB to Neo4j
python tools/neo4j/sync_skills_to_neo4j.py

# Sync documents (plans, reports, artifacts)
python tools/neo4j/document_sync.py --all

# Query skills
python tools/neo4j/query_skills_neo4j.py --all-skills

# Get learning path
python tools/neo4j/query_skills_neo4j.py --learning-path "Authentication"
```

### Layer 3: File-based KB

**What:** Human-readable markdown files with YAML metadata
**Location:** `.agent/knowledge-base/`

**Advantages:**
- Git-trackable
- Easily editable
- No database required
- Works offline

### Brain Workflows (Parallel Execution)

**Quick Sync (Recommended):**

```bash
# Sync all brain systems in parallel
python tools/neo4j/brain_parallel.py --sync
```

**Full Operations:**

```bash
# Complete sync (LEANN + Neo4j + Learning Engine)
python tools/neo4j/brain_parallel.py --full

# Get statistics
python tools/neo4j/brain_parallel.py --stats

# Get recommendations
python tools/neo4j/brain_parallel.py --recommend "implement caching"
```

**Self-Learning Commands:**

```bash
# Record error pattern
python tools/neo4j/learning_engine.py --record-error "TypeError" \
  "Cannot read property X of undefined" \
  --resolution "Added null check" \
  --approach "defensive_coding"

# Record success pattern
python tools/neo4j/learning_engine.py --record-success "task-123" \
  --task-type "auth_feature" \
  --success-approach "JWT with refresh tokens"

# Find similar errors
python tools/neo4j/learning_engine.py --similar-errors "ConnectionError"

# Get recommendations
python tools/neo4j/learning_engine.py --recommend \
  "implement user authentication"
```

**Statistics & Insights:**

```bash
# Learning statistics
python tools/neo4j/learning_engine.py --stats

# View learned patterns
python tools/neo4j/learning_engine.py --patterns

# View reasoning paths
python tools/neo4j/learning_engine.py --reasoning-path "TypeError" "null check"
```

---

## 🔄 Self-Learning Triggers

The brain **automatically learns** when these events occur:

| Trigger | What Gets Learned |
|---------|-------------------|
| Bug fixed (medium+ priority) | Error pattern, resolution, similar issues |
| Task required 3+ attempts | Complexity patterns, better approaches |
| Same error occurred 2+ times | Root cause, prevention strategy |
| Complex feature completed (4+ hours) | Implementation approach, best practices |
| Security/performance issue resolved | Vulnerability patterns, optimization techniques |

**How it works:**

1. **Detection** - Agent detects qualifying event
2. **Capture** - Automatically extracts:
   - Problem description
   - Solution approach
   - Code patterns
   - Related technologies
3. **Storage** - Saves to:
   - File-based KB (`.agent/knowledge-base/`)
   - Neo4j graph (relationships)
   - LEANN index (semantic search)
4. **Indexing** - Updates:
   - KB INDEX.md
   - Neo4j relationships
   - LEANN vectors
5. **Future Use** - Available for:
   - Recommendations
   - Similar problem detection
   - Learning path suggestions

---

## 📊 Best Practices

### Daily Workflow

```bash
# Morning: Sync brain
python tools/neo4j/brain_parallel.py --sync

# Before new task: Get recommendations
python tools/neo4j/brain_parallel.py --recommend "your task description"

# During work: Use workflows
/pm plan feature
/dev implement
/qa review

# After work: Check what was learned
python tools/neo4j/learning_engine.py --stats
```

### Weekly Maintenance

```bash
# Full brain sync
python tools/neo4j/brain_parallel.py --full

# Review knowledge base
python bin/kb_cli.py list --recent

# Update KB index
python bin/kb_cli.py update-index

# Check learning patterns
python tools/neo4j/learning_engine.py --patterns
```

### Team Collaboration

```bash
# Share brain via Git
git add .agent/knowledge-base/
git commit -m "docs: add OAuth implementation knowledge"
git push

# Pull team knowledge
git pull

# Re-sync brain
python tools/neo4j/brain_parallel.py --sync
```

---

## 🎨 IDE-Specific Integration

### For Cursor

**Setup:**
```bash
agentic-sdlc ide cursor
```

**Created files:**
- `.cursorrules` - References `.agent/` workflows
- Automatic role recognition with `@` mentions
- `/slash` command integration

**Usage:**
```
@pm Build a REST API
/dev implement authentication
/brain sync and recommend
```

### For Windsurf

**Setup:**
```bash
agentic-sdlc ide windsurf
```

**Created files:**
- `.windsurfrules` - References `.agent/` workflows
- Cascade integration
- Memory persistence

**Usage:**
```
@sa design the architecture
/cycle complete this feature
```

### For Cline

**Setup:**
```bash
agentic-sdlc ide cline
```

**Created files:**
- `.clinerules` - References `.agent/` workflows
- Custom instructions

**Usage:**
```
Read .agent/workflows/dev.md and implement this feature
Act as @QA and review the implementation
```

### For Aider

**Setup:**
```bash
agentic-sdlc ide aider
```

**Created files:**
- `.aider.conf.yml` - References `.agent/` workflows

**Usage:**
```bash
# In terminal
aider --read .agent/workflows/dev.md
aider --message "Act as @DEV and implement authentication"
```

---

## 🔧 Tools & Utilities

All executable tools are located in `tools/` directory:

```
tools/
├── neo4j/                   # Knowledge graph tools
│   ├── brain_parallel.py   # Parallel brain operations
│   ├── learning_engine.py  # Self-learning engine
│   ├── document_sync.py    # Document synchronization
│   └── sync_skills_to_neo4j.py
│
├── research/                # Research agent
│   ├── research_agent.py   # Automated research
│   └── research_mcp.py     # MCP integration
│
├── kb/                      # Knowledge base management
│   ├── kb_manager.py       # KB operations
│   └── update_index.py     # Index generation
│
├── github/                  # GitHub integration
│   └── sync_issues.py      # Issue synchronization
│
└── workflows/               # Workflow automation
    └── [workflow scripts]
```

**See `tools/README.md` for complete tool documentation.**

---

## 💡 Advanced Usage

### Research Agent Integration

The Research Agent automatically queries the brain when researching:

```bash
python tools/research/research_agent.py \
  --task "authentication" \
  --type feature

# Output includes:
# - LEANN semantic search results
# - Neo4j graph relationships
# - File-based KB entries
# - Confidence level
```

### Custom Workflows

Create your own workflows in `.agent/workflows/`:

```markdown
---
description: My Custom Workflow
---

# Custom Workflow

## Step 1: [Action]
[Instructions]

## Step 2: [Action]
[Instructions]

#custom #workflow
```

### Knowledge Base Search

```bash
# CLI search
python bin/kb_cli.py search "authentication"

# In IDE
/kb-search authentication

# Advanced search
python bin/kb_cli.py search "JWT" --category security --tags oauth
```

### Compound Learning

**Concept:** Knowledge from one project benefits all projects in the monorepo.

**How it works:**
1. Project A solves OAuth authentication
2. Knowledge saved to `.agent/knowledge-base/`
3. Project B needs authentication
4. Brain recommends OAuth approach from Project A
5. Project B adapts and improves solution
6. Updated knowledge benefits Projects C, D, E...

```bash
# Trigger compound learning
python tools/neo4j/brain_parallel.py --full

# View cross-project knowledge
python bin/kb_cli.py list --all-projects
```

---

## 🌟 Why This Structure?

### Single Source of Truth

✅ All knowledge in `.agent/`
✅ IDE integrations are just references
✅ Update once, available everywhere

### IDE Agnostic

✅ Works with any IDE
✅ Markdown-based (human-readable)
✅ CLI-accessible
✅ Git-friendly

### Scalable

✅ Add new roles easily
✅ Create custom workflows
✅ Extend knowledge categories
✅ Cross-project learning

### Maintainable

✅ Clear structure
✅ YAML metadata for automation
✅ Version-controllable
✅ Documentable

---

## 🚀 Quick Reference

### Most Used Commands

```bash
# Brain sync
python tools/neo4j/brain_parallel.py --sync

# Get recommendations
python tools/neo4j/brain_parallel.py --recommend "task description"

# Search KB
python bin/kb_cli.py search "query"

# View stats
python tools/neo4j/brain_parallel.py --stats
```

### Most Used Workflows

```
/auto      - Full automation
/pm        - Project planning
/dev       - Development
/qa        - Quality review
/brain     - Brain management
/kb-search - Search knowledge
```

### Most Used Roles

```
@PM    - Planning
@SA    - Architecture
@DEV   - Implementation
@QA    - Review
@SECA  - Security
```

---

## 📚 Additional Resources

- **Project Documentation:** [docs/](docs/)
- **Tools README:** [tools/README.md](tools/README.md)
- **Monorepo Architecture:** [docs/MONOREPO-ARCHITECTURE.md](docs/MONOREPO-ARCHITECTURE.md)
- **Quick Start Guide:** [docs/guides/QUICK-START.md](docs/guides/QUICK-START.md)
- **MCP Setup:** [docs/guides/MCP-SETUP.md](docs/guides/MCP-SETUP.md)

---

## ❓ FAQ

**Q: Can I use this without Neo4j?**
A: Yes! The file-based KB and LEANN work independently. Neo4j adds graph intelligence but is optional.

**Q: Does this work offline?**
A: Partially. File-based KB and LEANN work offline. Neo4j requires internet connection.

**Q: Can I customize workflows?**
A: Absolutely! Add your own workflows to `.agent/workflows/` following the existing format.

**Q: How do I share knowledge with my team?**
A: Commit `.agent/knowledge-base/` to Git. Team members sync brain after pulling.

**Q: What if my IDE isn't supported?**
A: All IDEs can reference `.agent/` files. Create custom integration or use CLI tools.

**Q: How do I migrate from another system?**
A: Run `agentic-sdlc install` in your project. It preserves existing code and adds the brain system.

---

**Version:** 2.0.0
**Last Updated:** 2026-01-03
**Philosophy:** IDE-agnostic, compound learning, single source of truth

**Next:** Read [Quick Start Guide](docs/guides/QUICK-START.md) or explore [workflows](.agent/workflows/)
