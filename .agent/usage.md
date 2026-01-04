# 📚 TeamLifecycle Instructions - Usage Guide

> **Version:** 1.0  
> **Last Updated:** 2026-01-01

---

## 🎯 Overview

This instruction set simulates a **complete Software Development Lifecycle (SDLC)** with specialized roles. When you invoke a role using `@tag`, the AI will act as that role and perform tasks according to the defined workflow.

**Supports all project types:**
- 🌐 Web Applications (SPA, SSR, PWA)
- 📱 Mobile Apps (iOS, Android, Cross-platform)
- 🖥️ Desktop Applications (Windows, macOS, Linux)
- 🔌 Embedded Systems & IoT
- ⚙️ CLI Tools & Utilities
- 📚 Libraries & SDKs
- 🔗 APIs & Backend Services

---

## 📁 Directory Structure

```
.agent/
├── global.md                    # Global rules (mandatory)
├── usage.md                     # This usage guide
├── skills/                       # Team skills
│   ├── pm.md                    # Project Manager
│   ├── po.md                    # Product Owner
│   ├── sa.md                    # System Analyst
│   ├── designer.md              # UI/UX Designer
│   ├── qa.md                    # Quality Assurance
│   ├── seca.md                  # Security Analyst
│   ├── dev.md                   # Developer
│   ├── devops.md                # DevOps Engineer
│   ├── tester.md                # Tester
│   ├── reporter.md              # Reporter
│   └── stakeholder.md           # Stakeholder
├── templates/                   # Document templates
│   ├── Project-Plan-Template.md
│   ├── Product-Backlog-Template.md
│   ├── System-Design-Spec-Template.md
│   ├── UIUX-Design-Spec-Template.md
│   ├── Design-Verification-Report-Template.md
│   ├── Security-Review-Report-Template.md
│   ├── Development-Log-Template.md
│   ├── DevOps-Plan-Template.md
│   ├── Test-Report-Template.md
│   ├── Phase-Report-Template.md
│   ├── Master-Documentation-Template.md
│   ├── Final-Project-Report-Template.md
│   ├── Final-Approval-Report-Template.md
│   ├── Knowledge-Entry-Template.md
│   ├── definition-of-done.md
│   └── incident-response.md
└── knowledge-base/              # Project memory
    ├── README.md                # Knowledge base guide
    ├── index.md                 # Searchable index
    ├── bugs/                    # Bug patterns
    ├── features/                # Complex features
    ├── architecture/            # Architecture decisions
    ├── security/                # Security issues
    ├── performance/             # Optimizations
    └── platform-specific/       # Platform issues
```

---

## 🚀 Getting Started

### Execution Modes

The system supports 3 execution modes:

#### Mode 1: Manual (Default)
You tag each role manually at each step. Full control, step-by-step.

```
@PM - I want to build a wedding website...
[Review plan]
"Approved"
@SA - Begin backend design
[Review design]
@QA - Review design
...
```

#### Mode 2: Semi-Auto
Orchestrator auto-executes within phases, waits at phase boundaries.

```
@PM - I want to build a wedding website --mode=semi-auto
[Review plan]
"Approved"
→ Auto-executes: SA + UIUX + PO → QA + SecA
[Review design phase results]
@ORCHESTRATOR - Continue to development
→ Auto-executes: DEV + DevOps
...
```

#### Mode 3: Full-Auto (Recommended for Speed)
Orchestrator executes entire workflow, only stops at critical gates.

```
@PM - I want to build a wedding website --mode=full-auto
[Review plan]
"Approved"
→ Auto-executes entire workflow
→ Stops only at: Critical bugs, Final approval

[30-60 minutes later]
"⚠️ Decision required: 2 high-priority bugs found"
[Make decision]
→ Continues automatically
"✅ Project complete, ready for stakeholder review"
```

---

### Step 1: Start a Project

**Manual Mode:**
```
@PM - I want to build a wedding website with:
- Couple introduction page
- Countdown timer
- Photo gallery
- RSVP form
```

**Full-Auto Mode:**
```
@PM - I want to build a wedding website with:
- Couple introduction page
- Countdown timer
- Photo gallery
- RSVP form
--mode=full-auto
```

