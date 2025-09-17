---
allowed-tools: ["Bash", "Read", "Grep"]
thinking-level: "think hard"
description: "Validate project setup and ensure everything works correctly"
argument-hint: "[--strict]"
---

# /project-validate

think hard about validating the project setup to ensure everything is configured correctly and working.

## Validation Checks

1. **Structure Validation**
   - Verify all required directories exist
   - Check for essential files
   - Validate file permissions

2. **Dependency Validation**
   - Check all dependencies are installed
   - Verify version compatibility
   - Test import/require statements

3. **Configuration Validation**
   - Validate config file syntax
   - Check environment variables
   - Verify tool configurations

4. **Functionality Validation**
   - Run basic tests if available
   - Execute build commands
   - Check development scripts

## Output Format

Provide clear validation report:
- ✅ Passing checks
- ❌ Failing checks
- ⚠️ Warnings
- 💡 Suggestions for improvements

## Usage

```bash
/project-validate          # Standard validation
/project-validate --strict # Strict validation with warnings as errors
```
