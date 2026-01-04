#!/usr/bin/env python3
"""
Release Management Tools
Automates changelog generation and version management for the agentic-sdlc project.

Features:
- Parse git commits using conventional commit format
- Generate changelog entries grouped by type
- Bump version following semver
- Create git tags for releases

Usage:
    python tools/release/release.py preview          # Preview changes
    python tools/release/release.py changelog        # Generate changelog
    python tools/release/release.py version --auto   # Auto-bump version
    python tools/release/release.py release          # Full release cycle

Research: KB-2026-01-03-001 (Release Automation)
Pattern: Conventional Commits + Semver
"""

import os
import sys
import re
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.common import (
    print_header, print_success, print_error, print_warning, print_info,
    get_project_root, read_file, write_file, get_date
)


# Conventional commit types and their changelog categories
COMMIT_TYPES = {
    'feat': ('Added', 'New features'),
    'fix': ('Fixed', 'Bug fixes'),
    'docs': ('Documentation', 'Documentation changes'),
    'refactor': ('Changed', 'Code refactoring'),
    'perf': ('Performance', 'Performance improvements'),
    'test': ('Testing', 'Test additions and changes'),
    'chore': ('Maintenance', 'Build and maintenance'),
    'style': ('Style', 'Code style changes'),
    'ci': ('CI/CD', 'Continuous integration'),
    'build': ('Build', 'Build system changes'),
}

# Scope to tag mapping for changelog entries
SCOPE_TAGS = {
    'landing': 'Landing Page',
    'agent': 'Agent System',
    'workflow': 'Workflows',
    'kb': 'Knowledge Base',
    'tools': 'Tools',
    'docs': 'Docs',
    'ui': 'UI',
    'api': 'API',
    'test': 'Testing',
    'monorepo': 'Monorepo',
}


