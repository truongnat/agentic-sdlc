#!/usr/bin/env python3
"""
Update Knowledge Base Index
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.common import print_header, print_success
from utils.kb_manager import update_kb_index


def main():
    """Update KB index"""
    print_header("Updating Knowledge Base Index")
    
    if update_kb_index():
        print_success("KB index updated successfully")
    else:
        print_error("Failed to update KB index")
        sys.exit(1)


if __name__ == "__main__":
    main()
