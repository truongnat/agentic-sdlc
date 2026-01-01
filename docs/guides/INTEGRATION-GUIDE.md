# Integration Guide - Add to Existing Projects

Complete guide to integrate TeamLifecycle SDLC into your existing projects.

---

## ✅ Yes, You Can Integrate!

TeamLifecycle works perfectly with existing projects. You can add it to:
- ✅ Existing codebases (any language/framework)
- ✅ Legacy projects
- ✅ Open source projects
- ✅ Team projects
- ✅ Monorepos
- ✅ Microservices

---

## 🚀 Quick Integration (3 Steps)

### Step 1: Navigate to Your Project

```bash
cd /path/to/your-existing-project
```

### Step 2: Install Instructions

```bash
agentic-sdlc install
```

**Output:**
```
🚀 Installing Template Instructions

→ Validating environment...
→ Checking for existing installation...
→ Copying template files...
✓ Installation complete!

Location: /path/to/your-project/.agent

Next Steps:
  • Setup IDE: agentic-sdlc ide cursor
  • Review: .agent/usage.md
  • Start: /pm Build your project
```

### Step 3: Setup IDE

```bash
agentic-sdlc ide cursor
# or
agentic-sdlc ide all
```

**That's it!** You can now use `/pm`, `/dev`, `/auto` commands in your IDE.

---

## 📁 What Gets Added to Your Project

```
your-existing-project/
├── .agent                    # NEW - Instructions folder
│   └── instructions/
│       ├── roles/              # 12 AI roles
│       ├── templates/          # 16 templates
│       ├── knowledge-base/     # Learning system
│       └── ide-integration/    # IDE configs
├── .cursorrules                # NEW - Cursor config (if setup)
├── .github/
│   └── copilot-instructions.md # NEW - Copilot config (if setup)
├── docs/                       # NEW - Documentation (created on use)
│   ├── sprints/
│   └── global/
├── src/                        # EXISTING - Your code (untouched)
├── package.json                # EXISTING - Your config (untouched)
└── ...                         # EXISTING - Everything else (untouched)
```

**Important:** Your existing code is **NOT modified**. Only new files are added.

---

## 🎯 Integration Scenarios

### Scenario 1: Solo Developer - Existing Side Project

```bash
# You have a personal project
cd ~/projects/my-blog

# Add TeamLifecycle
agentic-sdlc install
agentic-sdlc ide cursor

# Start improving
# In IDE: /pm Review current architecture and suggest improvements
# In IDE: /dev Refactor authentication module
# In IDE: /tester Add E2E tests for blog posts
```

---

### Scenario 2: Team Project - Add to Existing Repo

```bash
# Clone team repo
git clone https://github.com/team/project.git
cd project

# Add TeamLifecycle
agentic-sdlc install
agentic-sdlc ide all
agentic-sdlc init-kb

# Commit changes
git add .agent .cursorrules .github/copilot-instructions.md
git commit -m "Add TeamLifecycle SDLC system"
git push

# Team members pull and start using
# git pull
# Open IDE and use /pm, /dev, etc.
```

---

### Scenario 3: Legacy Project - Modernization

```bash
# Old project needs refactoring
cd ~/old-projects/legacy-app

# Add TeamLifecycle
agentic-sdlc install
agentic-sdlc ide cursor
agentic-sdlc init-kb

# Start modernization
# In IDE: /pm Analyze current codebase and create modernization plan
# In IDE: /sa Design new architecture for microservices migration
# In IDE: /dev Refactor module X to use modern patterns
```

---

### Scenario 4: Open Source Project

```bash
# Your open source project
cd ~/oss/my-library

# Add TeamLifecycle
agentic-sdlc install
agentic-sdlc ide copilot

# Add to .gitignore (optional - keep instructions private)
echo ".agent" >> .gitignore

# Or commit for contributors
git add .agent .github/copilot-instructions.md
git commit -m "Add AI-powered SDLC workflow"

# Contributors can now use consistent workflow
```

---

### Scenario 5: Monorepo

```bash
# Monorepo structure
cd ~/projects/monorepo

# Install at root
agentic-sdlc install
agentic-sdlc ide all

# Or install per package
cd packages/frontend
agentic-sdlc install
cd ../backend
agentic-sdlc install

# Use from anywhere in monorepo
# In IDE: /pm Review frontend architecture
# In IDE: /dev Implement new API endpoint in backend
```

---

## 🔧 Advanced Integration

### Option 1: Selective Installation

```bash
# Install only what you need
cd your-project

# Install instructions
agentic-sdlc install

# Setup only specific IDE
agentic-sdlc ide cursor

# Skip knowledge base (add later if needed)
# agentic-sdlc init-kb
```

