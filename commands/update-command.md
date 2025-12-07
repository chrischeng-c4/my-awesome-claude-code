---
allowed-tools: ["Bash", "Read", "Write", "Edit", "MultiEdit", "Glob", "Grep", "Task"]
model: "claude-opus-4-1-20250805"
description: "Intelligently generate or improve commands with deep project context awareness, memory integration, and subagent orchestration"
argument-hint: "<command-name> [description] [--level=project|user] [--agent=<agent-name>]"
thinking-level: "think harder"
---

# /update-command

think harder about generating or improving a custom Claude Code command with deep project intelligence, memory awareness, and subagent orchestration.

**Enhanced Intelligence**: When creating project-level commands, this command now:
- Analyzes entire project structure and dependencies
- Reads project memory from docs/ folder
- Understands CLAUDE.md instructions and conventions
- Maps codebase patterns and testing strategies
- Generates commands that integrate with project architecture

## Command Analysis Phase

Parse the command request:
- Command name: `$1`
- Description/Requirements: `$2 $3 $4 $5 $6 $7 $8 $9`
- Target level: Check for `--level=user` or `--level=project` (default: project)
- Subagent: Check for `--agent=<name>` to leverage specific subagent

## Phase 1: Subagent Discovery and Analysis

### Check Available Subagents

First, discover what subagents are available to leverage:

```bash
# Check user-level subagents
! ls ~/.claude/agents/*.md 2>/dev/null | xargs -I {} basename {} .md

# Check project-level subagents
! ls .claude/agents/*.md 2>/dev/null | xargs -I {} basename {} .md
```

### Analyze Subagent Capabilities

If subagents exist, analyze their capabilities:
1. Read their system prompts to understand expertise
2. Check their allowed tools
3. Determine if they can assist with the command generation

### Create Command-Generation Subagent (if needed)

If no suitable subagent exists, consider creating one:

```markdown
# Subagent: command-optimizer
Location: ~/.claude/agents/command-optimizer.md

---
allowed-tools: ["Read", "Write", "Edit", "Grep", "Glob"]
description: "Expert at generating optimized Claude Code commands with best practices"
---

You are a specialized command generation expert. Your role is to:
1. Analyze command requirements deeply
2. Apply prompt engineering best practices
3. Assign optimal thinking levels
4. Structure commands for maximum effectiveness
5. Include self-improvement capabilities in every command
```

## Phase 2: Pre-Generation Intelligence

### Project Context Analysis (For Project-Level Commands)

When creating or updating project-level commands, perform deep context analysis:

#### 1. Project Structure Discovery
```bash
# Understand the project layout
! find . -type f -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.go" | head -20
! ls -la
! cat pyproject.toml package.json go.mod 2>/dev/null | head -50
```

