"""Tests for the installer core module."""

from pathlib import Path
from unittest.mock import patch

import pytest

from claude_extensions.installer.core import ExtensionInstaller
from claude_extensions.models import Extension, ExtensionType, InstallLevel


class TestExtensionInstaller:
    """Test the ExtensionInstaller class."""

    def test_installer_initialization(self, mock_extensions_dir):
        """Test that installer initializes correctly."""
        with patch("claude_extensions.installer.core.find_extensions") as mock_find:
            mock_find.return_value = []
            installer = ExtensionInstaller()
            assert installer.extensions == []
            mock_find.assert_called_once()

    def test_get_extensions_no_filter(self, sample_extension):
        """Test getting all extensions without filter."""
        installer = ExtensionInstaller()
        installer.extensions = [sample_extension]

        result = installer.get_extensions()
        assert len(result) == 1
        assert result[0] == sample_extension

    def test_get_extensions_with_filter(self):
        """Test getting extensions with type filter."""
        cmd_ext = Extension("cmd", ExtensionType.COMMAND, Path("/tmp/cmd.md"))
        agent_ext = Extension("agent", ExtensionType.AGENT, Path("/tmp/agent.md"))

        installer = ExtensionInstaller()
        installer.extensions = [cmd_ext, agent_ext]

        commands = installer.get_extensions(ExtensionType.COMMAND)
        assert len(commands) == 1
        assert commands[0].name == "cmd"

        agents = installer.get_extensions(ExtensionType.AGENT)
        assert len(agents) == 1
        assert agents[0].name == "agent"

    def test_install_extension_user_level(self, sample_extension, mock_home_dir):
        """Test installing extension at user level."""
        installer = ExtensionInstaller()

        # Create the source file
        sample_extension.path.parent.mkdir(parents=True, exist_ok=True)
        sample_extension.path.write_text("test content")

        success, message = installer.install_extension(
            sample_extension,
            InstallLevel.USER
        )

        assert success is True
        assert "user level" in message

        # Check file was copied
        expected_path = mock_home_dir / ".claude" / "commands" / sample_extension.filename
        assert expected_path.exists()
        assert expected_path.read_text() == "test content"

    def test_install_extension_project_level(self, sample_extension, temp_dir):
        """Test installing extension at project level."""
        installer = ExtensionInstaller()
        project_path = temp_dir / "project"
        project_path.mkdir()

        # Create the source file
        sample_extension.path.parent.mkdir(parents=True, exist_ok=True)
        sample_extension.path.write_text("test content")

        success, message = installer.install_extension(
            sample_extension,
            InstallLevel.PROJECT,
            project_path
        )

        assert success is True
        assert "project" in message

        # Check file was copied
        expected_path = project_path / ".claude" / "commands" / sample_extension.filename
        assert expected_path.exists()

    def test_install_extension_project_without_path(self, sample_extension):
        """Test that project installation requires path."""
        installer = ExtensionInstaller()

        success, message = installer.install_extension(
            sample_extension,
            InstallLevel.PROJECT
        )

        assert success is False
        assert "Project path required" in message

    def test_install_multiple(self, temp_dir, mock_home_dir):
        """Test installing multiple extensions."""
        # Create two extensions
        ext1 = Extension("ext1", ExtensionType.COMMAND, temp_dir / "ext1.md")
        ext2 = Extension("ext2", ExtensionType.AGENT, temp_dir / "ext2.md")

        # Create source files
        ext1.path.write_text("content1")
        ext2.path.write_text("content2")

        installer = ExtensionInstaller()
        success_count, errors = installer.install_multiple(
            [ext1, ext2],
            InstallLevel.USER
        )

        assert success_count == 2
        assert len(errors) == 0

        # Check both files were installed
        cmd_path = mock_home_dir / ".claude" / "commands" / "ext1.md"
        agent_path = mock_home_dir / ".claude" / "agents" / "ext2.md"
        assert cmd_path.exists()
        assert agent_path.exists()

    def test_uninstall_extension(self, sample_extension, mock_home_dir):
        """Test uninstalling an extension."""
        installer = ExtensionInstaller()
        installer.extensions = [sample_extension]

        # Install first
        install_path = mock_home_dir / ".claude" / "commands" / sample_extension.filename
        install_path.parent.mkdir(parents=True, exist_ok=True)
        install_path.write_text("content")

        # Uninstall
        success, message = installer.uninstall_extension(
            sample_extension.name,
            InstallLevel.USER
        )

        assert success is True
        assert "Uninstalled" in message
        assert not install_path.exists()

    def test_uninstall_nonexistent(self):
        """Test uninstalling extension that doesn't exist."""
        installer = ExtensionInstaller()
        installer.extensions = []

        success, message = installer.uninstall_extension(
            "nonexistent",
            InstallLevel.USER
        )

        assert success is False
        assert "not found" in message

    def test_list_installed(self, mock_home_dir):
        """Test listing installed extensions."""
        installer = ExtensionInstaller()

        # Create some installed files
        commands_dir = mock_home_dir / ".claude" / "commands"
        agents_dir = mock_home_dir / ".claude" / "agents"
        commands_dir.mkdir(parents=True)
        agents_dir.mkdir(parents=True)

        (commands_dir / "cmd1.md").write_text("content")
        (commands_dir / "cmd2.md").write_text("content")
        (agents_dir / "agent1.md").write_text("content")

        installed = installer.list_installed(InstallLevel.USER)

        assert len(installed) == 3
        assert "command:cmd1" in installed
        assert "command:cmd2" in installed
        assert "agent:agent1" in installed