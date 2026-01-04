#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brain Judge

Layer 1 Root Component: Scores all results, requires mandatory reports.

The Judge is the "quality controller" that:
- Every action MUST have a report
- Scores reports on: completeness, quality, compliance
- Blocks progression if score < threshold
- Feeds scores to Learning Engine

Usage:
    python tools/brain/judge.py --score "path/to/report.md"
    python tools/brain/judge.py --review --sprint 1
    python tools/brain/judge.py --threshold 7
"""

import json
import sys
import re
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


def get_scores_path() -> Path:
    """Get the scores database path."""
    return get_project_root() / "docs" / ".brain-scores.json"


def load_scores() -> Dict[str, Any]:
    """Load the scores database."""
    scores_path = get_scores_path()
    if not scores_path.exists():
        return {
            "scores": [],
            "averageScore": 0,
            "totalReviews": 0,
            "passThreshold": 6,
            "createdAt": datetime.now().isoformat()
        }
    
    with open(scores_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_scores(data: Dict[str, Any]) -> None:
    """Save the scores database."""
    scores_path = get_scores_path()
    scores_path.parent.mkdir(parents=True, exist_ok=True)
    data["lastUpdated"] = datetime.now().isoformat()
    
    # Recalculate average
    if data["scores"]:
        total = sum(s.get("score", 0) for s in data["scores"])
        data["averageScore"] = round(total / len(data["scores"]), 2)
        data["totalReviews"] = len(data["scores"])
    
    with open(scores_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Scoring Rubric
RUBRIC = {
    "completeness": {
        "weight": 3,
        "criteria": [
            "Has problem description",
            "Has solution description",
            "Has artifacts listed",
            "Has next steps"
        ]
    },
    "quality": {
        "weight": 3,
        "criteria": [
            "Clear and readable",
            "Proper formatting",
            "No placeholder text",
            "Professional language"
        ]
    },
    "compliance": {
        "weight": 4,
        "criteria": [
            "Follows template",
            "Correct file location",
            "Has required tags",
            "Links to related docs"
        ]
    }
}


def score_report(report_path: str) -> Dict[str, Any]:
    """
    Score a report file based on the rubric.
    Returns score breakdown and total.
    """
    path = Path(report_path)
    if not path.exists():
        return {
            "error": f"Report not found: {report_path}",
            "score": 0,
            "passed": False
        }
    
    content = path.read_text(encoding='utf-8')
    
    scores = {}
    total_weight = 0
    weighted_score = 0
    
    # Score completeness
    completeness_score = 0
    if re.search(r'##.*problem|##.*issue|##.*challenge', content, re.I):
        completeness_score += 2.5
    if re.search(r'##.*solution|##.*fix|##.*implementation', content, re.I):
        completeness_score += 2.5
    if re.search(r'##.*artifact|##.*output|##.*deliverable', content, re.I):
        completeness_score += 2.5
    if re.search(r'##.*next|##.*todo|##.*action', content, re.I):
        completeness_score += 2.5
    scores["completeness"] = min(completeness_score, 10)
    
    # Score quality
    quality_score = 5  # Base score
    if len(content) > 500:
        quality_score += 2
    if "```" in content:  # Has code blocks
        quality_score += 1.5
    if "[TODO]" not in content and "[PLACEHOLDER]" not in content:
        quality_score += 1.5
    scores["quality"] = min(quality_score, 10)
    
    # Score compliance
    compliance_score = 0
    if content.startswith("---"):  # Has frontmatter
        compliance_score += 2
    if re.search(r'#[a-z-]+', content):  # Has tags
        compliance_score += 2
    if path.parent.name in ["plans", "designs", "reports", "logs"]:
        compliance_score += 3
    if re.search(r'\[.*\]\(.*\.md\)', content):  # Has links
        compliance_score += 3
    scores["compliance"] = min(compliance_score, 10)
    
    # Calculate weighted total
    for category, details in RUBRIC.items():
        weighted_score += scores[category] * details["weight"]
        total_weight += details["weight"] * 10
    
    final_score = round((weighted_score / total_weight) * 10, 1)
    
    # Load threshold
    data = load_scores()
    threshold = data.get("passThreshold", 6)
    
    result = {
        "file": str(path),
        "scores": scores,
        "finalScore": final_score,
        "passed": final_score >= threshold,
        "threshold": threshold,
        "timestamp": datetime.now().isoformat()
    }
    
    # Save to database
    data["scores"].append(result)
    save_scores(data)
    
    return result


def review_sprint(sprint: int) -> Dict[str, Any]:
    """
    Review all reports in a sprint.
    """
    project_root = get_project_root()
    sprint_dir = project_root / "docs" / "sprints" / f"sprint-{sprint}"
    
    if not sprint_dir.exists():
        return {"error": f"Sprint {sprint} not found"}
    
    results = []
    
    # Find all markdown files in sprint directories
    for subdir in ["plans", "designs", "reports", "logs"]:
        dir_path = sprint_dir / subdir
        if dir_path.exists():
            for md_file in dir_path.glob("*.md"):
                if not md_file.name.startswith("."):
                    result = score_report(str(md_file))
                    results.append(result)
    
    # Calculate sprint average
    if results:
        avg = sum(r.get("finalScore", 0) for r in results) / len(results)
    else:
        avg = 0
    
    return {
        "sprint": sprint,
        "totalReports": len(results),
        "averageScore": round(avg, 1),
        "results": results
    }


def set_threshold(value: int) -> Dict[str, Any]:
    """Set the pass threshold."""
    data = load_scores()
    data["passThreshold"] = value
    save_scores(data)
    return {"threshold": value, "message": f"Threshold set to {value}"}


def get_stats() -> Dict[str, Any]:
    """Get scoring statistics."""
    data = load_scores()
    return {
        "totalReviews": data.get("totalReviews", 0),
        "averageScore": data.get("averageScore", 0),
        "passThreshold": data.get("passThreshold", 6),
        "lastUpdated": data.get("lastUpdated")
    }


def print_score(result: Dict[str, Any]):
    """Print score result."""
    print("⚖️ Judge Score Report")
    print("━" * 50)
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return
    
    print(f"📄 File: {result['file']}")
    print()
    
    for category, score in result.get("scores", {}).items():
        bar = "█" * int(score) + "░" * (10 - int(score))
        print(f"  {category.capitalize():15} [{bar}] {score}/10")
    
    print()
    print(f"📊 Final Score: {result['finalScore']}/10")
    
    if result.get("passed"):
        print(f"✅ PASSED (threshold: {result['threshold']})")
    else:
        print(f"❌ FAILED (threshold: {result['threshold']})")
    
    print("━" * 50)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Brain Judge - Layer 1 Root Component")
    parser.add_argument("--score", type=str, help="Score a report file")
    parser.add_argument("--review", action="store_true", help="Review sprint reports")
    parser.add_argument("--sprint", type=int, help="Sprint number for review")
    parser.add_argument("--threshold", type=int, help="Set pass threshold (1-10)")
    parser.add_argument("--stats", action="store_true", help="Show scoring statistics")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    try:
        if args.score:
            result = score_report(args.score)
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print_score(result)
        
        elif args.review and args.sprint:
            result = review_sprint(args.sprint)
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print(f"📋 Sprint {args.sprint} Review")
                print("━" * 50)
                print(f"Total Reports: {result['totalReports']}")
                print(f"Average Score: {result['averageScore']}/10")
                for r in result.get("results", []):
                    status = "✅" if r.get("passed") else "❌"
                    print(f"  {status} {Path(r['file']).name}: {r['finalScore']}/10")
        
        elif args.threshold:
            result = set_threshold(args.threshold)
            print(f"✅ {result['message']}")
        
        elif args.stats:
            stats = get_stats()
            if args.json:
                print(json.dumps(stats, indent=2))
            else:
                print("📊 Judge Statistics")
                print("━" * 50)
                print(f"Total Reviews: {stats['totalReviews']}")
                print(f"Average Score: {stats['averageScore']}/10")
                print(f"Pass Threshold: {stats['passThreshold']}/10")
        
        else:
            stats = get_stats()
            print("⚖️ Brain Judge - Layer 1 Root Component")
            print("━" * 50)
            print(f"Total Reviews: {stats['totalReviews']}")
            print(f"Average Score: {stats['averageScore']}/10")
            print(f"Pass Threshold: {stats['passThreshold']}/10")
            print()
            print("Commands:")
            print("  --score <file>     Score a report")
            print("  --review --sprint N  Review sprint")
            print("  --threshold N      Set threshold")
            print("  --stats            Show statistics")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
