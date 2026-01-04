#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brain Self-Improver

Layer 1 Root Component: Brain creates self-improvement plans based on feedback
from A/B Tester, Judge, and Learner.

The Self-Improver:
- Analyzes results from A/B tests
- Reviews Judge scores patterns
- Learns from success/failure patterns
- Creates improvement plans for the Brain itself

Usage:
    python tools/brain/self_improver.py --analyze
    python tools/brain/self_improver.py --plan
    python tools/brain/self_improver.py --apply-plan
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


def get_improvement_path() -> Path:
    """Get the improvement plans path."""
    return get_project_root() / "docs" / ".brain-improvements.json"


def load_improvements() -> Dict[str, Any]:
    """Load improvement plans."""
    path = get_improvement_path()
    if not path.exists():
        return {
            "plans": [],
            "insights": [],
            "appliedImprovements": 0,
            "createdAt": datetime.now().isoformat()
        }
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_improvements(data: Dict[str, Any]) -> None:
    """Save improvement plans."""
    path = get_improvement_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    data["lastUpdated"] = datetime.now().isoformat()
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_ab_tests() -> Dict[str, Any]:
    """Load A/B test data."""
    path = get_project_root() / "docs" / ".brain-ab-tests.json"
    if not path.exists():
        return {"tests": []}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_scores() -> Dict[str, Any]:
    """Load Judge scores."""
    path = get_project_root() / "docs" / ".brain-scores.json"
    if not path.exists():
        return {"scores": []}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_learner_log() -> Dict[str, Any]:
    """Load Learner log."""
    path = get_project_root() / "docs" / ".brain-learner-log.json"
    if not path.exists():
        return {"learnings": []}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def analyze_data() -> Dict[str, Any]:
    """
    Analyze data from all Root components to find patterns.
    """
    ab_tests = load_ab_tests()
    scores = load_scores()
    learner = load_learner_log()
    
    insights = []
    
    # Analyze A/B Tests
    completed_tests = [t for t in ab_tests.get("tests", []) if t.get("status") == "COMPLETED"]
    if completed_tests:
        option_a_wins = sum(1 for t in completed_tests if t.get("winner") == "A")
        option_b_wins = sum(1 for t in completed_tests if t.get("winner") == "B")
        
        if option_a_wins > option_b_wins * 2:
            insights.append({
                "source": "A/B Tester",
                "finding": "Option A (first approach) wins significantly more",
                "suggestion": "First instinct approaches are often better - trust initial solutions"
            })
        elif option_b_wins > option_a_wins * 2:
            insights.append({
                "source": "A/B Tester",
                "finding": "Option B (alternative approach) wins significantly more",
                "suggestion": "Consider exploring alternative approaches more often"
            })
    
    # Analyze Judge Scores
    all_scores = scores.get("scores", [])
    if all_scores:
        avg_score = sum(s.get("finalScore", 0) for s in all_scores) / len(all_scores)
        failed = [s for s in all_scores if not s.get("passed")]
        
        if avg_score < 6:
            insights.append({
                "source": "Judge",
                "finding": f"Average score is low ({avg_score:.1f}/10)",
                "suggestion": "Improve report quality - add more detail, follow templates"
            })
        
        if failed:
            # Find common failure patterns
            low_scores = {}
            for s in failed:
                for category, score in s.get("scores", {}).items():
                    if score < 5:
                        low_scores[category] = low_scores.get(category, 0) + 1
            
            if low_scores:
                worst_category = max(low_scores, key=low_scores.get)
                insights.append({
                    "source": "Judge",
                    "finding": f"Reports consistently fail in '{worst_category}'",
                    "suggestion": f"Focus on improving {worst_category} in reports"
                })
    
    # Analyze Learner
    learnings = learner.get("learnings", [])
    if learnings:
        successful = sum(1 for l in learnings if l.get("success"))
        success_rate = (successful / len(learnings)) * 100 if learnings else 0
        
        if success_rate < 80:
            insights.append({
                "source": "Learner",
                "finding": f"Learning capture success rate is low ({success_rate:.0f}%)",
                "suggestion": "Ensure KB and Neo4j are properly configured"
            })
    
    return {
        "analyzed": True,
        "timestamp": datetime.now().isoformat(),
        "insights": insights,
        "summary": {
            "abTestsCompleted": len(completed_tests) if 'completed_tests' in dir() else 0,
            "reportsScored": len(all_scores) if 'all_scores' in dir() else 0,
            "learningsRecorded": len(learnings) if 'learnings' in dir() else 0
        }
    }


