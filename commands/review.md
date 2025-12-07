# Universal Review Command

Execute comprehensive project reviews with multiple perspectives and focus areas.

## Overview

A single, powerful command for all review needs that:
- Analyzes code quality, architecture, and best practices
- Reviews documentation completeness and accuracy
- Identifies security vulnerabilities and performance issues
- Checks documentation-code alignment
- Provides actionable recommendations for improvements

## Usage

```bash
# Full comprehensive review (all aspects)
/review

# Focused reviews
/review --code              # Code quality and architecture
/review --docs              # Documentation review
/review --security          # Security vulnerability scan
/review --performance       # Performance analysis
/review --api              # API design and consistency
/review --alignment        # Documentation-code alignment

# Combined reviews
/review --code --security   # Code + security review
/review --docs --alignment  # Documentation + alignment check

# Quick health check
/review --quick            # Fast overview of major issues

# Output options
/review --format=json      # JSON output for tooling
/review --output=./reports # Custom output directory
```

## Parameters

### Focus Areas
- `--code`: Code quality, architecture, patterns, maintainability
- `--docs`: Documentation completeness, clarity, accuracy
- `--security`: Security vulnerabilities, secrets, unsafe patterns
- `--performance`: Performance bottlenecks, optimization opportunities
- `--api`: API design, RESTful principles, consistency
- `--alignment`: Documentation-code synchronization
- `--quick`: Rapid health check (5-minute review)
- `--all`: Complete review (default if no flags specified)

### Output Options
- `--format=<type>`: Output format
  - `markdown` (default): Human-readable reports
  - `json`: Machine-readable for CI/CD integration
  - `summary`: Brief executive summary only

- `--output=<path>`: Output directory (default: `./review-results`)
- `--verbose`: Include detailed findings and examples
- `--quiet`: Only show critical issues

### Scope Control
- `--include=<pattern>`: Include specific files/directories
- `--exclude=<pattern>`: Exclude files/directories
- `--depth=<level>`: Analysis depth (1-5, default: 3)
- `--language=<lang>`: Focus on specific language

## Review Process

### Intelligent Agent Orchestration
The command automatically selects and coordinates appropriate agents:

```
User Input → Parameter Parsing → Agent Selection → Parallel Execution → Result Aggregation
```

### Agent Mapping
- `--code` → `@code-analyzer` + `@tech-lead-pe`
- `--docs` → `@docs-analyzer`
- `--security` → `@security-scanner`
- `--performance` → `@performance-analyzer`
- `--api` → `@api-analyzer`
- `--alignment` → `@alignment-checker`

## Output Structure

### Default Output (`./review-results/`)
```
review-results/
├── summary.md           # Executive summary
├── code-review.md       # Code quality findings
├── docs-review.md       # Documentation assessment
├── security-review.md   # Security vulnerabilities
├── performance.md       # Performance analysis
├── recommendations.md   # Prioritized action items
└── review.json         # Complete data (if --format=json)
```

### Report Sections

#### Executive Summary
- Overall health score (A-F grade)
- Critical issues requiring immediate attention
- Key strengths and achievements
- Top 5 priority improvements

#### Detailed Findings
- **Issues**: Specific problems identified
- **Location**: Where the issue exists
- **Severity**: Critical/High/Medium/Low
- **Recommendation**: How to fix it
- **Effort**: Estimated time to resolve

## Review Categories

### Code Review (`--code`)
- **Architecture**: Design patterns, structure, modularity
- **Quality**: Readability, maintainability, DRY principles
- **Testing**: Test coverage, quality, edge cases
- **Standards**: Coding conventions, linting compliance
- **Complexity**: Cyclomatic complexity, cognitive load
- **Dependencies**: Outdated packages, security advisories

