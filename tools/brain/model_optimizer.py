#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brain Model Optimizer

Layer 1 Root Component: Select optimal AI model for each task type.

The Model Optimizer helps optimize cost/performance by:
- Tracking token usage per model
- Analyzing task complexity
- Recommending fast vs. powerful models
- Optimizing cost/performance ratio

Usage:
    python tools/brain/model_optimizer.py --recommend "Task description"
    python tools/brain/model_optimizer.py --record --model "gemini-2.0" --tokens 1500 --task "feature"
    python tools/brain/model_optimizer.py --stats
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


def get_optimizer_path() -> Path:
    """Get the optimizer database path."""
    return get_project_root() / "docs" / ".brain-model-optimizer.json"


def load_optimizer_data() -> Dict[str, Any]:
    """Load the optimizer database."""
    path = get_optimizer_path()
    if not path.exists():
        return {
            "models": {
                "gemini-2.5-pro": {
                    "tier": "powerful",
                    "avgTokens": 0,
                    "usageCount": 0,
                    "successRate": 0,
                    "recommendFor": ["complex", "architecture", "security"]
                },
                "gemini-2.5-flash": {
                    "tier": "fast",
                    "avgTokens": 0,
                    "usageCount": 0,
                    "successRate": 0,
                    "recommendFor": ["simple", "formatting", "quick-fixes"]
                },
                "gemini-2.0-flash": {
                    "tier": "balanced",
                    "avgTokens": 0,
                    "usageCount": 0,
                    "successRate": 0,
                    "recommendFor": ["general", "coding", "testing"]
                }
            },
            "taskTypes": {
                "simple": {"preferredTier": "fast", "avgComplexity": 2},
                "general": {"preferredTier": "balanced", "avgComplexity": 5},
                "complex": {"preferredTier": "powerful", "avgComplexity": 8},
                "architecture": {"preferredTier": "powerful", "avgComplexity": 9},
                "security": {"preferredTier": "powerful", "avgComplexity": 8},
                "feature": {"preferredTier": "balanced", "avgComplexity": 6},
                "bug": {"preferredTier": "balanced", "avgComplexity": 5},
                "docs": {"preferredTier": "fast", "avgComplexity": 3}
            },
            "usageHistory": [],
            "totalTokens": 0,
            "createdAt": datetime.now().isoformat()
        }
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_optimizer_data(data: Dict[str, Any]) -> None:
    """Save the optimizer database."""
    path = get_optimizer_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    data["lastUpdated"] = datetime.now().isoformat()
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Task complexity keywords
COMPLEXITY_KEYWORDS = {
    "simple": ["format", "rename", "typo", "comment", "cleanup"],
    "general": ["implement", "add", "create", "update", "modify"],
    "complex": ["refactor", "optimize", "migrate", "integrate", "architecture"],
    "security": ["auth", "security", "encrypt", "permission", "vulnerability"],
    "docs": ["document", "readme", "changelog", "guide", "tutorial"]
}


def analyze_task(description: str) -> Dict[str, Any]:
    """
    Analyze task description to determine complexity.
    """
    desc_lower = description.lower()
    
    # Check keywords
    detected_type = "general"
    for task_type, keywords in COMPLEXITY_KEYWORDS.items():
        if any(kw in desc_lower for kw in keywords):
            detected_type = task_type
            break
    
    # Estimate complexity based on description length and type
    base_complexity = 5
    if len(description) > 100:
        base_complexity += 2
    if len(description) > 200:
        base_complexity += 1
    
    if detected_type in ["complex", "security", "architecture"]:
        base_complexity += 2
    elif detected_type in ["simple", "docs"]:
        base_complexity -= 2
    
    complexity = max(1, min(10, base_complexity))
    
    return {
        "taskType": detected_type,
        "complexity": complexity,
        "descriptionLength": len(description)
    }


def recommend_model(description: str) -> Dict[str, Any]:
    """
    Recommend the optimal model for a task.
    """
    data = load_optimizer_data()
    analysis = analyze_task(description)
    
    task_type = analysis["taskType"]
    complexity = analysis["complexity"]
    
    # Get preferred tier for this task type
    task_config = data["taskTypes"].get(task_type, {"preferredTier": "balanced"})
    preferred_tier = task_config["preferredTier"]
    
    # Find best model in preferred tier
    recommended_model = None
    for model_name, model_info in data["models"].items():
        if model_info["tier"] == preferred_tier:
            recommended_model = model_name
            break
    
    # Fallback
    if not recommended_model:
        recommended_model = "gemini-2.0-flash"
    
    return {
        "task": description[:100],
        "analysis": analysis,
        "recommendedModel": recommended_model,
        "tier": preferred_tier,
        "reason": f"Task type '{task_type}' with complexity {complexity}/10 suits '{preferred_tier}' tier"
    }


