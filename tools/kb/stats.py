#!/usr/bin/env python3
"""
Knowledge Base Statistics
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.common import print_header, print_info
from utils.kb_manager import get_kb_stats


def main():
    """Display KB statistics"""
    print_header("Knowledge Base Statistics")
    
    stats = get_kb_stats()
    
    print_info(f"Total Entries: {stats['total_entries']}\n")
    
    print("By Category:")
    for category, count in sorted(stats['by_category'].items()):
        print(f"  {category}: {count}")
    
    print("\nBy Priority:")
    for priority, count in sorted(stats['by_priority'].items()):
        print(f"  {priority}: {count}")
    
    print("\nRecent Entries:")
    for entry in stats['recent_entries'][:5]:
        print(f"  - {entry['title']} ({entry['date']})")


if __name__ == "__main__":
    main()
