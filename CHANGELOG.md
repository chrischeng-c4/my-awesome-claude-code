# Changelog

All notable changes to the CC Awesome Claude Code plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-08

### Added - Initial Plugin Release

#### Commands (7)
- `/smart-commit` - Intelligent git commit workflow with security scanning, change analysis, and .gitignore management
- `/workflow` - Complete development workflow orchestration framework
- `/project-init` - Comprehensive project scaffolding service
- `/update-agent` - Intelligent agent creation and update system
- `/update-command` - Command generation and improvement system
- `/improve` - Multi-dimensional code improvement tool
- `/review` - Intelligent code review system

#### Agents (13)
- `@security-scanner` - Security vulnerability and secret detection
- `@change-analyzer` - Git change analysis and logical grouping
- `@commit-generator` - Conventional commit message generation
- `@gitignore-manager` - Automatic .gitignore management
- `@project-builder` - Project structure generation
- `@project-init-validator` - Project initialization validation
- `@scaffold-analyzer` - Scaffolding pattern recommendations
- `@environment-setup` - Development environment configuration
- `@alignment-checker` - Requirement-implementation alignment verification
- `@code-analyzer` - Deep code analysis
- `@docs-analyzer` - Documentation quality analysis
- `@refactoring-specialist` - Code refactoring strategies
- `@tech-lead-pe` - Technical leadership and architecture guidance

#### Features
- Subagent orchestration system for complex workflows
- Security-first approach to git workflows
- Comprehensive project scaffolding templates
- Workflow automation framework
- Documentation-first development approach
- Token-optimized documentation structure
- Zero Python dependencies

### Changed
- Migrated from Python CLI tool (`claude-ext`) to native Claude Code plugin
- Reorganized extensions from `extensions/` to `commands/` and `agents/`
- Replaced CLI-based installation with Claude Code plugin marketplace installation

### Deprecated
- Python CLI tool (`claude-ext`) - Archived in `archive/` directory
- See `archive/DEPRECATION_NOTICE.md` for migration guide

### Migration Guide

**From Python CLI (Deprecated)**
```bash
uv pip install -e .
uv run claude-ext agent install security-scanner
uv run claude-ext command install smart-commit
```

**To Plugin (Current)**
```bash
/plugin marketplace add chrischeng/my-awesome-claude-code
/plugin install cc-awesome-cc@chrischeng

# Commands work immediately:
/smart-commit
/workflow
@security-scanner
```

---

## Unreleased

### Planned for Future Releases
- Integration with more CI/CD systems
- Additional project templates (Django, FastAPI, Vue, Next.js, etc.)
- Enhanced security scanning patterns
- Performance optimizations for large repositories
- Additional specialized agents
- Interactive CLI for plugin configuration
- Plugin settings UI in Claude Code
- Marketplace ratings and reviews integration

---

For detailed upgrade instructions and breaking changes, see the [Migration Guide](archive/DEPRECATION_NOTICE.md).

### How to Report Issues

Found a bug? Have a feature request? Please:
1. Check [GitHub Issues](https://github.com/chrischeng/my-awesome-claude-code/issues) for existing reports
2. Create a new issue with detailed information
3. Include version number: `1.0.0`
4. Describe expected vs actual behavior

### Support

- 📖 **Documentation**: See [README.md](README.md) and [docs/](docs/)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/chrischeng/my-awesome-claude-code/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/chrischeng/my-awesome-claude-code/issues)
- 📧 **Contact**: Open an issue to get in touch

---

**Version**: 1.0.0 | **Release Date**: December 8, 2025
