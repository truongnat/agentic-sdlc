"""
Release Tools Package
Provides automated changelog generation and version management.
"""

from pathlib import Path

__version__ = "1.0.0"
__all__ = ["ReleaseManager"]

# Package directory
PACKAGE_DIR = Path(__file__).parent
