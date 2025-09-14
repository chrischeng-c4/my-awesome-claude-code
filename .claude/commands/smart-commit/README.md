---
allowed-tools: ["Bash", "Read", "Write", "Edit", "Grep", "Task", "TodoWrite"]
model: "claude-opus-4-1-20250805"
description: "Intelligent git commit workflow with security scanning, change grouping, and automated commit messages"
argument-hint: "[--all] [--security-only] [--auto-gitignore] [--conventional]"
thinking-level: "ultrathink"
subagents: ["change-analyzer", "security-scanner", "commit-generator", "gitignore-manager"]
project-aware: true
---

# /smart-commit

ultrathink about creating intelligent git commits by analyzing changes for security issues, grouping related modifications, managing .gitignore automatically, and generating meaningful commit messages iteratively.

## Workflow Intelligence

This command orchestrates a comprehensive git commit workflow that:
- Scans changes for security vulnerabilities and secrets
- Groups related changes into logical commits
- Automatically updates .gitignore for sensitive files
- Generates conventional commit messages
- Iterates until all changes are committed
- Follows git best practices

## Workflow Phases

### Phase 1: Change Analysis
@change-analyzer: Analyze all uncommitted changes
```markdown
1. **Git Status Analysis**
   - Modified files
   - Untracked files
   - Deleted files
   - Renamed files

2. **Change Categorization**
   - Feature additions
   - Bug fixes
   - Documentation updates
   - Configuration changes
   - Test additions/modifications
   - Refactoring

3. **Logical Grouping**
   - Group related files by module/feature
   - Separate concerns (e.g., tests from implementation)
   - Identify dependencies between changes
```

### Phase 2: Security Scanning
@security-scanner: Check for security issues
```markdown
1. **Secret Detection**
   - API keys and tokens
   - Passwords and credentials
   - Private keys and certificates
   - Connection strings
   - Environment variables with secrets

2. **Vulnerability Scanning**
   - Hardcoded sensitive data
   - Insecure configurations
   - Exposed endpoints
   - Debug information
   - Personal data (PII)

3. **File Analysis**
   - Binary files that shouldn't be committed
   - Large files that should use LFS
   - Generated files that should be ignored
   - Temporary or cache files
```

### Phase 3: .gitignore Management
@gitignore-manager: Update .gitignore as needed
```markdown
1. **Detect Files to Ignore**
   - IDE configuration (.idea/, .vscode/)
   - Build artifacts (dist/, build/)
   - Dependencies (node_modules/, venv/)
   - Environment files (.env, .env.local)
   - OS files (.DS_Store, Thumbs.db)
   - Log files (*.log)
   - Cache files (__pycache__, .cache/)

2. **Update .gitignore**
   - Add new patterns
   - Organize by category
   - Add comments for clarity
   - Remove files from staging if needed

3. **Validate Changes**
   - Ensure critical files aren't ignored
   - Check for overly broad patterns
   - Verify gitignore syntax
```

### Phase 4: Commit Generation
@commit-generator: Create meaningful commits
```markdown
1. **Commit Message Generation**
   - Follow conventional commits format
   - Include scope when applicable
   - Add descriptive body for complex changes
   - Reference issues/tickets if found

2. **Commit Structure**
   Type: feat|fix|docs|style|refactor|test|chore|perf|ci
   Format: <type>(<scope>): <subject>

   [optional body]

   [optional footer]

3. **Interactive Confirmation**
   - Show proposed commit
   - Allow message editing
   - Confirm before committing
```

## Workflow Execution

### Main Loop
```bash
while [[ $(git status --porcelain) ]]; do
    # Phase 1: Analyze changes
    CHANGES=$(analyze_git_changes)

    # Phase 2: Security scan
    SECURITY_ISSUES=$(scan_for_security_issues "$CHANGES")

    if [[ -n "$SECURITY_ISSUES" ]]; then
        handle_security_issues "$SECURITY_ISSUES"
    fi

    # Phase 3: Update .gitignore if needed
    update_gitignore_if_needed "$CHANGES"

    # Phase 4: Group and commit
    GROUPS=$(group_related_changes "$CHANGES")

    for group in $GROUPS; do
        stage_files "$group"
        MESSAGE=$(generate_commit_message "$group")
        confirm_and_commit "$MESSAGE"
    done
done
```

## Security Patterns

### Secrets Detection
```python
SECRET_PATTERNS = [
    r'api[_-]?key["\']?\s*[:=]\s*["\'][^"\']+["\']',
    r'secret[_-]?key["\']?\s*[:=]\s*["\'][^"\']+["\']',
    r'password["\']?\s*[:=]\s*["\'][^"\']+["\']',
    r'token["\']?\s*[:=]\s*["\'][^"\']+["\']',
    r'-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----',
    r'[a-zA-Z0-9+/]{40,}={0,2}',  # Base64 encoded secrets
]

FILES_TO_CHECK = [
    '.env', '.env.*', '*.conf', '*.cfg', '*.ini',
    '*.json', '*.yaml', '*.yml', '*.toml'
]
```

