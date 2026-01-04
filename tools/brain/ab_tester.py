#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brain A/B Tester

Layer 1 Root Component: For small tasks, generate 2 options, compare, select better.

The A/B Tester enables self-improvement by:
- Detecting small tasks suitable for A/B testing
- Generating Option A and Option B approaches
- Comparing results using defined metrics
- Selecting winner and learning from comparison

Usage:
    python tools/brain/ab_tester.py --create "Task description"
    python tools/brain/ab_tester.py --compare --test-id TEST-001
    python tools/brain/ab_tester.py --select A --test-id TEST-001
    python tools/brain/ab_tester.py --stats
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


def get_tests_path() -> Path:
    """Get the A/B tests database path."""
    return get_project_root() / "docs" / ".brain-ab-tests.json"


def load_tests() -> Dict[str, Any]:
    """Load the A/B tests database."""
    tests_path = get_tests_path()
    if not tests_path.exists():
        return {
            "tests": [],
            "totalTests": 0,
            "optionAWins": 0,
            "optionBWins": 0,
            "createdAt": datetime.now().isoformat()
        }
    
    with open(tests_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_tests(data: Dict[str, Any]) -> None:
    """Save the A/B tests database."""
    tests_path = get_tests_path()
    tests_path.parent.mkdir(parents=True, exist_ok=True)
    data["lastUpdated"] = datetime.now().isoformat()
    data["totalTests"] = len(data.get("tests", []))
    
    with open(tests_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def generate_test_id() -> str:
    """Generate a unique test ID."""
    data = load_tests()
    count = len(data.get("tests", [])) + 1
    return f"TEST-{count:03d}"


def create_test(description: str) -> Dict[str, Any]:
    """
    Create a new A/B test.
    Returns the test with empty options to be filled.
    """
    test_id = generate_test_id()
    
    test = {
        "id": test_id,
        "description": description,
        "status": "PENDING",
        "optionA": {
            "description": "",
            "implemented": False,
            "score": None
        },
        "optionB": {
            "description": "",
            "implemented": False,
            "score": None
        },
        "winner": None,
        "createdAt": datetime.now().isoformat()
    }
    
    data = load_tests()
    data["tests"].append(test)
    save_tests(data)
    
    return test


def update_option(test_id: str, option: str, description: str, score: Optional[int] = None) -> Dict[str, Any]:
    """
    Update an option in an A/B test.
    """
    data = load_tests()
    
    for test in data["tests"]:
        if test["id"] == test_id:
            opt_key = f"option{option.upper()}"
            if opt_key in test:
                test[opt_key]["description"] = description
                test[opt_key]["implemented"] = True
                if score is not None:
                    test[opt_key]["score"] = score
                
                # Update status
                if test["optionA"]["implemented"] and test["optionB"]["implemented"]:
                    test["status"] = "READY_TO_COMPARE"
                
                save_tests(data)
                return test
    
    return {"error": f"Test {test_id} not found"}


def compare_test(test_id: str) -> Dict[str, Any]:
    """
    Compare options in an A/B test.
    """
    data = load_tests()
    
    for test in data["tests"]:
        if test["id"] == test_id:
            if test["status"] != "READY_TO_COMPARE":
                return {"error": "Test not ready for comparison. Both options must be implemented."}
            
            score_a = test["optionA"].get("score", 5)
            score_b = test["optionB"].get("score", 5)
            
            comparison = {
                "testId": test_id,
                "optionA": {
                    "description": test["optionA"]["description"],
                    "score": score_a
                },
                "optionB": {
                    "description": test["optionB"]["description"],
                    "score": score_b
                },
                "recommendation": "A" if score_a >= score_b else "B",
                "margin": abs(score_a - score_b)
            }
            
            return comparison
    
    return {"error": f"Test {test_id} not found"}


def select_winner(test_id: str, winner: str, reason: str = "") -> Dict[str, Any]:
    """
    Select the winner of an A/B test.
    """
    data = load_tests()
    
    for test in data["tests"]:
        if test["id"] == test_id:
            test["winner"] = winner.upper()
            test["winReason"] = reason
            test["status"] = "COMPLETED"
            test["completedAt"] = datetime.now().isoformat()
            
            # Update stats
            if winner.upper() == "A":
                data["optionAWins"] = data.get("optionAWins", 0) + 1
            else:
                data["optionBWins"] = data.get("optionBWins", 0) + 1
            
            save_tests(data)
            return test
    
    return {"error": f"Test {test_id} not found"}


def list_tests(status: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List all A/B tests.
    """
    data = load_tests()
    tests = data.get("tests", [])
    
    if status:
        tests = [t for t in tests if t.get("status") == status]
    
    return tests


def get_stats() -> Dict[str, Any]:
    """Get A/B testing statistics."""
    data = load_tests()
    
    completed = sum(1 for t in data.get("tests", []) if t.get("status") == "COMPLETED")
    
    return {
        "totalTests": data.get("totalTests", 0),
        "completedTests": completed,
        "optionAWins": data.get("optionAWins", 0),
        "optionBWins": data.get("optionBWins", 0),
        "pendingTests": data.get("totalTests", 0) - completed
    }


def print_test(test: Dict[str, Any]):
    """Print test details."""
    print(f"🔬 A/B Test: {test['id']}")
    print("━" * 50)
    print(f"Description: {test['description']}")
    print(f"Status: {test['status']}")
    print()
    print(f"Option A: {test['optionA'].get('description', 'Not set')}")
    print(f"  Score: {test['optionA'].get('score', 'N/A')}")
    print()
    print(f"Option B: {test['optionB'].get('description', 'Not set')}")
    print(f"  Score: {test['optionB'].get('score', 'N/A')}")
    
    if test.get("winner"):
        print()
        print(f"🏆 Winner: Option {test['winner']}")
        if test.get("winReason"):
            print(f"   Reason: {test['winReason']}")
    print("━" * 50)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Brain A/B Tester - Layer 1 Root Component")
    parser.add_argument("--create", type=str, help="Create new A/B test")
    parser.add_argument("--update", type=str, help="Update option (A or B)")
    parser.add_argument("--desc", type=str, help="Description for option")
    parser.add_argument("--score", type=int, help="Score for option (1-10)")
    parser.add_argument("--compare", action="store_true", help="Compare options")
    parser.add_argument("--select", type=str, help="Select winner (A or B)")
    parser.add_argument("--reason", type=str, default="", help="Reason for selection")
    parser.add_argument("--test-id", type=str, help="Test ID")
    parser.add_argument("--list", action="store_true", help="List all tests")
    parser.add_argument("--stats", action="store_true", help="Show statistics")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    try:
        if args.create:
            test = create_test(args.create)
            if args.json:
                print(json.dumps(test, indent=2))
            else:
                print(f"✅ Created A/B Test: {test['id']}")
                print(f"   Description: {test['description']}")
                print()
                print("Next steps:")
                print(f"  1. Update Option A: --update A --desc \"...\" --score N --test-id {test['id']}")
                print(f"  2. Update Option B: --update B --desc \"...\" --score N --test-id {test['id']}")
                print(f"  3. Compare: --compare --test-id {test['id']}")
                print(f"  4. Select winner: --select A/B --test-id {test['id']}")
        
        elif args.update and args.test_id and args.desc:
            result = update_option(args.test_id, args.update, args.desc, args.score)
            if "error" in result:
                print(f"❌ {result['error']}")
            else:
                print(f"✅ Updated Option {args.update.upper()} for {args.test_id}")
        
        elif args.compare and args.test_id:
            result = compare_test(args.test_id)
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                if "error" in result:
                    print(f"❌ {result['error']}")
                else:
                    print("🔬 Comparison Result")
                    print("━" * 50)
                    print(f"Option A: {result['optionA']['description'][:50]}...")
                    print(f"  Score: {result['optionA']['score']}")
                    print()
                    print(f"Option B: {result['optionB']['description'][:50]}...")
                    print(f"  Score: {result['optionB']['score']}")
                    print()
                    print(f"🏆 Recommendation: Option {result['recommendation']}")
                    print(f"   Margin: {result['margin']} points")
        
        elif args.select and args.test_id:
            result = select_winner(args.test_id, args.select, args.reason)
            if "error" in result:
                print(f"❌ {result['error']}")
            else:
                print(f"🏆 Winner selected: Option {args.select.upper()}")
        
        elif args.list:
            tests = list_tests()
            if args.json:
                print(json.dumps(tests, indent=2))
            else:
                print("🔬 A/B Tests")
                print("━" * 50)
                for test in tests:
                    status_icon = "✅" if test["status"] == "COMPLETED" else "⏳"
                    print(f"{status_icon} {test['id']}: {test['description'][:40]}...")
        
        elif args.stats:
            stats = get_stats()
            if args.json:
                print(json.dumps(stats, indent=2))
            else:
                print("📊 A/B Testing Statistics")
                print("━" * 50)
                print(f"Total Tests: {stats['totalTests']}")
                print(f"Completed: {stats['completedTests']}")
                print(f"Option A Wins: {stats['optionAWins']}")
                print(f"Option B Wins: {stats['optionBWins']}")
                print(f"Pending: {stats['pendingTests']}")
        
        else:
            stats = get_stats()
            print("🔬 Brain A/B Tester - Layer 1 Root Component")
            print("━" * 50)
            print(f"Total Tests: {stats['totalTests']}")
            print(f"Pending: {stats['pendingTests']}")
            print()
            print("Commands:")
            print("  --create \"description\"  Create new test")
            print("  --list                  List all tests")
            print("  --stats                 Show statistics")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
