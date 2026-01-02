#!/usr/bin/env python3
"""
Knowledge Base Manager
Handles KB search, creation, and indexing
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from .common import (
    get_project_root, ensure_dir, read_file, write_file,
    print_success, print_error, print_info
)


def get_kb_root():
    """Get knowledge base root directory"""
    return get_project_root() / '.agent' / 'knowledge-base'


def get_kb_index():
    """Get KB index file path"""
    return get_kb_root() / 'INDEX.md'


def parse_yaml_frontmatter(content):
    """Parse YAML frontmatter from markdown content"""
    if not content.startswith('---'):
        return None, content
    
    try:
        # Split content by frontmatter delimiters
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None, content
        
        # Parse YAML
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].strip()
        
        return frontmatter, body
    except Exception as e:
        print_error(f"Failed to parse YAML frontmatter: {str(e)}")
        return None, content


def search_kb(query, category=None, priority=None):
    """Search knowledge base for entries matching query"""
    kb_root = get_kb_root()
    results = []
    
    if not kb_root.exists():
        print_info("Knowledge base not initialized.")
        return results
    
    # Search in all KB files
    for kb_file in kb_root.rglob('*.md'):
        if kb_file.name in ['INDEX.md', 'README.md']:
            continue
        
        content = read_file(kb_file)
        if not content:
            continue
        
        frontmatter, body = parse_yaml_frontmatter(content)
        
        if not frontmatter:
            continue
        
        # Filter by category and priority if specified
        if category and frontmatter.get('category') != category:
            continue
        
        if priority and frontmatter.get('priority') != priority:
            continue
        
        # Search in title, tags, and body
        query_lower = query.lower()
        title = frontmatter.get('title', '').lower()
        tags = ' '.join(frontmatter.get('tags', [])).lower()
        body_lower = body.lower()
        
        if query_lower in title or query_lower in tags or query_lower in body_lower:
            results.append({
                'file': str(kb_file.relative_to(kb_root)),
                'title': frontmatter.get('title', 'Untitled'),
                'category': frontmatter.get('category', 'unknown'),
                'priority': frontmatter.get('priority', 'medium'),
                'tags': frontmatter.get('tags', []),
                'date': frontmatter.get('date', 'unknown'),
                'frontmatter': frontmatter,
                'body': body
            })
    
    # Sort by priority and date
    priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    results.sort(key=lambda x: (
        priority_order.get(x['priority'], 4),
        x['date']
    ), reverse=True)
    
    return results


def create_kb_entry(entry_data):
    """Create a new KB entry"""
    kb_root = get_kb_root()
    
    # Validate required fields
    required_fields = ['title', 'category', 'priority']
    for field in required_fields:
        if field not in entry_data:
            print_error(f"Missing required field: {field}")
            return None
    
    # Determine category directory
    category = entry_data['category']
    priority = entry_data.get('priority', 'medium')
    
    # Map category to directory
    category_dirs = {
        'bug': f'bugs/{priority}',
        'feature': 'features',
        'architecture': 'architecture',
        'security': 'security',
        'performance': 'performance',
        'platform': 'platform-specific'
    }
    
    category_dir = category_dirs.get(category, 'features')
    entry_dir = kb_root / category_dir
    ensure_dir(entry_dir)
    
    # Generate filename from title
    title = entry_data['title']
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    filename = re.sub(r'[-\s]+', '-', filename)
    filename = f"{filename}.md"
    
    entry_file = entry_dir / filename
    
    # Check if file already exists
    if entry_file.exists():
        print_warning(f"KB entry already exists: {entry_file}")
        if not confirm("Overwrite?", default=False):
            return None
    
    # Create frontmatter
    frontmatter = {
        'title': entry_data['title'],
        'category': entry_data['category'],
        'priority': entry_data['priority'],
        'sprint': entry_data.get('sprint', 'sprint-1'),
        'date': entry_data.get('date', datetime.now().strftime('%Y-%m-%d')),
        'tags': entry_data.get('tags', []),
        'related_files': entry_data.get('related_files', []),
        'attempts': entry_data.get('attempts', 1),
        'time_saved': entry_data.get('time_saved', 'N/A')
    }
    
    # Create content
    content = f"""---
{yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)}---

## Problem

{entry_data.get('problem', 'Description of the problem or requirement.')}

## Root Cause

