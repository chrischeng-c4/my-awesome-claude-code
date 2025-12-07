# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**CC Awesome Claude Code** is a Claude Code plugin (not a Python application) that provides 20 powerful extensions: 7 commands and 13 agents for intelligent development workflows.

This is an **official Claude Code plugin**, not a traditional software project. The extensions are markdown-based prompt specifications that Claude Code interprets directly. There is no build process, compilation, or application runtime.

## Key Architecture Concepts

### Plugin Structure
- **`.claude-plugin/plugin.json`** - Core manifest that registers all 20 extensions with Claude Code
  - Lists all 7 commands in `commands/` directory
  - Lists all 13 agents in `agents/` directory
  - All paths must use `./` prefix (relative to repository root)

- **`.claude-plugin/marketplace.json`** - Metadata for GitHub marketplace distribution
  - Used when plugin is distributed via `/plugin marketplace add` command

### Extension Types

**Commands** (`commands/` directory)
- Markdown files that define user-facing slash commands (e.g., `/smart-commit`)
- Each file has YAML frontmatter with metadata
- Key frontmatter fields:
  - `description`: Brief description
  - `model`: Claude model to use (currently `claude-opus-4-1-20250805`)
  - `thinking-level`: Set to `"ultrathink"` for complex reasoning
  - `allowed-tools`: Array of Claude Code tools available
  - `subagents`: Array of agent names the command orchestrates
  - `project-aware`: Boolean if command reads/writes project files
- Markdown content describes the workflow and what Claude should do

**Agents** (`agents/` directory)
- Markdown files that define specialized AI workers (e.g., `@security-scanner`)
- Similar YAML frontmatter with `name` field required for agents
- Agents are typically invoked by commands via the `subagents` mechanism
- Examples:
  - `/smart-commit` orchestrates 4 agents: @change-analyzer, @security-scanner, @commit-generator, @gitignore-manager
  - Can also be invoked directly in Claude Code as `@agent-name`

### Key Subagent Orchestration Example
`/smart-commit` demonstrates the command-agent pattern:
1. **@change-analyzer** - Groups related changes logically
2. **@security-scanner** - Detects secrets and vulnerabilities
3. **@gitignore-manager** - Suggests .gitignore updates
4. **@commit-generator** - Creates conventional commit messages

## Common Development Tasks

### Adding a New Command

1. Create `commands/my-command.md`:
```yaml
---
description: "What this command does"
model: "claude-opus-4-5-20251101"
thinking-level: "ultrathink"
allowed-tools: ["Bash", "Read", "Write", "Edit", "Grep", "Task"]
subagents: ["agent-name-1"]  # Optional
project-aware: true
---

# /my-command

Detailed markdown describing the workflow...
```

2. Update `.claude-plugin/plugin.json` to add entry under `"commands"`:
```json
{
  "name": "my-command",
  "path": "./commands/my-command.md",
  "description": "What this command does"
}
```

3. Test locally:
```bash
/plugin install /Users/chrischeng/projects/my-awesome-claude-code
/my-command
```

### Adding a New Agent

1. Create `agents/my-agent.md`:
```yaml
---
name: my-agent
description: "What this agent does"
model: "claude-opus-4-5-20251101"
thinking-level: "ultrathink"
allowed-tools: ["Read", "Bash", "Grep"]
project-aware: false
---

# @my-agent

Detailed markdown describing the agent's responsibilities...
```

2. Update `.claude-plugin/plugin.json` to add entry under `"agents"`:
```json
{
  "name": "my-agent",
  "path": "./agents/my-agent.md",
  "description": "What this agent does"
}
```

3. Reference in command's `subagents` field if using from a command

### Making Commits

Use `/smart-commit` command - it's designed for this plugin itself:
```bash
/smart-commit --conventional
```

This runs the complete workflow:
- Analyzes changes (@change-analyzer)
- Scans for secrets (@security-scanner)
- Updates .gitignore (@gitignore-manager)
- Generates commit message (@commit-generator)

### Validating Plugin Structure

Ensure JSON is valid:
```bash
python3 -m json.tool .claude-plugin/plugin.json
python3 -m json.tool .claude-plugin/marketplace.json
```

Check all referenced files exist:
```bash
# All commands listed in plugin.json should have files in commands/
# All agents listed in plugin.json should have files in agents/
# All subagent references should match agent names
```

### Testing Changes Locally

Install plugin in editable mode for immediate testing:
```bash
/plugin install /Users/chrischeng/projects/my-awesome-claude-code
```

