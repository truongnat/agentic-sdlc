# Implementation Plan: LEANN AI Brain Integration

This plan outlines the steps to integrate the **LEANN** (Lean and Efficient AI Near-memory) framework into the `agentic-sdlc` project to automate knowledge management and provide agents with deep project context.

## 🎯 Objectives
- Replace manual Knowledge Base indexing with automated LEANN indexing.
- Enable deep, AST-aware code search for AI roles.
- Integrate LEANN via MCP for real-time memory access in the IDE.

## 🛠️ Proposed Changes

### 1. New Workflow: `leann-brain.md`
Create a new workflow in `.agent/workflows/` to handle installation, indexing, and querying.

### 2. Update `kb-search.md`
Modified to prefer LEANN search over manual file grepping when available.

### 3. Documentation
Update `README.md` and create `docs/brain.md` to explain how to use the new "Project Brain".

### 4. Role Updates
Update the AI role instructions (PM, Dev, SA) to include the `/brain` command as their primary context source.

## 📅 Step-by-Step Execution

### Phase 1: Setup
1. **Command:** `pip install leann-core leann-backend-hnsw`
   - *Note: Suggest using `uv` if available for speed.*
2. **Command:** `leann index --path .`
   - Performs initial AST-aware indexing of the workspace.

### Phase 2: Workflow Creation
1. Create `.agent/workflows/leann-brain.md`.
2. Update `.agent/workflows/kb-search.md`.

### Phase 3: Integration
1. Configure MCP server for the IDE.
2. Update global rules to encourage using `/brain` for context.

---
**Status:** ⏳ Pending approval from USER.
