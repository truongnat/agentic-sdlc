#!/usr/bin/env python3
"""
Universal script runner for agent workflows
Cross-platform entry point
"""

import sys
import subprocess
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("Usage: run.py <script> [args...]")
        print("\nAvailable scripts:")
        print("  Workflows:")
        print("    cycle <task>          - Complete task lifecycle")
        print("    housekeeping          - Maintenance and cleanup")
        print("  KB:")
        print("    kb-search <query>     - Search knowledge base")
        print("    kb-stats              - KB statistics")
        print("  Validation:")
        print("    health-check          - System health check")
        sys.exit(1)
    
    script_name = sys.argv[1]
    script_args = sys.argv[2:]
    
    # Map script names to files
    script_map = {
        'cycle': 'workflows/cycle.py',
        'housekeeping': 'workflows/housekeeping.py',
        'kb-search': 'kb/search.py',
        'kb-stats': 'kb/stats.py',
        'health-check': 'validation/health-check.py'
    }
    
    if script_name not in script_map:
        print(f"Error: Unknown script '{script_name}'")
        sys.exit(1)
    
    # Get script path
    scripts_dir = Path(__file__).parent
    script_path = scripts_dir / script_map[script_name]
    
    if not script_path.exists():
        print(f"Error: Script not found: {script_path}")
        sys.exit(1)
    
    # Run script
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)] + script_args,
            check=False
        )
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
