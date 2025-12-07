"""Tests for the models module."""

from pathlib import Path

import pytest

from claude_extensions.models import Extension, ExtensionType, InstallLevel


class TestExtension:
    """Test the Extension model."""

    def test_extension_creation(self):
        """Test creating an Extension object."""
        ext = Extension(
            name="test-command",
            type=ExtensionType.COMMAND,
            path=Path("/tmp/test.md"),
            description="Test description"
        )

        assert ext.name == "test-command"
        assert ext.type == ExtensionType.COMMAND
        assert ext.path == Path("/tmp/test.md")
        assert ext.description == "Test description"
        assert ext.selected is False

    def test_extension_type_from_string(self):
        """Test that ExtensionType can be created from string."""
        ext = Extension(
            name="test",
            type="command",  # String instead of enum
            path=Path("/tmp/test.md")
        )

        assert ext.type == ExtensionType.COMMAND

    def test_extension_filename_property(self):
        """Test the filename property."""
        ext = Extension(
            name="test",
            type=ExtensionType.AGENT,
            path=Path("/tmp/test-agent.md")
        )

        assert ext.filename == "test-agent.md"
        assert ext.stem == "test-agent"

    def test_get_install_path_user_level(self, mock_home_dir):
        """Test getting installation path for user level."""
        ext = Extension(
            name="test-command",
            type=ExtensionType.COMMAND,
            path=Path("/tmp/test-command.md")
        )

        install_path = ext.get_install_path(InstallLevel.USER)
        expected = mock_home_dir / ".claude" / "commands" / "test-command.md"

        assert install_path == expected

    def test_get_install_path_project_level(self):
        """Test getting installation path for project level."""
        ext = Extension(
            name="test-agent",
            type=ExtensionType.AGENT,
            path=Path("/tmp/test-agent.md")
        )

        project_path = Path("/tmp/my-project")
        install_path = ext.get_install_path(InstallLevel.PROJECT, project_path)
        expected = project_path / ".claude" / "agents" / "test-agent.md"

        assert install_path == expected

    def test_get_install_path_project_without_path(self):
        """Test that project level requires a project path."""
        ext = Extension(
            name="test",
            type=ExtensionType.COMMAND,
            path=Path("/tmp/test.md")
        )

        with pytest.raises(ValueError, match="Project path required"):
            ext.get_install_path(InstallLevel.PROJECT)

    def test_extract_description(self, temp_dir):
        """Test extracting description from frontmatter."""
        test_file = temp_dir / "test.md"
        test_file.write_text("""---
description: "This is a test description"
other: value
---

# Content
""")

        description = Extension._extract_description(test_file)
        assert description == "This is a test description"

    def test_extract_metadata(self, temp_dir):
        """Test extracting metadata from frontmatter."""
        test_file = temp_dir / "test.md"
        test_file.write_text("""---
description: "Test description"
allowed-tools: ["Read", "Write", "Edit"]
model: "claude-3"
---

# Content
""")

        metadata = Extension._extract_metadata(test_file)
        assert metadata["description"] == "Test description"
        assert metadata["allowed-tools"] == ["Read", "Write", "Edit"]
        assert metadata["model"] == "claude-3"

    def test_from_file(self, temp_dir):
        """Test creating Extension from file."""
        test_file = temp_dir / "my-command.md"
        test_file.write_text("""---
description: "My command description"
version: "1.0"
---

# My Command
""")

        ext = Extension.from_file(test_file, ExtensionType.COMMAND)
        assert ext.name == "my-command"
        assert ext.type == ExtensionType.COMMAND
        assert ext.path == test_file
        assert ext.description == "My command description"
        assert ext.metadata["version"] == "1.0"