PM will create `Project-Plan-Sprint-1-v1.md` and wait for your approval.

### Step 2: Approval

After reviewing the plan, respond with:
- ✅ **"Approved"** - Proceed to next phase
- 🔄 **Provide feedback** - PM will revise and create a new version

### Step 3: Workflow Execution

**Manual Mode:** You tag each role as needed

**Semi-Auto/Full-Auto Mode:** Orchestrator handles the flow

```
Approved → Design (SA+UIUX+PO) → Review (QA+SecA) → Development (DEV+DevOps) 
→ Testing (TESTER) → Reporting (REPORTER) → Final Review (STAKEHOLDER)
```

---

## 🤖 Orchestrator Commands

### Check Status
```
@ORCHESTRATOR - Status
```

### Pause/Resume
```
@ORCHESTRATOR - Pause
@ORCHESTRATOR - Resume
```

### Change Mode
```
@ORCHESTRATOR - Switch to semi-auto mode
@ORCHESTRATOR - Switch to manual mode
```

### Skip to Phase (use with caution)
```
@ORCHESTRATOR - Skip to testing phase
```

---

## 📋 Roles & Tags

| Role | Tag | Responsibility | Works On |
|------|-----|----------------|----------|
| **Orchestrator** | `@ORCHESTRATOR` | Workflow automation, auto-execute phases | All project types |
| **Project Manager** | `@PM` | Planning, scope management, team coordination | All project types |
| **Product Owner** | `@PO` | Backlog management, feature prioritization, business value | All project types |
| **System Analyst** | `@SA` | System architecture, data models, interfaces (API/CLI/Protocol) | All project types |
| **UI/UX Designer** | `@UIUX` | Interface design, user experience (GUI/CLI/API DX) | GUI, CLI, API projects |
| **QA Analyst** | `@QA` | Design review, quality assurance, testability | All project types |
| **Security Analyst** | `@SECA` | Security assessment, vulnerability analysis | All project types |
| **Developer** | `@DEV` | Code implementation across all platforms | All project types |
| **DevOps** | `@DEVOPS` | CI/CD, deployment (cloud/stores/packages), infrastructure | All project types |
| **Tester** | `@TESTER` | Functional testing, bug detection, platform testing | All project types |
| **Reporter** | `@REPORTER` | Progress reports, comprehensive documentation | All project types |
| **Stakeholder** | `@STAKEHOLDER` | Final approval, business acceptance | All project types |

---

## 🏷️ Important Tags

### Phase Tags
| Tag | Description | Used By |
|-----|-------------|---------|
| `#orchestrator` | Workflow automation | ORCHESTRATOR |
| `#automation` | Automated execution | ORCHESTRATOR |
| `#planning` | Planning phase | PM |
| `#product-owner` | Product ownership activities | PO |
| `#backlog` | Backlog management | PO |
| `#designing` | Design phase (system architecture) | SA |
| `#uiux-design` | UI/UX design phase | UIUX |
| `#verify-design` | Design verification | QA |
| `#security-review` | Security review | SecA |
| `#development` | Development phase | DEV |
| `#devops` | DevOps activities | DevOps |
| `#testing` | Testing phase | TESTER |
| `#reporting` | Reporting phase | REPORTER |
| `#stakeholder-review` | Stakeholder review | STAKEHOLDER |

### Bug Priority Tags
| Tag | Severity |
|-----|----------|
| `#fixbug-critical` | Breaks core functionality |
| `#fixbug-high` | Major feature broken |
| `#fixbug-medium` | Works but incorrect behavior |
| `#fixbug-low` | Cosmetic issues |

### Special Tags
| Tag | Description | Used By |
|-----|-------------|---------|
| `#searching` | Research/web search activity | All roles |
| `#blocked` | Blocked, needs support | All roles |
| `#hotfix` | Emergency fix | DEV, DevOps |
| `#rollback` | Needs rollback | DevOps |
| `#deployed-staging` | Deployed to staging | DevOps |
| `#deployed-production` | Deployed to production | DevOps |
| `#incident` | Incident response | All roles |

---

## 📄 Generated Artifacts

Artifacts are organized by Sprint and type in the `docs/` folder:

