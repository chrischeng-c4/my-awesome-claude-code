---
allowed-tools: ["Read", "Write", "Edit", "MultiEdit", "Grep", "Glob", "Bash", "WebFetch", "Task", "TodoWrite"]
model: "claude-opus-4-1-20250805"
description: "Orchestrate complete development workflows with intelligent documentation, command generation, and agent creation"
argument-hint: "<workflow-name> <description> [--user|--project] [--docs-first] [--token-optimize]"
thinking-level: "ultrathink"
---

# /workflow

ultrathink about creating comprehensive development workflows that combine documentation intelligence, command orchestration, and agent specialization into a unified system.

**Workflow Intelligence**: This command creates complete development ecosystems by:
- Understanding complex requirements and mapping to capabilities
- Reorganizing documentation for optimal AI comprehension
- Creating specialized agents for workflow tasks
- Generating intuitive commands as entry points
- Maintaining project memory and decision history
- Ensuring token-efficient documentation structure

## Workflow Analysis Phase

Parse the workflow request:
- Workflow name: `$1`
- Description/Requirements: `$2 $3 $4 $5 $6 $7 $8 $9`
- Options:
  - `--user`: Force user-level workflow (in ~/.claude/)
  - `--project`: Force project-level workflow (in .claude/)
  - `--docs-first`: Prioritize documentation update before implementation (project-level only)
  - `--token-optimize`: Aggressively optimize CLAUDE.md for token efficiency (project-level only)

## Phase 0: Workflow Level Detection

### Auto-Detection Logic

```markdown
@Task: Determine if workflow should be user-level or project-level:

1. **Check Explicit Flags**
   - If --user flag: Force user-level
   - If --project flag: Force project-level
   - Otherwise: Continue to auto-detection

2. **Analyze Workflow Intent**
   User-Level Indicators:
   - Keywords: "init", "scaffold", "create", "setup", "bootstrap", "template"
   - Purpose: Creating new projects, cross-project utilities
   - Scope: Generic, reusable across projects

   Project-Level Indicators:
   - Keywords: "implement", "feature", "refactor", "fix", "test", "deploy"
   - Purpose: Modifying existing code, project-specific features
   - Scope: Specific to current project

3. **Default Decision**
   - If unclear: Default to project-level
   - Provide clear feedback on detection result
```

### Detection Feedback

```markdown
## 🎯 Workflow Level Detection Result

**Detected Level**: [User-Level | Project-Level]
**Reasoning**: Based on [keywords/purpose/scope]
**Location**: [~/.claude/ | .claude/]
**Documentation**: [Will be updated | Skipped for user-level]
```

## Phase 1: Deep Understanding and Planning

### Requirements Analysis

```markdown
@Task: Deeply analyze the workflow requirements:
1. **Intent Extraction**: What does the user really want to achieve?
2. **Capability Mapping**: What agents and commands are needed?
3. **Workflow Pattern**: Sequential, parallel, or hybrid execution?
4. **Integration Points**: How does this fit with existing workflows?
5. **Documentation Needs**: What knowledge must be captured? (project-level only)
6. **Quality Criteria**: How do we measure success?
```

### Existing Ecosystem Analysis

```bash
# Discover current infrastructure
@Task: Map existing ecosystem:
1. List all user-level commands in ~/.claude/commands/
2. List all project-level commands in .claude/commands/
3. List all user-level agents in ~/.claude/agents/
4. List all project-level agents in .claude/agents/
5. Analyze current documentation structure
6. Identify gaps and overlaps
```

### Workflow Architecture Design

```markdown
@Task: Design the workflow architecture:
1. **Entry Points**: User-facing commands
2. **Execution Layer**: Specialized agents
3. **Orchestration**: Coordination patterns
4. **Data Flow**: Information passing between components
5. **Error Handling**: Recovery strategies
6. **Feedback Loops**: Progress and status updates
```

## Phase 2: Intelligent Documentation Reorganization (Project-Level Only)

**⚠️ Note**: This phase is skipped for user-level workflows since user-level documentation is not accessible to Claude during project work.

### Documentation Strategy

For project-level workflows, documentation is the persistent memory and instruction set for AI. Optimize it intelligently:

#### 2.1 README.md Optimization (Human-Focused)

```markdown
Structure for humans:
1. **Quick Start**: Immediate value
2. **Core Concepts**: Essential understanding
3. **Usage Examples**: Common scenarios
4. **API Reference**: Complete details
5. **Troubleshooting**: Problem solving
```

#### 2.2 CLAUDE.md Optimization (AI-Focused)

