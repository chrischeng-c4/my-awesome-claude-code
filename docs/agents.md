# Agents Reference

Complete reference for all 13 specialized agents in CC Awesome Claude Code.

## Overview

Agents are specialized AI workers that handle specific tasks. They are typically invoked by commands but can also be used directly for deeper analysis.

## Agents

### 1. @security-scanner

**Description**: Scan git changes for security vulnerabilities, secrets, and sensitive data.

**Purpose**: Prevents accidental exposure of credentials, API keys, and sensitive information.

**Capabilities**:
- API key and token detection (AWS, GitHub, Slack, etc.)
- Password and credential detection
- Private key detection
- Connection string scanning
- High-entropy string analysis (potential secrets)
- Database connection scanning
- SSH key detection
- JWT token detection
- PII detection (Social Security numbers, credit cards, etc.)
- Binary file detection
- Large file detection

**Invoked By**:
- `/smart-commit` - Security phase
- `/improve --focus=security`
- `/review --type=security`

**Usage**:
```bash
@security-scanner
```

**Output**:
- List of detected security issues
- Risk levels (CRITICAL, HIGH, MEDIUM, LOW)
- Suggested fixes and remediation
- Files to add to .gitignore

---

### 2. @change-analyzer

**Description**: Analyze git changes for logical grouping and categorization.

**Purpose**: Helps organize related changes into logical commits.

**Capabilities**:
- Change grouping by feature/module
- File relationship detection
- Feature vs bugfix vs refactor classification
- Change dependency analysis
- Impact assessment
- Related file identification

**Invoked By**:
- `/smart-commit` - Change analysis phase
- `/workflow` - Task breakdown

**Usage**:
```bash
@change-analyzer
```

**Output**:
- Grouped changes with explanations
- Suggested commit boundaries
- Change classifications
- Dependencies between changes

---

### 3. @commit-generator

**Description**: Generate meaningful conventional commit messages.

**Purpose**: Creates consistent, descriptive commit messages following conventions.

**Capabilities**:
- Conventional commit format generation
- Scope detection
- Breaking change identification
- Commit body generation
- Footer generation (references, co-authors)
- Message validation

**Invoked By**:
- `/smart-commit` - Message generation phase

**Usage**:
```bash
@commit-generator
```

**Output**:
- Conventional commit message
- Optional detailed body
- Optional footer with references

**Conventional Format**:
```
<type>(<scope>): <subject>

<body>

<footer>
```

Examples:
- `feat(auth): implement JWT token validation`
- `fix(api): resolve memory leak in request handler`
- `docs: update API documentation`

---

### 4. @gitignore-manager

**Description**: Intelligently manage .gitignore patterns and rules.

**Purpose**: Keeps .gitignore organized and prevents sensitive files from being committed.

**Capabilities**:
- Pattern detection and suggestion
- IDE configuration detection (.vscode, .idea)
- Build artifact detection (dist, build, node_modules)
- Environment file detection (.env files)
- OS-specific file detection (.DS_Store, Thumbs.db)
- Log file detection
- Cache file detection
- Language-specific ignores (Python, Node, Ruby, etc.)
- Duplicate pattern detection
- Organization by category

**Invoked By**:
- `/smart-commit` - .gitignore update phase
- `/project-init` - Project setup

**Usage**:
```bash
@gitignore-manager
```

**Output**:
- Updated .gitignore content
- New patterns to add
- Patterns to remove
- Organized by category with comments

---

### 5. @project-builder

**Description**: Build complete project structures with all files and configurations.

**Purpose**: Creates fully functional project scaffolding for new projects.

**Capabilities**:
- Directory structure creation
- Configuration file generation
- Template selection and customization
- Package.json/pyproject.toml generation
- Build script generation
- CI/CD pipeline generation
- Documentation generation
- Example code creation
- Linting/formatting setup

**Invoked By**:
- `/project-init` - Project creation

**Usage**:
```bash
# Indirectly via:
/project-init my-app --type=react
```

**Output**:
- Complete project structure
- Configuration files
- Build and test scripts
- Development environment setup
- README with instructions

---

### 6. @project-init-validator

**Description**: Validate project initialization requirements and configurations.

**Purpose**: Ensures new projects are properly configured and ready for development.

**Capabilities**:
- Configuration validation
- Dependency checking
- Directory structure validation
- File permission verification
- Build script testing
- Development environment verification
- Best practice checking

**Invoked By**:
- `/project-init` - Validation phase

**Usage**:
```bash
# Indirectly via:
/project-init my-app --type=react
```

**Output**:
- Validation report
- Issues found and recommendations
- Setup verification
- Ready-to-develop confirmation

---

### 7. @scaffold-analyzer

**Description**: Analyze and recommend project scaffolding patterns.

**Purpose**: Helps choose appropriate scaffolding patterns and best practices.

**Capabilities**:
- Framework detection
- Scaffolding pattern analysis
- Best practice recommendations
- Alternative scaffolding suggestions
- Performance optimization recommendations
- Maintenance pattern suggestions

**Invoked By**:
- `/project-init` - Pattern recommendation

**Usage**:
```bash
# Indirectly via:
/project-init my-app --type=react
```

**Output**:
- Recommended patterns
- Alternatives with trade-offs
- Best practices for framework
- Configuration recommendations

---

### 8. @environment-setup

**Description**: Configure complete development environment with tools and dependencies.

