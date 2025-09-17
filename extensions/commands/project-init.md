---
allowed-tools: ["Task", "Bash", "Read", "Write"]
thinking-level: "think hard"
description: "Initialize a new project with best practices"
argument-hint: "<project-type> <project-name> [options]"
---

# /project-init

think hard about initializing a new project with comprehensive setup and best practices.

## Command Purpose

This command orchestrates the complete initialization of a new project by:
1. Analyzing requirements
2. Building project structure
3. Setting up development environment
4. Validating the setup

## Workflow Execution

1. **Analysis Phase**
   - Invoke @scaffold-analyzer to understand requirements
   - Determine project type and technology stack

2. **Building Phase**
   - Invoke @project-builder to create structure
   - Generate all necessary files and configurations

3. **Environment Phase**
   - Invoke @environment-setup to configure tools
   - Install dependencies and setup automation

4. **Validation Phase**
   - Verify project setup completeness
   - Run initial tests or checks

## Usage Examples

```bash
/project-init python my-cli-tool
/project-init react my-web-app --typescript
/project-init rust my-library --workspace
```

## Success Criteria

- Complete project structure created
- All dependencies installed
- Development environment ready
- Initial commit prepared
- Documentation generated
