# CLI Usage Examples

Complete guide with examples for `agentic-sdlc` CLI tool.

---

## 📦 Installation

```bash
# Install globally
npm install -g agentic-sdlc

# Or use with npx (no installation needed)
npx agentic-sdlc <command>
```

---

## 🚀 Quick Start

### 1. Create New Project (Recommended)

```bash
# Create a new project with everything set up
agentic-sdlc create my-awesome-project

# Navigate to project
cd my-awesome-project

# Setup IDE integration
agentic-sdlc ide cursor

# Start building
# Open IDE and type: /pm Build a todo app
```

**Output:**
```
🚀 Creating Project: my-awesome-project

→ Creating project directory...
→ Installing instructions...
→ Setting up project structure...
✓ Project created successfully!

Location: /path/to/my-awesome-project

Next Steps:
  cd my-awesome-project
  agentic-sdlc ide cursor
  • Review .agent/usage.md
  • Initialize git repository
  • Start: /pm Build your project

ℹ Completed in 0.85s
```

---

### 2. Install in Existing Project

```bash
# Navigate to your existing project
cd my-existing-project

# Install instructions
agentic-sdlc install

# Setup IDE
agentic-sdlc ide cursor
```

**Output:**
```
🚀 Installing Template Instructions

→ Validating environment...
→ Checking for existing installation...
→ Copying template files...
✓ Installation complete!

Location: /path/to/my-existing-project/.agent

Next Steps:
  • Setup IDE: agentic-sdlc ide cursor
  • Review: .agent/usage.md
  • Start: /pm Build your project

ℹ Completed in 0.42s
```

---

## 🔧 IDE Integration

### Setup Single IDE

```bash
# Cursor IDE
agentic-sdlc ide cursor

# GitHub Copilot
agentic-sdlc ide copilot

# Windsurf Cascade
agentic-sdlc ide windsurf

# Cline Extension
agentic-sdlc ide cline

# Aider CLI
agentic-sdlc ide aider
```

**Example Output (Cursor):**
```
🔧 Setting up CURSOR Integration

→ Installing Cursor IDE...
✓ Cursor IDE installed

Location: /path/to/project/.cursorrules

Next Steps:
  • Restart Cursor IDE
  • Type / in chat to see commands
  • Try: /pm Build a todo app

ℹ Completed in 0.15s
```

---

### Setup All IDEs at Once

```bash
agentic-sdlc ide all
```

**Output:**
```
🔧 Setting up ALL Integration

→ Installing Cursor IDE...
✓ Cursor IDE installed
→ Installing GitHub Copilot...
✓ GitHub Copilot installed
→ Installing Windsurf Cascade...
✓ Windsurf Cascade installed
→ Installing Cline Extension...
✓ Cline Extension installed
→ Installing Aider CLI...
✓ Aider CLI installed
✓ All IDE integrations installed!

Next Steps:
  • Restart your IDE
  • Type / in chat to see available commands
  • Try: /pm Build a todo app

ℹ Completed in 0.68s
```

---

## 🧠 Knowledge Base

### Initialize Knowledge Base

```bash
agentic-sdlc init-kb
```

**Output:**
```
🧠 Initializing Knowledge Base

→ Creating directory structure...
✓ Knowledge base initialized!

Location: /path/to/project/.agent/knowledge-base

Next Steps:
  • Read: .agent/knowledge-base/README.md
  • Use template: Knowledge-Entry-Template.md
  • Search: Check index.md

ℹ Completed in 0.23s
```

---

## 📋 List Available Resources

```bash
agentic-sdlc list
```

**Output:**
```
📋 Available Templates & Roles

Roles (12):
  • orchestrator
  • pm
  • po
  • sa
  • designer
  • qa
  • seca
  • dev
  • devops
  • tester
  • reporter
  • stakeholder

Templates (16):
  • Project-Plan-Template
  • Product-Backlog-Template
  • System-Design-Spec-Template
  • UIUX-Design-Spec-Template
  • Design-Verification-Report-Template
  • Security-Review-Report-Template
  • Development-Log-Template
  • DevOps-Plan-Template
  • Test-Report-Template
  • Phase-Report-Template
  • Master-Documentation-Template
  • Final-Project-Report-Template
  • Final-Approval-Report-Template
  • Knowledge-Entry-Template
  • definition-of-done
  • incident-response

Total: 12 roles, 16 templates
```