### Auto-gitignore Patterns
```python
SHOULD_IGNORE = {
    # IDE
    '.idea/': 'JetBrains IDE configuration',
    '.vscode/': 'VS Code configuration',
    '*.swp': 'Vim swap files',

    # Python
    '__pycache__/': 'Python cache',
    '*.pyc': 'Python compiled files',
    '.venv/': 'Virtual environment',
    'venv/': 'Virtual environment',
    '.pytest_cache/': 'Pytest cache',

    # Node.js
    'node_modules/': 'Node dependencies',
    'npm-debug.log': 'NPM debug log',

    # Environment
    '.env': 'Environment variables',
    '.env.*': 'Environment variants',

    # OS
    '.DS_Store': 'macOS folder attributes',
    'Thumbs.db': 'Windows thumbnails',

    # Builds
    'dist/': 'Distribution files',
    'build/': 'Build output',
    '*.egg-info/': 'Python package info',
}
```

## Commit Message Templates

### Conventional Commits
```markdown
feat: add user authentication system
feat(auth): implement JWT token validation
fix: resolve memory leak in data processor
docs: update API documentation
style: format code according to style guide
refactor: extract common logic to utils
test: add unit tests for auth module
chore: update dependencies
perf: optimize database queries
ci: add GitHub Actions workflow
```

### Commit Grouping Logic
```python
def group_changes(files):
    groups = {
        'feature': [],
        'tests': [],
        'docs': [],
        'config': [],
        'style': [],
    }

    for file in files:
        if 'test' in file or 'spec' in file:
            groups['tests'].append(file)
        elif file.endswith(('.md', '.rst', '.txt')):
            groups['docs'].append(file)
        elif file.endswith(('.json', '.yaml', '.toml', '.ini')):
            groups['config'].append(file)
        elif is_source_file(file):
            groups['feature'].append(file)
        else:
            groups['style'].append(file)

    return groups
```

## Interactive Mode

### Commit Review
```bash
echo "📝 Proposed Commit:"
echo "=================="
echo "Files to commit:"
git diff --cached --name-status

echo ""
echo "Commit message:"
echo "$COMMIT_MESSAGE"

echo ""
read -p "Accept this commit? (y/n/e for edit): " choice

case $choice in
    y) git commit -m "$COMMIT_MESSAGE" ;;
    e) git commit -e -m "$COMMIT_MESSAGE" ;;
    n) git reset HEAD ;;
esac
```

## Options

### Command Arguments
- `--all`: Stage and commit all changes at once
- `--security-only`: Only run security scan without committing
- `--auto-gitignore`: Automatically update .gitignore without prompting
- `--conventional`: Enforce conventional commit format
- `--no-group`: Don't group changes, commit files individually
- `--dry-run`: Show what would be done without making changes

## Output Example

```
🔍 Smart Commit Workflow Started
================================

📊 Analyzing changes...
  - 12 files modified
  - 3 files added
  - 1 file deleted

🔒 Security scan...
  ⚠️ Found potential secret in config/database.yml
  ✅ Added config/database.yml to .gitignore
  ✅ Created config/database.yml.example

📁 Updating .gitignore...
  + Added: *.log
  + Added: .env.local
  + Added: coverage/

🎯 Grouping related changes...

Group 1: Feature - User Authentication (5 files)
  - src/auth/login.py
  - src/auth/logout.py
  - src/models/user.py
  - src/middleware/auth.py
  - src/utils/jwt.py

  Suggested commit:
  "feat(auth): implement user authentication system"

  [y]es / [n]o / [e]dit / [s]kip? y
  ✅ Committed successfully

Group 2: Tests - Authentication Tests (3 files)
  - tests/test_login.py
  - tests/test_logout.py
  - tests/test_jwt.py

  Suggested commit:
  "test(auth): add authentication test suite"

  [y]es / [n]o / [e]dit / [s]kip? y
  ✅ Committed successfully

Group 3: Documentation Updates (2 files)
  - README.md
  - docs/authentication.md

  Suggested commit:
  "docs: add authentication documentation"

  [y]es / [n]o / [e]dit / [s]kip? y
  ✅ Committed successfully

✨ All changes committed successfully!

Summary:
- 3 commits created
- 1 security issue resolved
- .gitignore updated with 3 new patterns
- 16 files processed
```

## Best Practices Enforced

1. **Atomic Commits**: Each commit does one thing
2. **No Secrets**: Prevents credential exposure
3. **Clean History**: Logical, understandable commits
4. **Conventional Format**: Standardized messages
5. **Security First**: Scan before commit
6. **Automatic Cleanup**: Manages .gitignore

This workflow ensures professional, secure, and well-organized git commits every time.