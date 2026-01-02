#!/usr/bin/env python3
"""
Knowledge Base Search Tool
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.common import print_header, print_info, print_error
from utils.kb_manager import search_kb


def main():
    """Search knowledge base"""
    if len(sys.argv) < 2:
        print_error("Usage: search.py <query> [category] [priority]")
        print_error("Example: search.py 'authentication bug'")
        print_error("Example: search.py 'performance' --category=performance")
        sys.exit(1)
    
    query = sys.argv[1]
    category = None
    priority = None
    
    # Parse optional arguments
    for arg in sys.argv[2:]:
        if arg.startswith('--category='):
            category = arg.split('=')[1]
        elif arg.startswith('--priority='):
            priority = arg.split('=')[1]
    
    print_header(f"Searching KB: {query}")
    
    results = search_kb(query, category, priority)
    
    if not results:
        print_info("No results found")
        return
    
    print_info(f"Found {len(results)} results:\n")
    
    for i, result in enumerate(results, 1):
        print(f"{i}. [{result['priority'].upper()}] {result['title']}")
        print(f"   Category: {result['category']} | Date: {result['date']}")
        print(f"   File: {result['file']}")
        print(f"   Tags: {', '.join(result['tags'])}\n")


if __name__ == "__main__":
    main()
