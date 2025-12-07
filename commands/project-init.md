---
allowed-tools: ["Bash", "Read", "Write", "Edit", "MultiEdit", "Glob", "Grep", "Task", "TodoWrite"]
model: "claude-opus-4-1-20250805"
description: "Comprehensive project scaffolding service with complete development environment setup"
argument-hint: "<project-name> [--type=<type>] [--template=<template>] [--features=<list>]"
thinking-level: "ultrathink"
subagents: ["scaffold-analyzer", "project-builder", "environment-setup", "project-init-validator"]
project-aware: false
---

# /project-init

ultrathink about creating a comprehensive project scaffolding service that sets up complete development environments with proper structure, tooling, testing, CI/CD, documentation, and Claude AI integration.

## Scaffolding Intelligence

This command creates complete project ecosystems by:
- Analyzing project requirements and selecting appropriate templates
- Creating comprehensive directory structures and configurations
- Setting up complete development environments with testing and tooling
- Configuring CI/CD pipelines and automation
- Generating documentation templates and examples
- Integrating Claude AI capabilities as part of the development workflow

## Workflow Phases

### Phase 1: Project Analysis & Planning
@scaffold-analyzer: Analyze requirements and plan structure
```markdown
1. **Project Type Detection**
   - Language: Python/TypeScript/Rust/Go/Java
   - Framework: FastAPI/Django/React/Vue/Next.js
   - Application Type: CLI/API/Web/Library/Service

2. **Feature Selection**
   - Testing framework and coverage tools
   - Linting and formatting setup
   - CI/CD pipeline configuration
   - Documentation generation
   - Container/deployment setup
   - Claude AI integration level

3. **Template Selection**
   - Match requirements to templates
   - Customize for specific needs
   - Plan directory structure
```

### Phase 2: Project Structure Creation
@project-builder: Build complete project structure
```markdown
1. **Directory Scaffolding**
   project-name/
   ├── src/                 # Source code
   │   ├── core/           # Business logic
   │   ├── api/            # API interfaces
   │   ├── models/         # Data models
   │   ├── services/       # External services
   │   └── utils/          # Utilities
   ├── tests/              # Test suite
   │   ├── unit/
   │   ├── integration/
   │   └── e2e/
   ├── docs/               # Documentation
   │   ├── api/
   │   ├── guides/
   │   └── architecture/
   ├── scripts/            # Build/deploy scripts
   ├── config/             # Configuration files
   └── .claude/            # Claude AI setup

2. **Configuration Files**
   - Language-specific: pyproject.toml, package.json, Cargo.toml
   - Testing: pytest.ini, jest.config.js, .coveragerc
   - Linting: .ruff.toml, .eslintrc, .prettierrc
   - CI/CD: .github/workflows/, .gitlab-ci.yml
   - Container: Dockerfile, docker-compose.yml
   - Editor: .vscode/, .idea/
```

### Phase 3: Development Environment Setup
@environment-setup: Configure complete development environment
```markdown
1. **Dependency Management**
   - Create virtual environment
   - Install base dependencies
   - Set up development tools
   - Configure package manager

2. **Testing Framework**
   - Unit test setup with fixtures
   - Integration test configuration
   - Coverage reporting
   - Test automation

3. **Code Quality Tools**
   - Linters configuration
   - Formatters setup
   - Type checking
   - Security scanning

4. **Git Configuration**
   - Initialize repository
   - Create .gitignore
   - Set up pre-commit hooks
   - Configure branch protection
```

### Phase 4: CI/CD & Automation
```markdown
1. **GitHub Actions / GitLab CI**
   - Test automation pipeline
   - Build and package workflow
   - Security scanning
   - Deployment automation
   - Release management

2. **Pre-commit Hooks**
   - Code formatting check
   - Linting validation
   - Test execution
   - Security scan
   - Commit message validation
```

### Phase 5: Documentation & Claude Integration
```markdown
1. **Documentation Templates**
   - README.md with badges and sections
   - CONTRIBUTING.md guidelines
   - API documentation setup
   - Architecture documentation
   - Development guides

2. **Claude AI Integration**
   - CLAUDE.md with project context
   - Custom commands in .claude/commands/
   - Project-specific agents
   - Workflow documentation
   - AI-assisted development setup
```

## Project Templates

### Python FastAPI Service
```bash
/project-init my-api --type=python --template=fastapi --features=postgres,redis,celery
```
Creates:
- FastAPI application structure
- SQLAlchemy models with Alembic migrations
- Celery task queue setup
- Redis caching configuration
- Docker Compose for local development
- Comprehensive test suite with pytest
- OpenAPI documentation

### TypeScript React Application
```bash
/project-init my-app --type=typescript --template=react --features=tailwind,storybook,testing
```
Creates:
- React 18+ with TypeScript
- Vite build configuration
- Tailwind CSS styling
- Storybook component library
- Jest + React Testing Library
- ESLint + Prettier setup
- GitHub Actions CI/CD

### Rust CLI Tool
```bash
/project-init my-cli --type=rust --template=cli --features=async,serialization
```
Creates:
- Cargo workspace structure
- Clap for CLI parsing
- Tokio async runtime
- Serde serialization
- Integration tests
- Cross-compilation setup
- Release workflow

### Python Library Package
```bash
/project-init my-lib --type=python --template=library --features=docs,publishing
```
Creates:
- Proper package structure
- Setup.py and pyproject.toml
- Sphinx documentation
- Test suite with tox
- PyPI publishing workflow
- Version management
- Example usage