class ReleaseManager:
    """Manages changelog generation and version bumping."""
    
    def __init__(self, project_root: Path = None):
        self.root = project_root or get_project_root()
        self.changelog_path = self.root / 'CHANGELOG.md'
        self.package_path = self.root / 'package.json'
        
    def get_current_version(self) -> str:
        """Get current version from package.json."""
        try:
            with open(self.package_path, 'r') as f:
                data = json.load(f)
            return data.get('version', '0.0.0')
        except Exception as e:
            print_error(f"Failed to read version: {e}")
            return '0.0.0'
    
    def parse_version(self, version: str) -> Tuple[int, int, int]:
        """Parse version string into tuple."""
        match = re.match(r'^(\d+)\.(\d+)\.(\d+)', version)
        if match:
            return int(match.group(1)), int(match.group(2)), int(match.group(3))
        return 0, 0, 0
    
    def bump_version(self, bump_type: str, current: str = None) -> str:
        """Bump version based on type (major, minor, patch)."""
        if current is None:
            current = self.get_current_version()
        
        major, minor, patch = self.parse_version(current)
        
        if bump_type == 'major':
            return f"{major + 1}.0.0"
        elif bump_type == 'minor':
            return f"{major}.{minor + 1}.0"
        else:  # patch
            return f"{major}.{minor}.{patch + 1}"
    
    def get_last_tag(self) -> Optional[str]:
        """Get the last git tag."""
        try:
            result = subprocess.run(
                ['git', 'describe', '--tags', '--abbrev=0'],
                capture_output=True, text=True, cwd=self.root
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except Exception:
            pass
        return None
    
    def get_commits_since(self, since: str = None) -> List[Dict]:
        """Get commits since a reference (tag or date)."""
        cmd = ['git', 'log', '--pretty=format:%H|%s|%ad', '--date=short']
        
        if since:
            cmd.append(f'{since}..HEAD')
        else:
            # If no tag, get last 50 commits
            cmd.extend(['-n', '50'])
        
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, cwd=self.root
            )
            commits = []
            for line in result.stdout.strip().split('\n'):
                if '|' in line:
                    parts = line.split('|', 2)
                    if len(parts) >= 3:
                        commits.append({
                            'hash': parts[0][:7],
                            'message': parts[1],
                            'date': parts[2]
                        })
            return commits
        except Exception as e:
            print_error(f"Failed to get commits: {e}")
            return []
    
    def parse_commit(self, message: str) -> Optional[Dict]:
        """Parse a conventional commit message."""
        # Pattern: type(scope): description
        # or: type: description
        # Pattern: type(scope)!: description or type!: description
        # Regex: (type)(optional scope)(optional !): (description)
        pattern = r'^(\w+)(?:\(([^)]+)\))?(!)?\s*:\s*(.+)$'
        match = re.match(pattern, message, re.IGNORECASE)
        
        if match:
            commit_type = match.group(1).lower()
            scope = match.group(2)
            is_breaking_char = match.group(3) == '!'
            description = match.group(4)
            
            # Check for breaking change indicator
            breaking = is_breaking_char or 'BREAKING' in message.upper().split(':')[0]
            
            return {
                'type': commit_type,
                'scope': scope,
                'description': description,
                'breaking': breaking
            }
        return None
    
    def categorize_commits(self, commits: List[Dict]) -> Dict[str, List[Dict]]:
        """Categorize commits by type."""
        categories = {category: [] for category, _ in COMMIT_TYPES.values()}
        categories['Other'] = []
        
        for commit in commits:
            parsed = self.parse_commit(commit['message'])
            if parsed:
                commit_type = parsed['type']
                if commit_type in COMMIT_TYPES:
                    category, _ = COMMIT_TYPES[commit_type]
                    entry = {
                        'description': parsed['description'],
                        'scope': parsed['scope'],
                        'hash': commit['hash'],
                        'date': commit['date'],
                        'breaking': parsed['breaking']
                    }
                    categories[category].append(entry)
            else:
                # Non-conventional commits go to Other
                categories['Other'].append({
                    'description': commit['message'],
                    'scope': None,
                    'hash': commit['hash'],
                    'date': commit['date'],
                    'breaking': False
                })
        
        # Remove empty categories
        return {k: v for k, v in categories.items() if v}
    
    def detect_bump_type(self, commits: List[Dict]) -> str:
        """Auto-detect version bump type based on commits."""
        has_breaking = False
        has_feature = False
        
        for commit in commits:
            parsed = self.parse_commit(commit['message'])
            if parsed:
                if parsed['breaking']:
                    has_breaking = True
                if parsed['type'] == 'feat':
                    has_feature = True
        
        if has_breaking:
            return 'major'
        elif has_feature:
            return 'minor'
        return 'patch'
    
    def format_entry(self, entry: Dict) -> str:
        """Format a single changelog entry."""
        scope = entry.get('scope')
        desc = entry['description']
        
        # Format scope tag
        if scope:
            tag = SCOPE_TAGS.get(scope.lower(), scope.title())
            return f"- [{tag}] {desc}"
        return f"- {desc}"
    
    def generate_changelog_section(self, 
                                   categories: Dict[str, List[Dict]], 
                                   version: str,
                                   sprint: int = None) -> str:
        """Generate a changelog section."""
        lines = []
        date = get_date()
        
        # Header
        if sprint:
            lines.append(f"## [{version}] - {date} (Sprint {sprint})")
        else:
            lines.append(f"## [{version}] - {date}")
        lines.append("")
        
        # Categories
        for category, entries in categories.items():
            if entries:
                lines.append(f"### {category}")
                for entry in entries:
                    lines.append(self.format_entry(entry))
                lines.append("")
        
        return '\n'.join(lines)
    
    def update_changelog(self, new_section: str, dry_run: bool = False) -> bool:
        """Update CHANGELOG.md with new section."""
        try:
            content = read_file(self.changelog_path)
            if content is None:
                return False
            
            # Find the [Unreleased] section and insert after it
            unreleased_pattern = r'(## \[Unreleased\].*?)(\n---|\n## \[)'
            match = re.search(unreleased_pattern, content, re.DOTALL)
            
            if match:
                # Insert new section after [Unreleased] content
                insert_pos = match.end(1)
                separator = match.group(2)
                
                # Clear unreleased section and add new version
                unreleased_header = "## [Unreleased]\n\n"
                new_content = (
                    content[:match.start()] + 
                    unreleased_header + 
                    "---\n\n" +
                    new_section + 
                    "\n" +
                    content[match.end(1):]
                )
            else:
                # No unreleased section found, prepend
                header_end = content.find('\n## ')
                if header_end == -1:
                    header_end = content.find('\n---')
                if header_end == -1:
                    header_end = len(content)
                
                new_content = (
                    content[:header_end] + 
                    "\n\n" + new_section + 
                    content[header_end:]
                )
            
            if dry_run:
                print_info("DRY RUN - Would update CHANGELOG.md")
                print(new_section)
                return True
            
            return write_file(self.changelog_path, new_content)
        except Exception as e:
            print_error(f"Failed to update changelog: {e}")
            return False
    
    def update_version(self, new_version: str, dry_run: bool = False) -> bool:
        """Update version in package.json."""
        try:
            with open(self.package_path, 'r') as f:
                data = json.load(f)
            
            old_version = data.get('version', '0.0.0')
            data['version'] = new_version
            
            if dry_run:
                print_info(f"DRY RUN - Would update version: {old_version} → {new_version}")
                return True
            
            with open(self.package_path, 'w') as f:
                json.dump(data, f, indent=2)
                f.write('\n')  # Add trailing newline
            
            print_success(f"Updated version: {old_version} → {new_version}")
            return True
        except Exception as e:
            print_error(f"Failed to update version: {e}")
            return False
    
    def create_tag(self, version: str, dry_run: bool = False) -> bool:
        """Create a git tag for the release."""
        tag = f"v{version}"
        
        if dry_run:
            print_info(f"DRY RUN - Would create tag: {tag}")
            return True
        
        try:
            result = subprocess.run(
                ['git', 'tag', '-a', tag, '-m', f'Release {version}'],
                capture_output=True, text=True, cwd=self.root
            )
            if result.returncode == 0:
                print_success(f"Created tag: {tag}")
                return True
            else:
                print_error(f"Failed to create tag: {result.stderr}")
                return False
        except Exception as e:
            print_error(f"Failed to create tag: {e}")
            return False

    def commit_changes(self, version: str, dry_run: bool = False) -> bool:
        """Commit release files."""
        if dry_run:
            print_info(f"DRY RUN - Would commit changes as: chore(release): v{version}")
            return True
            
        try:
            print_info("Committing release changes...")
            # Configure git user if needed? Assuming env is set.
            
            # Add files
            subprocess.run(['git', 'add', 'package.json', 'CHANGELOG.md'], check=True, cwd=self.root)
            
            # Commit
            msg = f"chore(release): v{version}"
            subprocess.run(['git', 'commit', '-m', msg], check=True, cwd=self.root)
            
            print_success("Changes committed successfully!")
            return True
        except Exception as e:
            print_error(f"Failed to commit: {e}")
            return False

    def push_changes(self, dry_run: bool = False) -> bool:
        """Push changes and tags to remote."""
        if dry_run:
            print_info("DRY RUN - Would push changes and tags")
            return True
            
        try:
            print_info("Pushing changes...")
            subprocess.run(['git', 'push'], check=True, cwd=self.root)
            
            print_info("Pushing tags...")
            subprocess.run(['git', 'push', '--tags'], check=True, cwd=self.root)
            
            print_success("Changes and tags pushed successfully!")
            return True
        except Exception as e:
            print_error(f"Failed to push: {e}")
            return False

    def publish_package(self, dry_run: bool = False) -> bool:
        """Publish package to npm/bun registry."""
        if dry_run:
            print_info("DRY RUN - Would publish to registry")
            return True
            
        try:
            # Check if private
            with open(self.package_path, 'r') as f:
                data = json.load(f)
            
            if data.get('private') is True:
                print_warning("Package is marked as private. Skipping publish.")
                return False
            
            cmd = ['npm', 'publish']
                
            print_info(f"Publishing with {' '.join(cmd)}...")
            subprocess.run(cmd, check=True, cwd=self.root)
            
            print_success("Package published successfully!")
            return True
        except Exception as e:
            print_error(f"Failed to publish: {e}")
            return False