def create_improvement_plan() -> Dict[str, Any]:
    """
    Create an improvement plan based on analysis.
    """
    analysis = analyze_data()
    insights = analysis.get("insights", [])
    
    if not insights:
        return {
            "status": "NO_PLAN_NEEDED",
            "message": "No significant issues found. System is performing well."
        }
    
    # Create plan from insights
    actions = []
    for i, insight in enumerate(insights):
        actions.append({
            "id": f"ACTION-{i+1}",
            "source": insight["source"],
            "action": insight["suggestion"],
            "priority": "high" if "consistently" in insight.get("finding", "").lower() else "medium",
            "status": "PENDING"
        })
    
    plan = {
        "id": f"PLAN-{datetime.now().strftime('%Y%m%d-%H%M')}",
        "createdAt": datetime.now().isoformat(),
        "status": "CREATED",
        "insights": insights,
        "actions": actions,
        "summary": f"{len(actions)} improvement actions identified"
    }
    
    # Save plan
    data = load_improvements()
    data["plans"].append(plan)
    data["insights"].extend(insights)
    save_improvements(data)
    
    return plan


def apply_plan(plan_id: str) -> Dict[str, Any]:
    """
    Mark a plan as applied and record the improvements.
    """
    data = load_improvements()
    
    for plan in data["plans"]:
        if plan["id"] == plan_id:
            plan["status"] = "APPLIED"
            plan["appliedAt"] = datetime.now().isoformat()
            data["appliedImprovements"] += 1
            save_improvements(data)
            return {"status": "APPLIED", "planId": plan_id}
    
    return {"error": f"Plan {plan_id} not found"}


def get_stats() -> Dict[str, Any]:
    """Get Self-Improver statistics."""
    data = load_improvements()
    
    pending_plans = sum(1 for p in data.get("plans", []) if p.get("status") == "CREATED")
    
    return {
        "totalPlans": len(data.get("plans", [])),
        "pendingPlans": pending_plans,
        "appliedImprovements": data.get("appliedImprovements", 0),
        "totalInsights": len(data.get("insights", []))
    }


def print_analysis(analysis: Dict[str, Any]):
    """Print analysis results."""
    print("🔍 Brain Self-Analysis")
    print("━" * 50)
    print()
    
    summary = analysis.get("summary", {})
    print(f"Data Analyzed:")
    print(f"  A/B Tests: {summary.get('abTestsCompleted', 0)}")
    print(f"  Reports Scored: {summary.get('reportsScored', 0)}")
    print(f"  Learnings: {summary.get('learningsRecorded', 0)}")
    print()
    
    insights = analysis.get("insights", [])
    if insights:
        print(f"🔎 Insights Found: {len(insights)}")
        for i, insight in enumerate(insights):
            print(f"\n  {i+1}. [{insight['source']}]")
            print(f"     Finding: {insight['finding']}")
            print(f"     Suggestion: {insight['suggestion']}")
    else:
        print("✅ No issues found - System is performing well")
    
    print()
    print("━" * 50)


def print_plan(plan: Dict[str, Any]):
    """Print improvement plan."""
    print("📋 Brain Self-Improvement Plan")
    print("━" * 50)
    print(f"Plan ID: {plan.get('id', 'N/A')}")
    print(f"Status: {plan.get('status', 'UNKNOWN')}")
    print()
    
    actions = plan.get("actions", [])
    if actions:
        print(f"Actions ({len(actions)}):")
        for action in actions:
            priority = "🔴" if action["priority"] == "high" else "🟡"
            print(f"\n  {priority} {action['id']}: {action['action']}")
            print(f"     Source: {action['source']}")
    else:
        print("No actions needed")
    
    print()
    print("━" * 50)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Brain Self-Improver - Layer 1 Root Component")
    parser.add_argument("--analyze", action="store_true", help="Analyze data from all components")
    parser.add_argument("--plan", action="store_true", help="Create improvement plan")
    parser.add_argument("--apply-plan", type=str, help="Apply an improvement plan")
    parser.add_argument("--stats", action="store_true", help="Show statistics")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    try:
        if args.analyze:
            result = analyze_data()
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print_analysis(result)
        
        elif args.plan:
            plan = create_improvement_plan()
            if args.json:
                print(json.dumps(plan, indent=2))
            else:
                if plan.get("status") == "NO_PLAN_NEEDED":
                    print("✅ No improvements needed at this time")
                else:
                    print_plan(plan)
        
        elif args.apply_plan:
            result = apply_plan(args.apply_plan)
            if "error" in result:
                print(f"❌ {result['error']}")
            else:
                print(f"✅ Plan {args.apply_plan} applied")
        
        elif args.stats:
            stats = get_stats()
            if args.json:
                print(json.dumps(stats, indent=2))
            else:
                print("📊 Self-Improver Statistics")
                print("━" * 50)
                print(f"Total Plans: {stats['totalPlans']}")
                print(f"Pending: {stats['pendingPlans']}")
                print(f"Applied: {stats['appliedImprovements']}")
                print(f"Total Insights: {stats['totalInsights']}")
        
        else:
            stats = get_stats()
            print("🧠 Brain Self-Improver - Layer 1 Root Component")
            print("━" * 50)
            print(f"Plans Created: {stats['totalPlans']}")
            print(f"Improvements Applied: {stats['appliedImprovements']}")
            print()
            print("Commands:")
            print("  --analyze      Analyze all component data")
            print("  --plan         Create improvement plan")
            print("  --apply-plan X Apply a plan")
            print("  --stats        Show statistics")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
