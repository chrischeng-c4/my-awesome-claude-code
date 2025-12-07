# Commands Reference

Complete reference for all 7 commands in CC Awesome Claude Code.

## Overview

Commands are the main entry points for users. Each command orchestrates one or more agents to accomplish specific tasks.

## Commands

### 1. /smart-commit

**Description**: Intelligent git commit workflow with security scanning, change analysis, and automated commit message generation.

**Usage**:
```bash
/smart-commit [--all] [--security-only] [--auto-gitignore] [--conventional]
```

**Options**:
- `--all` - Stage and commit all changes at once
- `--security-only` - Only run security scan without committing
- `--auto-gitignore` - Automatically update .gitignore without prompting
- `--conventional` - Enforce conventional commit format

**Orchestrated Agents**:
- `@change-analyzer` - Analyzes and groups related changes
- `@security-scanner` - Scans for secrets and vulnerabilities
- `@gitignore-manager` - Suggests and updates .gitignore
- `@commit-generator` - Generates commit messages

**Example**:
```bash
# Stage some files
git add src/auth.py tests/test_auth.py

# Run smart-commit
/smart-commit

# Verify and confirm commits
```

**Features**:
- Groups related changes logically
- Detects API keys, passwords, and secrets
- Automatically adds sensitive files to .gitignore
- Generates conventional commit messages
- Iterative workflow for multiple commits

---

### 2. /workflow

**Description**: Create and orchestrate complex development workflows with documentation-first approach.

**Usage**:
```bash
/workflow <workflow-type> <description> [--user|--project] [--docs-first] [--token-optimize]
```

**Arguments**:
- `<workflow-type>` - Type of workflow (e.g., "create-api", "build-ui", "refactor")
- `<description>` - Description of what to build

**Options**:
- `--user` - Create user-level workflow
- `--project` - Create project-level workflow (default)
- `--docs-first` - Generate documentation before implementation
- `--token-optimize` - Optimize for token usage

**Example**:
```bash
/workflow create-api "Build REST API with user authentication"

/workflow build-ui "Create responsive dashboard with charts" --docs-first

/workflow refactor "Improve database query performance"
```

**Features**:
- Documentation-first development approach
- Agent specialization for different tasks
- Workflow step tracking and memory
- Token-optimized documentation
- Integrated decision logging

---

### 3. /project-init

**Description**: Comprehensive project scaffolding service with complete development environment setup.

**Usage**:
```bash
/project-init <project-name> [--type=<type>] [--features=<list>] [--template=<template>]
```

**Arguments**:
- `<project-name>` - Name of the new project

**Options**:
- `--type` - Project type (e.g., "react", "node", "python", "rust")
- `--features` - Comma-separated list of features to include
- `--template` - Specific template to use

**Orchestrated Agents**:
- `@project-builder` - Creates project structure
- `@project-init-validator` - Validates configuration
- `@environment-setup` - Sets up development environment

**Example**:
```bash
# Create React project with TypeScript and testing
/project-init my-app --type=react --features=typescript,testing,eslint

# Create Python API with FastAPI
/project-init api-service --type=python --features=fastapi,sqlalchemy,pytest

# Create Node.js backend
/project-init backend --type=node --features=express,cors,helmet
```

**Includes**:
- Project structure and directories
- Configuration files (.eslintrc, tsconfig.json, etc.)
- Example code and entry points
- Testing setup (Jest, Pytest, etc.)
- Git initialization
- README with setup instructions
- Development and build scripts

---

### 4. /update-agent

**Description**: Create or update subagents with deep analysis, optimization, and self-improvement.

**Usage**:
```bash
/update-agent <agent-name> <description/requirements> [--level=user|project] [--tools=tool1,tool2]
```

**Arguments**:
- `<agent-name>` - Name of the agent to create/update
- `<description>` - Description or requirements for the agent

**Options**:
- `--level` - Installation level (user or project)
- `--tools` - Comma-separated list of allowed tools

