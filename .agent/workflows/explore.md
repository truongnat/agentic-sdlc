---
description: [Process] Deep Investigation Workflow
---

# /explore - Multi-Order Analysis

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
1. **USE BEFORE PLANNING:** Run before major architectural decisions.
2. **MULTI-ORDER THINKING:** Go beyond surface-level analysis.
3. **EVIDENCE-BASED:** All findings must have supporting evidence.
4. **DOCUMENT FINDINGS:** Create exploration report.

## When to Use

- **Complex Features:** Before implementing features with many dependencies
- **Architecture Decisions:** Before major structural changes
- **Unknown Territory:** When entering unfamiliar domains
- **Risk Assessment:** Before high-impact changes

## Workflow Steps

### 1. First-Order Analysis (Surface Level)
**Question:** What does the user want?

```bash
# Basic research
python tools/research/research_agent.py --task "[feature]" --type general
```

- [ ] Understand explicit requirements
- [ ] Identify immediate stakeholders
- [ ] List obvious technical needs

### 2. Second-Order Analysis (Dependencies)
**Question:** What does this depend on?

- [ ] Identify technical dependencies
- [ ] Map affected components
- [ ] Find related existing implementations

```bash
# Search KB for related entries
python bin/kb_cli.py search "[related topic]"
```

### 3. Third-Order Analysis (Implications)
**Question:** What are the ripple effects?

- [ ] Performance implications
- [ ] Security implications
- [ ] Scalability considerations
- [ ] Maintenance burden

### 4. Fourth-Order Analysis (Hidden Risks)
**Question:** What could go wrong that we haven't considered?

- [ ] Edge cases
- [ ] Failure modes
- [ ] Integration conflicts
- [ ] Future constraints

```bash
# Check for similar issues in KB
python bin/kb_cli.py search "bug" --category bugs
```

### 5. Synthesis
**Question:** What's the recommended approach?

Create exploration report with:
- Key findings per order of analysis
- Risk assessment matrix
- Recommended approach with rationale
- Alternative approaches considered
- Open questions requiring stakeholder input

## Output Template

```markdown
# Exploration Report: [Feature/Decision]

**Date:** YYYY-MM-DD  
**Author:** @[ROLE]

## Executive Summary
[1-2 paragraph summary]

## First-Order Analysis
### User Requirements
- ...

## Second-Order Analysis
### Dependencies
- ...

## Third-Order Analysis
### Implications
- ...

## Fourth-Order Analysis
### Hidden Risks
- ...

## Risk Matrix
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| ... | ... | ... | ... |

## Recommendation
[Recommended approach with rationale]

## Alternatives Considered
1. ...
2. ...

## Open Questions
- [ ] ...
```

## Integration

- **@PM** triggers before major planning
- **@SA** uses for architecture decisions
- **@SECA** incorporates in security review
- **/cycle** may trigger for complex tasks

## Example Usage

```
User: "We need to add OAuth authentication"

/explore OAuth implementation

First-Order: User wants social login
Second-Order: Depends on token storage, session management, user model
Third-Order: Affects all API endpoints, session timeout, refresh logic
Fourth-Order: Token revocation, multi-device sessions, privacy compliance
```

#explore #analysis #research #architecture #risk-assessment
