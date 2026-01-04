#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brain Learner

Layer 1 Root Component: Auto-learning when tasks/features complete.

The Learner is the "memory" that:
- Monitors for completed tasks/features
- Automatically triggers /compound learning
- Captures knowledge to the Knowledge Base
- Updates Neo4j and indexes

Usage:
    python tools/brain/learner.py --watch
    python tools/brain/learner.py --learn "Task completed: User authentication"
    python tools/brain/learner.py --stats
"""

import json
import sys
import subprocess
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


def get_tools_dir() -> Path:
    """Get the tools directory."""
    return Path(__file__).parent.parent


def get_learner_log_path() -> Path:
    """Get the learner log path."""
    return get_project_root() / "docs" / ".brain-learner-log.json"


def load_learner_log() -> Dict[str, Any]:
    """Load the learner log."""
    log_path = get_learner_log_path()
    if not log_path.exists():
        return {
            "learnings": [],
            "totalLearnings": 0,
            "autoLearnEnabled": True,
            "createdAt": datetime.now().isoformat()
        }
    
    with open(log_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_learner_log(log: Dict[str, Any]) -> None:
    """Save the learner log."""
    log_path = get_learner_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log["lastUpdated"] = datetime.now().isoformat()
    log["totalLearnings"] = len(log.get("learnings", []))
    
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=2, ensure_ascii=False)


def trigger_compound(description: str) -> Dict[str, Any]:
    """
    Trigger the compound learning workflow.
    """
    # Run KB index update
    kb_cli = get_project_root() / "bin" / "kb_cli.py"
    neo4j_sync = get_tools_dir() / "neo4j" / "sync_skills_to_neo4j.py"
    learning_engine = get_tools_dir() / "neo4j" / "learning_engine.py"
    
    results = {
        "description": description,
        "timestamp": datetime.now().isoformat(),
        "steps": []
    }
    
    # Step 1: Update KB Index
    try:
        if kb_cli.exists():
            subprocess.run(
                [sys.executable, str(kb_cli), "update-index"],
                capture_output=True,
                text=True,
                timeout=60
            )
            results["steps"].append({"step": "KB Index Update", "status": "success"})
    except Exception as e:
        results["steps"].append({"step": "KB Index Update", "status": "failed", "error": str(e)})
    
    # Step 2: Sync to Neo4j (if available)
    try:
        if neo4j_sync.exists():
            subprocess.run(
                [sys.executable, str(neo4j_sync)],
                capture_output=True,
                text=True,
                timeout=120
            )
            results["steps"].append({"step": "Neo4j Sync", "status": "success"})
    except Exception as e:
        results["steps"].append({"step": "Neo4j Sync", "status": "skipped", "error": str(e)})
    
    # Step 3: Record success in learning engine
    try:
        if learning_engine.exists():
            subprocess.run(
                [sys.executable, str(learning_engine), 
                 "--record-success", description,
                 "--task-type", "feature"],
                capture_output=True,
                text=True,
                timeout=60
            )
            results["steps"].append({"step": "Learning Engine", "status": "success"})
    except Exception as e:
        results["steps"].append({"step": "Learning Engine", "status": "skipped", "error": str(e)})
    
    results["success"] = all(s.get("status") in ["success", "skipped"] for s in results["steps"])
    
    return results


def learn(description: str) -> Dict[str, Any]:
    """
    Trigger learning for a completed task.
    """
    log = load_learner_log()
    
    if not log.get("autoLearnEnabled", True):
        return {
            "status": "disabled",
            "message": "Auto-learning is disabled"
        }
    
    # Trigger compound learning
    result = trigger_compound(description)
    
    # Record learning
    learning = {
        "description": description,
        "timestamp": datetime.now().isoformat(),
        "success": result.get("success", False),
        "steps": result.get("steps", [])
    }
    
    log["learnings"].append(learning)
    save_learner_log(log)
    
    return {
        "status": "learned" if result["success"] else "partial",
        "description": description,
        "steps": result["steps"]
    }


def watch() -> Dict[str, Any]:
    """
    Watch mode - check for completed tasks that need learning.
    """
    project_root = get_project_root()
    
    # Check for recently modified files in KB
    kb_dir = project_root / ".agent" / "knowledge-base"
    recent_entries = []
    
    if kb_dir.exists():
        for md_file in kb_dir.rglob("*.md"):
            if md_file.name != "INDEX.md":
                stat = md_file.stat()
                # Modified in last hour
                if (datetime.now().timestamp() - stat.st_mtime) < 3600:
                    recent_entries.append(str(md_file.relative_to(project_root)))
    
    return {
        "status": "watching",
        "recentEntries": len(recent_entries),
        "entries": recent_entries[:10],  # Last 10
        "message": "Learner is active and monitoring for completed tasks"
    }


def toggle_auto_learn(enabled: bool) -> Dict[str, Any]:
    """Toggle auto-learning."""
    log = load_learner_log()
    log["autoLearnEnabled"] = enabled
    save_learner_log(log)
    return {"autoLearnEnabled": enabled}


def get_stats() -> Dict[str, Any]:
    """Get learner statistics."""
    log = load_learner_log()
    
    successful = sum(1 for l in log.get("learnings", []) if l.get("success"))
    
    return {
        "totalLearnings": log.get("totalLearnings", 0),
        "successfulLearnings": successful,
        "autoLearnEnabled": log.get("autoLearnEnabled", True),
        "lastUpdated": log.get("lastUpdated")
    }


def print_stats():
    """Print learner statistics."""
    stats = get_stats()
    
    print("🎓 Brain Learner Statistics")
    print("━" * 50)
    print(f"Total Learnings: {stats['totalLearnings']}")
    print(f"Successful: {stats['successfulLearnings']}")
    print(f"Auto-Learn: {'✅ Enabled' if stats['autoLearnEnabled'] else '❌ Disabled'}")
    print(f"Last Updated: {stats['lastUpdated'] or 'Never'}")
    print("━" * 50)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Brain Learner - Layer 1 Root Component")
    parser.add_argument("--watch", action="store_true", help="Watch for completed tasks")
    parser.add_argument("--learn", type=str, help="Trigger learning for a task")
    parser.add_argument("--enable", action="store_true", help="Enable auto-learning")
    parser.add_argument("--disable", action="store_true", help="Disable auto-learning")
    parser.add_argument("--stats", action="store_true", help="Show statistics")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    try:
        if args.learn:
            result = learn(args.learn)
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print(f"🎓 Learning triggered: {args.learn}")
                for step in result.get("steps", []):
                    status = "✅" if step["status"] == "success" else "⚠️"
                    print(f"  {status} {step['step']}")
        
        elif args.watch:
            result = watch()
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print("👁️ Learner Watch Mode")
                print("━" * 50)
                print(f"Status: {result['status']}")
                print(f"Recent KB entries: {result['recentEntries']}")
                for entry in result.get("entries", []):
                    print(f"  📄 {entry}")
        
        elif args.enable:
            result = toggle_auto_learn(True)
            print("✅ Auto-learning enabled")
        
        elif args.disable:
            result = toggle_auto_learn(False)
            print("❌ Auto-learning disabled")
        
        elif args.stats:
            if args.json:
                print(json.dumps(get_stats(), indent=2))
            else:
                print_stats()
        
        else:
            print_stats()
            print()
            print("Commands:")
            print("  --learn \"description\"  Trigger learning")
            print("  --watch               Watch mode")
            print("  --enable/--disable    Toggle auto-learn")
            print("  --stats               Show statistics")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
