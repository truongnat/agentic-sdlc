---
description: [Support] Release Management Workflow
---

# /release - Changelog and Version Management

## ⚠️ STRICT EXECUTION PROTOCOL (MANDATORY)
1. **CONVENTIONAL COMMITS:** All commits must follow conventional commit format.
2. **SEMVER:** Version bumps follow semantic versioning.
3. **CHANGELOG:** Update CHANGELOG.md before releasing.

## Quick Commands

```bash
# Preview changes (dry run)
python tools/release/release.py preview

# Generate changelog only
python tools/release/release.py changelog --sprint 6

# Bump version only
python tools/release/release.py version --auto

# Full release cycle
python tools/release/release.py release --tag
```

## Conventional Commit Format

```
type(scope): description

feat(landing): add hero section animation
fix(api): resolve timeout issue
docs(kb): update authentication guide
refactor(core): extract utility functions
```

### Types and Changelog Categories

| Type | Changelog Category | Version Bump |
|------|-------------------|--------------|
| `feat` | Added | Minor |
| `fix` | Fixed | Patch |
| `docs` | Documentation | Patch |
| `refactor` | Changed | Patch |
| `perf` | Performance | Patch |
| `test` | Testing | - |
| `chore` | Maintenance | - |
| `BREAKING CHANGE` | Breaking | Major |

### Scopes (Optional)

| Scope | Tag in Changelog |
|-------|------------------|
| `landing` | [Landing Page] |
| `agent` | [Agent System] |
| `workflow` | [Workflows] |
| `kb` | [Knowledge Base] |
| `tools` | [Tools] |
| `ui` | [UI] |
| `api` | [API] |

## Workflow Steps

### 1. Preview Changes
```bash
python tools/release/release.py preview --sprint 6
```
Shows:
- Last git tag
- Current version
- Commits since last release
- Auto-detected bump type
- Preview changelog entry

### 2. Generate Changelog
```bash
python tools/release/release.py changelog --sprint 6 --dry-run
```
- Parses commits since last tag
- Categorizes by type
- Generates markdown section
- Inserts into CHANGELOG.md

### 3. Bump Version
```bash
# Auto-detect based on commits
python tools/release/release.py version --auto

# Explicit bump type
python tools/release/release.py version --bump minor
```
Updates `package.json` version.

### 4. Full Release
```bash
python tools/release/release.py release --sprint 6 --tag
```
Executes:
1. Parse commits
2. Detect bump type
3. Generate changelog
4. Update version
5. Create git tag (optional)

### 5. Push Release
```bash
git add CHANGELOG.md package.json
git commit -m "chore(release): v1.2.0"
git push && git push --tags
```

## Example Changelog Output

```markdown
## [1.2.0] - 2026-01-03 (Sprint 6)

### Added
- [Landing Page] Hero section with animations
- [Agent System] New orchestrator workflow

### Fixed
- [API] Timeout issue in authentication
- [KB] Index update race condition

### Documentation
- Updated quick start guide
- Added MCP integration docs
```

## Integration

- **Package Scripts:**
  ```bash
  bun run release:preview    # Preview changes
  bun run release:changelog  # Generate changelog
  bun run release            # Full release
  ```

- **CI/CD:** Can be triggered in GitHub Actions

#release #versioning #changelog #semver #git-tags
