# Workflows Guide

Common patterns and workflows for using CC Awesome Claude Code effectively.

## Daily Development Workflow

### Morning Standup
```bash
# Review code quality
/review --type=all

# Check for security issues
@security-scanner

# Plan improvements
/improve --focus=all
```

### During Development
```bash
# Create new feature
/workflow create-feature "Add user authentication"

# Make changes...

# Smart commit
/smart-commit

# Get feedback
/review
```

### End of Sprint
```bash
# Comprehensive review
/review --type=all

# Improve codebase
/improve --focus=all

# Update documentation
@docs-analyzer
```

## Feature Development Workflow

### Step 1: Plan Feature
```bash
/workflow create-feature "Feature description"
```

### Step 2: Initialize if New Module
```bash
/project-init feature-module --type=<type>
```

### Step 3: Implement
- Write code
- Run tests
- Make commits

### Step 4: Review
```bash
/review --type=all
```

### Step 5: Improve
```bash
/improve --focus=all
```

### Step 6: Commit
```bash
/smart-commit
```

---

## Bug Fix Workflow

### Discovery Phase
1. Identify the bug
2. Write failing test
3. Run existing tests to understand impact

### Investigation Phase
```bash
# Analyze code around bug
@code-analyzer

# Review architecture
@tech-lead-pe
```

### Fix Phase
1. Implement fix
2. Run tests
3. Verify fix works

### Commit Phase
```bash
# Security check
@security-scanner

# Smart commit
/smart-commit --conventional
```

### Verification Phase
```bash
# Code review
/review --type=code

# Architecture impact
/review --type=architecture
```

---

## Refactoring Workflow

### Analysis Phase
```bash
# Identify refactoring needs
@code-analyzer

# Get specialist advice
@refactoring-specialist
```

### Planning Phase
```bash
# Create refactoring workflow
/workflow refactor "Refactor module X"
```

### Implementation Phase
1. Implement changes
2. Run tests
3. Ensure backwards compatibility

### Review Phase
```bash
# Comprehensive review
/review --type=all

# Architecture check
@tech-lead-pe

# Code quality check
@code-analyzer
```

### Commit Phase
```bash
# Smart commits for refactoring
/smart-commit --conventional

# Document changes
@docs-analyzer
```

---

## Security-Focused Workflow

### Before Every Commit
```bash
/smart-commit --security-only
```

### Regular Security Reviews
```bash
# Monthly security audit
/review --type=security

# Deep security scan
@security-scanner
```

### When Handling Sensitive Data
1. Mark sensitive files
2. Add to .gitignore
3. Create environment templates
4. Document security practices
5. Run security scan

```bash
@security-scanner
@gitignore-manager
```

---

## Documentation Workflow

### Creation Phase
```bash
# Plan documentation
/workflow create-docs "Document API endpoints"
```

### Writing Phase
1. Write documentation
2. Add examples
3. Include code snippets

### Review Phase
```bash
# Review documentation
@docs-analyzer

# Verify examples work
/review --type=docs
```

### Improvement Phase
```bash
# Improve documentation
/improve --focus=all
```

---

## Performance Optimization Workflow

### Analysis Phase
```bash
# Identify performance issues
@code-analyzer

# Get optimization strategy
@tech-lead-pe
```

### Optimization Phase
1. Profile code
2. Identify bottlenecks
3. Implement optimizations
4. Benchmark improvements

### Review Phase
```bash
# Code review
/review --type=code

# Architecture review
@tech-lead-pe
```

### Verification Phase
```bash
# Final performance check
/improve --focus=performance

# Commit
/smart-commit
```

---

## Testing Workflow

### Test Creation
```bash
# Generate tests
# (Use update-command to create custom test generator)
```

### Test Coverage
```bash
# Check coverage
/review --type=code

# Improve coverage
/improve
```

### Test Maintenance
```bash
# Regular test review
/review

# Update tests with code changes
/smart-commit
```

---

## Release Workflow

### Preparation Phase
```bash
# Final comprehensive review
/review --type=all

# Security scan before release
@security-scanner

# Performance check
@code-analyzer

# Documentation check
@docs-analyzer
```

### Testing Phase
1. Run full test suite
2. Manual testing
3. Integration testing
4. Security testing

### Commit Phase
```bash
# Smart commit with conventional format
/smart-commit --conventional --all

# Tag version
# (Update version in package.json, etc.)
```

### Verification Phase
```bash
# Final alignment check
@alignment-checker

# Release readiness check
/review --type=all
```

---

## Multi-Developer Workflow

### Code Review Process
```bash
# When you receive a PR
/review

# Detailed code analysis
@code-analyzer

# Architecture review
@tech-lead-pe

# Security review
@security-scanner
```

### Merge Strategy
```bash
# Before merging
/smart-commit

# Final verification
/review --type=all
```

### Conflict Resolution
1. Use @change-analyzer to understand changes
2. Review both versions
3. Merge carefully
4. Run full test suite
5. Commit merged version

---

## Quick Reference

| Task | Command |
|------|---------|
| Commit changes | `/smart-commit` |
| Review code | `/review` |
| Security check | `@security-scanner` |
| Analyze code | `@code-analyzer` |
| Improve codebase | `/improve` |
| Plan feature | `/workflow` |
| Initialize project | `/project-init` |
| Get architecture advice | `@tech-lead-pe` |
| Check documentation | `@docs-analyzer` |
| Refactoring tips | `@refactoring-specialist` |

---

## Tips for Effective Workflows

1. **Start Simple** - Use basic commands first, add complexity as needed
2. **Security First** - Always run security scans before committing
3. **Iterate** - Use agents multiple times with different focuses
4. **Combine Commands** - Chain commands for complex tasks
5. **Review Regularly** - Don't wait until the end to review
6. **Document Early** - Maintain documentation as you code
7. **Test Continuously** - Run tests frequently, not just at the end
8. **Commit Often** - Make small, logical commits with smart-commit
9. **Use Agents** - Leverage agents directly for deep analysis
10. **Automate** - Create custom commands for repetitive tasks

---

See [Commands Reference](commands.md) and [Agents Reference](agents.md) for detailed documentation.