Test specific command/agent:
```bash
/smart-commit
@security-scanner
```

## Documentation Structure

- **README.md** - User-facing overview and quick start
- **CONTRIBUTING.md** - Development guidelines for adding extensions
- **CHANGELOG.md** - Version history
- **docs/commands.md** - Detailed reference for all 7 commands
- **docs/agents.md** - Detailed reference for all 13 agents
- **docs/workflows.md** - Common workflow patterns and combinations
- **docs/configuration.md** - Project-level configuration options
- **archive/DEPRECATION_NOTICE.md** - Migration guide from old Python CLI

## Important Implementation Details

### YAML Frontmatter Requirements

All commands and agents MUST have valid YAML frontmatter. Key requirements:
- Start and end with `---` (three dashes)
- For agents, `name:` field is required
- `description:` field should be concise
- `model:` and `thinking-level:` affect behavior
- `allowed-tools:` restricts what Claude can do
- `subagents:` names MUST match existing agent filenames

### Plugin.json Path Format

All paths in `.claude-plugin/plugin.json` MUST:
- Use `./` prefix (e.g., `./commands/smart-commit.md`)
- Be relative to repository root
- Match actual filenames exactly (case-sensitive on Linux/Mac)
- Use forward slashes, not backslashes

Incorrect paths will prevent plugin from loading.

### Model Versions

Currently using `claude-opus-4-1-20250805`. When updating:
- Test that new model version is accessible
- Commands using `ultrathink` need capable models
- Update all frontmatter consistently for major upgrades

### Git Workflow

The plugin is git-based distribution:
1. Changes committed to main branch
2. Releases tagged (e.g., `v1.0.0`)
3. Users install via: `/plugin marketplace add chrischeng/my-awesome-claude-code`
4. Plugin loaded directly from GitHub

Never commit:
- `.claude/settings.local.json` (user-specific permissions)
- Temporary test files
- Personal configuration

## Testing Strategy

### Validation Checklist

Before committing changes:

1. **JSON Syntax**
   ```bash
   python3 -m json.tool .claude-plugin/plugin.json
   python3 -m json.tool .claude-plugin/marketplace.json
   ```

2. **File References**
   - All commands in plugin.json have files in `commands/`
   - All agents in plugin.json have files in `agents/`
   - All subagent references match agent names exactly

3. **YAML Frontmatter**
   - Each command/agent file starts with `---`
   - Valid YAML syntax
   - Required fields present

4. **Functional Testing**
   ```bash
   # Install locally
   /plugin install /path/to/repo

   # Test key commands
   /smart-commit
   /review
   /improve

   # Test agents
   @security-scanner
   @code-analyzer
   ```

5. **Documentation Sync**
   - docs/commands.md reflects all commands in plugin.json
   - docs/agents.md reflects all agents in plugin.json
   - Description fields match README/docs

## Special Considerations

### This Plugin is Self-Referential

The plugin defines tools for development itself. Examples:
- `/smart-commit` can be used on this repository
- `/improve` can analyze the plugin extensions
- `/review` can review command/agent quality

This makes it ideal for testing during development.

### No Runtime Dependencies

Unlike traditional projects, there are:
- No npm/pip dependencies to install
- No build process
- No compilation
- No test runner

Everything is text-based markdown prompts interpreted by Claude Code.

### Backward Compatibility

The plugin is currently at v1.0.0. If making breaking changes:
1. Update version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`
2. Add migration notes to CHANGELOG.md
3. Tag new release (e.g., `v1.1.0`)

## Permissions

See `.claude/.settings.local.json` for the current permission configuration. It allows:
- Git operations (add, commit, push, tag, pull, merge, stash)
- File operations (Read, Write, Edit, Bash with specific commands)
- Tool invocations for development tasks

These are project-level permissions for development convenience.

## References

- **Official Docs**: [Claude Code Plugins](https://code.claude.com/docs/en/plugins)
- **Plugin Reference**: [Plugin Manifest Schema](https://code.claude.com/docs/en/plugins-reference)
- **Marketplaces**: [Plugin Distribution](https://code.claude.com/docs/en/plugin-marketplaces)
- **Slash Commands**: [Command Development](https://code.claude.com/docs/en/slash-commands)
- **Agent Skills**: [Building Agents](https://code.claude.com/docs/en/skills)

---

**Version**: 1.0.0 | **Last Updated**: December 8, 2025