**Example**:
```bash
/update-agent performance-analyzer "Analyze code performance and suggest optimizations"

/update-agent api-documentation "Generate API documentation from code"

/update-agent test-generator --tools=Read,Write,Bash "Generate unit tests for functions"
```

**Features**:
- Creates new agents or updates existing ones
- Analyzes requirements and optimizes implementation
- Handles tool permissions
- Creates agent markdown files
- Updates plugin.json automatically
- Tests agent functionality

---

### 5. /update-command

**Description**: Generate or improve commands with deep project context awareness.

**Usage**:
```bash
/update-command <command-name> [description] [--level=project|user] [--agent=<agent-name>]
```

**Arguments**:
- `<command-name>` - Name of the command

**Options**:
- `--level` - Installation level (user or project)
- `--agent` - Specific agent to use

**Example**:
```bash
/update-command deploy "Deploy application to production"

/update-command lint-fix --agent=code-analyzer "Auto-fix linting issues"

/update-command test-coverage "Run tests and generate coverage reports"
```

**Features**:
- Creates new commands or improves existing ones
- Understands project context
- Generates command documentation
- Creates command markdown files
- Updates plugin.json automatically
- Integrates with agents

---

### 6. /improve

**Description**: Multi-dimensional code improvement and optimization across your project.

**Usage**:
```bash
/improve [file-path] [--focus=readability|performance|security|tests|all]
```

**Arguments**:
- `[file-path]` - Optional file or directory to improve

**Options**:
- `--focus` - Improvement focus area (default: all)

**Example**:
```bash
# Improve entire codebase
/improve --focus=all

# Improve specific file
/improve src/api.js --focus=performance

# Improve security
/improve --focus=security
```

**Improvements Include**:
- Code readability (naming, structure, clarity)
- Performance optimization
- Security hardening
- Test coverage
- Documentation quality
- Error handling

---

### 7. /review

**Description**: Intelligent code review with multi-dimensional analysis and actionable feedback.

**Usage**:
```bash
/review [file-path] [--type=code|architecture|security|docs|all]
```

**Arguments**:
- `[file-path]` - Optional file or directory to review

**Options**:
- `--type` - Review type (default: all)

**Example**:
```bash
# Review entire codebase
/review --type=all

# Security review
/review --type=security

# Architecture review of specific module
/review src/services/ --type=architecture
```

**Review Dimensions**:
- **Code Quality** - Readability, structure, patterns
- **Architecture** - Design patterns, scalability, maintainability
- **Security** - Vulnerabilities, safe practices
- **Testing** - Coverage, test quality, edge cases
- **Documentation** - Completeness, clarity, accuracy
- **Performance** - Optimization opportunities

---

## Common Patterns

### Chain Commands
```bash
# Initialize project, then review
/project-init my-app --type=react
/review

# Create workflow, then improve
/workflow create-api "Build API"
/improve --focus=all
```

### Combine with Agents
```bash
# Run command, then follow up with agent analysis
/smart-commit

# Directly invoke agent for deeper analysis
@code-analyzer
```

### Use Options
```bash
# Conventional commits with security focus
/smart-commit --security-only --conventional

# Auto-gitignore and commit everything
/smart-commit --all --auto-gitignore
```

## Tips and Tricks

1. **Start with /smart-commit** - Keep commits organized and secure
2. **Use /review regularly** - Maintain code quality throughout development
3. **Leverage /workflow** - Plan complex features systematically
4. **Chain commands** - Combine multiple commands for complex tasks
5. **Direct agent use** - Use agents directly for deep analysis

## Troubleshooting

### Command not found
- Ensure plugin is installed: `/plugin list`
- Check command name spelling
- Restart Claude Code if needed

### Command fails with error
- Check file/directory paths are correct
- Verify you have necessary permissions
- Review error message for specific guidance

### Agent not invoked
- Check agent names in plugin.json
- Verify agent files exist
- Look for subagent name typos

---

See [Agents Reference](agents.md) for details on individual agents.