#### 2. Memory Analysis (Documentation)
Read and understand the project's persistent memory:
- **CLAUDE.md**: Project-specific AI instructions and conventions
- **docs/STATUS.md**: Current development state
- **docs/PROGRESS.md**: Feature completion tracking
- **docs/development/**: Development history and decisions
- **docs/**: All documentation for domain knowledge

```bash
@Task: Analyze project documentation and extract:
- Core functionality and architecture
- Development patterns and conventions
- Testing strategies
- Common workflows
- Known issues and constraints
```

#### 3. Codebase Analysis
```bash
@Task: Analyze the codebase structure:
- Main entry points
- Core modules and their responsibilities
- API patterns and interfaces
- Testing patterns
- Build and deployment processes
```

#### 4. Command Context Relevance
Based on project analysis, determine:
- Which project components the command will interact with
- Required project-specific knowledge
- Integration points with existing code
- Testing requirements specific to this project

### Command Conflict Detection

Use Task tool with general-purpose agent to thoroughly check for conflicts:

```markdown
@Task: Check all existing commands (built-in and custom) for potential conflicts with "$1":
- Search ~/.claude/commands/ for similar command names
- Search .claude/commands/ for similar functionality
- Check for namespace collisions
- Identify related commands that could be enhanced instead
- For project commands, check project-specific command patterns
```

### Complexity Analysis with Subagent

If command-optimizer subagent exists, delegate complexity analysis:

```markdown
@command-optimizer: Analyze the complexity of this task and recommend thinking level:
Task: $2 $3 $4 $5 $6 $7 $8 $9
Consider:
- Number of steps required
- Decision complexity
- Risk/criticality
- Performance requirements
- Project-specific constraints from CLAUDE.md
```

## Phase 3: Intelligent Command Generation

### Thinking Level Assignment Matrix 2.0

| Task Category | Indicators | Base Level | With Subagent | Directive |
|--------------|------------|------------|---------------|-----------|
| Simple Utility | Basic I/O, wrappers | None | None | No directive |
| Data Processing | Parsing, transformation | "think" | None | "think about" |
| Code Generation | Creating new code | "think hard" | "think" | "think hard about" |
| Complex Analysis | Multi-step reasoning | "think harder" | "think hard" | "think harder about" |
| Architecture/Security | System design, critical ops | "ultrathink" | "think harder" | "ultrathink about" |

### Prompt Optimization with 5R+ Framework

Apply enhanced optimization with subagent assistance:

#### 1. Rephrase (Clarity Enhancement)
- Transform requirements into clear objectives
- Eliminate ambiguity
- Use consistent terminology

#### 2. Rewrite (Structure Optimization)
- Apply inverted pyramid structure
- Lead with most important information
- Group related concepts

#### 3. Reorganize (Logical Flow)
- Context → Objective → Process → Validation → Output
- Include checkpoints and decision trees
- Add fallback strategies

#### 4. Refine (Intelligence Injection)
- Add meta-cognitive instructions
- Include self-evaluation criteria
- Enable adaptive behavior

#### 5. Review (Quality Assurance)
- Validate completeness
- Check for edge cases
- Ensure thinking level appropriateness

#### +1. Reinforce (Subagent Integration)
- Identify tasks suitable for delegation
- Add subagent invocation points
- Include coordination instructions

## Phase 4: Command Template with Project Intelligence

Generate commands with this enhanced structure:

```markdown
---
allowed-tools: [<tools>, "Task"]  # Include Task for subagent access
model: "claude-opus-4-1-20250805"
description: "<concise-description>"
argument-hint: "<usage-pattern>"
thinking-level: <determined-level>
subagents: ["<relevant-subagents>"]  # Document which subagents to use
project-aware: true  # For project commands
---

# /<command-name>

<thinking-directive> about <primary-task-description>.

## Project Context Integration
<for-project-level-commands>
This command understands the project structure and conventions:
- Architecture: <from-project-analysis>
- Patterns: <from-CLAUDE.md>
- Memory: Reads docs/ for persistent context
- Codebase: Aware of modules and dependencies
</for-project-level-commands>

## Intelligent Execution Strategy

### Subagent Utilization
<if-applicable>
Leverage specialized subagents for enhanced capabilities:
- @<subagent-1>: <specific-task-delegation>
- @<subagent-2>: <specific-task-delegation>
</if-applicable>

### Phase 1: Deep Analysis
<exploration-with-optional-subagent-assistance>
<for-project-commands>
- Check project documentation in docs/
- Review CLAUDE.md for project conventions
- Analyze relevant code modules
</for-project-commands>

### Phase 2: Strategic Planning
<planning-with-appropriate-thinking-level>
<consider-subagent-recommendations>
<apply-project-specific-patterns>

### Phase 3: Execution
<action-steps-with-delegation-points>
<follow-project-conventions>
<update-project-docs-if-needed>

### Phase 4: Validation
<verification-including-subagent-review>
<project-specific-validation>

## Self-Optimization Protocol

This command continuously improves through:

1. **Prompt Evolution**
   - Rephrase unclear requirements automatically
   - Rewrite for better AI comprehension
   - Reorganize workflow based on discoveries
   - Refine approach with context
   - Review before execution

2. **Subagent Orchestration**
   - Identify tasks for specialized agents
   - Coordinate multi-agent workflows
   - Aggregate insights from different agents

3. **Adaptive Intelligence**
   - Adjust thinking level based on actual complexity
   - Switch strategies based on intermediate results
   - Learn from execution patterns

## Arguments
- `$1`: <first-argument>
- `$2`: <second-argument>
- `$ARGUMENTS`: Full argument string for complex parsing

## Subagent Delegation Points

<if-subagents-available>
### When to Use @<subagent-name>
- Condition: <when-to-delegate>
- Task: <what-to-delegate>
- Expected Output: <what-to-expect>
</if-subagents-available>

## Examples with Subagent Usage

### Example 1: Simple Command
```
/<command-name> basic-task
# Executes directly without subagent
```

### Example 2: Complex Command with Subagent
```
/<command-name> complex-analysis --agent=analyzer
# Delegates analysis to @analyzer subagent
```

## Error Handling and Recovery
- Fallback if subagent unavailable
- Graceful degradation strategies
- Error context preservation
```

## Phase 5: Implementation Instructions

### For Project-Level Commands (Enhanced)

When `--level=project` or default (project):

1. **Deep Project Understanding**:
   ```bash
   @Task: Analyze entire project context:
   - Read CLAUDE.md for AI instructions
   - Scan docs/ for project memory and decisions
   - Map codebase structure and dependencies
   - Identify testing patterns and quality standards
   - Extract domain-specific terminology
   ```

2. **Intelligent Command Generation**:
   - Incorporate project-specific patterns
   - Reference actual modules and functions
   - Use project's coding conventions
   - Include relevant test commands
   - Update project docs if command affects workflow

3. **Project Memory Integration**:
   ```markdown
   The generated command should:
   - Read docs/STATUS.md to understand current state
   - Check docs/development/ for architectural decisions
   - Follow patterns defined in CLAUDE.md
   - Update docs/ when making significant changes
   ```

### For New Commands

1. **Check for relevant subagents**:
   ```bash
   @Task: List all available subagents and their capabilities
   ```

2. **Generate with subagent awareness**:
   - Include Task tool in allowed-tools if subagents needed
   - Document which subagents the command uses
   - Add delegation instructions

3. **Create companion subagent if beneficial**:
   - For complex commands, create a specialized subagent
   - Place in same level (user/project) as command

### For Existing Commands

1. **Analyze current implementation**:
   ```bash
   @Task: Analyze existing command and identify improvement opportunities
   ```

2. **Enhance with subagent capabilities**:
   - Add Task tool to allowed-tools
   - Identify delegatable portions
   - Update documentation

### Subagent Creation Template

When creating a companion subagent for a command:

```markdown
---
allowed-tools: [<specific-tools-needed>]
description: "Specialized agent for <command-name> operations"
---

You are a specialized agent for <specific-domain>. Your expertise includes:

1. **Core Competencies**
   - <competency-1>
   - <competency-2>

2. **Optimization Focus**
   - <optimization-area-1>
   - <optimization-area-2>

3. **Quality Standards**
   - <standard-1>
   - <standard-2>

When invoked, you should:
1. Deeply analyze the specific request
2. Apply domain best practices
3. Provide actionable recommendations
4. Include validation criteria
```

## Output Format with Subagent Info

After generating/improving a command:

1. **Summary**: Created/improved command with capabilities
2. **Location**: `<path-to-command>`
3. **Thinking Level**: Assigned level and rationale
4. **Subagent Integration**:
   - Subagents used: <list>
   - Subagents created: <list>
   - Delegation strategy: <description>
5. **Usage Examples**: Including subagent variants
6. **Enhancement Opportunities**: Future improvements

## Project Context Leverage Examples

### Example: Creating a Test Command for CCI Project
When creating a test command for the CCI project, the command would:
1. Read `CLAUDE.md` to understand it's a git worktree-first IDE
2. Scan `docs/` to find testing patterns and coverage requirements
3. Analyze `pyproject.toml` to find test scripts
4. Check `src/cci/` structure to understand module organization
5. Generate a command that:
   - Uses `uv run pytest` (project's test runner)
   - Includes coverage requirements from CLAUDE.md
   - Updates `docs/STATUS.md` after test runs
   - Follows the project's quality standards

### Example: Creating a Feature Implementation Command
For implementing new features in the project:
1. Reads `docs/development/CURRENT_SPRINT.md` for active work
2. Checks `docs/PROGRESS.md` for completion tracking patterns
3. Analyzes codebase for similar features
4. Generates command that:
   - Follows TDD approach (from CLAUDE.md)
   - Updates progress tracking
   - Uses project-specific tools (Typer, Textual, etc.)
   - Maintains documentation in `docs/`

## Meta-Command Intelligence

This command demonstrates advanced capabilities:

1. **Multi-Agent Orchestration**: Coordinates multiple specialized agents
2. **Adaptive Optimization**: Adjusts approach based on discoveries
3. **Self-Improvement**: Each execution enhances future performance
4. **Context Awareness**: Recognizes when to leverage external expertise
5. **Project Memory**: Leverages documentation as persistent memory
6. **Codebase Intelligence**: Understands and follows project patterns

## Verification with Subagent Review

Final validation using subagents:

```markdown
@Task: Review the generated command for:
- Correctness of YAML frontmatter
- Appropriate thinking level assignment
- Effective subagent utilization
- Prompt optimization quality
- No conflicts with existing commands
```

## Advanced Features

### Dynamic Subagent Selection
The command can intelligently select which subagents to use based on:
- Task complexity
- Available subagents
- Performance requirements
- User preferences

### Subagent Chaining
For complex commands, orchestrate multiple subagents:
1. @analyzer: Understand requirements
2. @optimizer: Enhance approach
3. @validator: Verify output

### Fallback Strategies
If subagents unavailable:
- Execute with enhanced thinking level
- Use Task tool with general-purpose agent
- Provide manual workflow

## Key Enhancement Summary

This updated version of `update-command` now provides:

1. **Deep Project Context Integration**
   - Reads and understands CLAUDE.md for project-specific instructions
   - Analyzes entire docs/ folder for persistent memory and decisions
   - Maps codebase structure to generate contextually-aware commands
   - Follows project testing patterns and quality standards

2. **Intelligent Command Generation**
   - Commands understand actual project modules and functions
   - Incorporates project-specific tools and dependencies
   - Maintains project documentation automatically
   - Follows established coding conventions

3. **Memory-Aware Operations**
   - Commands read docs/STATUS.md to understand current state
   - Updates docs/development/ with significant changes
   - Maintains progress tracking in docs/PROGRESS.md
   - Preserves architectural decisions in documentation

Remember: Every command generated should be capable of leveraging project context, documentation memory, and subagents for enhanced intelligence and self-improvement.