def cmd_preview(manager: ReleaseManager, args):
    """Preview changes without applying."""
    print_header("Release Preview")
    
    last_tag = manager.get_last_tag()
    print_info(f"Last tag: {last_tag or 'None'}")
    
    current_version = manager.get_current_version()
    print_info(f"Current version: {current_version}")
    
    commits = manager.get_commits_since(last_tag)
    print_info(f"Commits since last release: {len(commits)}")
    
    if not commits:
        print_warning("No new commits found.")
        return
    
    categories = manager.categorize_commits(commits)
    bump_type = manager.detect_bump_type(commits)
    new_version = manager.bump_version(bump_type, current_version)
    
    print_info(f"Detected bump type: {bump_type}")
    print_info(f"New version would be: {new_version}")
    
    print("\n" + "="*60)
    print("CHANGELOG PREVIEW:")
    print("="*60 + "\n")
    
    section = manager.generate_changelog_section(
        categories, new_version, sprint=args.sprint if hasattr(args, 'sprint') else None
    )
    print(section)


def cmd_changelog(manager: ReleaseManager, args):
    """Generate changelog entries."""
    print_header("Generating Changelog")
    
    last_tag = manager.get_last_tag()
    commits = manager.get_commits_since(last_tag)
    
    if not commits:
        print_warning("No new commits found.")
        return
    
    categories = manager.categorize_commits(commits)
    
    # Determine version
    if args.version:
        new_version = args.version
    else:
        current = manager.get_current_version()
        bump = args.bump or manager.detect_bump_type(commits)
        new_version = manager.bump_version(bump, current)
    
    section = manager.generate_changelog_section(
        categories, new_version, sprint=args.sprint
    )
    
    if manager.update_changelog(section, dry_run=args.dry_run):
        if not args.dry_run:
            print_success("Changelog updated successfully!")


