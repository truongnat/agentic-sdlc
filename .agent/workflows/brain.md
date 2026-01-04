---
description: [Support] @BRAIN Meta-Level System Controller
---

# Brain Workflow

> **Skill Definition:** [View Skill](../../skills/role-brain.md)

## Identity
@BRAIN is the **Meta-Level Controller** that supervises ALL workflows in the system.
Brain is NOT an executor—it monitors, detects issues, routes to handlers, scores quality, and creates self-improvement plans.

// turbo-all

## Root Components (Layer 1)

### Observer (Halt on Errors)
```bash
agentic-sdlc run tools/brain/observer.py --watch       # Monitor workflows
agentic-sdlc run tools/brain/observer.py --halt "Err"  # Halt system
agentic-sdlc run tools/brain/observer.py --resume      # Resume after halt
```

### Judge (Score Quality)
```bash
agentic-sdlc run tools/brain/judge.py --score "path/to/report.md"
agentic-sdlc run tools/brain/judge.py --review --sprint 1
agentic-sdlc run tools/brain/judge.py --threshold 7    # Set pass threshold
```

### Learner (Auto-Learning)
```bash
agentic-sdlc learn --learn "Task completed"
agentic-sdlc learn --watch
agentic-sdlc learn --stats
```

### A/B Tester (Compare Options)
```bash
agentic-sdlc run tools/brain/ab_tester.py --create "Test description"
agentic-sdlc run tools/brain/ab_tester.py --compare --test-id TEST-001
agentic-sdlc run tools/brain/ab_tester.py --select A --test-id TEST-001
```

### Model Optimizer (Token Efficiency)
```bash
agentic-sdlc run tools/brain/model_optimizer.py --recommend "Task description"
agentic-sdlc run tools/brain/model_optimizer.py --record --model "gemini-2.5" --tokens 1500
```

### Self-Improver (Create Improvement Plans)
```bash
agentic-sdlc run tools/brain/self_improver.py --analyze  # Analyze all data
agentic-sdlc run tools/brain/self_improver.py --plan     # Create improvement plan
agentic-sdlc run tools/brain/self_improver.py --apply-plan PLAN-ID
```

## State Management
```bash
agentic-sdlc brain init 1          # Initialize sprint
agentic-sdlc brain status          # Check status
agentic-sdlc brain transition STATE --reason "Reason"
agentic-sdlc brain validate        # Validate state
agentic-sdlc brain rollback        # Rollback
```

## Supervisor Commands
```bash
agentic-sdlc brain watch   # Monitor workflows
agentic-sdlc run tools/brain/brain_cli.py route "request"  # Route to workflow
agentic-sdlc health  # Health check
```

## Sync Commands
```bash
agentic-sdlc kb compound sync
agentic-sdlc kb compound sync --full
```

#brain #root-layer #meta-controller


---

## ENFORCEMENT REMINDER
Before executing, complete /preflight checks.
