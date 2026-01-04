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
python tools/brain/observer.py --watch       # Monitor workflows
python tools/brain/observer.py --halt "Err"  # Halt system
python tools/brain/observer.py --resume      # Resume after halt
```

### Judge (Score Quality)
```bash
python tools/brain/judge.py --score "path/to/report.md"
python tools/brain/judge.py --review --sprint 1
python tools/brain/judge.py --threshold 7    # Set pass threshold
```

### Learner (Auto-Learning)
```bash
python tools/brain/learner.py --learn "Task completed"
python tools/brain/learner.py --watch
python tools/brain/learner.py --stats
```

### A/B Tester (Compare Options)
```bash
python tools/brain/ab_tester.py --create "Test description"
python tools/brain/ab_tester.py --compare --test-id TEST-001
python tools/brain/ab_tester.py --select A --test-id TEST-001
```

### Model Optimizer (Token Efficiency)
```bash
python tools/brain/model_optimizer.py --recommend "Task description"
python tools/brain/model_optimizer.py --record --model "gemini-2.5" --tokens 1500
```

### Self-Improver (Create Improvement Plans)
```bash
python tools/brain/self_improver.py --analyze  # Analyze all data
python tools/brain/self_improver.py --plan     # Create improvement plan
python tools/brain/self_improver.py --apply-plan PLAN-ID
```

## State Management
```bash
python tools/brain/brain_cli.py init 1          # Initialize sprint
python tools/brain/brain_cli.py status          # Check status
python tools/brain/brain_cli.py transition STATE --reason "Reason"
python tools/brain/brain_cli.py validate        # Validate state
python tools/brain/brain_cli.py rollback        # Rollback
```

## Supervisor Commands
```bash
python tools/brain/brain_cli.py watch   # Monitor workflows
python tools/brain/brain_cli.py route "request"  # Route to workflow
python tools/brain/brain_cli.py health  # Health check
```

## Sync Commands
```bash
python tools/neo4j/brain_parallel.py --sync  # Quick sync
python tools/neo4j/brain_parallel.py --full  # Full sync
```

#brain #root-layer #meta-controller
