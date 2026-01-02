# Shared Utilities

Common utilities used by all tools.

## Available Modules

### `common.py` - Common Functions
Shared utility functions for all tools.

**Functions:**
- `load_config()` - Load configuration
- `get_sprint_dir()` - Get sprint directory path
- `ensure_dir()` - Create directory if not exists
- `read_yaml_frontmatter()` - Parse YAML frontmatter
- `write_yaml_frontmatter()` - Write YAML frontmatter

**Usage:**
```python
from tools.utils.common import load_config, ensure_dir

config = load_config()
ensure_dir('docs/sprints/sprint-3')
```

---

### `kb_manager.py` - KB Management
Knowledge base management utilities.

**Functions:**
- `search_kb()` - Search knowledge base
- `add_entry()` - Add new KB entry
- `update_index()` - Update KB index
- `get_related()` - Find related patterns
- `validate_entry()` - Validate entry structure

**Usage:**
```python
from tools.utils.kb_manager import search_kb, add_entry

results = search_kb(query="authentication")
add_entry(category="bugs", priority="high", content=entry)
```

---

### `artifact_manager.py` - Artifact Management
Manage sprint artifacts and deliverables.

**Functions:**
- `create_artifact()` - Create new artifact
- `get_artifact_path()` - Get artifact location
- `validate_placement()` - Verify artifact placement
- `archive_sprint()` - Archive completed sprint
- `list_artifacts()` - List sprint artifacts

**Usage:**
```python
from tools.utils.artifact_manager import create_artifact

create_artifact(
    sprint=3,
    type="plan",
    name="Project-Plan-v1.md",
    content=plan_content
)
```

## Integration

Used by:
- All workflow scripts
- KB management scripts
- Validation scripts
- GitHub integration
- Neo4j integration

## Dependencies

```bash
pip install pyyaml
```

## See Also

- **Tools Overview:** `tools/README.md`
