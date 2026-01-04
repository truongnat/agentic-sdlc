---
description: [Utility] Metrics - Project Statistics
---

# /metrics - Metrics Dashboard Generator

## ⚠️ PURPOSE
Analyzes KB entries, workflow usage, and project health to generate a metrics dashboard showing learning velocity, quality indicators, and system health.

## Quick Commands

```bash
# Generate dashboard
python tools/kb/metrics-dashboard.py

# Weekly report focus
python tools/kb/metrics-dashboard.py --weekly

# Sprint-specific metrics
python tools/kb/metrics-dashboard.py --sprint 6

# Custom output path
python tools/kb/metrics-dashboard.py --output ./my-report.md
```

## What It Measures

### 1. Knowledge Base Metrics
- **Total KB Entries:** Count of all knowledge entries
- **This Week:** Entries added in last 7 days
- **This Month:** Entries added in last 30 days
- **Category Breakdown:** Distribution across categories

### 2. Learning Velocity
- Entries per week trend
- Strong (3+), Moderate (1-2), Low (0)

### 3. Time Saved
- Estimated hours saved per entry
- Total accumulated time saved
- Average time per entry

### 4. Quality Indicators
- Priority distribution (critical, high, medium, low)
- Category diversity
- Contributor activity

## Console Output

```
============================================================
Metrics Dashboard Generator
============================================================
[INFO] Analyzing knowledge base...
[OK] Analyzed 12 entries

============================================================
Quick Stats
============================================================
  Total Entries:      12
  This Week:          +3
  This Month:         +8
  Total Time Saved:   24 hours

  Health Status: Good
```

## Dashboard Report

Generates `docs/reports/Metrics-Dashboard-YYYY-MM-DD.md`:

```markdown
# 📊 Metrics Dashboard

**Generated:** 2026-01-03 18:30  
**Overall Health:** 🟢 Excellent

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total KB Entries | 12 |
| This Week | +3 |
| This Month | +8 |
| Total Time Saved | 24 hours |
| Avg Time per Entry | 2.0 hours |

---

## 📈 Learning Velocity

✅ **Strong learning velocity** - Team is actively documenting solutions

---

## 📁 Category Breakdown

| Category | Count | % |
|----------|-------|---|
| feature | 7 | 58% |
| bug | 3 | 25% |
| security | 2 | 17% |

---

## ⚠️ Priority Distribution

| Priority | Count |
|----------|-------|
| 🟠 High | 4 |
| 🟡 Medium | 6 |
| 🟢 Low | 2 |

---

## 👥 Top Contributors

| Author | Entries |
|--------|---------|
| @DEV | 5 |
| @SA | 3 |
| @TESTER | 2 |

---

## 🎯 Recommendations

- ✅ Keep up the great work!
```

## Health Score Calculation

| Points | Criteria |
|--------|----------|
| +30 | 20+ total entries |
| +20 | 10-19 total entries |
| +30 | 3+ entries this week |
| +15 | 1-2 entries this week |
| +20 | 5+ categories |
| +20 | 10+ hours time saved |

| Score | Status |
|-------|--------|
| 80-100 | 🟢 Excellent |
| 50-79 | 🟡 Good |
| 0-49 | 🔴 Needs Attention |

## Recommendations Engine

Auto-generates recommendations based on:
- Low documentation velocity
- Missing bug documentation
- Missing architecture decisions
- Unbalanced category distribution

## When to Run

- **Weekly:** Track learning velocity
- **End of Sprint:** Generate sprint metrics
- **Monthly:** Long-term trend analysis
- **Stakeholder Reports:** Project health overview

## Integration

- **/brain** - Uses KB data for recommendations
- **/compound** - Creates entries that affect metrics
- **/housekeeping** - References health status
- **/sprint close** - Include metrics in retrospective

#metrics #dashboard #analytics #health #knowledge-base