### Sprint-Based Structure
```
docs/
├── sprints/
│   ├── sprint-1/
│   │   ├── plans/          # Project plans, backlogs
│   │   ├── designs/        # System & UI/UX designs
│   │   ├── reviews/        # QA & Security reviews
│   │   ├── logs/           # Development & DevOps logs
│   │   ├── tests/          # Test reports
│   │   └── reports/        # Phase reports
│   └── sprint-2/
│       └── ...
└── global/
    ├── Master-Documentation.md
    └── reports/
        ├── Final-Project-Report.md
        └── Final-Approval-Report.md
```

### Artifact Types by Category

| Category | Artifacts | Owner | Location |
|----------|-----------|-------|----------|
| **Plans** | Project-Plan-Sprint-[N]-v*.md<br>Product-Backlog-Sprint-[N]-v*.md | PM, PO | `docs/sprints/sprint-[N]/plans/` |
| **Designs** | System-Design-Spec-Sprint-[N]-v*.md<br>UIUX-Design-Spec-Sprint-[N]-v*.md | SA, UIUX | `docs/sprints/sprint-[N]/designs/` |
| **Reviews** | Design-Verification-Report-Sprint-[N]-v*.md<br>Security-Review-Report-Sprint-[N]-v*.md | QA, SecA | `docs/sprints/sprint-[N]/reviews/` |
| **Logs** | Development-Log-Sprint-[N]-v*.md<br>DevOps-Plan-and-Log-Sprint-[N]-v*.md | DEV, DevOps | `docs/sprints/sprint-[N]/logs/` |
| **Tests** | Test-Report-Sprint-[N]-v*.md | TESTER | `docs/sprints/sprint-[N]/tests/` |
| **Reports** | Phase-Report-Sprint-[N]-v*.md | REPORTER | `docs/sprints/sprint-[N]/reports/` |
| **Global** | Master-Documentation.md<br>Final-Project-Report.md<br>Final-Approval-Report.md | REPORTER, STAKEHOLDER | `docs/global/` and `docs/global/reports/` |

> ⚠️ **CRITICAL:** All artifacts are in `docs/`, NEVER in `.agent/` (reserved for instructions only)

---

## 💡 Usage Examples

### Quick Start with Full-Auto Mode

```
@PM - Build a todo app with:
- User authentication
- Task CRUD operations
- Priority levels
- Due dates
Platform: Web (React + Node.js)
--mode=full-auto

[Review plan]
"Approved"

[Wait 30-60 minutes - Orchestrator handles everything]

[Only interrupted for critical decisions]
"⚠️ Decision required: High-priority bug found"
"1" (to fix)

[Final notification]
"✅ Project complete - ready for stakeholder review"
```

### Starting Different Project Types

#### Web Application
```
@PM - I want to build a wedding website with:
- Couple introduction page
- Countdown timer
- Photo gallery
- RSVP form
Platform: Web (responsive)
Tech preference: React/Next.js
```

#### Mobile App
```
@PM - I need a fitness tracking mobile app with:
- Workout logging
- Progress charts
- Goal setting
- Push notifications
Platform: iOS and Android
Tech preference: React Native or Flutter
```

#### CLI Tool
```
@PM - Build a CLI tool for:
- File conversion (JSON to YAML)
- Batch processing
- Configuration validation
Platform: Cross-platform CLI
Tech preference: Node.js or Go
```

#### Desktop Application
```
@PM - Create a desktop note-taking app with:
- Rich text editor
- Local storage
- Search functionality
- Export to PDF
Platform: Windows and macOS
Tech preference: Electron
```

#### API/Backend Service
```
@PM - Develop a REST API for:
- User authentication
- CRUD operations for tasks
- Real-time notifications
- Rate limiting
Platform: Backend API
Tech preference: Node.js/Express or Python/FastAPI
```

### Role-Specific Requests

#### Request system design
```
@SA - Design the architecture for a real-time chat system
```

#### Request UI/UX design
```
@UIUX - Design a mobile-first dashboard with dark mode support
```

#### Request bug fix
```
@DEV - Fix BUG-001: Countdown not displaying correctly on mobile
```

#### Request security review
```
@SECA - Review authentication flow for OAuth vulnerabilities
```

