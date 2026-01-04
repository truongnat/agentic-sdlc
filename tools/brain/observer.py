#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brain Observer

Layer 1 Root Component: Monitors all actions, halts on errors, ensures compliance.

The Observer is the "eye" of the Brain that:
- Watches all workflow executions
- Detects violations of SDLC rules
- HALTS execution immediately on critical errors
- Alerts user for intervention

Usage:
    python tools/brain/observer.py --watch
    python tools/brain/observer.py --check
    python tools/brain/observer.py --halt "Critical error description"
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except:
        pass


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent.parent


def get_observer_log_path() -> Path:
    """Get the observer log file path."""
    return get_project_root() / "docs" / ".brain-observer-log.json"


def load_observer_log() -> Dict[str, Any]:
    """Load the observer log."""
    log_path = get_observer_log_path()
    if not log_path.exists():
        return {
            "status": "ACTIVE",
            "halted": False,
            "haltReason": None,
            "violations": [],
            "observations": [],
            "lastCheck": None,
            "createdAt": datetime.now().isoformat()
        }
    
    with open(log_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_observer_log(log: Dict[str, Any]) -> None:
    """Save the observer log."""
    log_path = get_observer_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log["lastUpdated"] = datetime.now().isoformat()
    
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=2, ensure_ascii=False)


# Violation Rules
SDLC_RULES = {
    "PHASE_ORDER": {
        "description": "Phases must execute in order",
        "severity": "critical"
    },
    "APPROVAL_GATE": {
        "description": "Approval gates must be respected",
        "severity": "critical"
    },
    "ARTIFACT_REQUIRED": {
        "description": "Required artifacts must exist",
        "severity": "high"
    },
    "REPORT_REQUIRED": {
        "description": "Every action must have a report",
        "severity": "medium"
    },
    "SCOPE_CREEP": {
        "description": "No features outside approved plan",
        "severity": "high"
    }
}


def check_violations() -> List[Dict[str, Any]]:
    """
    Check for SDLC rule violations.
    Returns list of detected violations.
    """
    violations = []
    project_root = get_project_root()
    
    # Check 1: Brain state exists and is valid
    sprints_dir = project_root / "docs" / "sprints"
    if sprints_dir.exists():
        for sprint_dir in sprints_dir.iterdir():
            if sprint_dir.is_dir() and sprint_dir.name.startswith("sprint-"):
                state_file = sprint_dir / ".brain-state.json"
                if state_file.exists():
                    with open(state_file, 'r', encoding='utf-8') as f:
                        state = json.load(f)
                    
                    # Check for invalid state
                    if state.get("currentState") not in [
                        "IDLE", "PLANNING", "PLAN_APPROVAL", "DESIGNING",
                        "DESIGN_REVIEW", "DEVELOPMENT", "TESTING", "BUG_FIXING",
                        "DEPLOYMENT", "REPORTING", "FINAL_REVIEW", "FINAL_APPROVAL", "COMPLETE"
                    ]:
                        violations.append({
                            "rule": "PHASE_ORDER",
                            "message": f"Invalid state: {state.get('currentState')}",
                            "severity": "critical",
                            "timestamp": datetime.now().isoformat()
                        })
    
    return violations


def observe() -> Dict[str, Any]:
    """
    Perform observation check on the system.
    Returns observation report.
    """
    log = load_observer_log()
    
    if log.get("halted"):
        return {
            "status": "HALTED",
            "reason": log.get("haltReason"),
            "message": "System is halted. Use --resume to continue."
        }
    
    # Check for violations
    violations = check_violations()
    
    # Record observation
    observation = {
        "timestamp": datetime.now().isoformat(),
        "violationsFound": len(violations),
        "violations": violations
    }
    
    log["observations"].append(observation)
    log["lastCheck"] = datetime.now().isoformat()
    
    # Auto-halt on critical violations
    critical_violations = [v for v in violations if v.get("severity") == "critical"]
    if critical_violations:
        log["halted"] = True
        log["haltReason"] = f"Critical violation: {critical_violations[0]['message']}"
        log["status"] = "HALTED"
    
    log["violations"].extend(violations)
    save_observer_log(log)
    
    return {
        "status": log["status"],
        "violationsFound": len(violations),
        "criticalViolations": len(critical_violations),
        "halted": log.get("halted", False)
    }


def halt(reason: str) -> Dict[str, Any]:
    """
    Manually halt the system.
    """
    log = load_observer_log()
    log["halted"] = True
    log["haltReason"] = reason
    log["status"] = "HALTED"
    log["violations"].append({
        "rule": "MANUAL_HALT",
        "message": reason,
        "severity": "critical",
        "timestamp": datetime.now().isoformat()
    })
    save_observer_log(log)
    
    return {"status": "HALTED", "reason": reason}


def resume() -> Dict[str, Any]:
    """
    Resume the system after halt.
    """
    log = load_observer_log()
    log["halted"] = False
    log["haltReason"] = None
    log["status"] = "ACTIVE"
    save_observer_log(log)
    
    return {"status": "ACTIVE", "message": "System resumed"}


def get_status() -> Dict[str, Any]:
    """
    Get current observer status.
    """
    log = load_observer_log()
    return {
        "status": log.get("status", "UNKNOWN"),
        "halted": log.get("halted", False),
        "haltReason": log.get("haltReason"),
        "totalViolations": len(log.get("violations", [])),
        "lastCheck": log.get("lastCheck")
    }


def print_status():
    """Print observer status."""
    status = get_status()
    
    print("👁️ Brain Observer Status")
    print("━" * 50)
    
    if status["halted"]:
        print(f"🛑 Status: HALTED")
        print(f"   Reason: {status['haltReason']}")
    else:
        print(f"✅ Status: {status['status']}")
    
    print(f"📊 Total Violations: {status['totalViolations']}")
    print(f"🕒 Last Check: {status['lastCheck'] or 'Never'}")
    print("━" * 50)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Brain Observer - Layer 1 Root Component")
    parser.add_argument("--watch", action="store_true", help="Perform observation check")
    parser.add_argument("--check", action="store_true", help="Alias for --watch")
    parser.add_argument("--halt", type=str, help="Halt the system with reason")
    parser.add_argument("--resume", action="store_true", help="Resume after halt")
    parser.add_argument("--status", action="store_true", help="Show current status")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    try:
        if args.halt:
            result = halt(args.halt)
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print(f"🛑 System HALTED: {args.halt}")
        
        elif args.resume:
            result = resume()
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print("✅ System resumed")
        
        elif args.watch or args.check:
            result = observe()
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                if result["halted"]:
                    print(f"🛑 HALTED: {result.get('status')}")
                    print(f"   Critical violations: {result.get('criticalViolations', 0)}")
                else:
                    print(f"✅ Observation complete")
                    print(f"   Violations found: {result.get('violationsFound', 0)}")
        
        elif args.status:
            if args.json:
                print(json.dumps(get_status(), indent=2))
            else:
                print_status()
        
        else:
            print_status()
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
