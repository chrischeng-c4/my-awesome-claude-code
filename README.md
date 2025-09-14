# Claude Code Extensions

Simple manager for Claude Code commands and agents.

## Installation

```bash
# Using uv (recommended)
uv pip install -e .

# Or with pip
pip install -e .
```

## Usage

### List available extensions
```bash
# List available agents
uv run claude-ext agent list

# List available commands
uv run claude-ext command list
```

### Install extensions
```bash
# Install to user level (default if no --project specified)
uv run claude-ext agent install security-scanner
uv run claude-ext command install smart-commit

# Install to specific project
uv run claude-ext agent install security-scanner --project ~/my-project
uv run claude-ext command install smart-commit --project .
```

### List installed extensions
```bash
# List user-level installations
uv run claude-ext agent list --installed
uv run claude-ext command list --installed

# List project-level installations
uv run claude-ext agent list --installed --project .
uv run claude-ext command list --installed --project ~/my-project
```

### Uninstall extensions
```bash
# Uninstall from user level
uv run claude-ext agent uninstall security-scanner
uv run claude-ext command uninstall smart-commit

# Uninstall from project
uv run claude-ext agent uninstall security-scanner --project ~/my-project
uv run claude-ext command uninstall smart-commit --project .
```

## Quick Examples

```bash
# See what agents are available
uv run claude-ext agent list

# Install an agent to user level (globally)
uv run claude-ext agent install security-scanner

# Install a command to current project
uv run claude-ext command install smart-commit --project .

# Check what's installed globally
uv run claude-ext agent list --installed
uv run claude-ext command list --installed
```

## Project Structure

```
claude-code-extensions/
├── main.py             # Single CLI file with typer
├── extensions/         # Extensions to install
│   ├── commands/       # Claude Code commands
│   └── agents/         # Claude Code agents
├── pyproject.toml      # Project configuration for uv
└── README.md          # This file
```

## Installation Behavior

- **Without `--project`**: Installs to user level (`~/.claude/`)
- **With `--project`**: Installs to project level (`<project>/.claude/`)

## Development

```bash
# Install with dev dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Format code
ruff format main.py

# Lint
ruff check main.py
```

## Creating your own extensions

1. Add your command to `extensions/commands/your-command/`
2. Add your agent to `extensions/agents/your-agent/`
3. Install with: `uv run claude-ext [agent|command] install <name>`

Simple as that!