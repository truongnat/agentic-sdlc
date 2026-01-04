import pytest
import sys
from unittest.mock import MagicMock, patch, mock_open
from pathlib import Path

# Add tools to path
sys.path.append(str(Path(__file__).parent.parent / "tools"))

from release.release import ReleaseManager

@pytest.fixture
def release_manager():
    return ReleaseManager(project_root=Path("."))

class TestReleaseManager:
    def test_bump_version_patch(self, release_manager):
        assert release_manager.bump_version("patch", "1.0.0") == "1.0.1"

    def test_bump_version_minor(self, release_manager):
        assert release_manager.bump_version("minor", "1.0.0") == "1.1.0"

    def test_bump_version_major(self, release_manager):
        assert release_manager.bump_version("major", "1.0.0") == "2.0.0"

    def test_detect_bump_type_feat(self, release_manager):
        commits = [{"message": "feat: new feature"}]
        assert release_manager.detect_bump_type(commits) == "minor"

    def test_detect_bump_type_fix(self, release_manager):
        commits = [{"message": "fix: bug fix"}]
        assert release_manager.detect_bump_type(commits) == "patch"
        
    def test_detect_bump_type_breaking(self, release_manager):
        commits = [{"message": "feat!: breaking change"}]
        assert release_manager.detect_bump_type(commits) == "major"
        
    @patch("subprocess.run")
    def test_commit_changes(self, mock_run, release_manager):
        # Mock successful git add and commit
        mock_run.return_value.returncode = 0
        
        assert release_manager.commit_changes("1.1.0", dry_run=False) is True
        
        # Verify git calls
        assert mock_run.call_count == 2
        args_list = [call.args[0] for call in mock_run.call_args_list]
        assert ['git', 'add', 'package.json', 'CHANGELOG.md'] in args_list
        assert ['git', 'commit', '-m', 'chore(release): v1.1.0'] in args_list

    @patch("subprocess.run")
    def test_publish_package_npm(self, mock_run, release_manager):
        # Mock package.json read
        with patch("builtins.open", mock_open(read_data='{"name": "test", "version": "1.0.0"}')):
            mock_run.return_value.returncode = 0
            assert release_manager.publish_package(dry_run=False) is True
            
            # Verify npm publish call
            mock_run.assert_called_with(['npm', 'publish'], check=True, cwd=Path("."))
