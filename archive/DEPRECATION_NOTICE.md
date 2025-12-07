# Python CLI Tool - Deprecated

**Date**: December 8, 2025
**Status**: DEPRECATED - Do not use

## What Happened

This project has been converted from a Python CLI tool (`claude-ext`) to an official Claude Code plugin (`cc-awesome-cc`).

## Migration Path

### Old Way (Deprecated)
```bash
# This no longer works
uv pip install -e .
uv run claude-ext agent install security-scanner
uv run claude-ext command install smart-commit
```

### New Way (Current)
```bash
# Install the plugin
/plugin marketplace add chrischeng/my-awesome-claude-code
/plugin install cc-awesome-cc@chrischeng

# Use commands and agents directly in Claude Code
/smart-commit
/workflow
/project-init
@security-scanner
@code-analyzer
```

## What's Archived

- `cli/main.py` - Original 1,100-line CLI application
- `tests/` - Python test suite (pytest)
- `pyproject.toml.old` - Python project configuration
- `uv.lock` - UV dependency lock file

## Why the Change

The Claude Code plugin system provides:

1. **Native Integration** - Commands and agents work directly in Claude Code
2. **No Installation Required** - No Python dependencies or virtual environments
3. **Automatic Updates** - Plugin updates via Claude Code's plugin system
4. **Better Discovery** - Browse and install from Claude Code marketplace
5. **Simplified Distribution** - Single GitHub repository, no PyPI needed
6. **Zero Dependencies** - Pure markdown-based extensions

## For Historical Reference

The archived Python CLI tool is preserved for reference but should not be used. All functionality has been migrated to the plugin format with enhanced features.

## Questions or Issues?

If you have questions about the migration, please:
1. Check the [main README.md](../README.md) for plugin installation
2. Review [docs/](../docs/) for detailed documentation
3. Open an issue on [GitHub](https://github.com/chrischeng/my-awesome-claude-code/issues)

Thank you for using CC Awesome Claude Code!
