# Validation & Health Check Scripts

System health monitoring and validation.

## Available Scripts

### `health-check.py` - System Health Monitoring
Comprehensive system health check.

**Usage:**
```bash
python tools/validation/health-check.py
```

**Checks:**
- Artifact placement validation
- Documentation drift detection
- YAML frontmatter validation
- KB index integrity
- Sprint structure verification
- Git status check

**Called by:**
- Kiro IDE: `/housekeeping` command
- CLI: `agentic-sdlc health`
- Automated: Pre-commit hooks

**Output:**
```
📊 System Health Check
✅ Artifacts: All in correct locations
✅ Documentation: No drift detected
✅ KB Index: Up to date
⚠️  Git: 3 uncommitted files
```

## Integration

Called by:
- **Kiro IDE** - `/housekeeping` command
- **CLI** - Health monitoring commands
- **CI/CD** - Pre-deployment checks

## Dependencies

```bash
pip install pyyaml
```

## See Also

- **Tools Overview:** `tools/README.md`
- **Critical Patterns:** `.kiro/steering/critical-patterns.md`
