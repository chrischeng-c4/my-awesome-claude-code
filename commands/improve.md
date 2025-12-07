# Universal Improvement Command

Execute intelligent improvements based on review findings or specific enhancement requests.

## Overview

A single, powerful command for all improvement needs that:
- Refactors code for better quality and maintainability
- Updates and enhances documentation
- Fixes security vulnerabilities automatically
- Optimizes performance bottlenecks
- Adds missing tests and validation
- Applies best practices and design patterns

## Usage

```bash
# Auto-improve based on recent review
/improve

# Specific improvement types
/improve --refactor        # Code refactoring and cleanup
/improve --docs            # Documentation updates
/improve --security        # Security vulnerability fixes
/improve --performance     # Performance optimizations
/improve --tests           # Add missing tests
/improve --style          # Code style and formatting

# Combined improvements
/improve --refactor --tests   # Refactor code and add tests
/improve --docs --examples    # Update docs with examples

# Targeted improvements
/improve --file="src/api.js"  # Improve specific file
/improve --fix="TODO markers"  # Fix specific issues

# Safe mode options
/improve --dry-run         # Preview changes without applying
/improve --interactive     # Confirm each change
```

## Parameters

### Improvement Types
- `--refactor`: Code structure, patterns, and quality improvements
- `--docs`: Documentation updates, fixes, and enhancements
- `--security`: Fix security vulnerabilities and unsafe patterns
- `--performance`: Optimize slow code and algorithms
- `--tests`: Add unit tests, integration tests, edge cases
- `--style`: Fix formatting, linting, naming conventions
- `--api`: Improve API design and consistency
- `--types`: Add/improve type annotations (TypeScript, Python, etc.)

### Control Options
- `--dry-run`: Show what would be changed without modifying files
- `--interactive`: Review and approve each change
- `--safe`: Only apply low-risk improvements
- `--aggressive`: Apply all possible improvements (use carefully)
- `--backup`: Create backup before changes (default: true)

### Scope Options
- `--file=<path>`: Target specific file(s)
- `--dir=<path>`: Target specific directory
- `--include=<pattern>`: Include file patterns
- `--exclude=<pattern>`: Exclude file patterns
- `--fix=<issue>`: Fix specific issue type from review
- `--priority=<level>`: Focus on priority level (critical/high/medium/low)

### Output Options
- `--verbose`: Show detailed change explanations
- `--quiet`: Minimal output, only show summary
- `--report`: Generate improvement report
- `--diff`: Show diff-style changes

## Improvement Process

### Intelligent Workflow
```
Review Analysis → Priority Assessment → Change Planning → Safe Execution → Validation
```

### Agent Orchestration
- `--refactor` → `@refactoring-specialist`
- `--docs` → `@docs-writer`
- `--security` → `@security-fixer`
- `--performance` → `@performance-optimizer`
- `--tests` → `@test-writer`
- `--style` → `@style-formatter`

## Improvement Categories

### Code Refactoring (`--refactor`)
- **Extract Methods**: Break down large functions
- **Remove Duplication**: Consolidate repeated code
- **Improve Naming**: Better variable/function names
- **Simplify Logic**: Reduce complexity
- **Apply Patterns**: Implement design patterns
- **Modernize Code**: Update to modern syntax/features

### Documentation (`--docs`)
- **Add Missing Docs**: Document undocumented code
- **Update Outdated**: Sync docs with implementation
- **Improve Examples**: Add/enhance code examples
- **Fix Errors**: Correct documentation mistakes
- **Enhance Clarity**: Improve readability
- **Add Diagrams**: Generate helpful diagrams

### Security Fixes (`--security`)
- **Patch Vulnerabilities**: Update vulnerable dependencies
- **Remove Secrets**: Clean exposed credentials
- **Fix Injection**: Prevent SQL/XSS/command injection
- **Improve Auth**: Strengthen authentication
- **Add Validation**: Input validation and sanitization
- **Encrypt Data**: Add encryption where needed

### Performance (`--performance`)
- **Algorithm Optimization**: Replace inefficient algorithms
- **Add Caching**: Implement strategic caching
- **Reduce Queries**: Optimize database access
- **Memory Management**: Fix leaks, reduce allocation
- **Async Operations**: Convert blocking to async
- **Lazy Loading**: Defer expensive operations

