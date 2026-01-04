# Agentic SDLC

> Transform your IDE into a complete Software Development Lifecycle team with AI-powered agents, automated workflows, and intelligent knowledge management.

## 🎯 What is Agentic SDLC?

**Agentic SDLC** is an AI-powered development framework that simulates a complete software development team within your IDE. It provides:

- **14 Specialized AI Roles** - PM, BA, SA, UI/UX, QA, Security, Dev, DevOps, Tester, Reporter, and more
- **12 Automated Workflows** - From planning to deployment with `/slash` commands
- **Intelligent Brain System** - 3-Layer architecture with state management and self-learning
- **Cross-IDE Compatibility** - Works with Cursor, Windsurf, Cline, Aider, Gemini, and any AI-powered IDE
- **Monorepo Architecture** - Shared brain system across multiple projects

## 🧠 The Brain System

At the core of Agentic SDLC is the **Brain** - an intelligent knowledge management system that:

- **Learns from every task** - Automatically captures patterns from bugs, features, and solutions
- **Provides recommendations** - Suggests approaches based on past successes
- **Builds knowledge graphs** - Maps relationships between skills, technologies, and solutions
- **Enables compound intelligence** - Each project's knowledge benefits all others

→ See **[GEMINI.md](GEMINI.md)** for complete Brain documentation

## ✨ Quick Start

### Installation

```bash
# Install globally
npm install -g agentic-sdlc

# Or with bun
bun install -g agentic-sdlc
```

### Create New Project

```bash
# Create project with brain system
agentic-sdlc create my-project
cd my-project

# Setup your IDE
agentic-sdlc ide cursor  # or windsurf, cline, etc.

# Start building
/pm Build a todo app with authentication
```

### Add to Existing Project

```bash
# Install brain system in current directory
agentic-sdlc install

# Setup IDE integration
agentic-sdlc ide cursor

# Initialize knowledge base
agentic-sdlc init-kb
```

## 🚀 Core Features

### 1. AI Role System (14 Roles)

Specialized AI agents for every SDLC phase:

```
Planning    → @PM, @BA, @PO
Design      → @SA, @UIUX
Review      → @QA, @SECA
Development → @DEV, @DEVOPS
Testing     → @TESTER
Delivery    → @REPORTER, @STAKEHOLDER
Meta        → @BRAIN, @ORCHESTRATOR
```

### 2. Slash Commands (12 Workflows)

Execute complete workflows with simple commands:

```bash
/brain           # Brain system management (sync, stats)
/cycle           # Complete task lifecycle
/explore         # Deep investigation
/orchestrator    # Full SDLC automation
/sprint          # Sprint management
/validate        # System validation
/metrics         # View metrics dashboard
/release         # Release management
/emergency       # Critical incident response
/route           # Intelligent workflow routing
/compound        # Knowledge capture
/housekeeping    # Cleanup & maintenance
```

### 3. Monorepo Architecture

```
agentic-sdlc/              # 🧠 Brain (Root)
├── .agent/                # AI workflows, skills, KB
├── tools/                 # Neo4j, research, utilities
├── docs/                  # Documentation
└── projects/              # Your projects
    ├── project-1/
    ├── project-2/
    └── [add-yours]/
```

**Benefits:**
- ✅ Shared brain across all projects
- ✅ Compound learning from every solution
- ✅ Consistent workflows and quality
- ✅ Centralized knowledge management

### 4. Knowledge Management

**Automated Learning:**
- Records error patterns and solutions
- Captures successful implementation approaches
- Builds skill and technology graphs
- Provides context-aware recommendations

**Three-Layer System:**
1. **LEANN** - Vector-based semantic search
2. **Neo4j** - Knowledge graph with relationships
3. **File-based KB** - Categorized markdown entries

## 📖 Documentation

### Getting Started
- **[GEMINI.md](GEMINI.md)** - Complete brain system guide (IDE-agnostic)
- **[Quick Start](docs/guides/QUICK-START.md)** - 5-minute setup guide
- **[CLI Examples](docs/guides/CLI-EXAMPLES.md)** - Command usage examples

### Architecture
- **[Monorepo Architecture](docs/MONOREPO-ARCHITECTURE.md)** - System design
- **[Project Structure](PROJECT-STRUCTURE.md)** - Directory organization
- **[Documentation Index](docs/PROJECT-DOCUMENTATION-INDEX.md)** - All docs

### Tools & Setup
- **[Neo4j Tools](tools/neo4j/README.md)** - Knowledge graph system
- **[Research Agent](tools/research/README.md)** - Automated research
- **[MCP Setup](docs/guides/MCP-SETUP.md)** - Model Context Protocol

## 🎯 Use Cases

### Solo Developer
```bash
/auto Create a SaaS platform with authentication and billing
# Complete automation from planning to deployment
```

### Team Development
```bash
# Each team member uses the same brain
agentic-sdlc ide all
git pull  # Share knowledge base
/pm Start Sprint 3
```

### Existing Large Project
```bash
agentic-sdlc install
/brain  # Index and analyze codebase
/pm Migrate authentication to OAuth2
```

## 🔧 Available Commands

```bash
# Project Management
agentic-sdlc create <name>      # Create new project
agentic-sdlc install            # Add to existing project

# IDE Integration
agentic-sdlc ide cursor         # Setup Cursor IDE
agentic-sdlc ide all            # Setup all supported IDEs

# Knowledge Base
agentic-sdlc init-kb            # Initialize KB
agentic-sdlc list               # List roles & workflows

# Brain System (see GEMINI.md)
python tools/neo4j/brain_parallel.py --sync      # Sync brain
python tools/neo4j/brain_parallel.py --recommend  # Get recommendations
```

## 🌟 Why Agentic SDLC?

| Traditional Development | With Agentic SDLC |
|------------------------|-------------------|
| Manual planning | Automated with @PM |
| Ad-hoc architecture | Structured with @SA, @UIUX |
| Inconsistent code quality | Enforced by @QA, @SECA |
| Lost knowledge | Compound learning brain |
| Repetitive tasks | Automated with @AUTO |
| Solo problem-solving | 13+ AI experts available |

## 🔗 Links

- **Repository:** https://github.com/truongnat/agentic-sdlc
- **NPM Package:** https://www.npmjs.com/package/agentic-sdlc
- **Issues:** https://github.com/truongnat/agentic-sdlc/issues
- **Documentation:** [docs/](docs/)

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

---

**Next Steps:**
1. Read [GEMINI.md](GEMINI.md) to understand the brain system
2. Follow [Quick Start](docs/guides/QUICK-START.md) to get started
3. Explore [workflows](.agent/workflows/) to see available automations

**Questions?** Check the [documentation](docs/) or [open an issue](https://github.com/truongnat/agentic-sdlc/issues).