## Interactive Mode

When run without arguments, enters interactive wizard:
```bash
/project-init

? Project name: my-awesome-project
? Project type: (Use arrow keys)
  ❯ Python
    TypeScript/JavaScript
    Rust
    Go
    Java
    Other

? Application type:
  ❯ Web API/Service
    CLI Application
    Library/Package
    Web Frontend
    Microservice
    Data Pipeline

? Select features: (Press space to select, Enter to confirm)
  ◯ Testing Framework
  ◯ CI/CD Pipeline
  ◯ Docker Setup
  ◯ Database Integration
  ◯ Authentication
  ◯ Documentation
  ◯ Claude AI Integration

? Initialize git repository? (Y/n)
? Create virtual environment? (Y/n)
? Install dependencies now? (Y/n)
```

## Configuration Schema

### Project Configuration (project.config.toml)
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "Project description"
authors = ["Name <email@example.com>"]
license = "MIT"

[project.urls]
repository = "https://github.com/user/project"
documentation = "https://docs.project.dev"
homepage = "https://project.dev"

[development]
python_version = "3.12"
virtual_env = ".venv"
test_coverage_threshold = 80

[features]
testing = true
ci_cd = true
docker = true
documentation = true
claude_ai = true

[tools]
formatter = "ruff"
linter = "ruff"
type_checker = "mypy"
test_runner = "pytest"

[claude]
model = "claude-3-opus"
commands_enabled = true
agents_enabled = true
auto_documentation = true
```

## Generated File Examples

### Generated README.md
```markdown
# Project Name

[![CI](https://github.com/user/project/workflows/CI/badge.svg)](https://github.com/user/project/actions)
[![Coverage](https://codecov.io/gh/user/project/branch/main/graph/badge.svg)](https://codecov.io/gh/user/project)
[![License](https://img.shields.io/github/license/user/project)](LICENSE)

## Features
- ✨ Feature 1
- 🚀 Feature 2
- 🔧 Feature 3

## Quick Start
\`\`\`bash
# Clone repository
git clone https://github.com/user/project.git
cd project

# Setup development environment
make setup

# Run tests
make test

# Start development server
make dev
\`\`\`

## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup.

## Documentation
Full documentation at [docs.project.dev](https://docs.project.dev)
```

### Generated Makefile
```makefile
.PHONY: help setup test lint format clean

help:
	@echo "Available commands:"
	@echo "  make setup    - Set up development environment"
	@echo "  make test     - Run test suite"
	@echo "  make lint     - Run linters"
	@echo "  make format   - Format code"
	@echo "  make clean    - Clean generated files"

setup:
	python -m venv .venv
	.venv/bin/pip install -e ".[dev]"
	pre-commit install

test:
	pytest --cov=src --cov-report=term-missing

lint:
	ruff check src tests
	mypy src

format:
	ruff format src tests

clean:
	rm -rf .venv build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
```

### Generated GitHub Actions Workflow
```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"

    - name: Run linters
      run: |
        ruff check src tests
        mypy src

    - name: Run tests
      run: |
        pytest --cov=src --cov-report=xml

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

## Success Metrics

### Project Quality Indicators
- Complete directory structure created
- All configuration files in place
- Development environment ready
- Tests passing out of the box
- CI/CD pipeline functional
- Documentation templates filled
- Claude AI integration configured

### Validation Checklist
@project-init-validator: Ensures complete setup
```markdown
□ Directory structure complete
□ Configuration files valid
□ Dependencies installable
□ Tests executable
□ Linters configured
□ Git repository initialized
□ CI/CD pipeline valid
□ Documentation present
□ Claude integration working
□ Development server startable
```

## Output Summary

```markdown
🎉 Project Scaffolding Complete!

Project: my-awesome-project
Type: Python FastAPI Service
Template: Microservice with PostgreSQL

✅ Created Structure:
  - 15 directories
  - 32 files
  - 5 configuration files
  - 8 documentation files

✅ Configured Tools:
  - Testing: pytest with 85% coverage target
  - Linting: ruff + mypy
  - Formatting: ruff format
  - CI/CD: GitHub Actions
  - Containers: Docker + Docker Compose

✅ Development Environment:
  - Virtual environment: .venv
  - Dependencies installed
  - Pre-commit hooks configured
  - Git repository initialized

✅ Claude AI Integration:
  - CLAUDE.md configured
  - 3 custom commands created
  - 2 project agents initialized

📚 Next Steps:
  1. cd my-awesome-project
  2. make dev        # Start development server
  3. make test       # Run test suite
  4. Read README.md for detailed setup

🚀 Ready for development!
```

## Integration with Other Workflows

### Downstream Workflows
- `/cci-implement`: Use scaffolded structure for features
- `/cci-test`: Leverage test setup
- `/cci-deploy`: Use CI/CD configuration
- `/cci-docs`: Build on documentation structure

### Workflow Composition
```bash
# Complete project setup with feature
/project-init my-app --type=python --template=fastapi && \
cd my-app && \
/cci-implement "user authentication with JWT"
```

## Self-Improvement

The workflow learns from:
1. Template usage patterns
2. Feature selection frequency
3. Common customizations
4. Setup failures and fixes
5. User feedback on generated structure

This creates a sophisticated project initialization system that goes far beyond simple setup, providing a complete, production-ready development environment with all modern tooling and practices.