### Test Coverage (`--tests`)
- **Unit Tests**: Add missing unit tests
- **Edge Cases**: Test boundary conditions
- **Error Cases**: Test error handling
- **Integration Tests**: Test component interactions
- **Performance Tests**: Add benchmarks
- **Snapshot Tests**: Add regression tests

## Safe Improvement Practices

### Change Validation
Every improvement goes through validation:
1. **Syntax Check**: Ensure code still compiles/runs
2. **Test Execution**: Run existing tests
3. **Behavior Preservation**: Verify functionality unchanged
4. **Performance Check**: No performance regressions
5. **Security Scan**: No new vulnerabilities introduced

### Rollback Capability
- Automatic backup before changes
- Git commit before improvements (if in git repo)
- Detailed change log for manual rollback
- Atomic changes when possible

### Risk Levels
- **Safe**: Formatting, comments, simple renames
- **Low**: Extract method, add tests, update docs
- **Medium**: Refactor logic, update dependencies
- **High**: Architecture changes, API modifications

## Examples

### Auto-Improve After Review
```bash
# First run review
/review --code --security

# Then auto-improve based on findings
/improve
# Automatically fixes issues found in review
# Prioritizes by severity and safety
```

### Safe Refactoring
```bash
/improve --refactor --dry-run
# Shows planned refactoring changes
# Review changes before applying

/improve --refactor --safe
# Applies only safe refactoring
# No risky changes
```

### Fix Security Issues
```bash
/improve --security --priority=critical
# Fixes critical security vulnerabilities first
# Updates dependencies, patches code
```

### Enhance Documentation
```bash
/improve --docs --examples
# Adds missing documentation
# Includes working code examples
# Updates outdated sections
```

### Add Test Coverage
```bash
/improve --tests --file="src/utils.js"
# Analyzes utils.js
# Generates comprehensive test suite
# Includes edge cases
```

### Performance Optimization
```bash
/improve --performance --aggressive
# Applies all possible optimizations
# May change code structure significantly
# Best used with good test coverage
```

### Interactive Improvement
```bash
/improve --refactor --interactive
# Shows each proposed change
# Asks for confirmation
# Allows skipping specific changes
```

## Integration

### Git Workflow
```bash
# Create branch for improvements
git checkout -b improvements

# Run improvements
/improve --refactor --tests

# Review changes
git diff

# Commit if satisfied
git commit -m "Apply automated improvements"
```

### CI/CD Pipeline
```yaml
# Example GitHub Actions
- name: Auto-Improve
  run: |
    /improve --style --safe
    git add .
    git commit -m "Auto-improvements [skip ci]"
    git push
```

### Pre-Commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit
/improve --style --quiet
git add .
```

## Best Practices

### Improvement Strategy
1. **Start Safe**: Use `--dry-run` and `--safe` initially
2. **Review Changes**: Always review automated changes
3. **Test Thoroughly**: Run tests after improvements
4. **Incremental**: Improve in small batches
5. **Document**: Keep record of improvements made

### Team Workflows
- Run improvements before code review
- Use `--interactive` for team discussions
- Set improvement standards in CI/CD
- Track improvement metrics over time

## Improvement Metrics

### Success Metrics
- **Code Quality Score**: Before/after comparison
- **Test Coverage**: Percentage increase
- **Performance Gains**: Speed improvements
- **Security Score**: Vulnerabilities fixed
- **Documentation Coverage**: Docs added/updated
- **Technical Debt**: Reduction percentage

### Report Generation
```bash
/improve --report
# Generates improvement report with:
# - Changes made
# - Metrics improved
# - Time saved estimate
# - Risk assessment
# - Recommendations for manual improvements
```

## Configuration

### Default Behavior
Can be configured via `.improve.config.json`:
```json
{
  "safe_mode": true,
  "backup": true,
  "auto_commit": false,
  "exclude_patterns": ["node_modules", "dist"],
  "priority_threshold": "medium",
  "max_file_size": "1MB"
}
```

## Command Architecture

The command operates as an intelligent improvement engine:

1. **Analyze Context**: Understand current state and issues
2. **Plan Improvements**: Determine what can be improved
3. **Assess Risk**: Evaluate safety of each change
4. **Execute Changes**: Apply improvements systematically
5. **Validate Results**: Ensure improvements are successful
6. **Generate Report**: Document what was improved

This design ensures:
- Single entry point for all improvements
- Safe, validated changes
- Intelligent prioritization
- Measurable results
- Continuous improvement workflow