---

## 🎯 Real-World Workflows

### Workflow 1: Start Fresh Project

```bash
# Step 1: Create project
agentic-sdlc create wedding-website
cd wedding-website

# Step 2: Setup IDE
agentic-sdlc ide cursor

# Step 3: Initialize git
git init
git add .
git commit -m "Initial commit with TeamLifecycle"

# Step 4: Start building (in IDE)
# Type: /pm Build a wedding website with photo gallery and RSVP form
```

---

### Workflow 2: Add to Existing Project

```bash
# Step 1: Navigate to project
cd my-existing-app

# Step 2: Install instructions
agentic-sdlc install

# Step 3: Setup IDE (all at once)
agentic-sdlc ide all

# Step 4: Initialize knowledge base
agentic-sdlc init-kb

# Step 5: Commit changes
git add .
git commit -m "Add TeamLifecycle SDLC system"

# Step 6: Start using (in IDE)
# Type: /pm Review and improve current architecture
```

---

### Workflow 3: Team Setup

```bash
# Team lead sets up template
agentic-sdlc create team-project
cd team-project

# Setup all IDE integrations for team
agentic-sdlc ide all

# Initialize knowledge base for shared learning
agentic-sdlc init-kb

# Commit to repo
git init
git add .
git commit -m "Setup TeamLifecycle for team"
git remote add origin <repo-url>
git push -u origin main

# Team members clone and start
# git clone <repo-url>
# cd team-project
# Open IDE and type: /pm [their task]
```

---

## 🔄 Options & Flags

### Force Overwrite

```bash
# Overwrite existing installation
agentic-sdlc install --force

# Overwrite existing project
agentic-sdlc create my-project --force

# Overwrite IDE config
agentic-sdlc ide cursor --force
```

---

### Quiet Mode

```bash
# Minimal output
agentic-sdlc install --quiet

# Useful for scripts
agentic-sdlc ide all -q
```

---

### Verbose Mode

```bash
# Detailed output with file counts
agentic-sdlc install --verbose

# See all operations
agentic-sdlc create my-project --verbose
```

---

### Combined Options

```bash
# Force + Verbose
agentic-sdlc install -f --verbose

# Quiet + Force (for automation)
agentic-sdlc ide all -q -f
```

---

## 📚 Help & Version

### Show Help

```bash
agentic-sdlc --help
agentic-sdlc -h
agentic-sdlc help
```

---

### Show Version

```bash
agentic-sdlc --version
agentic-sdlc -v
agentic-sdlc version
```

**Output:**
```
agentic-sdlc v1.1.4
Simulating a complete Software Development Lifecycle (SDLC) with specialized AI Agents.
```

---

## 🎨 Using Slash Commands (After Setup)

### In Cursor / Copilot / Windsurf

```bash
# Start new project
/pm Build a REST API for task management with authentication

# Full automation
/auto Create a mobile fitness tracking app for iOS and Android

# Specific roles
/sa Design database schema for e-commerce platform
/uiux Create mobile-first dashboard with dark mode
/dev Implement OAuth2 authentication flow
/devops Setup CI/CD pipeline with GitHub Actions
/tester Run E2E tests for checkout flow

# Knowledge base
/kb-search React hydration error
/kb-add Solution for Next.js caching issue
```

---

## 🐛 Troubleshooting

### Command Not Found

```bash
# If installed globally but not found
npm install -g agentic-sdlc

# Or use npx
npx agentic-sdlc install
```

---

### Permission Denied

```bash
# On Unix/Mac, use sudo for global install
sudo npm install -g agentic-sdlc

# Or install without sudo using nvm
nvm use node
npm install -g agentic-sdlc
```

---

### Already Exists Error