#### Check progress
```
@REPORTER - Summarize current project progress
```

#### Request deployment
```
@DEVOPS - Deploy current version to staging environment
```

#### Request testing
```
@TESTER - Test the new payment integration on iOS and Android
```

---

## 🔧 Platform-Specific Workflows

### Web Application Workflow
1. **@PM** - Define features and target browsers
2. **@SA** - Design API architecture and data flow
3. **@UIUX** - Create responsive designs (mobile-first)
4. **@QA** - Review for cross-browser compatibility
5. **@SECA** - Check for XSS, CSRF, security headers
6. **@DEV** - Implement frontend and backend
7. **@DEVOPS** - Setup CI/CD, deploy to cloud
8. **@TESTER** - Test across browsers and devices

### Mobile App Workflow
1. **@PM** - Define features and target platforms (iOS/Android)
2. **@SA** - Design app architecture and offline support
3. **@UIUX** - Create platform-specific designs (iOS HIG, Material Design)
4. **@QA** - Review for platform guidelines compliance
5. **@SECA** - Check for data storage security, API security
6. **@DEV** - Implement using native or cross-platform framework
7. **@DEVOPS** - Setup app store deployment pipeline
8. **@TESTER** - Test on multiple devices and OS versions

### CLI Tool Workflow
1. **@PM** - Define commands and use cases
2. **@SA** - Design command structure and configuration
3. **@UIUX** - Design CLI UX (prompts, output formatting, help text)
4. **@QA** - Review for usability and error handling
5. **@SECA** - Check for command injection, file access security
6. **@DEV** - Implement CLI logic
7. **@DEVOPS** - Setup package registry publishing (npm, PyPI, etc.)
8. **@TESTER** - Test commands and edge cases

### Desktop App Workflow
1. **@PM** - Define features and target OS
2. **@SA** - Design app architecture and local storage
3. **@UIUX** - Create OS-native designs
4. **@QA** - Review for OS guidelines compliance
5. **@SECA** - Check for privilege escalation, auto-update security
6. **@DEV** - Implement using Electron, Qt, or native frameworks
7. **@DEVOPS** - Setup installer/package creation
8. **@TESTER** - Test on target operating systems

### API/Backend Workflow
1. **@PM** - Define API requirements and consumers
2. **@SA** - Design API endpoints, data models, authentication
3. **@UIUX** - Design API documentation and developer experience
4. **@QA** - Review for API design best practices
5. **@SECA** - Check for authentication, rate limiting, input validation
6. **@DEV** - Implement API endpoints
7. **@DEVOPS** - Setup API gateway, monitoring, scaling
8. **@TESTER** - Test API endpoints, load testing

### ✅ DO:
- Start with `@PM` for new projects
- Provide clear approval before phase transitions
- Use correct tags to invoke roles
- Review generated artifacts
- **Create and save the required report file after completing any task**
- **Search knowledge base before starting complex work**
- **Document difficult bugs/features in knowledge base (3+ attempts)**

### ❌ DON'T:
- Skip phases (e.g., coding before design approval)
- Add features not in approved plan
- Bypass security review
- Ignore knowledge base when facing similar issues

---

## 🔄 Changing Scope

1. Invoke `@PM` with change request
2. PM creates new plan version
3. Wait for re-approval
4. Continue workflow

---

## 📚 Available Templates

All templates are located in `.agent/templates/`:

### Planning Templates
- `Project-Plan-Template.md` - Initial project planning
- `Product-Backlog-Template.md` - Feature backlog management

### Design Templates
- `System-Design-Spec-Template.md` - System/backend architecture (all platforms)
- `UIUX-Design-Spec-Template.md` - UI/UX design (GUI, CLI, API DX)

### Review Templates
- `Design-Verification-Report-Template.md` - QA design review
- `Security-Review-Report-Template.md` - Security assessment

### Development Templates
- `Development-Log-Template.md` - Development progress tracking
- `DevOps-Plan-Template.md` - Infrastructure and deployment

### Testing Templates
- `Test-Report-Template.md` - Testing results and bugs

