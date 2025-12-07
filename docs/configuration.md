# Configuration Guide

Customize CC Awesome Claude Code to match your workflow and preferences.

## Installation Configuration

### Plugin-Level Installation

By default, plugins are installed at the user level. To install at project level:

```bash
# User level (default)
/plugin install cc-awesome-cc@chrischeng

# Project level (within a specific project)
/plugin install cc-awesome-cc@chrischeng --project .
```

### Multiple Instances

Install custom variants of commands or agents for specific projects:

```bash
# Create project-specific version
/update-command deploy --level=project
/update-agent performance-analyzer --level=project
```

---

## Project Configuration

Create `.claude-plugins.json` in your project root for plugin customization:

```json
{
  "cc-awesome-cc": {
    "enabled": true,
    "version": "1.0.0",
    "settings": {
      "security": {
        "scanSecrets": true,
        "checkVulnerabilities": true,
        "allowedSecretPatterns": []
      },
      "commits": {
        "conventional": true,
        "requireDescription": true,
        "maxLineLength": 100
      },
      "project": {
        "defaultType": "react",
        "defaultFeatures": ["typescript", "testing"]
      }
    }
  }
}
```

### Configuration Options

#### Security Settings

```json
"security": {
  "scanSecrets": true,           // Enable secret scanning
  "checkVulnerabilities": true,  // Check for vulnerabilities
  "allowedSecretPatterns": [],   // Patterns to whitelist
  "scanBinaryFiles": false,      // Scan binary files
  "scanLargeFiles": true,        // Scan >1MB files
  "entropyThreshold": 4.5        // High-entropy detection
}
```

#### Commit Settings

```json
"commits": {
  "conventional": true,          // Enforce conventional commits
  "requireDescription": true,    // Require commit body
  "maxLineLength": 100,          // Max line length
  "skipSecurityScan": false,     // Always scan
  "autoGitignore": false,        // Auto-update gitignore
  "groupRelated": true           // Group related changes
}
```

#### Project Settings

```json
"project": {
  "defaultType": "react",                    // Default project type
  "defaultFeatures": ["typescript", "testing"], // Default features
  "defaultTemplate": "cra"                    // Default template
}
```

#### Workflow Settings

```json
"workflow": {
  "docsFirst": false,            // Documentation-first approach
  "tokenOptimize": true,         // Optimize for token usage
  "enableMemory": true,          // Track workflow memory
  "logDecisions": true           // Log workflow decisions
}
```

---

## Environment Variables

Configure via environment variables (optional):

```bash
# Disable plugin
export CLAUDE_PLUGIN_CC_AWESOME_CC_DISABLED=true

# Set security scan level
export CC_AWESOME_CC_SECURITY_LEVEL=strict

# Set commit conventions
export CC_AWESOME_CC_CONVENTIONAL=true

# Custom model for commands
export CC_AWESOME_CC_MODEL=claude-opus-4-5-20251101
```

---

## Custom Commands and Agents

### Create Custom Command

```bash
/update-command my-command "Description of what it does"

# Creates: commands/my-command.md
# Updates: plugin.json with new command
```

### Create Custom Agent

```bash
/update-agent my-agent "Description of what it does"

# Creates: agents/my-agent.md
# Updates: plugin.json with new agent
```

### Edit Custom Extensions

Edit the markdown files directly in `commands/` or `agents/` directories:

```markdown
---
description: "What this does"
model: "claude-opus-4-5-20251101"
thinking-level: "ultrathink"
allowed-tools: ["Read", "Write", "Bash"]
---

# /my-command

Your custom implementation...
```

---

## IDE Integration

### VS Code

Create `.vscode/settings.json`:

```json
{
  "claude-code.plugins": [
    "cc-awesome-cc@chrischeng"
  ],
  "claude-code.autoSecurity": true,
  "claude-code.autoFormat": true
}
```

### JetBrains IDEs

Create `.idea/claude.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ClaudeCodeSettings">
    <option name="plugins" value="cc-awesome-cc@chrischeng"/>
    <option name="autoSecurity" value="true"/>
  </component>
</project>
```

---

## Git Hooks

### Pre-commit Hook

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
set -e