```bash
# Use --force to overwrite
agentic-sdlc install --force
agentic-sdlc create my-project --force
```

---

### IDE Commands Not Working

```bash
# Re-run IDE setup
agentic-sdlc ide cursor --force

# Restart your IDE after setup

# Check file was created
ls -la .cursorrules  # For Cursor
ls -la .github/copilot-instructions.md  # For Copilot
```

---

## 📊 Project Structure After Setup

```
my-project/
├── .agent/
│   └── instructions/
│       ├── global.md
│       ├── usage.md
│       ├── roles/              # 12 role definitions
│       ├── templates/          # 16 templates
│       ├── knowledge-base/     # Knowledge base system
│       └── ide-integration/    # IDE configs
├── docs/
│   ├── sprints/
│   │   └── sprint-1/
│   │       ├── plans/
│   │       ├── designs/
│   │       ├── reviews/
│   │       ├── logs/
│   │       ├── tests/
│   │       └── reports/
│   └── global/
│       └── reports/
├── .cursorrules                # Cursor IDE config
├── .github/
│   └── copilot-instructions.md # Copilot config
├── .gitignore
├── package.json
└── README.md
```

---

## 🎓 Learning Path

### Day 1: Setup
```bash
agentic-sdlc create learning-project
cd learning-project
agentic-sdlc ide cursor
# Read: .agent/usage.md
```

### Day 2: First Project
```bash
# In IDE: /pm Build a simple todo app
# Follow the workflow, approve plans
# Let orchestrator handle the rest
```

### Day 3: Manual Control
```bash
# In IDE: /pm Build a blog platform --mode=manual
# Tag each role manually to learn the flow
# /sa, /uiux, /qa, /dev, etc.
```

### Day 4: Knowledge Base
```bash
agentic-sdlc init-kb
# Document learnings as you encounter challenges
# /kb-add [topic] when you solve difficult problems
```

### Day 5: Team Collaboration
```bash
# Share project with team
# Everyone uses same slash commands
# Knowledge base grows with team experience
```

---

## 💡 Pro Tips

### 1. Use Aliases
```bash
# Add to ~/.bashrc or ~/.zshrc
alias ci='agentic-sdlc'
alias ci-new='agentic-sdlc create'
alias ci-ide='agentic-sdlc ide'

# Usage
ci install
ci-new my-project
ci-ide cursor
```

---

### 2. Project Templates
```bash
# Create your own project template
agentic-sdlc create template-project
cd template-project
# Customize .agent/
# Use as base for future projects
```

---

### 3. Automation Scripts
```bash
#!/bin/bash
# setup-new-project.sh

PROJECT_NAME=$1

agentic-sdlc create $PROJECT_NAME
cd $PROJECT_NAME
agentic-sdlc ide all
agentic-sdlc init-kb
git init
git add .
git commit -m "Initial setup with TeamLifecycle"

echo "✓ Project $PROJECT_NAME ready!"
```

---

### 4. CI/CD Integration
```yaml
# .github/workflows/setup.yml
name: Setup TeamLifecycle
on: [push]
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install -g agentic-sdlc
      - run: agentic-sdlc install --quiet
      - run: agentic-sdlc ide all --quiet
```

---

## 📞 Support

- **Documentation:** `.agent/usage.md`
- **Issues:** https://github.com/yourusername/agentic-sdlc/issues
- **Examples:** This file!

---

## 🎉 Success Stories

### Example 1: Solo Developer
```bash
agentic-sdlc create saas-platform
cd saas-platform
agentic-sdlc ide cursor
# Used /auto mode, completed MVP in 2 days
```

### Example 2: Team of 5
```bash
agentic-sdlc create team-app
agentic-sdlc ide all
agentic-sdlc init-kb
# Shared knowledge base, consistent workflow
# Reduced onboarding time by 70%
```

### Example 3: Open Source Project
```bash
agentic-sdlc install
agentic-sdlc ide copilot
# Contributors use same workflow
# Consistent documentation and quality
```

---

**Happy Building! 🚀**
