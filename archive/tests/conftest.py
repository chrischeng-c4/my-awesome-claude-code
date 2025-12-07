"""Pytest configuration and fixtures."""

import shutil
import tempfile
from pathlib import Path
from typing import Generator

import pytest

from claude_extensions.models import Extension, ExtensionType


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for testing."""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def mock_extensions_dir(temp_dir: Path) -> Path:
    """Create a mock extensions directory with sample files."""
    extensions_dir = temp_dir / "extensions"
    commands_dir = extensions_dir / "commands"
    agents_dir = extensions_dir / "agents"

    commands_dir.mkdir(parents=True)
    agents_dir.mkdir(parents=True)

    # Create sample command file
    command_file = commands_dir / "test-command.md"
    command_file.write_text("""---
description: "Test command for unit tests"
allowed-tools: ["Read", "Write"]
---

# Test Command

This is a test command.
""")

    # Create sample agent file
    agent_file = agents_dir / "test-agent.md"
    agent_file.write_text("""---
description: "Test agent for unit tests"
model: "claude-3"
---

# Test Agent

This is a test agent.
""")

    return extensions_dir


@pytest.fixture
def sample_extension() -> Extension:
    """Create a sample Extension object."""
    return Extension(
        name="test-extension",
        type=ExtensionType.COMMAND,
        path=Path("/tmp/test-extension.md"),
        description="A test extension",
        metadata={"allowed-tools": ["Read", "Write"]}
    )


@pytest.fixture
def mock_home_dir(temp_dir: Path, monkeypatch) -> Path:
    """Mock the home directory for testing user-level installations."""
    home_dir = temp_dir / "home"
    home_dir.mkdir()
    monkeypatch.setattr(Path, "home", lambda: home_dir)
    return home_dir


@pytest.fixture
def mock_project_dir(temp_dir: Path) -> Path:
    """Create a mock project directory."""
    project_dir = temp_dir / "project"
    project_dir.mkdir()
    return project_dir