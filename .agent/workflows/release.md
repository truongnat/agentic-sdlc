---
description: Release Management - Changelog generation and version control
---

# Release Workflow

Automates changelog generation, version bumping, and release tagging for the project.

## Quick Reference

```bash
# Preview what will be released
// turbo
python tools/release/release.py preview

# Generate changelog only
python tools/release/release.py changelog --sprint [N]

# Bump version (auto-detect)
python tools/release/release.py version --auto

# Full release cycle
python tools/release/release.py release --bump [major|minor|patch] --tag
```

## Workflow Steps

### 1. Pre-Release Check
Before creating a release:
- [ ] All tests passing
- [ ] Documentation updated
- [ ] No uncommitted changes
- [ ] On correct branch (main/develop)

```bash
// turbo
git status
python tools/validation/health-check.py
```

### 2. Preview Release
Check what will be included in the release:
```bash
// turbo
python tools/release/release.py preview
```

Review the output:
- Commits since last release
- Auto-detected version bump type
- Changelog preview

### 3. Generate Changelog
Create changelog entries from commits:
```bash
# With sprint number
python tools/release/release.py changelog --sprint 5

# Preview only (dry run)
// turbo
python tools/release/release.py changelog --dry-run
```

### 4. Bump Version
Update version in package.json:
```bash
# Auto-detect based on commits
python tools/release/release.py version --auto

# Specific bump
python tools/release/release.py version --bump minor
```

### 5. Full Release (Recommended)
Combine all steps into one command:
```bash
# Standard release
python tools/release/release.py release --bump minor --sprint 5

# Release with git tag
python tools/release/release.py release --bump minor --tag

# Preview full release
// turbo
python tools/release/release.py release --dry-run
```

### 6. Push Release
After release is complete:
```bash
git add CHANGELOG.md package.json
git commit -m "chore: release v[VERSION]"
git push
git push --tags  # If tags were created
```

## Conventional Commits

For best results, use conventional commit format:

```
feat(scope): add new feature
fix(scope): fix bug
docs: update documentation
refactor: code cleanup
chore: maintenance task
```

### Scopes
- `landing` - Landing page
- `agent` - Agent system
- `workflow` - Workflows
- `kb` - Knowledge base
- `tools` - Tools/scripts
- `ui` - User interface
- `api` - API changes

### Breaking Changes
Add `!` after type for breaking changes:
```
feat!: remove deprecated API
```

## Version Bump Rules

| Commit Type | Bump |
|-------------|------|
| `feat!` (breaking) | major |
| `feat` | minor |
| `fix`, `docs`, etc. | patch |

## NPM/Bun Scripts

```bash
bun run release:preview    # Preview changes
bun run release:changelog  # Generate changelog
bun run release:version    # Bump version
bun run release            # Full release
```

## Examples

### Typical Sprint Release
```bash
# 1. Preview changes
python tools/release/release.py preview

# 2. Create release for Sprint 5
python tools/release/release.py release --bump minor --sprint 5 --tag

# 3. Push
git add . && git commit -m "chore: release v1.2.0"
git push && git push --tags
```

### Hotfix Release
```bash
# Quick patch release
python tools/release/release.py release --bump patch
git add . && git commit -m "chore: release v1.1.1"
git push
```

#release #changelog #version #automation
