# 🧠 Auto-Learning System - Quick Start Guide

## What is Auto-Learning?

The auto-learning system automatically captures knowledge from every task, issue, and bug fix to build project intelligence. This creates a self-improving system that learns from experience.

---

## 🚀 Quick Start (3 Steps)

### Step 1: Check if Learning is Required
After completing ANY task, ask yourself:

```markdown
### Auto-Learn Check
- [ ] Bug priority medium or higher?
- [ ] Required 3+ attempts?
- [ ] Same error occurred before?
- [ ] Implementation took 4+ hours?
- [ ] Security or performance issue?

**Result:** [YES/NO]
```

### Step 2: Create Knowledge Entry (if YES)
```bash
# Copy template
cp .agent/templates/Knowledge-Entry-Template.md \
   .agent/knowledge-base/[category]/[severity]/KB-$(date +%Y-%m-%d)-[###]-[title].md

# Fill in the template
# Set "Auto-Generated: Yes"
# Set "Source Task: [Your Task ID]"
```

### Step 3: Update Index
Add entry to `.agent/knowledge-base/index.md`:
- Update statistics
- Add to recent entries
- Add to category table
- Add to technology search
- Add to tag search

---

## 📋 Auto-Learning Triggers

| Trigger | Action | Priority |
|---------|--------|----------|
| 🐛 Bug Fixed (Medium+) | Create KB entry | High |
| 🔄 3+ Attempts | Create KB entry | High |
| 🔁 Recurring Error | Create KB entry | Critical |
| ⏱️ 4+ Hours Work | Create KB entry | Medium |
| 🔒 Security Issue | Create KB entry | Critical |
| ⚡ Performance Fix | Create KB entry | Medium |
| 🔗 Integration Issue | Create KB entry | Medium |
| 🏗️ Architecture Decision | Create KB entry | High |
| 🚨 Rollback Event | Create KB entry | Critical |

---

## 🎯 Role-Specific Quick Actions

### @DEV
```markdown
## After Bug Fix
1. Check severity: [critical/high/medium/low]
2. If medium+: Create KB entry
3. Document: Problem → Root Cause → Solution → Prevention
4. Tag: #bug-pattern #[technology] #auto-learned
```

### @DEVOPS
```markdown
## After Deployment Issue
1. Document: What failed → Why → How fixed
2. Create KB entry in platform-specific/
3. Add monitoring/alert recommendations
4. Tag: #deployment #infrastructure #auto-learned
```

### @TESTER
```markdown
## After Finding Edge Case
1. Document: Test scenario → Expected vs Actual → Root cause
2. Create KB entry in bugs/ or features/
3. Add regression test details
4. Tag: #testing #edge-case #auto-learned
```

### @SECA
```markdown
## After Security Issue
1. Document: Vulnerability → Impact → Fix → Prevention
2. Create KB entry in security/
3. Add detection strategy
4. Tag: #security #vulnerability #auto-learned
```

---

## 🔍 Search Before Starting

**ALWAYS search knowledge base before starting work:**

```markdown
### KB Search
**Keywords:** [error message, technology, component]
**Category:** [bugs/features/architecture/security/performance]
**Results Found:** [number]

#### Relevant Entries:
1. KB-[ID]: [Title] - Relevance: [high/medium/low]
   - **Solution:** [Brief summary]
   - **Applicable:** [yes/no]

2. KB-[ID]: [Title] - Relevance: [high/medium/low]
   - **Solution:** [Brief summary]
   - **Applicable:** [yes/no]
```

---

## 📝 Quick Template

Use this minimal template for fast knowledge capture:

```markdown
# KB-[YYYY-MM-DD]-[###] - [Title]

**Auto-Generated:** Yes  
**Source:** [Task ID]  
**Category:** [Category]  
**Severity:** [Severity]

## Problem
[What went wrong]

## Root Cause
[Why it happened]

## Solution
[What fixed it]

```code
[Code snippet]
```

## Prevention
- [How to avoid]
- [How to detect early]

## Tags
#auto-learned #[category] #[technology]
```

---

## 🎓 Learning Categories

| Category | When to Use | Location |
|----------|-------------|----------|
| **Bugs** | Any bug fix | `bugs/[severity]/` |
| **Features** | Complex implementation | `features/[type]/` |
| **Architecture** | Design decision | `architecture/` |
| **Security** | Security issue | `security/` |
| **Performance** | Optimization | `performance/` |
| **Platform** | Platform-specific | `platform-specific/[platform]/` |

---

## 📊 Quality Checklist

Before saving KB entry, verify:

- [ ] Clear problem description
- [ ] Root cause explained
- [ ] Working solution documented
- [ ] Code snippets included
- [ ] Prevention measures listed
- [ ] Proper category and severity
- [ ] Relevant tags added
- [ ] Source task referenced
- [ ] Index updated

---

## 🔄 Weekly Maintenance

Every Friday, @REPORTER should:

1. **Review** all auto-generated entries
2. **Verify** completeness and quality
3. **Add** missing details
4. **Update** cross-references
5. **Archive** duplicates

---

## 💡 Pro Tips

### Tip 1: Be Specific
❌ Bad: "Fixed login bug"  
✅ Good: "Fixed OAuth token refresh race condition in login flow"

### Tip 2: Include Error Messages
Always include exact error messages for searchability:
```
Error: Cannot read property 'user' of undefined
```

### Tip 3: Document Failed Attempts
Don't just document what worked - document what DIDN'T work:
```markdown
## What Didn't Work
- Tried increasing timeout → Still failed
- Tried different library → Compatibility issues
- Tried caching → Race condition persisted
```

### Tip 4: Add Visual Aids
Include screenshots, diagrams, or recordings when helpful.

### Tip 5: Cross-Reference
Link to related KB entries:
```markdown
## Related Entries
- KB-2026-01-01-001: Similar hydration issue
- KB-2025-12-15-042: SSR best practices
```

---

## 📞 Need Help?

- **What to document:** Tag @REPORTER
- **Where to store:** Check category structure
- **How to search:** Use index.md or grep
- **Quality issues:** Tag @REPORTER for review

---

## 🎯 Success Metrics

Track your learning impact:

| Metric | Target | Current |
|--------|--------|---------|
| KB Entries Created | Growing | 1 |
| KB Entries Referenced | >50% | - |
| Similar Issues Prevented | >80% | - |
| Resolution Time Reduced | >30% | - |

---

## 🚀 Advanced Features

### Auto-Tagging
System can suggest tags based on:
- Error messages
- Technology stack
- Component names
- File paths

### Auto-Linking
System can find related entries by:
- Similar keywords
- Same technology
- Same component
- Same error pattern

### Auto-Metrics
System tracks:
- Most common issues
- Fastest resolutions
- Most referenced entries
- Learning trends

---

#auto-learning #knowledge-base #quick-start #guide

