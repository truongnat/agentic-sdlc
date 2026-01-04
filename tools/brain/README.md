# Brain Tools

> **@BRAIN - Meta-Level System Controller**

This directory contains the Root Layer (Layer 1) of the 3-layer architecture.

## 3-Layer Architecture

```
┌────────────────────────────────────────────────────────────┐
│              LAYER 1: ROOT (Brain)                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ Observer │ │  Judge   │ │ Learner  │ │A/B Tester│       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│  ┌──────────────┐ ┌────────────────┐                       │
│  │Model Optimizer│ │ Self-Improver  │                       │
│  └──────────────┘ └────────────────┘                       │
├────────────────────────────────────────────────────────────┤
│              LAYER 2: WORKFLOW                              │
│  /orchestrator │ /cycle │ /emergency │ /sprint             │
├────────────────────────────────────────────────────────────┤
│              LAYER 3: EXECUTION                             │
│  @PM │ @BA │ @SA │ @DEV │ @TESTER │ Scripts                │
└────────────────────────────────────────────────────────────┘
```

## Root Components

| Component | File | Purpose |
|-----------|------|---------|
| **Observer** | `observer.py` | Monitors all actions, halts on errors |
| **Judge** | `judge.py` | Scores reports, requires mandatory reporting |
| **Learner** | `learner.py` | Auto-triggers learning on task completion |
| **A/B Tester** | `ab_tester.py` | Tests 2 options, selects better |
| **Model Optimizer** | `model_optimizer.py` | Selects optimal AI model |
| **Self-Improver** | `self_improver.py` | Creates self-improvement plans |

## Quick Commands

```bash
# State Management
python tools/brain/brain_cli.py init 1
python tools/brain/brain_cli.py status
python tools/brain/brain_cli.py transition DESIGNING

# Supervision
python tools/brain/observer.py --watch
python tools/brain/observer.py --halt "Error"

# Quality
python tools/brain/judge.py --score "path/to/report.md"
python tools/brain/judge.py --stats

# Learning
python tools/brain/learner.py --learn "Task completed"
python tools/brain/learner.py --stats

# A/B Testing
python tools/brain/ab_tester.py --create "Test description"
python tools/brain/ab_tester.py --stats

# Model Optimization
python tools/brain/model_optimizer.py --recommend "Task description"

# Self-Improvement
python tools/brain/self_improver.py --analyze
python tools/brain/self_improver.py --plan
```

## Integration

- Skills: `.agent/skills/role-brain.md`
- Workflow: `.agent/workflows/support/brain.md`
