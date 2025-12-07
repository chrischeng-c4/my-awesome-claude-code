# Contributing to CC Awesome Claude Code

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on ideas, not individuals
- Help others learn and grow

## Ways to Contribute

### 1. Report Bugs
If you find a bug, please:
1. Check [GitHub Issues](https://github.com/chrischeng/my-awesome-claude-code/issues) to ensure it hasn't been reported
2. Create a detailed issue including:
   - Description of the bug
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment (OS, Claude Code version)
   - Error messages or logs

### 2. Suggest Enhancements
Have an idea for improvement? Please:
1. Describe the enhancement clearly
2. Provide use cases and examples
3. Explain expected benefits
4. Consider potential drawbacks

### 3. Improve Documentation
Documentation improvements are always welcome:
- Fix typos and unclear sections
- Add examples
- Improve organization
- Add missing documentation

### 4. Add New Commands or Agents
Want to add a new extension? Great! Here's how:

#### Adding a New Command

1. **Create the command file** in `commands/`:
   ```bash
   touch commands/my-command.md
   ```

2. **Add YAML frontmatter**:
   ```yaml
   ---
   description: "Brief description of what this command does"
   model: "claude-opus-4-5-20251101"
   thinking-level: "ultrathink"
   allowed-tools: ["Bash", "Read", "Write", "Edit", "Grep", "Task"]
   subagents: ["agent-name-1", "agent-name-2"]
   project-aware: true
   ---

   # /my-command

   Detailed markdown content describing the command...
   ```

3. **Update plugin.json**:
   ```json
   {
     "commands": [
       {
         "name": "my-command",
         "path": "./commands/my-command.md",
         "description": "Brief description"
       }
     ]
   }
   ```

4. **Test locally**:
   ```bash
   /plugin install /Users/chrischeng/projects/my-awesome-claude-code
   /my-command
   ```

#### Adding a New Agent

1. **Create the agent file** in `agents/`:
   ```bash
   touch agents/my-agent.md
   ```

2. **Add YAML frontmatter**:
   ```yaml
   ---
   name: my-agent
   description: "Brief description"
   model: "claude-opus-4-5-20251101"
   thinking-level: "ultrathink"
   allowed-tools: ["Read", "Bash", "Grep"]
   project-aware: false
   ---

   # @my-agent

   Detailed markdown content describing the agent...
   ```

3. **Update plugin.json**:
   ```json
   {
     "agents": [
       {
         "name": "my-agent",
         "path": "./agents/my-agent.md",
         "description": "Brief description"
       }
     ]
   }
   ```

4. **Test with a command**:
   ```bash
   # Use in a command's subagents field to test
   # Then invoke the command that uses it
   ```

### 5. Review and Test

Help review pull requests and test extensions:
- Test new commands and agents
- Check documentation accuracy
- Verify code quality
- Suggest improvements

## Development Workflow

### 1. Fork and Clone
```bash
git clone https://github.com/chrischeng/my-awesome-claude-code.git
cd my-awesome-claude-code
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/my-feature
# or
git checkout -b fix/my-bug-fix
```

### 3. Make Your Changes

- Add or modify extensions in `commands/` or `agents/`
- Update `plugin.json` if adding new extensions
- Update documentation as needed

### 4. Test Locally

```bash
# Install the plugin locally
/plugin install /path/to/my-awesome-claude-code

# Test your new extension
/my-command
@my-agent

# Test existing extensions still work
/smart-commit
/review
```

### 5. Validate Changes

Before committing, ensure:
- All 20 extensions still load correctly
- New files have proper YAML frontmatter
- JSON files are valid
- Documentation links work
- No breaking changes to existing extensions

### 6. Commit Changes

Follow conventional commits:
```bash
git add .
git commit -m "feat(agents): add new analysis agent

- Detailed description of changes
- Mention any breaking changes
- Reference related issues"
```

### 7. Push and Create PR

```bash
git push origin feature/my-feature
```

Then create a Pull Request with:
- Clear title describing the change
- Description of what changed and why
- How to test the changes
- Any breaking changes or migrations needed
- References to related issues

## Extension Guidelines

### Naming Conventions

- **Commands**: kebab-case (e.g., `smart-commit`, `project-init`)
- **Agents**: kebab-case (e.g., `security-scanner`, `code-analyzer`)
- **Files**: match the command/agent name exactly

### Quality Standards

- **Clear Descriptions**: Write clear, concise descriptions in frontmatter
- **Comprehensive Content**: Provide detailed markdown documentation
- **Practical Examples**: Include real-world usage examples
- **Error Handling**: Handle edge cases gracefully
- **Performance**: Consider performance for large codebases

### YAML Frontmatter Requirements

```yaml
---
# Required fields
name: command-or-agent-name          # For agents only
description: "What this does"
model: "claude-opus-4-5-20251101"    # Or appropriate model

# Recommended fields
thinking-level: "ultrathink"         # For complex tasks
allowed-tools: ["Tool1", "Tool2"]    # Tools the extension uses
project-aware: true                  # If it reads project files
subagents: ["agent-1", "agent-2"]    # For command orchestration
---
```

### Documentation Standards

- Use clear, concise language
- Include practical examples
- Explain complex concepts
- Provide troubleshooting tips
- Link to related extensions

## Review Process

1. **Automated Checks**
   - JSON validation
   - YAML frontmatter validation
   - File path verification
   - Plugin.json consistency

2. **Manual Review**
   - Code quality and clarity
   - Documentation completeness
   - Functionality testing
   - Consistency with existing extensions

3. **Testing**
   - Local installation test
   - Integration with other extensions
   - Edge case handling
   - Performance impact

## Community

- **GitHub Issues**: [Report bugs and request features](https://github.com/chrischeng/my-awesome-claude-code/issues)
- **GitHub Discussions**: [General discussion and questions](https://github.com/chrischeng/my-awesome-claude-code/discussions)
- **GitHub Releases**: [View releases and updates](https://github.com/chrischeng/my-awesome-claude-code/releases)

## Recognition

Contributors are recognized in:
- Release notes for their contributions
- GitHub contributor list
- README.md (for significant contributions)

## Questions?

Have questions about contributing?
- Open a discussion in [GitHub Discussions](https://github.com/chrischeng/my-awesome-claude-code/discussions)
- Check existing documentation in [docs/](docs/)
- Review the [README.md](README.md) for more information

---

Thank you for contributing to CC Awesome Claude Code! 🎉
