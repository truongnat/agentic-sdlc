# TeamLifecycle Instructions

> **Simulating a complete Software Development Lifecycle (SDLC) with specialized AI Agents.**

## 🎯 Overview

This repository contains the instruction sets and templates for **TeamLifecycle**, a project designed to simulate a professional SDLC using Gemini agents acting as specialized roles (Project Manager, Solution Architect, Developer, etc.).

By invoking specific roles using `@tags`, you can trigger a coordinated workflow that takes a project from planning to deployment and reporting.

## ✨ Why Use TeamLifecycle? (Benefits & Optimization)

Adopting this **Agentic SDLC** approach offers significant advantages over standard single-agent coding:

### 1. 🚀 Optimized Process & Quality Assurance
-   **Zero Ambiguity**: By splitting **Planning**, **Design**, and **Implementation**, potential issues are caught *before* code is written.
-   **Strict "Definition of Done"**: Code isn't just "written"; it's **designed**, **reviewed**, **security-checked**, **implemented**, and **tested**.
-   **Self-Correction**: The workflow includes loop-backs (cycle repeats) if a design is rejected or critical bugs are found, ensuring the final output is robust.

### 2. 🧠 Specialized Intelligence (Agentic Roles)
Instead of one "generic" AI trying to do everything, you get specialized experts:
-   **@SA** thinks purely about *scalability and database structure*.
-   **@UIUX** focuses solely on *user flow and aesthetics*.
-   **@SECA** acts as a dedicated adversary to find *vulnerabilities*.
-   **@DEV** can focus purely on *implementation details* without worrying about high-level architecture.

### 3. 📚 Comprehensive Documentation (Audit Trail)
-   This system **automatically generates** a full project documentation suite (`docs/`):
    -   Requirement Plans & Backlogs
    -   Technical & Design Specs
    -   Security & QA Reports
    -   Test Results & Change Logs
-   This makes "handover" to human teams or other agents seamless.

### 4. ⚡ Benefit Analysis
| Feature | Traditional AI Coding | TeamLifecycle (Agentic) |
| :--- | :--- | :--- |
| **Context** | Often loses context in long chats | Structured artifacts preserve context per Sprint |
| **Safety** | May generate insecure code | Dedicated **@SECA** review step |
| **Architecture** | Often "spaghetti code" | Planned by **@SA** before implementation |
| **Debugging** | User has to debug | **@TESTER** finds bugs, **@DEV** fixes them |

### 5. 🔄 Sprint-Based Organization
-   Optimized for iterative development.
-   Keeps files organized by Sprint (`docs/sprints/sprint-X/`), preventing clutter and ensuring version control.

## � Installation

### Prerequisites
- Node.js (version 14 or higher)
- npm or yarn

### Install the CLI Tool
```bash
npm install -g template-instructions
```

### Create a New Project with Instructions
```bash
create-instructions my-sdlc-project
```

This will create a new folder `my-sdlc-project` containing a `.gemini/instructions` folder with all the instruction files and templates.

### Manual Setup
Alternatively, clone this repository and copy the `.gemini/instructions/` folder to your desired location.

## 🔧 Setup with Gemini

1. Copy the instruction files to your Gemini workspace:
   ```bash
   cp -r .gemini/instructions/ ~/.gemini/instructions/
   ```
   (Or manually copy the `.gemini/instructions/` folder to `.gemini/instructions/` in your project.)

2. Ensure your Gemini configuration points to this instructions directory.

## 📁 Repository Structure

```
.
├── bin/
│   └── cli.js                      # CLI tool for scaffolding new projects
├── .gemini/
│   └── instructions/
│       ├── global.md                   # Mandatory global rules and SDLC workflows
│       ├── usage.md                    # Detailed usage guide and examples
│       ├── roles/                      # Role-specific instruction definitions
│       │   ├── pm.md, po.md, sa.md...  # (PM, PO, SA, UIUX, QA, etc.)
│       └── templates/                  # Standardized document templates
│           ├── Project-Plan-Template.md
│           ├── Product-Backlog-Template.md
│           └── ...
├── package.json                    # Project metadata and scripts
└── README.md                       # This file
```

## 🚀 Quick Start

1.  **Start a Project**: Invoke the Project Manager (`@PM`) with your idea.
    ```text
    @PM - I want to build a personal finance dashboard.
    ```
2.  **Approve Plan**: The PM will create a plan. Review and reply `Approved`.
3.  **Watch the Magic**: The agents will automatically hand off work through the phases:
    `PM → SA/UIUX/PO → QA/SecA → DEV/DevOps → TESTER → REPORTER`

## 📋 Available Roles

| Tag | Role | Responsibility |
| :--- | :--- | :--- |
| `@PM` | **Project Manager** | Planning & Coordination |
| `@PO` | **Product Owner** | Backlog & Prioritization |
| `@SA` | **Solution Architect** | Backend & API Design |
| `@UIUX` | **UI/UX Designer** | Interface & UX Design |
| `@QA` | **QA Analyst** | Design Review & Quality Standards |
| `@SECA` | **Security Analyst** | Security Audits |
| `@DEV` | **Developer** | Implementation |
| `@DEVOPS` | **DevOps Engineer** | CI/CD & Deployment |
| `@TESTER` | **Tester** | Verification & Validation |
| `@REPORTER` | **Reporter** | Documentation & Reporting |
| `@STAKEHOLDER`| **Stakeholder** | Final Approval |

## 📚 Documentation

For detailed instructions, rules, and workflows, please refer to:

*   **[Usage Guide](.gemini/instructions/usage.md)**: How to use the system, examples, and commands.
*   **[Global Rules](.gemini/instructions/global.md)**: The strict SDLC protocols and rules every agent follows.

---
*Maintained by the TeamLifecycle Project Team.*
