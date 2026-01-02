# Release Tools

Automated changelog generation and version management for the agentic-sdlc project.

## 📋 Features

- **Conventional Commit Parsing**: Automatically categorizes commits by type
- **Changelog Generation**: Creates properly formatted changelog entries
- **Semver Versioning**: Auto-detects and applies semantic version bumps
- **Git Tag Support**: Creates release tags for version tracking
- **Sprint Integration**: Supports sprint-based changelog organization

## 🚀 Quick Start

### Preview Changes
```bash
python tools/release/release.py preview
```

### Generate Changelog
```bash
# Auto-detect version bump
python tools/release/release.py changelog

# Specify sprint number
python tools/release/release.py changelog --sprint 5

# Specific version
python tools/release/release.py changelog --version 1.2.0
```

### Bump Version
```bash
# Auto-detect based on commits
python tools/release/release.py version --auto

# Specific bump type
python tools/release/release.py version --bump minor
```

### Full Release
```bash
# Release with auto-detected version
python tools/release/release.py release

# Release with git tag
python tools/release/release.py release --tag --bump minor
```

## 📝 Conventional Commits

The tool parses commits following the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>
```

### Commit Types

| Type | Changelog Category | Version Bump |
|------|-------------------|--------------|
| `feat` | Added | minor |
| `fix` | Fixed | patch |
| `docs` | Documentation | patch |
| `refactor` | Changed | patch |
| `perf` | Performance | patch |
| `test` | Testing | patch |
| `chore` | Maintenance | patch |
| `style` | Style | patch |
| `ci` | CI/CD | patch |
| `build` | Build | patch |

### Breaking Changes

Mark breaking changes with `!` after the type:
```
feat!: remove deprecated API
```
This triggers a **major** version bump.

### Scopes

Common scopes are mapped to tags:

| Scope | Tag |
|-------|-----|
| `landing` | [Landing Page] |
| `agent` | [Agent System] |
| `workflow` | [Workflows] |
| `kb` | [Knowledge Base] |
| `tools` | [Tools] |
| `ui` | [UI] |
| `api` | [API] |

## 📦 NPM Scripts

```bash
# Preview changes
bun run release:preview

# Generate changelog
bun run release:changelog

# Bump version
bun run release:version

# Full release
bun run release
```

## 🔧 Configuration

No additional configuration required. The tool automatically:
- Finds the project root
- Reads `package.json` for version
- Updates `CHANGELOG.md` with proper formatting

## 📚 Examples

### Example: Feature Release
```bash
# 1. Preview what will be released
python tools/release/release.py preview

# 2. Create release with changelog and tag
python tools/release/release.py release --bump minor --tag --sprint 5

# 3. Push changes
git push && git push --tags
```

### Example: Patch Release
```bash
# Quick patch release
python tools/release/release.py release --bump patch
git add . && git commit -m "chore: release v1.0.2"
git push
```

## 🧪 Testing

Run with `--dry-run` to preview changes without applying:

```bash
python tools/release/release.py changelog --dry-run
python tools/release/release.py release --dry-run
```