def cmd_version(manager: ReleaseManager, args):
    """Bump version."""
    print_header("Version Bump")
    
    current = manager.get_current_version()
    print_info(f"Current version: {current}")
    
    # Determine bump type
    if args.auto:
        last_tag = manager.get_last_tag()
        commits = manager.get_commits_since(last_tag)
        bump_type = manager.detect_bump_type(commits)
        print_info(f"Auto-detected bump type: {bump_type}")
    elif args.bump:
        bump_type = args.bump
    else:
        print_error("Specify --auto or --bump [major|minor|patch]")
        return
    
    new_version = manager.bump_version(bump_type, current)
    print_info(f"New version: {new_version}")
    
    manager.update_version(new_version, dry_run=args.dry_run)


def cmd_release(manager: ReleaseManager, args):
    """Full release cycle."""
    print_header("Full Release")
    
    # 1. Get commits
    last_tag = manager.get_last_tag()
    commits = manager.get_commits_since(last_tag)
    
    if not commits:
        print_warning("No new commits found. Nothing to release.")
        return
    
    categories = manager.categorize_commits(commits)
    
    # 2. Determine version
    current = manager.get_current_version()
    if args.version:
        new_version = args.version
    else:
        bump = args.bump or manager.detect_bump_type(commits)
        new_version = manager.bump_version(bump, current)
    
    print_info(f"Releasing: {current} → {new_version}")
    
    # 3. Generate changelog
    section = manager.generate_changelog_section(
        categories, new_version, sprint=args.sprint
    )
    
    if not manager.update_changelog(section, dry_run=args.dry_run):
        print_error("Failed to update changelog. Aborting.")
        return
    
    # 4. Update version
    if not manager.update_version(new_version, dry_run=args.dry_run):
        print_error("Failed to update version. Aborting.")
        return
    
    # 5. Commit changes (optional but recommended before tagging)
    if args.commit:
        if not manager.commit_changes(new_version, dry_run=args.dry_run):
            print_error("Failed to commit changes.")
            # Continue? Or abort? Aborting seems safer for tagging.
            if not args.dry_run:
                return

    # 6. Create tag (optional)
    if args.tag and not args.dry_run:
        manager.create_tag(new_version, dry_run=args.dry_run)
    
    # 7. Push changes (optional)
    if args.push:
        manager.push_changes(dry_run=args.dry_run)
        
    # 8. Publish package (optional)
    if args.publish:
        manager.publish_package(dry_run=args.dry_run)
    
    if not args.dry_run:
        print_success(f"Release {new_version} completed!")
        if not args.push:
            print_info("Don't forget to: git push && git push --tags")


def main():
    parser = argparse.ArgumentParser(
        description='Release management for agentic-sdlc',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python release.py preview                    Preview changes
  python release.py changelog --sprint 5       Generate changelog for Sprint 5
  python release.py version --auto             Auto-detect version bump
  python release.py version --bump minor       Bump minor version
  python release.py release --bump patch       Full release with patch bump
  python release.py release --tag              Release and create git tag
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Preview command
    preview_parser = subparsers.add_parser('preview', help='Preview changes')
    preview_parser.add_argument('--sprint', type=int, help='Sprint number')
    
    # Changelog command
    changelog_parser = subparsers.add_parser('changelog', help='Generate changelog')
    changelog_parser.add_argument('--sprint', type=int, help='Sprint number')
    changelog_parser.add_argument('--version', help='Explicit version')
    changelog_parser.add_argument('--bump', choices=['major', 'minor', 'patch'])
    changelog_parser.add_argument('--dry-run', action='store_true', help='Preview only')
    
    # Version command
    version_parser = subparsers.add_parser('version', help='Bump version')
    version_parser.add_argument('--auto', action='store_true', help='Auto-detect bump type')
    version_parser.add_argument('--bump', choices=['major', 'minor', 'patch'])
    version_parser.add_argument('--dry-run', action='store_true', help='Preview only')
    
    # Release command
    release_parser = subparsers.add_parser('release', help='Full release cycle')
    release_parser.add_argument('--sprint', type=int, help='Sprint number')
    release_parser.add_argument('--version', help='Explicit version')
    release_parser.add_argument('--bump', choices=['major', 'minor', 'patch'])
    release_parser.add_argument('--commit', action='store_true', help='Commit release files')
    release_parser.add_argument('--tag', action='store_true', help='Create git tag')
    release_parser.add_argument('--push', action='store_true', help='Push changes and tags')
    release_parser.add_argument('--publish', action='store_true', help='Publish to npm/bun registry')
    release_parser.add_argument('--dry-run', action='store_true', help='Preview only')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    manager = ReleaseManager()
    
    commands = {
        'preview': cmd_preview,
        'changelog': cmd_changelog,
        'version': cmd_version,
        'release': cmd_release,
    }
    
    commands[args.command](manager, args)


if __name__ == '__main__':
    main()
