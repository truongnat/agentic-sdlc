import subprocess
import shutil
import pytest
from pathlib import Path

CLI_JS = Path("bin/cli.js")

@pytest.mark.skipif(not shutil.which("node"), reason="Node.js not found")
class TestJSCLI:
    def test_cli_help(self):
        """Test that the CLI help command runs successfully."""
        cmd = ["node", str(CLI_JS), "--help"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        assert "Usage: agentic-sdlc" in result.stdout
        assert "Commands:" in result.stdout

    def test_cli_release_help(self):
        """Test that the release subcommand help runs."""
        cmd = ["node", str(CLI_JS), "release", "--help"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        assert "usage: release.py" in result.stdout

    def test_cli_unknown_command(self):
        """Test proper error for unknown command."""
        cmd = ["node", str(CLI_JS), "unknown_cmd"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        assert result.returncode != 0
        assert "Unknown command: unknown_cmd" in result.stderr