**Purpose**: Sets up a fully functional development environment.

**Capabilities**:
- Dependency installation scripts
- Development tool setup
- Environment variable configuration
- Database initialization
- Cache setup (Redis, etc.)
- Build tool configuration
- Testing framework setup
- Documentation tool setup
- Pre-commit hook installation

**Invoked By**:
- `/project-init` - Environment setup phase
- `/workflow` - Setup tasks

**Usage**:
```bash
@environment-setup
```

**Output**:
- Setup instructions
- Installation scripts
- Configuration files
- Environment variable templates
- Verification commands

---

### 9. @alignment-checker

**Description**: Verify alignment between requirements and implementation.

**Purpose**: Ensures implementation matches intended requirements.

**Capabilities**:
- Requirement vs implementation comparison
- Feature completeness checking
- Specification compliance checking
- Test coverage verification
- Documentation accuracy validation
- API contract validation
- Database schema verification

**Invoked By**:
- `/improve` - Alignment checking
- `/review` - Architecture review

**Usage**:
```bash
@alignment-checker
```

**Output**:
- Alignment report
- Missing implementations
- Specification violations
- Recommendations for alignment

---

### 10. @code-analyzer

**Description**: Deep code analysis for patterns, quality, and improvements.

**Purpose**: Identifies patterns, quality issues, and improvement opportunities.

**Capabilities**:
- Design pattern detection
- Anti-pattern detection
- Code smell identification
- Complexity analysis
- Dependency analysis
- Type safety checking
- Error handling verification
- Performance bottleneck identification
- Memory leak detection
- Dead code detection

**Invoked By**:
- `/improve` - Code analysis phase
- `/review --type=code`
- `/review --type=all`

**Usage**:
```bash
@code-analyzer
```

**Output**:
- Code analysis report
- Patterns found
- Issues identified
- Improvement suggestions
- Severity levels

---

### 11. @docs-analyzer

**Description**: Analyze documentation for completeness and clarity.

**Purpose**: Ensures documentation is complete, accurate, and easy to understand.

**Capabilities**:
- Documentation completeness checking
- Clarity assessment
- Example verification
- Link validation
- Format consistency checking
- Outdated information detection
- Missing documentation detection
- Accessibility checking

**Invoked By**:
- `/improve --focus=docs`
- `/review --type=docs`
- `/review --type=all`

**Usage**:
```bash
@docs-analyzer
```

**Output**:
- Documentation analysis report
- Missing documentation sections
- Clarity issues
- Outdated information
- Improvement suggestions

---

### 12. @refactoring-specialist

**Description**: Specialized refactoring strategies and implementation.

**Purpose**: Provides specific refactoring recommendations and implementation guidance.

**Capabilities**:
- Extract method refactoring
- Extract class refactoring
- Rename refactoring
- Simplification refactoring
- Duplication elimination
- Function decomposition
- Module organization
- Dependency injection suggestions
- Interface extraction
- Testing strategy for refactoring

**Invoked By**:
- `/improve --focus=readability`
- `/review --type=architecture`

**Usage**:
```bash
@refactoring-specialist
```

**Output**:
- Refactoring recommendations
- Before/after examples
- Implementation steps
- Risk assessment
- Testing strategy

---

### 13. @tech-lead-pe

**Description**: Technical leadership and architecture guidance with prompt engineering expertise.

**Purpose**: Provides high-level architectural advice and strategic guidance.

**Capabilities**:
- Architecture review
- Design pattern guidance
- Scalability assessment
- Technology selection advice
- Team structure recommendations
- Technical debt assessment
- Performance optimization strategy
- Security architecture review
- Deployment strategy
- Tool and framework recommendations
- Prompt engineering expertise

**Invoked By**:
- `/review --type=architecture`
- `/review --type=all`
- `/improve` (when needed)
- `/workflow` (strategic guidance)

**Usage**:
```bash
@tech-lead-pe
```

**Output**:
- Architecture assessment
- Strategic recommendations
- High-level guidance
- Trade-off analysis
- Best practices
- Implementation strategy

---

## Agent Usage Patterns

### Sequential Agent Use
```bash
# Agents work in sequence
/smart-commit
# 1. @change-analyzer (groups changes)
# 2. @security-scanner (checks security)
# 3. @gitignore-manager (updates .gitignore)
# 4. @commit-generator (creates message)
```

### Direct Agent Invocation
```bash
# Use agent directly for detailed analysis
@code-analyzer

# Combine with multiple analysis
@security-scanner
@code-analyzer
@tech-lead-pe
```

### Combined Analysis
```bash
# Use multiple agents for comprehensive review
/review --type=all
# Uses: code-analyzer, security-scanner, alignment-checker, docs-analyzer, tech-lead-pe
```

## Tips and Best Practices

1. **Use agents sequentially** - Start with one agent, build on results
2. **Security first** - Always run security-scanner before committing
3. **Chain agents** - Use agent outputs as inputs for next agent
4. **Code before architecture** - Use code-analyzer before tech-lead-pe
5. **Document thoroughly** - Use docs-analyzer to ensure quality documentation

## Related Documentation

- [Commands Reference](commands.md) - How commands use agents
- [Workflows](workflows.md) - Common patterns and workflows
- [README](../README.md) - Plugin overview

---

**Total Agents**: 13 | **Version**: 1.0.0
