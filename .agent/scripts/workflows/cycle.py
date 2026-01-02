#!/usr/bin/env python3
"""
Cycle Workflow - Complete Task Lifecycle
Executes: Research → Plan → Work → Review → Compound
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from utils.common import (
        print_header, print_success, print_error, print_info,
        get_project_root, ensure_dir, load_config
    )
    from utils.kb_manager import search_kb, create_kb_entry
    from utils.artifact_manager import create_artifact, get_current_sprint
except ImportError:
    print("Error: Required utility modules not found. Run setup first.")
    sys.exit(1)


def search_knowledge_base(task_description):
    """Search KB for similar patterns"""
    print_header("Step 1: Search Knowledge Base")
    
    results = search_kb(task_description)
    
    if results:
        print_success(f"Found {len(results)} related KB entries:")
        for i, result in enumerate(results[:5], 1):
            print(f"  {i}. {result['title']} ({result['category']})")
        return results
    else:
        print_info("No related KB entries found. Starting fresh.")
        return []


def plan_task(task_description, kb_results):
    """Create task plan"""
    print_header("Step 2: Plan Task")
    
    plan = {
        "task": task_description,
        "timestamp": datetime.now().isoformat(),
        "kb_references": [r['title'] for r in kb_results[:3]],
        "steps": [
            "Analyze requirements",
            "Review related KB entries",
            "Implement solution",
            "Test locally",
            "Document changes"
        ],
        "estimated_time": "< 4 hours"
    }
    
    print_info(f"Task: {task_description}")
    print_info(f"Estimated time: {plan['estimated_time']}")
    print_info(f"KB references: {len(plan['kb_references'])}")
    
    return plan


def execute_task(plan):
    """Execute the planned task"""
    print_header("Step 3: Execute Task")
    
    print_info("This step requires manual implementation.")
    print_info("After completing the task:")
    print_info("  1. Test your changes locally")
    print_info("  2. Commit with: git commit -m '[TASK-ID] Description'")
    print_info("  3. Continue to review step")
    
    response = input("\nTask completed? (y/n): ").strip().lower()
    
    if response != 'y':
        print_error("Task not completed. Exiting workflow.")
        sys.exit(1)
    
    return True


def review_task(plan):
    """Review task completion"""
    print_header("Step 4: Review Task")
    
    checklist = [
        "Code follows project standards",
        "Local testing passed",
        "Changes committed to git",
        "Documentation updated"
    ]
    
    print_info("Review checklist:")
    all_passed = True
    
    for item in checklist:
        response = input(f"  ✓ {item}? (y/n): ").strip().lower()
        if response != 'y':
            all_passed = False
            print_error(f"    Failed: {item}")
    
    if not all_passed:
        print_error("\nReview failed. Please address issues before continuing.")
        sys.exit(1)
    
    print_success("\nReview passed!")
    return True


def compound_knowledge(task_description, plan, attempts=1):
    """Create KB entry if task was complex"""
    print_header("Step 5: Compound Knowledge")
    
    if attempts < 3:
        print_info("Task was straightforward (< 3 attempts).")
        response = input("Create KB entry anyway? (y/n): ").strip().lower()
        if response != 'y':
            print_info("Skipping KB entry creation.")
            return None
    else:
        print_info(f"Task required {attempts} attempts - creating KB entry.")
    
    # Gather information for KB entry
    print_info("\nKB Entry Information:")
    
    category = input("Category (bug/feature/architecture/security/performance): ").strip()
    priority = input("Priority (critical/high/medium/low): ").strip()
    problem = input("Problem description: ").strip()
    solution = input("Solution summary: ").strip()
    
    entry_data = {
        "title": task_description,
        "category": category or "feature",
        "priority": priority or "medium",
        "sprint": get_current_sprint(),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "tags": [category, "cycle-workflow"],
        "attempts": attempts,
        "problem": problem,
        "solution": solution
    }
    
    kb_entry = create_kb_entry(entry_data)
    
    if kb_entry:
        print_success(f"KB entry created: {kb_entry}")
        return kb_entry
    else:
        print_error("Failed to create KB entry")
        return None


def generate_report(task_description, plan, kb_entry):
    """Generate cycle completion report"""
    print_header("Cycle Complete")
    
    report = {
        "task": task_description,
        "completed_at": datetime.now().isoformat(),
        "duration": plan.get("estimated_time", "< 4 hours"),
        "kb_entry": kb_entry,
        "status": "completed"
    }
    
    # Save report
    sprint = get_current_sprint()
    report_dir = get_project_root() / "docs" / "sprints" / sprint / "logs"
    ensure_dir(report_dir)
    
    report_file = report_dir / f"cycle-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print_success(f"\n✓ Task completed: {task_description}")
    print_info(f"✓ Report saved: {report_file}")
    if kb_entry:
        print_info(f"✓ Knowledge captured: {kb_entry}")
    
    return report


def main():
    """Main cycle workflow execution"""
    if len(sys.argv) < 2:
        print_error("Usage: cycle.py <task_description>")
        print_error("Example: cycle.py 'Add user avatar upload feature'")
        sys.exit(1)
    
    task_description = " ".join(sys.argv[1:])
    
    print_header(f"Cycle Workflow: {task_description}")
    
    try:
        # Step 1: Search KB
        kb_results = search_knowledge_base(task_description)
        
        # Step 2: Plan
        plan = plan_task(task_description, kb_results)
        
        # Step 3: Execute
        execute_task(plan)
        
        # Step 4: Review
        review_task(plan)
        
        # Step 5: Compound
        attempts = int(input("\nHow many attempts did this task require? (1-10): ").strip() or "1")
        kb_entry = compound_knowledge(task_description, plan, attempts)
        
        # Generate report
        generate_report(task_description, plan, kb_entry)
        
        print_success("\n🎉 Cycle workflow completed successfully!")
        
    except KeyboardInterrupt:
        print_error("\n\nWorkflow interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print_error(f"\n\nWorkflow failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