{entry_data.get('root_cause', 'Analysis of what caused the issue (for bugs).')}

## Solution

{entry_data.get('solution', 'Step-by-step solution or implementation details.')}

## Prevention

{entry_data.get('prevention', 'How to avoid this issue in the future.')}

## Related Patterns

{entry_data.get('related_patterns', 'Links to similar KB entries or external resources.')}
"""
    
    # Write file
    if write_file(entry_file, content):
        print_success(f"KB entry created: {entry_file.relative_to(kb_root)}")
        
        # Update index
        update_kb_index()
        
        return str(entry_file.relative_to(kb_root))
    else:
        return None


def update_kb_index():
    """Update KB index with all entries"""
    kb_root = get_kb_root()
    index_file = get_kb_index()
    
    print_info("Updating KB index...")
    
    # Collect all entries
    entries_by_category = {}
    
    for kb_file in kb_root.rglob('*.md'):
        if kb_file.name in ['INDEX.md', 'README.md']:
            continue
        
        content = read_file(kb_file)
        if not content:
            continue
        
        frontmatter, _ = parse_yaml_frontmatter(content)
        
        if not frontmatter:
            continue
        
        category = frontmatter.get('category', 'unknown')
        
        if category not in entries_by_category:
            entries_by_category[category] = []
        
        entries_by_category[category].append({
            'file': str(kb_file.relative_to(kb_root)),
            'title': frontmatter.get('title', 'Untitled'),
            'priority': frontmatter.get('priority', 'medium'),
            'date': frontmatter.get('date', 'unknown'),
            'tags': frontmatter.get('tags', [])
        })
    
    # Generate index content
    index_content = f"""# Knowledge Base Index

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This index provides a searchable overview of all knowledge base entries.

## Statistics

- **Total Entries:** {sum(len(entries) for entries in entries_by_category.values())}
- **Categories:** {len(entries_by_category)}

## Entries by Category

"""
    
    # Sort categories
    for category in sorted(entries_by_category.keys()):
        entries = entries_by_category[category]
        
        # Sort by priority and date
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        entries.sort(key=lambda x: (
            priority_order.get(x['priority'], 4),
            x['date']
        ), reverse=True)
        
        index_content += f"\n### {category.title()}\n\n"
        
        for entry in entries:
            tags_str = ', '.join(entry['tags']) if entry['tags'] else 'no tags'
            index_content += f"- **[{entry['title']}]({entry['file']})** "
            index_content += f"[{entry['priority']}] - {entry['date']} - {tags_str}\n"
    
    # Write index
    if write_file(index_file, index_content):
        print_success(f"KB index updated: {len(entries_by_category)} categories")
        return True
    else:
        return False


def get_kb_stats():
    """Get knowledge base statistics"""
    kb_root = get_kb_root()
    
    stats = {
        'total_entries': 0,
        'by_category': {},
        'by_priority': {},
        'recent_entries': []
    }
    
    for kb_file in kb_root.rglob('*.md'):
        if kb_file.name in ['INDEX.md', 'README.md']:
            continue
        
        content = read_file(kb_file)
        if not content:
            continue
        
        frontmatter, _ = parse_yaml_frontmatter(content)
        
        if not frontmatter:
            continue
        
        stats['total_entries'] += 1
        
        # Count by category
        category = frontmatter.get('category', 'unknown')
        stats['by_category'][category] = stats['by_category'].get(category, 0) + 1
        
        # Count by priority
        priority = frontmatter.get('priority', 'medium')
        stats['by_priority'][priority] = stats['by_priority'].get(priority, 0) + 1
        
        # Track recent entries
        stats['recent_entries'].append({
            'title': frontmatter.get('title', 'Untitled'),
            'date': frontmatter.get('date', 'unknown'),
            'category': category
        })
    
    # Sort recent entries by date
    stats['recent_entries'].sort(key=lambda x: x['date'], reverse=True)
    stats['recent_entries'] = stats['recent_entries'][:10]
    
    return stats


if __name__ == "__main__":
    # Test KB manager
    from common import print_header
    
    print_header("Testing KB Manager")
    
    # Test search
    results = search_kb("authentication")
    print(f"Search results: {len(results)}")
    
    # Test stats
    stats = get_kb_stats()
    print(f"Total entries: {stats['total_entries']}")
    print(f"Categories: {stats['by_category']}")
