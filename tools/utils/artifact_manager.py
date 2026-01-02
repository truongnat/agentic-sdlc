#!/usr/bin/env python3
"""
Artifact Manager
Handles artifact creation and sprint management
"""

import os
from pathlib import Path
from datetime import datetime
from .common import (
    get_project_root, ensure_dir, load_config, save_config,
    print_success, print_error, print_info
)


def get_current_sprint():
    """Get current sprint name from config"""
    config = load_config()
    return config.get('current_sprint', 'sprint-1')


def set_current_sprint(sprint_name):
    """Set current sprint in config"""
    config = load_config()
    config['current_sprint'] = sprint_name
    save_config(config)
    print_success(f"Current sprint set to: {sprint_name}")


def get_sprint_dir(sprint_name=None):
    """Get sprint directory path"""
    if sprint_name is None:
        sprint_name = get_current_sprint()
    
    return get_project_root() / 'docs' / 'sprints' / sprint_name


def create_sprint_structure(sprint_name):
    """Create directory structure for a new sprint"""
    sprint_dir = get_sprint_dir(sprint_name)
    
    subdirs = ['plans', 'designs', 'reviews', 'logs', 'tests', 'reports']
    
    for subdir in subdirs:
        ensure_dir(sprint_dir / subdir)
    
    print_success(f"Sprint structure created: {sprint_dir}")
    return sprint_dir
