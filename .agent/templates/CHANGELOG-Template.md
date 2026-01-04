# Changelog Template

**⚠️ IMPORTANT:** This is a TEMPLATE. Root `CHANGELOG.md` is managed AUTOMATICALLY by `release.py`.

All project changes should be documented in:
- Sprint-specific: `docs/sprints/sprint-[N]/reports/Phase-Report-Sprint-[N]-v*.md`
- Project-wide: `docs/global/reports/Final-Project-Report.md`

---

## Template Format (For Reference Only)

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security improvements

---

## [1.0.0] - YYYY-MM-DD

### Added
- Initial release
- Feature 1
- Feature 2

### Changed
- Updated dependency X to version Y

### Fixed
- Fixed bug in component Z
```

---

## Usage Guidelines

1. **DO NOT** manually edit CHANGELOG.md in project root (Automation Only)
2. **DO** document changes in Phase Reports per sprint
3. **DO** consolidate in Final Project Report
4. **DO** use semantic versioning for releases
5. **DO** group changes by type (Added, Changed, Fixed, etc.)
6. **DO** include dates in YYYY-MM-DD format
7. **DO** link to relevant issues/PRs when applicable

---

## Alternative Documentation Locations

| Document Type | Location | Purpose |
|---------------|----------|---------|
| Sprint Changes | `docs/sprints/sprint-[N]/reports/Phase-Report-Sprint-[N]-v*.md` | Track changes per sprint |
| Development Log | `docs/sprints/sprint-[N]/logs/Development-Log-Sprint-[N]-v*.md` | Detailed dev activities |
| DevOps Log | `docs/sprints/sprint-[N]/logs/DevOps-Plan-and-Log-Sprint-[N]-v*.md` | Deployment history |
| Final Report | `docs/global/reports/Final-Project-Report.md` | Complete project changelog |

---

*Template Version: 1.0*  
*Last Updated: 2026-01-01*