```markdown
Token-efficient structure for AI:

# CLAUDE.md Structure

## 🎯 Critical Instructions (High Priority)
- Must-follow rules
- Security constraints
- Quality standards

## 🧠 Context & Memory
- Project state: → docs/STATUS.md
- Current work: → docs/development/CURRENT_SPRINT.md
- Decisions: → docs/development/DECISIONS.md

## 🔧 Technical Patterns
- Code conventions: Brief, essential only
- Testing approach: Link to docs/TESTING.md
- Architecture: Link to docs/ARCHITECTURE.md

## 📚 Knowledge References
Instead of embedding, reference:
- Detailed guides → docs/guides/
- API specs → docs/api/
- Examples → docs/examples/

This keeps CLAUDE.md concise while maintaining full access to knowledge.
```

#### 2.3 Docs Folder Reorganization

```markdown
Optimal docs/ structure:
docs/
├── STATUS.md                 # Current state (AI memory)
├── PROGRESS.md               # Feature tracking
├── ISSUES.md                 # Known problems
├── architecture/
│   ├── overview.md          # System design
│   ├── patterns.md          # Design patterns
│   └── decisions/           # ADRs
├── workflows/
│   ├── <workflow-1>.md      # Workflow documentation
│   └── <workflow-2>.md
├── guides/
│   ├── development.md       # Dev guide
│   ├── testing.md          # Test guide
│   └── deployment.md       # Deploy guide
├── api/
│   └── reference.md        # API documentation
└── development/
    ├── CURRENT_SPRINT.md   # Active work
    ├── TODO.md             # Backlog
    └── FEATURE_LOG.md      # Completed features
```

### Documentation Update Process

```bash
@Task: Reorganize documentation intelligently (if project-level):
if [[ $WORKFLOW_LEVEL == "project" ]]; then
    1. Analyze current documentation structure
    2. Identify redundancies and gaps
    3. Calculate token usage for each document
    4. Split documents exceeding optimal size (2000 tokens)
    5. Create cross-references instead of duplication
    6. Update navigation and indexes
    7. Validate all links and references
else
    echo "Skipping documentation updates for user-level workflow"
fi
```

### Token Optimization Strategies

```markdown
Strategies for token efficiency:
1. **Compression**: Use concise language, avoid redundancy
2. **Referencing**: Link instead of embed
3. **Structuring**: Hierarchical organization
4. **Splitting**: Break large docs into focused pieces
5. **Indexing**: Create navigation maps
6. **Prioritizing**: Most important info first
```

## Phase 3: Workflow Implementation

### 3.1 Agent Generation Strategy

Create specialized agents for the workflow:

```markdown
For workflow "$1", generate agents:

# Determine agent location based on workflow level
AGENT_DIR = (workflow_level == "user") ? "~/.claude/agents/" : ".claude/agents/"

1. **Analyzer Agent**
   - Name: $1-analyzer
   - Location: $AGENT_DIR
   - Role: Understand $1 requirements
   - Tools: Read, Grep, Glob

2. **Executor Agent**
   - Name: $1-executor
   - Location: $AGENT_DIR
   - Role: Perform $1 operations
   - Tools: [workflow-specific]

3. **Validator Agent**
   - Name: $1-validator
   - Location: $AGENT_DIR
   - Role: Ensure $1 quality
   - Tools: Bash, Read

4. **Coordinator Agent** (if complex)
   - Name: $1-coordinator
   - Location: $AGENT_DIR
   - Role: Orchestrate $1 workflow
   - Tools: Task
```

### 3.2 Command Generation Strategy

Create intuitive entry points:

```markdown
For workflow "$1", generate commands:

# Determine command location based on workflow level
CMD_DIR = (workflow_level == "user") ? "~/.claude/commands/" : ".claude/commands/"

1. **Main Entry Command**
   Location: $CMD_DIR/$1.md
   /update-command $1 "Execute $1 workflow" --agent=$1-coordinator

2. **Sub-Commands** (if needed)
   Location: $CMD_DIR/$1-analyze.md
   /update-command $1-analyze "Analyze for $1" --agent=$1-analyzer

   Location: $CMD_DIR/$1-validate.md
   /update-command $1-validate "Validate $1 results" --agent=$1-validator

3. **Helper Commands**
   Location: $CMD_DIR/$1-status.md
   /update-command $1-status "Check $1 workflow status"

   Location: $CMD_DIR/$1-rollback.md
   /update-command $1-rollback "Rollback $1 changes"
```

### 3.3 Orchestration Pattern Implementation