echo "🔒 Running security scan..."
# Use security-scanner agent
# Or call smart-commit with --security-only

exit 0
```

### Pre-push Hook

Create `.git/hooks/pre-push`:

```bash
#!/bin/bash
set -e

echo "📋 Final code review..."
# Use review command

exit 0
```

---

## CI/CD Integration

### GitHub Actions

Create `.github/workflows/code-quality.yml`:

```yaml
name: Code Quality

on: [push, pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Code Review
        run: |
          # Invoke review command
          # Run security scan
          # Check documentation
```

### GitLab CI

Create `.gitlab-ci.yml`:

```yaml
code-quality:
  image: ubuntu:latest
  script:
    - |
      # Invoke review command
      # Run security scan
      # Check documentation
```

---

## Workflow Templates

### Feature Development Template

Create `.claude-templates/feature-workflow.json`:

```json
{
  "name": "feature-workflow",
  "steps": [
    "plan-feature",
    "implement",
    "test",
    "review",
    "improve",
    "document",
    "commit"
  ]
}
```

### Bug Fix Template

Create `.claude-templates/bugfix-workflow.json`:

```json
{
  "name": "bugfix-workflow",
  "steps": [
    "analyze",
    "create-failing-test",
    "implement-fix",
    "verify-fix",
    "test",
    "security-check",
    "commit"
  ]
}
```

---

## Advanced Configuration

### Custom Tool Permissions

Allow specific tools for your extensions:

```json
{
  "cc-awesome-cc": {
    "tools": {
      "allowed": ["Bash", "Read", "Write", "Edit", "Grep"],
      "denied": ["KillShell", "UnlimitedBash"]
    }
  }
}
```

### Model Configuration

Use different models for different tasks:

```json
{
  "cc-awesome-cc": {
    "models": {
      "default": "claude-opus-4-5-20251101",
      "security": "claude-opus-4-5-20251101",
      "documentation": "claude-opus-4-5-20251101",
      "analysis": "claude-opus-4-5-20251101"
    }
  }
}
```

### Rate Limiting

Configure rate limits:

```json
{
  "cc-awesome-cc": {
    "rateLimits": {
      "commandsPerHour": 100,
      "agentsPerHour": 500,
      "tokensPerDay": 1000000
    }
  }
}
```

---

## Performance Tuning

### For Large Codebases

```json
{
  "cc-awesome-cc": {
    "performance": {
      "batchSize": 100,
      "parallelAgents": 3,
      "cacheResults": true,
      "skipLargeFiles": true
    }
  }
}
```

### For Token Optimization

```json
{
  "cc-awesome-cc": {
    "optimization": {
      "tokenOptimize": true,
      "summaryLength": "short",
      "focusedAnalysis": true,
      "skipRedundantChecks": true
    }
  }
}
```

---

## Troubleshooting Configuration

### Reset to Defaults

Delete `.claude-plugins.json` and reinstall plugin:

```bash
/plugin uninstall cc-awesome-cc@chrischeng
/plugin install cc-awesome-cc@chrischeng
```

### Validate Configuration

Check JSON syntax:

```bash
# Use online JSON validator or
# cat .claude-plugins.json | python -m json.tool
```

### Debug Configuration

Enable debug logging:

```bash
export DEBUG=claude-code-plugins
# or
export CC_AWESOME_CC_DEBUG=true
```

---

## Best Practices

1. **Use Project Configuration** - Store settings in `.claude-plugins.json`
2. **Version Control** - Commit configuration files
3. **Team Consistency** - Share `.claude-plugins.json` across team
4. **Security First** - Enable security scanning
5. **Conventional Commits** - Enable conventional commit format
6. **Code Review** - Set up review processes
7. **Documentation** - Maintain documentation settings
8. **Automation** - Use CI/CD integration
9. **Custom Extensions** - Create project-specific commands/agents
10. **Regular Updates** - Keep plugin and configuration up to date

---

## Related Documentation

- [Commands Reference](commands.md)
- [Agents Reference](agents.md)
- [Workflows Guide](workflows.md)
- [README](../README.md)

---

**Version**: 1.0.0 | **Last Updated**: December 8, 2025