def record_usage(model: str, tokens: int, task_type: str, success: bool = True) -> Dict[str, Any]:
    """
    Record model usage for learning.
    """
    data = load_optimizer_data()
    
    # Update model stats
    if model in data["models"]:
        model_data = data["models"][model]
        old_count = model_data["usageCount"]
        old_avg = model_data["avgTokens"]
        
        # Update average tokens
        new_count = old_count + 1
        new_avg = ((old_avg * old_count) + tokens) / new_count
        
        model_data["usageCount"] = new_count
        model_data["avgTokens"] = round(new_avg, 0)
        
        # Update success rate
        if success:
            old_success = model_data.get("successRate", 100)
            model_data["successRate"] = round(((old_success * old_count) + 100) / new_count, 1)
        else:
            old_success = model_data.get("successRate", 100)
            model_data["successRate"] = round(((old_success * old_count) + 0) / new_count, 1)
    
    # Record in history
    data["usageHistory"].append({
        "model": model,
        "tokens": tokens,
        "taskType": task_type,
        "success": success,
        "timestamp": datetime.now().isoformat()
    })
    
    # Keep only last 100 records
    data["usageHistory"] = data["usageHistory"][-100:]
    
    # Update total tokens
    data["totalTokens"] = data.get("totalTokens", 0) + tokens
    
    save_optimizer_data(data)
    
    return {
        "recorded": True,
        "model": model,
        "tokens": tokens,
        "totalTokens": data["totalTokens"]
    }


def get_stats() -> Dict[str, Any]:
    """Get optimizer statistics."""
    data = load_optimizer_data()
    
    model_stats = []
    for model_name, model_info in data["models"].items():
        model_stats.append({
            "model": model_name,
            "tier": model_info["tier"],
            "usageCount": model_info["usageCount"],
            "avgTokens": model_info["avgTokens"],
            "successRate": model_info.get("successRate", 0)
        })
    
    return {
        "models": model_stats,
        "totalTokens": data.get("totalTokens", 0),
        "totalUsages": len(data.get("usageHistory", []))
    }


def print_recommendation(result: Dict[str, Any]):
    """Print model recommendation."""
    print("🤖 Model Recommendation")
    print("━" * 50)
    print(f"Task: {result['task']}...")
    print()
    print(f"Analysis:")
    print(f"  Type: {result['analysis']['taskType']}")
    print(f"  Complexity: {result['analysis']['complexity']}/10")
    print()
    print(f"📌 Recommended: {result['recommendedModel']}")
    print(f"   Tier: {result['tier'].upper()}")
    print(f"   Reason: {result['reason']}")
    print("━" * 50)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Brain Model Optimizer - Layer 1 Root Component")
    parser.add_argument("--recommend", type=str, help="Get model recommendation for task")
    parser.add_argument("--record", action="store_true", help="Record model usage")
    parser.add_argument("--model", type=str, help="Model name for recording")
    parser.add_argument("--tokens", type=int, help="Token count for recording")
    parser.add_argument("--task", type=str, help="Task type for recording")
    parser.add_argument("--failed", action="store_true", help="Mark as failed usage")
    parser.add_argument("--stats", action="store_true", help="Show statistics")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    try:
        if args.recommend:
            result = recommend_model(args.recommend)
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print_recommendation(result)
        
        elif args.record and args.model and args.tokens:
            result = record_usage(
                args.model,
                args.tokens,
                args.task or "general",
                not args.failed
            )
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print(f"✅ Recorded: {args.model} used {args.tokens} tokens")
                print(f"   Total tokens: {result['totalTokens']}")
        
        elif args.stats:
            stats = get_stats()
            if args.json:
                print(json.dumps(stats, indent=2))
            else:
                print("📊 Model Optimizer Statistics")
                print("━" * 50)
                print(f"Total Tokens Used: {stats['totalTokens']:,}")
                print(f"Total Usage Records: {stats['totalUsages']}")
                print()
                print("Model Performance:")
                for m in stats["models"]:
                    print(f"  {m['model']}")
                    print(f"    Tier: {m['tier']}")
                    print(f"    Usage: {m['usageCount']}")
                    print(f"    Avg Tokens: {m['avgTokens']:,.0f}")
                    print(f"    Success: {m['successRate']}%")
        
        else:
            stats = get_stats()
            print("🤖 Brain Model Optimizer - Layer 1 Root Component")
            print("━" * 50)
            print(f"Total Tokens: {stats['totalTokens']:,}")
            print()
            print("Commands:")
            print("  --recommend \"task\"   Get model recommendation")
            print("  --record --model X --tokens N --task T  Record usage")
            print("  --stats             Show statistics")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