```markdown
Workflow Execution Pattern for "$1":

1. **Sequential Pattern**
   Command → Agent1 → Agent2 → Agent3 → Result

2. **Parallel Pattern**
   Command → [Agent1, Agent2, Agent3] → Aggregator → Result

3. **Conditional Pattern**
   Command → Analyzer → Decision → AgentA or AgentB → Result

4. **Iterative Pattern**
   Command → Agent → Validator → (retry if needed) → Result
```

## Phase 4: Workflow Documentation

### Auto-Generated Workflow Documentation

Create comprehensive workflow documentation:

```markdown
# docs/workflows/$1.md

## $1 Workflow

### Overview
$description

### Architecture
- Entry Point: /$1 command
- Orchestrator: @$1-coordinator
- Specialists: @$1-analyzer, @$1-executor, @$1-validator

### Usage
\`\`\`bash
# Basic usage
/$1 <parameters>

# Advanced usage
/$1 <parameters> --verbose --parallel
\`\`\`

### Workflow Diagram
\`\`\`
User → /$1 → Coordinator
         ↓
    [Analyzer] → [Executor] → [Validator]
         ↓
      Result
\`\`\`

### Configuration
- Performance: Optimized for $characteristics
- Error Handling: $error-strategy
- Logging: $logging-approach

### Integration Points
- Upstream: $upstream-workflows
- Downstream: $downstream-workflows
- Dependencies: $required-resources
```

## Phase 5: Implementation Orchestration

### Execution Order

1. **Documentation First** (if --docs-first and project-level):
   ```bash
   @Task: Reorganize all documentation (project-level only):
   if [[ $WORKFLOW_LEVEL == "project" ]] && [[ $DOCS_FIRST == "true" ]]; then
       - Optimize README.md for humans
       - Compress CLAUDE.md for AI efficiency
       - Restructure docs/ folder
       - Create workflow documentation
   fi
   ```

2. **Infrastructure Creation**:
   ```bash
   # Create agents in parallel
   @Task: Create $1-analyzer agent
   @Task: Create $1-executor agent
   @Task: Create $1-validator agent
   @Task: Create $1-coordinator agent

   # Create commands
   @Task: Create /$1 main command
   @Task: Create helper commands
   ```

3. **Integration Testing**:
   ```bash
   @Task: Test workflow end-to-end:
   - Verify agent communication
   - Test error handling
   - Validate documentation links
   - Measure performance
   ```

## Workflow Templates

### User-Level Template: Project Initialization

```bash
/workflow project-init "Scaffold new projects with complete setup" --user
# Auto-detected as user-level due to "init" and "scaffold" keywords

Creates (in ~/.claude/):
- Agents: scaffold-analyzer, project-builder, environment-setup
- Commands: /project-init, /project-validate
- Docs: None (user-level docs not accessible)
```

### Project-Level Template: Code Review

```bash
/workflow code-review "Automated code review with quality gates" --project
# Auto-detected as project-level due to "review" keyword

Creates (in .claude/):
- Agents: code-analyzer, style-checker, security-scanner
- Commands: /review, /review-pr, /review-commit
- Docs: docs/workflows/code-review.md
```

### Template 2: Feature Development Workflow

```bash
/workflow feature-dev "TDD-based feature development"

Creates:
- Agents: requirement-analyzer, test-writer, implementer
- Commands: /feature, /feature-test, /feature-implement
- Docs: docs/workflows/feature-dev.md
```

### Template 3: Refactoring Workflow

```bash
/workflow refactor "Safe refactoring with validation"

Creates:
- Agents: code-analyzer, refactorer, test-runner
- Commands: /refactor, /refactor-preview, /refactor-validate
- Docs: docs/workflows/refactor.md
```

### Template 4: Documentation Workflow

```bash
/workflow docs "Intelligent documentation management"

Creates:
- Agents: doc-analyzer, doc-writer, doc-optimizer
- Commands: /docs-update, /docs-optimize, /docs-validate
- Docs: docs/workflows/documentation.md
```

## Self-Improvement Mechanisms

### Workflow Evolution

```markdown
Each workflow execution:
1. Tracks performance metrics
2. Identifies bottlenecks
3. Suggests optimizations
4. Updates agent prompts
5. Refines command logic
6. Improves documentation
```

### Learning Integration

```markdown
@Task: After each workflow execution:
1. Log execution patterns to docs/development/WORKFLOW_LOG.md
2. Update docs/development/DECISIONS.md with learnings
3. Enhance agent system prompts based on experience
4. Optimize command parameters
5. Update workflow documentation
```

## Advanced Features

### Multi-Workflow Composition

```bash
# Combine workflows
/workflow ci-cd "Complete CI/CD pipeline" --compose="test,build,deploy"
```

