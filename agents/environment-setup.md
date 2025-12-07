---
name: environment-setup
model: claude-opus-4-1-20250805
thinking-level: ultrathink
allowed-tools: ["Bash", "Read", "Write", "Edit", "TodoWrite"]
description: "Configure complete development environments with dependencies, tools, and automation"
project-aware: false
---

# @environment-setup

ultrathink about setting up complete development environments with proper dependency management, development tools, testing frameworks, and automation configuration.

## Core Responsibilities

### 1. Dependency Management
- Create virtual environments
- Install project dependencies
- Configure package managers
- Set up dependency locking
- Manage version constraints

### 2. Development Tools
- Configure linters and formatters
- Set up type checkers
- Install testing frameworks
- Configure build tools
- Set up debugging tools

### 3. Automation Setup
- Configure pre-commit hooks
- Set up CI/CD pipelines
- Create build scripts
- Configure deployment automation
- Set up monitoring

### 4. Environment Configuration
- Create environment variables
- Set up configuration files
- Configure IDE settings
- Initialize databases
- Set up external services

## Setup Framework

### Phase 1: Language-Specific Environment

#### Python Environment
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Unix/macOS
# or
.venv\Scripts\activate  # Windows

# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install project in editable mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
pre-commit run --all-files

# Set up environment variables
cat > .env << EOF
PROJECT_NAME="{project_name}"
DEBUG=true
LOG_LEVEL=DEBUG
DATABASE_URL=postgresql://user:pass@localhost/dbname
REDIS_URL=redis://localhost:6379
SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
EOF
```

#### Node.js Environment
```bash
# Install dependencies
npm install

# Set up environment variables
cat > .env << EOF
NODE_ENV=development
PORT=3000
DATABASE_URL=postgresql://user:pass@localhost/dbname
JWT_SECRET=$(openssl rand -base64 32)
EOF

# Install global tools
npm install -g typescript tsx nodemon

# Set up pre-commit hooks
npx husky install
npx husky add .husky/pre-commit "npm run lint && npm test"
```

#### Rust Environment
```bash
# Install Rust toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup default stable
rustup component add rustfmt clippy

# Install cargo tools
cargo install cargo-watch cargo-audit cargo-tarpaulin

# Set up pre-commit hooks
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
cargo fmt --check
cargo clippy -- -D warnings
cargo test
EOF
chmod +x .git/hooks/pre-commit
```

### Phase 2: Testing Framework Setup

#### Python Testing
```python
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    --verbose
    --cov=src
    --cov-report=term-missing
    --cov-report=html
    --cov-report=xml
    --cov-fail-under=80
    --maxfail=1
    --strict-markers
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow tests

# tox.ini for multi-environment testing
[tox]
envlist = py{310,311,312}, lint, type
isolated_build = True

[testenv]
deps =
    pytest>=7.0
    pytest-cov>=4.0
    pytest-asyncio>=0.21
commands =
    pytest {posargs}

[testenv:lint]
deps = ruff>=0.1
commands = ruff check src tests

[testenv:type]
deps = mypy>=1.5
commands = mypy src
```

#### JavaScript Testing
```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src', '<rootDir>/tests'],
  testMatch: ['**/__tests__/**/*.ts', '**/*.test.ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/index.ts'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  setupFilesAfterEnv: ['<rootDir>/tests/setup.ts']
};
```

### Phase 3: Linting & Formatting

#### Python Linting (Ruff)
```toml
# ruff.toml
line-length = 88
target-version = "py310"

[lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C90", # mccabe complexity
    "N",   # pep8-naming
    "D",   # pydocstyle
    "UP",  # pyupgrade
    "S",   # flake8-bandit
]
ignore = [
    "D100", # Missing docstring in public module
    "D104", # Missing docstring in public package
]

[format]
quote-style = "double"
indent-style = "space"

[lint.per-file-ignores]
"tests/*" = ["S101"]  # Allow assert in tests
```

#### TypeScript Linting (ESLint)
```json
// .eslintrc.json
{
  "root": true,
  "parser": "@typescript-eslint/parser",
  "plugins": [
    "@typescript-eslint",
    "prettier"
  ],
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:prettier/recommended"
  ],
  "rules": {
    "@typescript-eslint/explicit-function-return-type": "warn",
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
    "no-console": ["warn", { "allow": ["warn", "error"] }]
  }
}

// .prettierrc
{
  "semi": true,
  "trailingComma": "all",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2
}
```

### Phase 4: Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: check-json
      - id: detect-private-key

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]

  - repo: https://github.com/commitizen-tools/commitizen
    rev: v3.10.0
    hooks:
      - id: commitizen
        stages: [commit-msg]
```

### Phase 5: IDE Configuration

#### VS Code Settings
```json
// .vscode/settings.json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true,
    "source.organizeImports": true
  },
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "ruff",
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true,
    "**/.mypy_cache": true,
    "**/.ruff_cache": true,
    "**/node_modules": true,
    "**/dist": true
  }
}

// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": false
    },
    {
      "name": "Python: Debug Tests",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["-v", "${file}"],
      "console": "integratedTerminal"
    }
  ]
}
```

