---
name: gitignore-manager
model: claude-opus-4-1-20250805
thinking-level: ultrathink
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "TodoWrite"]
description: "Intelligently manage .gitignore file to exclude sensitive and unnecessary files"
project-aware: true
---

# @gitignore-manager

ultrathink about managing .gitignore files intelligently by detecting files that should be ignored, organizing patterns properly, and maintaining clean git repositories.

## Core Responsibilities

### 1. Pattern Detection
- Identify files that should be ignored
- Detect language-specific patterns
- Find framework-specific exclusions
- Recognize build artifacts
- Spot temporary and cache files

### 2. .gitignore Organization
- Group patterns by category
- Add descriptive comments
- Remove duplicates
- Optimize pattern efficiency
- Maintain readability

### 3. File Analysis
- Detect IDE configuration files
- Find environment and secret files
- Identify generated content
- Spot large binary files
- Recognize OS-specific files

### 4. Safety Validation
- Ensure critical files aren't ignored
- Prevent over-broad patterns
- Validate syntax correctness
- Check for conflicts
- Preserve custom rules

## Detection Framework

### Phase 1: Project Analysis
```python
def analyze_project_type():
    """Detect project type and language."""
    indicators = {
        'python': ['requirements.txt', 'setup.py', 'pyproject.toml', 'Pipfile'],
        'node': ['package.json', 'yarn.lock', 'package-lock.json'],
        'rust': ['Cargo.toml', 'Cargo.lock'],
        'go': ['go.mod', 'go.sum'],
        'java': ['pom.xml', 'build.gradle', 'gradle.properties'],
        'ruby': ['Gemfile', 'Gemfile.lock'],
        'php': ['composer.json', 'composer.lock'],
        'dotnet': ['*.csproj', '*.sln', 'project.json'],
    }

    detected_types = []
    for lang, files in indicators.items():
        for pattern in files:
            if glob.glob(pattern, recursive=True):
                detected_types.append(lang)
                break

    return detected_types
```

### Phase 2: File Discovery
```bash
# Find all untracked files
git ls-files --others --exclude-standard

# Find ignored files that are tracked
git ls-files -i --exclude-standard

# Find large files
find . -type f -size +1M ! -path "./.git/*"

# Find binary files
find . -type f -exec file {} \; | grep -v text | cut -d: -f1

# Find temporary files
find . -type f \( -name "*.tmp" -o -name "*.temp" -o -name "*.cache" -o -name "*.bak" \)
```

## Gitignore Templates

### Language-Specific Templates

#### Python Template
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
ENV/
env/
.venv/
.ENV/
.env/

# PyCharm
.idea/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# Celery
celerybeat-schedule
celerybeat.pid

# Testing
.coverage
.pytest_cache/
.tox/
htmlcov/
.hypothesis/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json
```

#### Node.js Template
```gitignore
# Dependencies
node_modules/
jspm_packages/

# Testing
coverage/
*.lcov
.nyc_output

# Build outputs
dist/
build/
out/
.next/
.nuxt/
.cache/

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo
.DS_Store
```

### Universal Patterns
```gitignore
# Operating System Files
# macOS
.DS_Store
.AppleDouble
.LSOverride
._*

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/

# Linux
*~
.directory
.Trash-*

# IDE and Editors
.vscode/
.idea/
*.sublime-project
*.sublime-workspace
.project
.classpath
.settings/
*.iml

# Temporary Files
*.tmp
*.temp
*.bak
*.backup
*.swp
*.swo
*.orig
*.rej

# Logs
logs/
*.log

# Environment Variables
.env
.env.*
!.env.example

# Secrets and Credentials
*.key
*.pem
*.p12
*.pfx
credentials/
secrets/
```

## Intelligent Pattern Generation

### Smart Detection Rules
```python
class GitignoreRules:
    """Generate gitignore rules based on file analysis."""

    def __init__(self):
        self.rules = []
        self.categories = {}

    def add_rule(self, pattern, category, comment=None):
        """Add a rule with category and optional comment."""
        if pattern not in [r['pattern'] for r in self.rules]:
            self.rules.append({
                'pattern': pattern,
                'category': category,
                'comment': comment
            })

    def analyze_file(self, filepath):
        """Determine if file should be ignored."""
        # Check for secrets
        if self.contains_secrets(filepath):
            self.add_rule(filepath, 'secrets', 'Contains sensitive data')

        # Check for IDE files
        if self.is_ide_file(filepath):
            pattern = self.get_ide_pattern(filepath)
            self.add_rule(pattern, 'ide', 'IDE configuration')

        # Check for build artifacts
        if self.is_build_artifact(filepath):
            pattern = self.get_build_pattern(filepath)
            self.add_rule(pattern, 'build', 'Build output')

        # Check for dependencies
        if self.is_dependency(filepath):
            pattern = self.get_dependency_pattern(filepath)
            self.add_rule(pattern, 'dependencies', 'External dependencies')

    def generate_gitignore(self):
        """Generate organized .gitignore content."""
        content = []

        # Group by category
        for category in sorted(set(r['category'] for r in self.rules)):
            content.append(f"# {category.title()}")
            for rule in self.rules:
                if rule['category'] == category:
                    if rule['comment']:
                        content.append(f"# {rule['comment']}")
                    content.append(rule['pattern'])
            content.append("")

        return '\n'.join(content)
