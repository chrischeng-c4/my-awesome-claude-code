# CC Awesome Claude Code 🚀

A comprehensive collection of powerful commands and agents for Claude Code that supercharge your development workflow.

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/chrischeng/my-awesome-claude-code/releases/tag/v1.0.0)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-purple.svg)](https://claude.ai)

## 📦 What's Included

### 🎯 Commands (7)
- **`/smart-commit`** - Intelligent git commits with security scanning and auto-gitignore
- **`/workflow`** - Orchestrate complete development workflows
- **`/project-init`** - Comprehensive project scaffolding
- **`/update-agent`** - Create or update subagents intelligently
- **`/update-command`** - Generate or improve commands
- **`/improve`** - Multi-dimensional code improvement
- **`/review`** - Intelligent code review with actionable feedback

### 🤖 Agents (13)
- **`@security-scanner`** - Scan for vulnerabilities and secrets
- **`@change-analyzer`** - Analyze git changes for logical grouping
- **`@commit-generator`** - Generate conventional commit messages
- **`@gitignore-manager`** - Automatically manage .gitignore
- **`@project-builder`** - Build complete project structures
- **`@project-init-validator`** - Validate initialization configs
- **`@scaffold-analyzer`** - Recommend scaffolding patterns
- **`@environment-setup`** - Configure development environment
- **`@alignment-checker`** - Verify requirement alignment
- **`@code-analyzer`** - Deep code analysis
- **`@docs-analyzer`** - Documentation analysis
- **`@refactoring-specialist`** - Specialized refactoring
- **`@tech-lead-pe`** - Technical leadership guidance

## 🚀 Installation

### Quick Start (Recommended)

```bash
# Add the plugin repository
/plugin marketplace add chrischeng/my-awesome-claude-code

# Install the plugin
/plugin install cc-awesome-cc@chrischeng
```

That's it! All commands and agents are now available in Claude Code.

### Direct Installation (Alternative)

```bash
# Install directly from GitHub
/plugin install https://github.com/chrischeng/my-awesome-claude-code
```

## 📚 Usage

Once installed, all commands and agents are immediately available in Claude Code.

### Quick Start Examples

```bash
# Smart commit your changes with security scanning
/smart-commit

# Create a new workflow
/workflow create-api "Build a REST API with authentication"

# Initialize a new project
/project-init my-app --type=react

# Get code review
/review

# Improve code quality
/improve

# Scan for security issues
@security-scanner

# Analyze code quality
@code-analyzer

# Get architectural guidance
@tech-lead-pe
```

## 🎯 Key Features

### 🔒 Security First
Built-in security scanning for every commit:
- API keys and secrets detection
- Credential scanning
- Vulnerability detection
- PII detection
- High-entropy string analysis

### 🎨 Smart Git Workflows
Intelligent commit management:
- Automatic change grouping
- Conventional commit messages
- Security-aware commits
- Auto-gitignore management
- Iterative commit workflow

### 🏗️ Project Scaffolding
Complete project initialization:
- Multiple project templates
- Best practice configurations
- Development environment setup
- CI/CD pipeline generation
- Documentation scaffolding

### 🔄 Workflow Orchestration
Create complex workflows:
- Documentation-first approach
- Agent specialization
- Command generation
- Token-optimized documentation
- Memory and decision tracking

### 📊 Code Intelligence
Deep analysis and improvements:
- Multi-dimensional code review
- Refactoring recommendations
- Architecture guidance
- Documentation analysis
- Quality metrics

## 🏗️ Plugin Architecture

This plugin uses a command-agent architecture where:

- **Commands** (`/command-name`) - User-facing entry points
- **Agents** (`@agent-name`) - Specialized workers invoked by commands
- **Subagent Orchestration** - Commands coordinate multiple agents for complex tasks

### Example Workflow

When you run `/smart-commit`, it orchestrates multiple agents:

```
/smart-commit
  ├─> @change-analyzer (group changes by category)
  ├─> @security-scanner (check for secrets/vulnerabilities)
  ├─> @gitignore-manager (suggest .gitignore updates)
  └─> @commit-generator (create commit message)
```

Each phase builds on the previous, creating an intelligent workflow.

## 📖 Documentation

- **[Commands Reference](docs/commands.md)** - Detailed command documentation
- **[Agents Reference](docs/agents.md)** - Agent capabilities and usage
- **[Workflow Examples](docs/workflows.md)** - Common workflow patterns
- **[Configuration](docs/configuration.md)** - Customization options
- **[Migration Guide](archive/DEPRECATION_NOTICE.md)** - From Python CLI to plugin

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new commands or agents
- Improving existing extensions
- Reporting issues
- Suggesting features

## 📋 Commands Summary

### `/smart-commit`
```bash
/smart-commit [--all] [--security-only] [--auto-gitignore] [--conventional]
```
Intelligent git commits with security scanning, change analysis, and auto-gitignore management.

### `/workflow`
```bash
/workflow <workflow-type> <description>
```
Create and orchestrate complex development workflows.

### `/project-init`
```bash
/project-init <project-name> [--type=<type>] [--features=<list>]
```
Initialize new projects with templates and configurations.

### `/update-agent`
```bash
/update-agent <agent-name> <description>
```
Create or update specialized agents.

### `/update-command`
```bash
/update-command <command-name> [description]
```
Generate or improve commands.

### `/improve`
```bash
/improve [file-path]
```
Multi-dimensional code improvement.

### `/review`
```bash
/review [file-path]
```
Intelligent code review.

## 🔧 Advanced Usage

### Using Agents Directly

While agents are typically invoked by commands, you can also use them directly:

```bash
# Scan for security issues in changes
@security-scanner

# Deep code quality analysis
@code-analyzer

# Architecture and design review
@tech-lead-pe

# Documentation quality check
@docs-analyzer
```

### Configuration

Create a `.claude-plugins.json` in your project root to customize behavior:

```json
{
  "cc-awesome-cc": {
    "security": {
      "scanSecrets": true,
      "checkVulnerabilities": true
    },
    "commits": {
      "conventional": true,
      "requireDescription": true
    }
  }
}
```

See [Configuration](docs/configuration.md) for more details.

## 🐛 Troubleshooting

### Plugin not installing
- Ensure you're in a Claude Code environment
- Check: `/plugin list` to see installed plugins
- Verify GitHub repo is publicly accessible

### Commands not appearing
- Try restarting Claude Code
- Run `/plugin enable cc-awesome-cc` to ensure it's enabled
- Check plugin.json for syntax errors: `cat .claude-plugin/plugin.json`

### Agents not working
- Verify agent names with `/plugin list`
- Check agent file paths in plugin.json
- Ensure YAML frontmatter is valid

## 📊 Statistics

- **Total Extensions**: 20
- **Commands**: 7
- **Agents**: 13
- **Lines of Code**: ~7,500+
- **Dependencies**: 0 (pure markdown)

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

Built for the Claude Code community. Inspired by modern development workflows and best practices.

## 🔗 Links

- **Repository**: https://github.com/chrischeng/my-awesome-claude-code
- **Issues**: https://github.com/chrischeng/my-awesome-claude-code/issues
- **Discussions**: https://github.com/chrischeng/my-awesome-claude-code/discussions
- **Claude Code**: https://claude.ai/code

## 📢 Feedback

Love it? Have suggestions? Found a bug?

- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/chrischeng/my-awesome-claude-code/discussions)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/chrischeng/my-awesome-claude-code/issues)
- ⭐ **Show Support**: Star the repo!

---

**Note**: This project was previously a Python CLI tool (`claude-ext`). It has been converted to a native Claude Code plugin for better integration and ease of use. See [Migration Guide](archive/DEPRECATION_NOTICE.md) for details.

**Version**: 1.0.0 | **Last Updated**: December 8, 2025