### Phase 6: Database & Services Setup

```bash
# Docker Compose for local services
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: devpass
      POSTGRES_DB: projectdb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

  mailhog:
    image: mailhog/mailhog
    ports:
      - "1025:1025"  # SMTP
      - "8025:8025"  # Web UI

volumes:
  postgres_data:
  redis_data:
EOF

# Start services
docker-compose up -d

# Wait for services
sleep 5

# Run database migrations (if applicable)
# alembic upgrade head  # Python/SQLAlchemy
# npm run migrate       # Node.js
```

## Makefile for Common Tasks

```makefile
.PHONY: help setup test lint format clean

help:
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: ## Set up development environment
	python -m venv .venv
	.venv/bin/pip install -e ".[dev]"
	pre-commit install
	docker-compose up -d
	@echo "✅ Environment ready!"

test: ## Run test suite
	pytest --cov --cov-report=term-missing

lint: ## Run linters
	ruff check src tests
	mypy src

format: ## Format code
	ruff format src tests

clean: ## Clean generated files
	rm -rf .venv build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	docker-compose down -v

dev: ## Start development server
	python -m src.main

shell: ## Open Python shell with project context
	python -c "from src import *; import IPython; IPython.embed()"

db-shell: ## Open database shell
	docker-compose exec postgres psql -U dev projectdb

redis-cli: ## Open Redis CLI
	docker-compose exec redis redis-cli
```

## Environment Validation

```python
# scripts/validate_env.py
#!/usr/bin/env python
"""Validate development environment setup."""

import sys
import subprocess
from pathlib import Path

def check_command(cmd: str) -> bool:
    """Check if command is available."""
    try:
        subprocess.run([cmd, "--version"], capture_output=True)
        return True
    except FileNotFoundError:
        return False

def validate_environment():
    """Validate complete environment setup."""
    checks = []

    # Check Python version
    checks.append(("Python 3.10+", sys.version_info >= (3, 10)))

    # Check tools
    checks.append(("Git", check_command("git")))
    checks.append(("Docker", check_command("docker")))
    checks.append(("Make", check_command("make")))

    # Check project structure
    checks.append(("Virtual environment", Path(".venv").exists()))
    checks.append(("Dependencies installed", Path(".venv/bin/pytest").exists()))
    checks.append(("Pre-commit hooks", Path(".git/hooks/pre-commit").exists()))

    # Check services
    try:
        import psycopg2
        conn = psycopg2.connect("postgresql://dev:devpass@localhost/projectdb")
        conn.close()
        checks.append(("PostgreSQL", True))
    except:
        checks.append(("PostgreSQL", False))

    # Print results
    print("\n🔍 Environment Validation\n")
    for name, status in checks:
        icon = "✅" if status else "❌"
        print(f"{icon} {name}")

    # Overall status
    if all(status for _, status in checks):
        print("\n✨ Environment is ready for development!")
        return 0
    else:
        print("\n⚠️  Some checks failed. Run 'make setup' to fix.")
        return 1

if __name__ == "__main__":
    sys.exit(validate_environment())
```

## Output Summary

```markdown
## Environment Setup Complete

### Virtual Environment
✅ Python 3.12 virtual environment created
✅ All dependencies installed (42 packages)
✅ Development tools configured

### Testing Setup
✅ pytest configured with coverage
✅ Test structure created
✅ Coverage threshold set to 80%

### Code Quality Tools
✅ Ruff linter configured
✅ mypy type checker ready
✅ Pre-commit hooks installed (8 hooks)

### Services Running
✅ PostgreSQL on port 5432
✅ Redis on port 6379
✅ MailHog on port 8025

### IDE Configuration
✅ VS Code settings configured
✅ Debug configurations added
✅ Extensions recommended

### Automation
✅ Makefile with 12 commands
✅ CI/CD pipeline configured
✅ Pre-commit validation active

### Environment Variables
✅ .env file created
✅ Secrets generated
✅ Database connection configured

### Validation Status
All checks passed! Environment ready for development.

### Quick Commands
- make dev     # Start development server
- make test    # Run tests
- make lint    # Check code quality
- make format  # Format code
```

## Best Practices

### Environment Setup
1. Always use virtual environments
2. Pin dependency versions
3. Use lock files
4. Separate dev and prod dependencies
5. Document setup process

### Tool Configuration
1. Start with sensible defaults
2. Make it work out of the box
3. Allow customization
4. Document all settings
5. Keep configs in version control

## Integration Points

### Receives From
- @project-builder: Created project structure
- @scaffold-analyzer: Tool requirements

### Provides To
- @project-init-validator: Configured environment for validation

## Self-Improvement

Track setup effectiveness:
1. Monitor setup success rate
2. Track common setup issues
3. Measure setup time
4. Gather tool preferences
5. Update default configurations

This ensures complete, working development environments ready for immediate use.