---

### Option 2: Custom Configuration

```bash
# Install
agentic-sdlc install

# Customize roles
nano .agent/roles/dev.md

# Customize templates
nano .agent/templates/Development-Log-Template.md

# Commit customizations
git add .agent
git commit -m "Customize TeamLifecycle for our workflow"
```

---

### Option 3: Gradual Adoption

```bash
# Week 1: Install and learn
agentic-sdlc install
agentic-sdlc ide cursor
# Use for documentation only: /reporter, /pm

# Week 2: Add development
# Use for coding: /dev, /sa

# Week 3: Add testing
agentic-sdlc init-kb
# Use for testing: /tester, /qa

# Week 4: Full workflow
# Use automation: /auto
```

---

## 🔄 Integration with Existing Tools

### Git Integration

```bash
# Add to .gitignore (if you want to keep instructions private)
echo ".agent" >> .gitignore
echo ".cursorrules" >> .gitignore

# Or commit (recommended for teams)
git add .agent .cursorrules .github/copilot-instructions.md
git commit -m "Add TeamLifecycle SDLC"
```

---

### CI/CD Integration

```yaml
# .github/workflows/teamlifecycle.yml
name: TeamLifecycle Integration

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install TeamLifecycle
        run: |
          npm install -g agentic-sdlc
          agentic-sdlc install --quiet
      
      - name: Validate Documentation
        run: |
          # Check if docs exist
          test -d docs/sprints || echo "No sprints yet"
      
      - name: Run Tests
        run: npm test
```

---

### Docker Integration

```dockerfile
# Dockerfile
FROM node:20-alpine

WORKDIR /app

# Copy project files
COPY package*.json ./
RUN npm ci

# Install TeamLifecycle (optional - for development)
RUN npm install -g agentic-sdlc

COPY . .

# Your existing build steps
RUN npm run build

CMD ["npm", "start"]
```

---

### VS Code Workspace

```json
// .vscode/settings.json
{
  "files.associations": {
    ".cursorrules": "markdown",
    ".agent**/*.md": "markdown"
  },
  "files.exclude": {
    ".agent/knowledge-base/bugs/**": false
  },
  "search.exclude": {
    ".agent/ide-integration/**": true
  }
}
```

---

## 📊 Before & After Comparison

### Before Integration

```
your-project/
├── src/
├── tests/
├── package.json
└── README.md

# Development process:
1. Write code
2. Manual testing
3. Hope for the best
4. Fix bugs later
```

### After Integration

```
your-project/
├── .agent/    # NEW - AI-powered SDLC
├── docs/sprints/            # NEW - Organized documentation
├── src/                     # EXISTING - Your code
├── tests/                   # EXISTING - Your tests
├── package.json             # EXISTING
└── README.md                # EXISTING

# Development process:
1. /pm Plan feature
2. /sa Design architecture
3. /dev Implement with guidance
4. /tester Automated testing
5. /reporter Documentation
6. Knowledge base learns
```

---

## 🎓 Learning Path for Existing Projects

### Day 1: Installation & Exploration
```bash
cd your-project
agentic-sdlc install
agentic-sdlc ide cursor

# Explore
cat .agent/usage.md
cat .agent/global.md

# Try simple command
# In IDE: /pm Analyze current project structure
```

---

### Day 2: Documentation
```bash
# Generate documentation for existing code
# In IDE: /reporter Create documentation for current codebase
# In IDE: /sa Document current architecture
```

---

### Day 3: Code Review
```bash
# Review existing code
# In IDE: /qa Review code quality in src/
# In IDE: /seca Security audit of authentication module
```

---

### Day 4: Improvements
```bash
# Start making improvements
# In IDE: /dev Refactor user service
# In IDE: /tester Add unit tests for utils
```

---

### Day 5: Knowledge Base
```bash
agentic-sdlc init-kb

# Document existing issues
# In IDE: /kb-add Solution for database connection pooling issue
# In IDE: /kb-add React state management pattern we use
```

---

## ⚠️ Common Issues & Solutions

### Issue 1: .agent Already Exists

```bash
# If you have existing .agent folder
agentic-sdlc install --force

# Or backup first
mv .agent .agent.backup
agentic-sdlc install
```

---

### Issue 2: Conflicts with Existing IDE Config

```bash
# Backup existing config
cp .cursorrules .cursorrules.backup

# Install
agentic-sdlc ide cursor --force

# Merge if needed
cat .cursorrules.backup >> .cursorrules
```

---

### Issue 3: Large Existing Codebase