### Reporting Templates
- `Phase-Report-Template.md` - Sprint/phase summaries
- `Master-Documentation-Template.md` - Complete project documentation
- `Final-Project-Report-Template.md` - Final project summary
- `Final-Approval-Report-Template.md` - Stakeholder approval

### Reference Templates
- `definition-of-done.md` - Quality checklist
- `incident-response.md` - Emergency procedures
- `Knowledge-Entry-Template.md` - Knowledge base entry

---

## 🧠 Knowledge Base

### What is Knowledge Base?
A memory system that stores lessons learned, bug patterns, and difficult features for future reference.

### When to Use
**Create Entry When:**
- Bug required 3+ attempts to fix
- Feature was particularly challenging
- Solution was non-obvious
- Issue likely to recur

**Search Before:**
- Starting complex features
- Fixing unfamiliar bugs
- Making architecture decisions
- Dealing with platform-specific issues

### How to Use
1. **Search:** Check `.agent/knowledge-base/index.md`
2. **Browse:** Navigate by category (bugs, features, architecture, etc.)
3. **Create:** Use `Knowledge-Entry-Template.md` when needed
4. **Update:** Keep index.md current

### Structure
```
knowledge-base/
├── index.md              # Searchable index
├── README.md             # Usage guide
├── bugs/                 # Bug patterns
│   ├── critical/
│   ├── high/
│   ├── medium/
│   └── low/
├── features/             # Complex features
│   ├── authentication/
│   ├── performance/
│   ├── integration/
│   └── ui-ux/
├── architecture/         # Architecture decisions
├── security/             # Security issues
├── performance/          # Optimizations
└── platform-specific/    # Platform issues
    ├── web/
    ├── mobile/
    ├── desktop/
    ├── cli/
    └── embedded/
```

---

## 📞 Need Help?

If unsure which role to invoke:
```
@PM - I need help with [describe issue], who should I contact?
```

PM will direct you to the right person.

---

#instructions #usage-guide


# Git & Task Workflow
---
description: Unified Git and Task Workflow
---

# Git & Task Management Workflow

**Requirement:** All tasks must be tracked with Jira-like precision and committed atomically.

## A. Task Board Logic
- All `Product-Backlog` items (User Stories) must be broken down into **Tasks** in the `Development-Log`.
- **Status Columns:** `Todo` | `In Progress` | `Review` | `Done`.
- **Assignal:** Every task must have an owner (e.g., `@DEV`, `@SA`).
- **Tracing:** Every completed task must link to a **Git Commit Hash**.

## B. Atomic Commit Rule
- ⚠️ **DO NOT** commit all changes at once at the end of a sprint.
- **Workflow:**
  1. Pick a task from `Development-Log` (Mark as `In Progress`)
  2. Implement the code
  3. Verify locally
  4. **COMMIT IMMEDIATELY:** `git commit -m "[Task-ID] <Description>"`
  5. Update `Development-Log` (Mark as `Done` and add Commit Hash)
- This ensures a clean, traceable history and prevents "big bang" integration issues.

## C. Definition of Done (DoD)
A feature/task is "Done" when ALL of the following are true:

### For Development Tasks:
- [ ] Code implemented according to approved design specs
- [ ] Code follows project coding standards
- [ ] Local testing passed
- [ ] Evidence captured (screenshots/logs)
- [ ] Tagged with `#development`
- [ ] **Git Commit created and linked in Log**
- [ ] Handoff to TESTER completed

### For Testing:
- [ ] All test cases executed
- [ ] No critical/high bugs open
- [ ] Evidence documented in Test-Report
- [ ] Tagged with `#testing`

### For Deployment:
- [ ] CI/CD pipeline passing
- [ ] Staging environment verified
- [ ] Security checklist completed
- [ ] Tagged with `#deployed-staging` or `#deployed-production`

### For Project Completion:
- [ ] All Must-Have features verified
- [ ] STAKEHOLDER approved
- [ ] Final documentation complete
- [ ] User notified

## D. Automated Changelog Updates
- **Requirement:** Every commit MUST be followed by an update to CHANGELOG.md.
- **Format:**
  `markdown
  - [YYYY-MM-DD] [Commit-Hash] [Type]: [Description] (@Author)
  ``r
- **Types:** Feature, Fix, Refactor, Docs, Chore, Test.
