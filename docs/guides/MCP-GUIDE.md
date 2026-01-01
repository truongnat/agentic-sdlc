# 🌐 Distributed Intelligence Network: MCP Integration Guide

This project leverages the **Model Context Protocol (MCP)** to provide agents with real-world tools, system access, and external data.

## 🛠️ Core MCP Servers

The following servers are integrated into the team roles. Ensure these are configured in your environment for full automation.

| MCP Server | Key Tools | Primary Role |
| :--- | :--- | :--- |
| **GitHub** | Issue tracking, Milestones, PRs | @PM, @PO, @REPORTER |
| **Vercel** | Deployment status, Logs | @DEVOPS |
| **Docker** | Container management | @DEVOPS |
| **GitIngest** | Codebase snapshots | @ORCHESTRATOR, @REPORTER |
| **Apidog** | API Testing & Design | @SA, @TESTER |
| **Brave Search** | External Research | @PM, @PO |
| **Firecrawl** | Web Scraper / Log research | @SECA, @DEVOPS |
| **Playwright** | E2E / Browser Testing | @QA, @TESTER |
| **Context7** | Architecture Analysis | @SA, @DEV |
| **Supabase / PG** | Database Operations | @SA, @DEV |
| **Sequential Thinking** | Logic & Reasoning | @ORCHESTRATOR, @DEV |
| **DesktopCommander** | OS Management | @ORCHESTRATOR, @DEVOPS |

---

## 🚀 Advanced MCP Suggestions (Future-Proofing)

Beyond the requested list, the following MCPs are highly recommended for advanced project scaling:

### 1. Productivity & Handoffs
- **Slack/Discord MCP:** Push real-time role handoff notifications (e.g., `@QA: Design is ready for review`).
- **Linear MCP:** If GitHub Issues become too complex, Linear offers a high-performance alternative for engineering tasks.
- **Sentry MCP:** Automatically pull crash reports into @DEV's context for instant bug analysis.

### 2. Knowledge & AI Enhancement
- **Exa / Perplexity MCP:** For "AI-Search" that provides factual, cited answers faster than a standard search engine.
- **Zotero / Mendeley MCP:** If the project requires heavy academic or technical research documentation.
- **Obsidian / Logseq MCP:** Personal knowledge management sync for stakeholders.

### 3. Data & Cloud
- **Snowflake / Databricks MCP:** For heavy data engineering projects.
- **AWS / GCP / Azure MCPs:** To manage infrastructure directly from the chat.

---

## 📋 Best Practices for Agents

1. **Facts First:** Before starting a task, use `Brave Search` or `GitIngest` to verify the current state.
2. **Atomic Integration:** When mentioning an MCP tool, provide the context (e.g., *"According to Playwright logs, the login button is obscured..."*).
3. **Loop Verification:** Always use `Apidog` or `Playwright` to verify a fix before tagging the next role.

---
*Created by Antigravity - 2026-01-01*