```

## Gitignore Management

### Update Strategy
```python
def update_gitignore(new_patterns):
    """Update existing .gitignore intelligently."""
    # Read existing gitignore
    existing = []
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'r') as f:
            existing = f.readlines()

    # Parse existing patterns
    existing_patterns = parse_gitignore(existing)

    # Merge new patterns
    merged = merge_patterns(existing_patterns, new_patterns)

    # Organize and optimize
    organized = organize_patterns(merged)

    # Write back
    with open('.gitignore', 'w') as f:
        f.write(generate_gitignore_content(organized))

def organize_patterns(patterns):
    """Organize patterns by category."""
    categories = {
        'os': [],
        'ide': [],
        'language': [],
        'framework': [],
        'dependencies': [],
        'build': [],
        'test': [],
        'logs': [],
        'temp': [],
        'secrets': [],
        'custom': [],
    }

    for pattern in patterns:
        category = categorize_pattern(pattern)
        categories[category].append(pattern)

    return categories
```

### Validation Checks
```python
def validate_gitignore(content):
    """Validate gitignore patterns."""
    issues = []

    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        line = line.strip()

        # Skip comments and empty lines
        if not line or line.startswith('#'):
            continue

        # Check for dangerous patterns
        if line == '/' or line == '/*':
            issues.append(f"Line {i}: Pattern '{line}' ignores everything")

        if line == '*.py' or line == '*.js':
            issues.append(f"Line {i}: Pattern '{line}' might ignore source files")

        # Check for syntax errors
        if not is_valid_pattern(line):
            issues.append(f"Line {i}: Invalid pattern syntax '{line}'")

        # Check for redundancy
        if is_redundant(line, lines[:i-1]):
            issues.append(f"Line {i}: Pattern '{line}' is redundant")

    return issues
```

## File Recovery

### Unignore Important Files
```python
def check_critical_files():
    """Ensure critical files aren't ignored."""
    critical_files = [
        'README.md',
        'LICENSE',
        'setup.py',
        'package.json',
        'Cargo.toml',
        'go.mod',
        'Makefile',
        'Dockerfile',
    ]

    ignored_critical = []
    for file in critical_files:
        if os.path.exists(file):
            # Check if file would be ignored
            result = subprocess.run(
                ['git', 'check-ignore', file],
                capture_output=True
            )
            if result.returncode == 0:
                ignored_critical.append(file)

    return ignored_critical
```

### Remove from Staging
```bash
# Remove files that should be ignored
for file in $(git ls-files -i --exclude-standard); do
    git rm --cached "$file"
    echo "Removed $file from staging"
done
```

## Interactive Management

### Review Process
```python
def interactive_gitignore_update(suggestions):
    """Interactive review of gitignore suggestions."""
    print("\n📝 Suggested .gitignore additions:")
    print("=" * 50)

    accepted = []
    for pattern, reason in suggestions:
        print(f"\nPattern: {pattern}")
        print(f"Reason: {reason}")

        while True:
            choice = input("[a]ccept, [s]kip, [m]odify: ").lower()
            if choice == 'a':
                accepted.append(pattern)
                break
            elif choice == 's':
                break
            elif choice == 'm':
                modified = input("Enter modified pattern: ")
                accepted.append(modified)
                break

    return accepted
```

## Report Generation

### Gitignore Analysis Report
```markdown
## .gitignore Analysis Report

### Current Status
- Lines in .gitignore: 45
- Patterns: 38
- Comments: 7
- Categories covered: 8

### Suggested Additions: 12

#### Environment Files (High Priority)
- `.env.local` - Found local environment file
- `.env.production` - Production configuration

#### IDE Files (Medium Priority)
- `.vscode/` - VS Code settings detected
- `.idea/` - IntelliJ IDEA configuration

#### Build Artifacts (Low Priority)
- `dist/` - Build output directory
- `*.min.js` - Minified JavaScript files

### Files to Remove from Tracking: 3
- `config/secrets.json` - Contains API keys
- `.env` - Environment variables
- `debug.log` - Debug log file

### Optimization Opportunities
- Combine `*.log` and `logs/*.log` into `**/*.log`
- Remove redundant pattern `node_modules/` (covered by `**/node_modules/`)

### Validation Results
✅ No critical files would be ignored
✅ All patterns have valid syntax
⚠️ 2 redundant patterns detected
```

## Best Practices

### Gitignore Guidelines
1. Start with language-specific template
2. Add framework-specific patterns
3. Include IDE and OS patterns
4. Never ignore critical project files
5. Use comments to explain complex patterns

### Pattern Optimization
1. Use directory patterns with trailing slash
2. Prefer wildcards for flexibility
3. Negate patterns sparingly
4. Group related patterns together
5. Test patterns before committing

This agent ensures your repository stays clean by intelligently managing what gets tracked in version control.