```bash
# Install normally
agentic-sdlc install

# Use gradually
# Start with documentation: /reporter, /pm
# Then add development: /dev
# Finally add testing: /tester

# Don't try to refactor everything at once
```

---

### Issue 4: Team Resistance

```bash
# Install for yourself first
agentic-sdlc install
agentic-sdlc ide cursor

# Show results to team
# Generate impressive documentation
# Demonstrate faster development

# Then roll out to team
git add .agent
git commit -m "Add optional AI-powered SDLC tools"
```

---

## 🔒 Security Considerations

### Private Projects

```bash
# Keep instructions private
echo ".agent" >> .gitignore
echo ".cursorrules" >> .gitignore
echo ".github/copilot-instructions.md" >> .gitignore

# Install locally only
agentic-sdlc install
```

---

### Public Projects

```bash
# Safe to commit (no secrets)
git add .agent .cursorrules .github/copilot-instructions.md
git commit -m "Add TeamLifecycle SDLC"

# Instructions contain no sensitive data
# Only workflow definitions and templates
```

---

### Sensitive Data

```bash
# Never commit sensitive data to knowledge base
# Add to .gitignore
echo ".agent/knowledge-base/bugs/critical/*" >> .gitignore

# Or use separate private repo for knowledge base
```

---

## 📈 Measuring Success

### Before Integration
- Manual documentation
- Inconsistent code quality
- No structured workflow
- Knowledge in developers' heads

### After Integration (1 month)
- ✅ Automated documentation generation
- ✅ Consistent code reviews
- ✅ Structured SDLC workflow
- ✅ Knowledge base with 20+ entries
- ✅ 50% faster onboarding
- ✅ 30% fewer bugs

---

## 🎯 Best Practices

### 1. Start Small
```bash
# Don't refactor everything at once
# Start with new features
# In IDE: /pm Plan new feature X
# In IDE: /dev Implement feature X
```

---

### 2. Document Existing Code
```bash
# Before making changes, document what exists
# In IDE: /sa Document current architecture
# In IDE: /reporter Create API documentation
```

---

### 3. Build Knowledge Base
```bash
agentic-sdlc init-kb

# Document existing patterns
# In IDE: /kb-add Our authentication pattern
# In IDE: /kb-add Database migration strategy
```

---

### 4. Team Training
```bash
# Create team guide
# In IDE: /reporter Create onboarding guide for TeamLifecycle

# Share examples
# In IDE: /pm Example: How to add new feature
```

---

### 5. Gradual Rollout
```bash
# Week 1: You only
# Week 2: Your team
# Week 3: Other teams
# Week 4: Whole organization
```

---

## 🚀 Success Stories

### Example 1: E-commerce Platform (5 years old)
```bash
cd ecommerce-platform
agentic-sdlc install
agentic-sdlc ide all
agentic-sdlc init-kb

# Results after 2 months:
# - Documented entire legacy codebase
# - Refactored 3 major modules
# - Added 500+ tests
# - Knowledge base: 45 entries
# - Team velocity: +40%
```

---

### Example 2: Startup MVP (6 months old)
```bash
cd startup-mvp
agentic-sdlc install
agentic-sdlc ide cursor

# Results after 2 weeks:
# - Proper documentation
# - Security audit completed
# - Technical debt documented
# - Investor-ready documentation
```

---

### Example 3: Open Source Library (3 years old)
```bash
cd oss-library
agentic-sdlc install
agentic-sdlc ide copilot

# Results after 1 month:
# - Contributors use consistent workflow
# - Documentation always up-to-date
# - Code quality improved
# - 10 new contributors onboarded easily
```

---

## 📞 Support

### Questions?
- Read: `.agent/usage.md`
- Examples: `CLI-EXAMPLES.md`
- Issues: https://github.com/yourusername/agentic-sdlc/issues

### Need Help?
```bash
# Check installation
agentic-sdlc list

# Reinstall if needed
agentic-sdlc install --force

# Setup IDE again
agentic-sdlc ide cursor --force
```

---

## ✅ Integration Checklist

- [ ] Navigate to existing project
- [ ] Run `agentic-sdlc install`
- [ ] Run `agentic-sdlc ide <your-ide>`
- [ ] Test with simple command: `/pm Analyze project`
- [ ] Review generated documentation
- [ ] Initialize knowledge base (optional)
- [ ] Commit changes to git (optional)
- [ ] Share with team (optional)
- [ ] Start using in daily workflow

---

**Ready to integrate? Let's go! 🚀**

```bash
cd your-project
agentic-sdlc install
agentic-sdlc ide cursor
# In IDE: /pm Let's improve this project!
```