### Documentation Review (`--docs`)
- **Completeness**: Coverage of all features
- **Clarity**: Readability and understanding
- **Accuracy**: Correctness of examples and descriptions
- **Structure**: Logical organization and navigation
- **Freshness**: Up-to-date with current implementation
- **Accessibility**: Ease of finding information

### Security Review (`--security`)
- **Vulnerabilities**: Known CVEs in dependencies
- **Secrets**: Exposed API keys, passwords, tokens
- **Injection**: SQL, XSS, command injection risks
- **Authentication**: Weak auth patterns
- **Authorization**: Access control issues
- **Data Protection**: Encryption, PII handling

### Performance Review (`--performance`)
- **Bottlenecks**: Slow operations, N+1 queries
- **Memory**: Leaks, excessive allocation
- **Algorithms**: Inefficient implementations
- **Caching**: Missing cache opportunities
- **Database**: Query optimization needs
- **Concurrency**: Threading issues, race conditions

### API Review (`--api`)
- **REST Compliance**: Proper HTTP methods, status codes
- **Consistency**: Naming conventions, response formats
- **Documentation**: OpenAPI/Swagger completeness
- **Versioning**: Version strategy and compatibility
- **Error Handling**: Consistent error responses
- **Security**: Authentication, rate limiting

## Examples

### Quick Project Health Check
```bash
/review --quick
# Runs rapid analysis focusing on critical issues
# Generates 1-page summary in 5 minutes
```

### Pre-Release Security Review
```bash
/review --security --code --format=json
# Deep security and code review
# JSON output for CI/CD pipeline integration
# Fails build if critical issues found
```

### Documentation Audit
```bash
/review --docs --alignment --verbose
# Comprehensive documentation review
# Checks if docs match actual implementation
# Includes specific examples of mismatches
```

### Performance Optimization Review
```bash
/review --performance --include="src/api/*"
# Focused performance review of API code
# Identifies bottlenecks and optimization opportunities
```

### Full Project Review
```bash
/review
# Complete review of all aspects
# Generates comprehensive report suite
# Provides prioritized improvement roadmap
```

## Integration

### CI/CD Pipeline
```yaml
# Example GitHub Actions integration
- name: Code Review
  run: /review --code --security --format=json

- name: Check Review Results
  run: |
    if [ $(jq '.critical_issues' review.json) -gt 0 ]; then
      exit 1
    fi
```

### Pre-Commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit
/review --quick --quiet
if [ $? -ne 0 ]; then
  echo "Review found critical issues. Please fix before committing."
  exit 1
fi
```

## Best Practices

### Regular Reviews
- **Daily**: `--quick` during development
- **Weekly**: `--code --security` for sprints
- **Monthly**: `--performance --api` for optimization
- **Quarterly**: Full review for comprehensive assessment

### Team Workflows
1. Run review before code reviews
2. Include review results in PR descriptions
3. Track improvement metrics over time
4. Set quality gates based on review scores

## Review Scoring

### Grade Calculation
- **A**: 90-100% (Excellent, minimal issues)
- **B**: 80-89% (Good, minor improvements needed)
- **C**: 70-79% (Acceptable, several areas for improvement)
- **D**: 60-69% (Poor, significant issues)
- **F**: <60% (Critical, immediate attention required)

### Factors
- Issue severity and count
- Test coverage percentage
- Documentation completeness
- Security vulnerability presence
- Performance metrics
- Code complexity scores

## Command Architecture

The command acts as an intelligent orchestrator:

1. **Parse Arguments**: Understand user intent
2. **Select Agents**: Choose appropriate analysis agents
3. **Configure Scope**: Set include/exclude patterns
4. **Execute Parallel**: Run agents concurrently for speed
5. **Aggregate Results**: Combine findings coherently
6. **Generate Reports**: Create requested output format
7. **Provide Recommendations**: Prioritize improvements

This design ensures:
- Single entry point for all review needs
- Consistent user experience
- Efficient execution through parallelization
- Comprehensive yet focused analysis
- Actionable outcomes