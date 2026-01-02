#!/usr/bin/env python3
"""
Common utility functions for agent scripts
Cross-platform compatible
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime


# ANSI color codes (work on Windows 10+, macOS, Linux)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Enable ANSI colors on Windows
if sys.platform == 'win32':
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except:
        pass


def print_header(message):
    """Print header message"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{message}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}\n")


def print_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {message}{Colors.ENDC}")


def print_error(message):
    """Print error message"""
    print(f"{Colors.RED}✗ {message}{Colors.ENDC}", file=sys.stderr)


def print_warning(message):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.ENDC}")


def print_info(message):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ {message}{Colors.ENDC}")


def get_project_root():
    """Get project root directory"""
    # Start from script location and go up to find .agent directory
    current = Path(__file__).resolve()
    
    while current != current.parent:
        if (current / '.agent').exists():
            return current
        current = current.parent
    
    # Fallback to current working directory
    return Path.cwd()


def ensure_dir(path):
    """Ensure directory exists"""
    Path(path).mkdir(parents=True, exist_ok=True)
    return Path(path)


def load_config():
    """Load project configuration"""
    root = get_project_root()
    config_file = root / '.agent' / 'config.json'
    
    if config_file.exists():
        with open(config_file, 'r') as f:
            return json.load(f)
    
    # Default config
    return {
        "project_name": "TeamLifecycle Project",
        "current_sprint": "sprint-1",
        "kb_enabled": True,
        "auto_compound": True
    }


def save_config(config):
    """Save project configuration"""
    root = get_project_root()
    config_file = root / '.agent' / 'config.json'
    
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)


def get_timestamp():
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()


def get_date():
    """Get current date in YYYY-MM-DD format"""
    return datetime.now().strftime("%Y-%m-%d")


def read_file(filepath):
    """Read file content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print_error(f"Failed to read {filepath}: {str(e)}")
        return None


def write_file(filepath, content):
    """Write content to file"""
    try:
        ensure_dir(Path(filepath).parent)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print_error(f"Failed to write {filepath}: {str(e)}")
        return False


def append_file(filepath, content):
    """Append content to file"""
    try:
        ensure_dir(Path(filepath).parent)
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print_error(f"Failed to append to {filepath}: {str(e)}")
        return False


def list_files(directory, pattern="*"):
    """List files in directory matching pattern"""
    try:
        return list(Path(directory).glob(pattern))
    except Exception as e:
        print_error(f"Failed to list files in {directory}: {str(e)}")
        return []


def file_exists(filepath):
    """Check if file exists"""
    return Path(filepath).exists()


def confirm(message, default=False):
    """Ask user for confirmation"""
    default_str = "Y/n" if default else "y/N"
    response = input(f"{message} ({default_str}): ").strip().lower()
    
    if not response:
        return default
    
    return response in ['y', 'yes']


def select_option(message, options):
    """Let user select from options"""
    print(f"\n{message}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    
    while True:
        try:
            choice = input("\nSelect option (number): ").strip()
            index = int(choice) - 1
            if 0 <= index < len(options):
                return options[index]
            else:
                print_error("Invalid option. Try again.")
        except ValueError:
            print_error("Please enter a number.")
        except KeyboardInterrupt:
            print_error("\nCancelled by user.")
            sys.exit(1)


def format_duration(seconds):
    """Format duration in human-readable format"""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes}m"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h {minutes}m"


def truncate_string(text, max_length=80):
    """Truncate string to max length"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


if __name__ == "__main__":
    # Test utilities
    print_header("Testing Common Utilities")
    print_success("Success message")
    print_error("Error message")
    print_warning("Warning message")
    print_info("Info message")
    print(f"\nProject root: {get_project_root()}")
    print(f"Timestamp: {get_timestamp()}")
    print(f"Date: {get_date()}")
