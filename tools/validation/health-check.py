#!/usr/bin/env python3
"""
System Health Check
Validates project structure and configuration
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.common import (
    print_header, print_success, print_error, print_warning,
    get_project_root, file_exists
)
from utils.kb_manager import get_kb_stats
from utils.artifact_manager import get_current_sprint, get_sprint_dir


def check_directory_structure():
    """Check if required directories exist"""
    print_header("Checking Directory Structure")
    
    root = get_project_root()
    required_dirs = [
        '.agent',
        '.agent/roles',
        '.agent/workflows',
        '.agent/templates',
        '.agent/knowledge-base',
        'tools',
        'docs/sprints'
    ]
    
    all_good = True
    for dir_path in required_dirs:
        full_path = root / dir_path
        if full_path.exists():
            print_success(f"✓ {dir_path}")
        else:
            print_error(f"✗ {dir_path} - MISSING")
            all_good = False
    
    return all_good


def check_knowledge_base():
    """Check knowledge base health"""
    print_header("Checking Knowledge Base")
    
    stats = get_kb_stats()
    
    print_success(f"✓ Total entries: {stats['total_entries']}")
    print_success(f"✓ Categories: {len(stats['by_category'])}")
    
    if stats['total_entries'] == 0:
        print_warning("⚠ No KB entries found - consider documenting learnings")
    
    return True


def check_current_sprint():
    """Check current sprint configuration"""
    print_header("Checking Current Sprint")
    
    sprint = get_current_sprint()
    sprint_dir = get_sprint_dir()
    
    print_success(f"✓ Current sprint: {sprint}")
    
    if sprint_dir.exists():
        print_success(f"✓ Sprint directory exists: {sprint_dir}")
    else:
        print_warning(f"⚠ Sprint directory missing: {sprint_dir}")
    
    return True


def check_configuration():
    """Check configuration files"""
    print_header("Checking Configuration")
    
    root = get_project_root()
    config_files = [
        '.agent/CONFIG.md',
        '.agent/USAGE.md',
        '.agent/README.md'
    ]
    
    all_good = True
    for config_file in config_files:
        if file_exists(root / config_file):
            print_success(f"✓ {config_file}")
        else:
            print_error(f"✗ {config_file} - MISSING")
            all_good = False
    
    return all_good


def main():
    """Run all health checks"""
    print_header("System Health Check")
    
    checks = [
        ("Directory Structure", check_directory_structure),
        ("Knowledge Base", check_knowledge_base),
        ("Current Sprint", check_current_sprint),
        ("Configuration", check_configuration)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print_error(f"Check failed: {str(e)}")
            results.append((name, False))
    
    # Summary
    print_header("Health Check Summary")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"  {name}: {status}")
    
    print(f"\nOverall: {passed}/{total} checks passed")
    
    if passed == total:
        print_success("\n✓ System is healthy!")
        sys.exit(0)
    else:
        print_error("\n✗ System has issues - please review")
        sys.exit(1)


if __name__ == "__main__":
    main()