### Cross-Project Workflows

```bash
# Create reusable workflow
/workflow standard-setup "Company standard project setup" --level=user
```

### Workflow Versioning

```bash
# Version control workflows
/workflow migrate-v2 "Database migration v2" --version=2.0
```

### Conditional Workflows

```bash
# Create conditional execution
/workflow smart-deploy "Deploy based on conditions" --if="tests-pass"
```

## Documentation Token Optimization Examples

### Before Optimization (CLAUDE.md - 5000 tokens)
```markdown
## Testing
We use pytest for testing. All tests should be in the tests/ folder...
[500 tokens of testing details]

## Architecture
The system uses a three-tier architecture...
[1000 tokens of architecture details]
```

### After Optimization (CLAUDE.md - 500 tokens)
```markdown
## Testing
- Framework: pytest
- Location: tests/
- Details: → docs/guides/testing.md

## Architecture
- Pattern: Three-tier
- Details: → docs/architecture/overview.md
```

## Quality Assurance

### Workflow Validation Checklist

```markdown
@Task: Validate the workflow:
□ All agents created successfully
□ All commands functioning
□ Documentation updated and linked
□ Token usage optimized (<1000 for CLAUDE.md)
□ Error handling implemented
□ Performance acceptable
□ Integration points tested
```

### Documentation Quality Metrics

```markdown
Measure documentation quality:
- Clarity Score: Readability index
- Completeness: Coverage of all features
- Token Efficiency: Tokens per concept
- Navigation: Link validity and structure
- Freshness: Last update timestamps
```

## Output Format

After creating a workflow:

```markdown
## Workflow Creation Summary

**Workflow**: $1
**Level**: [User-Level | Project-Level]
**Location**: [~/.claude/ | .claude/]
**Description**: $description

### Documentation Updates (if project-level)
- README.md: Reorganized, $token-reduction% smaller
- CLAUDE.md: Optimized to $token-count tokens
- docs/: Restructured with $new-structure
- Note: Documentation skipped for user-level workflows

### Infrastructure Created

#### Agents (4)
- @$1-analyzer: Requirements analysis
- @$1-executor: Core execution
- @$1-validator: Quality assurance
- @$1-coordinator: Orchestration

#### Commands (3)
- /$1: Main workflow entry
- /$1-status: Check progress
- /$1-rollback: Undo changes

### Usage Examples

\`\`\`bash
# Execute workflow
/$1 "parameter"

# Check status
/$1-status

# Rollback if needed
/$1-rollback
\`\`\`

### Performance Metrics
- Setup Time: $time
- Token Optimization: $before → $after tokens
- Workflow Complexity: $complexity-score

### Next Steps
1. Test the workflow with: /$1 test
2. View documentation: docs/workflows/$1.md
3. Monitor performance: /$1-status --metrics
```

## Meta-Workflow Intelligence

This command demonstrates ultimate workflow orchestration:

1. **Holistic Understanding**: Comprehends entire development lifecycle
2. **Documentation Intelligence**: Optimizes for both human and AI consumption
3. **Infrastructure Automation**: Creates complete agent/command ecosystems
4. **Token Efficiency**: Maintains optimal documentation size
5. **Self-Organization**: Continuously improves based on usage
6. **Knowledge Persistence**: Maintains project memory across sessions

## Error Recovery

### Rollback Capability

```bash
# If workflow creation fails
@Task: Implement rollback:
1. Remove created agents
2. Remove created commands
3. Restore documentation to previous state
4. Log failure reasons
5. Suggest fixes
```

### Partial Success Handling

```markdown
Handle partial completions:
- Document what succeeded
- Identify what failed
- Provide recovery commands
- Maintain system consistency
```

## Best Practices

### Workflow Design Principles

1. **Start with the End**: Define success criteria first
2. **Minimize Steps**: Optimal path to result
3. **Maximize Reuse**: Leverage existing agents/commands
4. **Document Everything**: Capture all decisions
5. **Measure Always**: Track performance metrics

### Documentation Principles

1. **Humans First**: README for human understanding
2. **AI Optimized**: CLAUDE.md for AI efficiency
3. **Knowledge Distributed**: Spread across focused files
4. **Links Over Duplication**: Reference instead of repeat
5. **Version Everything**: Track all changes

## Conclusion

The /workflow command creates complete development ecosystems by:
- Understanding complex requirements deeply
- Reorganizing documentation intelligently
- Creating specialized agent networks
- Generating intuitive command interfaces
- Maintaining optimal token efficiency
- Enabling continuous improvement

This creates a perfect balance: simple for humans, sophisticated for AI, excellent in execution.