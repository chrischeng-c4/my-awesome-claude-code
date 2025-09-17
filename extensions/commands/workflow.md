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

### 3.0 Complexity Assessment System

Evaluate workflow complexity to assign appropriate thinking levels:

```bash
# Calculate workflow complexity score (0-10)
calculate_complexity() {
    local name="$1"
    local desc="$2"
    local score=5  # Default medium complexity

    # Adjust score based on keywords in description
    if [[ "$desc" =~ (simple|basic|utility|wrapper|helper|trivial) ]]; then
        score=2
    elif [[ "$desc" =~ (security|architect|critical|infrastructure|system|sensitive) ]]; then
        score=9
    elif [[ "$desc" =~ (analyze|refactor|optimize|complex|multi-step|orchestrate) ]]; then
        score=7
    elif [[ "$desc" =~ (generate|implement|create|build|develop) ]]; then
        score=6
    elif [[ "$desc" =~ (process|transform|convert|parse|extract) ]]; then
        score=4
    fi

    # Adjust for workflow patterns
    if [[ "$desc" =~ (parallel|concurrent|distributed) ]]; then
        ((score++))
    fi
    if [[ "$desc" =~ (validate|verify|audit|review) ]]; then
        ((score++))
    fi

    # Cap at 10
    [ $score -gt 10 ] && score=10

    echo $score
}

# Map complexity score to thinking level
map_score_to_thinking_level() {
    local score=$1

    if [ $score -le 2 ]; then
        echo ""  # No thinking level needed
    elif [ $score -le 4 ]; then
        echo "think"
    elif [ $score -le 6 ]; then
        echo "think hard"
    elif [ $score -le 8 ]; then
        echo "think harder"
    else
        echo "ultrathink"
    fi
}

# Get thinking directive for prompts
get_thinking_directive() {
    local level="$1"

    case "$level" in
        "")           echo "" ;;
        "think")      echo "think about" ;;
        "think hard") echo "think hard about" ;;
        "think harder") echo "think harder about" ;;
        "ultrathink") echo "ultrathink about" ;;
        *)            echo "" ;;
    esac
}

# Get agent-specific thinking level
get_agent_thinking_level() {
    local agent_type="$1"
    local base_complexity=$2

    case "$agent_type" in
        "analyzer")
            # Analyzers need deep thinking
            if [ $base_complexity -le 4 ]; then
                echo "think hard"
            elif [ $base_complexity -le 7 ]; then
                echo "think harder"
            else
                echo "ultrathink"
            fi
            ;;
        "executor")
            # Executors need moderate thinking
            if [ $base_complexity -le 3 ]; then
                echo ""
            elif [ $base_complexity -le 6 ]; then
                echo "think"
            else
                echo "think hard"
            fi
            ;;
        "validator")
            # Validators need careful thinking
            if [ $base_complexity -le 5 ]; then
                echo "think hard"
            else
                echo "think harder"
            fi
            ;;
        "coordinator")
            # Coordinators need complex thinking
            if [ $base_complexity -le 6 ]; then
                echo "think harder"
            else
                echo "ultrathink"
            fi
            ;;
        *)
            map_score_to_thinking_level $base_complexity
            ;;
    esac
}
```

### 3.1 Agent Generation Strategy

Create specialized agents for the workflow with appropriate thinking levels:

```markdown
For workflow "$1", generate agents with intelligent thinking assignment:

# Calculate workflow complexity
COMPLEXITY_SCORE=$(calculate_complexity "$1" "$description")

# Determine agent location based on workflow level
AGENT_DIR = (workflow_level == "user") ? "~/.claude/agents/" : ".claude/agents/"

1. **Analyzer Agent**
   - Name: $1-analyzer
   - Location: $AGENT_DIR
   - Role: Understand $1 requirements
   - Tools: Read, Grep, Glob
   - Thinking: $(get_agent_thinking_level "analyzer" $COMPLEXITY_SCORE)

2. **Executor Agent**
   - Name: $1-executor
   - Location: $AGENT_DIR
   - Role: Perform $1 operations
   - Tools: [workflow-specific]
   - Thinking: $(get_agent_thinking_level "executor" $COMPLEXITY_SCORE)

3. **Validator Agent**
   - Name: $1-validator
   - Location: $AGENT_DIR
   - Role: Ensure $1 quality
   - Tools: Bash, Read
   - Thinking: $(get_agent_thinking_level "validator" $COMPLEXITY_SCORE)

4. **Coordinator Agent** (if complex)
   - Name: $1-coordinator
   - Location: $AGENT_DIR
   - Role: Orchestrate $1 workflow
   - Tools: Task
   - Thinking: $(get_agent_thinking_level "coordinator" $COMPLEXITY_SCORE)

# Agent Generation Template
@Task: Generate each agent with appropriate thinking directive:

AGENT_THINKING=$(get_agent_thinking_level "$AGENT_TYPE" $COMPLEXITY_SCORE)
THINKING_DIRECTIVE=$(get_thinking_directive "$AGENT_THINKING")

cat > $AGENT_DIR/$1-$AGENT_TYPE.md << 'EOF'
---
allowed-tools: [...]
thinking-level: "$AGENT_THINKING"
description: "$AGENT_DESCRIPTION"
---

You are the $1 $AGENT_TYPE agent.

$THINKING_DIRECTIVE performing $AGENT_TYPE operations for the $1 workflow.

[Agent-specific instructions and patterns...]
EOF
```

### 3.2 Command Generation Strategy

Create intuitive entry points with appropriate thinking levels:

```markdown
For workflow "$1", generate commands with intelligent thinking assignment:

# Calculate complexity for commands
COMPLEXITY_SCORE=$(calculate_complexity "$1" "$description")
COMMAND_THINKING=$(map_score_to_thinking_level $COMPLEXITY_SCORE)
THINKING_DIRECTIVE=$(get_thinking_directive "$COMMAND_THINKING")

# Determine command location based on workflow level
CMD_DIR = (workflow_level == "user") ? "~/.claude/commands/" : ".claude/commands/"

1. **Main Entry Command**
   Location: $CMD_DIR/$1.md
   Thinking: $COMMAND_THINKING

   @Task: Generate main command with thinking directive:

   cat > $CMD_DIR/$1.md << 'EOF'
   ---
   allowed-tools: ["Task", "Bash", "Read", "Write"]
   thinking-level: "$COMMAND_THINKING"
   description: "Execute $1 workflow"
   argument-hint: "<parameters>"
   ---

   # /$1

   $THINKING_DIRECTIVE executing the $1 workflow to $description.

   [Command implementation with coordinator agent invocation...]
   EOF

2. **Sub-Commands** (if needed)
   # Analyze command - typically needs deeper thinking
   ANALYZE_THINKING=$([ $COMPLEXITY_SCORE -ge 7 ] && echo "think harder" || echo "think hard")
   ANALYZE_DIRECTIVE=$(get_thinking_directive "$ANALYZE_THINKING")

   Location: $CMD_DIR/$1-analyze.md
   cat > $CMD_DIR/$1-analyze.md << 'EOF'
   ---
   thinking-level: "$ANALYZE_THINKING"
   ---

   # /$1-analyze

   $ANALYZE_DIRECTIVE analyzing requirements for $1.
   EOF

   # Validate command - needs careful thinking
   VALIDATE_THINKING=$([ $COMPLEXITY_SCORE -ge 6 ] && echo "think hard" || echo "think")
   VALIDATE_DIRECTIVE=$(get_thinking_directive "$VALIDATE_THINKING")

   Location: $CMD_DIR/$1-validate.md
   cat > $CMD_DIR/$1-validate.md << 'EOF'
   ---
   thinking-level: "$VALIDATE_THINKING"
   ---

   # /$1-validate

   $VALIDATE_DIRECTIVE validating $1 results for quality and correctness.
   EOF

3. **Helper Commands**
   # Status command - simple, no deep thinking needed
   Location: $CMD_DIR/$1-status.md
   cat > $CMD_DIR/$1-status.md << 'EOF'
   ---
   thinking-level: ""
   ---

   # /$1-status

   Check the current status of the $1 workflow.
   EOF

   # Rollback command - needs careful thinking
   ROLLBACK_THINKING=$([ $COMPLEXITY_SCORE -ge 7 ] && echo "think harder" || echo "think hard")
   ROLLBACK_DIRECTIVE=$(get_thinking_directive "$ROLLBACK_THINKING")

   Location: $CMD_DIR/$1-rollback.md
   cat > $CMD_DIR/$1-rollback.md << 'EOF'
   ---
   thinking-level: "$ROLLBACK_THINKING"
   ---

   # /$1-rollback

   $ROLLBACK_DIRECTIVE safely rolling back $1 changes while preserving system integrity.
   EOF
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
# Complexity: 6/10 (keywords: scaffold, setup)
# Base thinking: "think hard"

Creates (in ~/.claude/):
- Agents:
  - scaffold-analyzer [thinking: "think harder"]
  - project-builder [thinking: "think hard"]
  - environment-setup [thinking: "think hard"]
- Commands:
  - /project-init [thinking: "think hard"]
  - /project-validate [thinking: "think hard"]
- Docs: None (user-level docs not accessible)
```

### Project-Level Template: Code Review

```bash
/workflow code-review "Automated code review with quality gates" --project
# Auto-detected as project-level due to "review" keyword
# Complexity: 8/10 (keywords: review, quality + validation pattern)
# Base thinking: "think harder"

Creates (in .claude/):
- Agents:
  - code-analyzer [thinking: "ultrathink"]
  - style-checker [thinking: "think hard"]
  - security-scanner [thinking: "ultrathink"]
- Commands:
  - /review [thinking: "think harder"]
  - /review-pr [thinking: "think harder"]
  - /review-commit [thinking: "think harder"]
- Docs: docs/workflows/code-review.md
```

### Template 2: Feature Development Workflow

```bash
/workflow feature-dev "TDD-based feature development"
# Complexity: 6/10 (keywords: development)
# Base thinking: "think hard"

Creates:
- Agents:
  - requirement-analyzer [thinking: "think harder"]
  - test-writer [thinking: "think"]
  - implementer [thinking: "think hard"]
- Commands:
  - /feature [thinking: "think hard"]
  - /feature-test [thinking: "think"]
  - /feature-implement [thinking: "think hard"]
- Docs: docs/workflows/feature-dev.md
```

### Template 3: Refactoring Workflow

```bash
/workflow refactor "Safe refactoring with validation"
# Complexity: 8/10 (keywords: refactor + validation)
# Base thinking: "think harder"

Creates:
- Agents:
  - code-analyzer [thinking: "ultrathink"]
  - refactorer [thinking: "think hard"]
  - test-runner [thinking: "think hard"]
- Commands:
  - /refactor [thinking: "think harder"]
  - /refactor-preview [thinking: "think harder"]
  - /refactor-validate [thinking: "think hard"]
- Docs: docs/workflows/refactor.md
```

### Template 4: Documentation Workflow

```bash
/workflow docs "Intelligent documentation management"
# Complexity: 5/10 (default medium complexity)
# Base thinking: "think hard"

Creates:
- Agents:
  - doc-analyzer [thinking: "think harder"]
  - doc-writer [thinking: "think"]
  - doc-optimizer [thinking: "think"]
- Commands:
  - /docs-update [thinking: "think hard"]
  - /docs-optimize [thinking: "think"]
  - /docs-validate [thinking: "think"]
- Docs: docs/workflows/documentation.md
```

### Template 5: Security Audit Workflow

```bash
/workflow security-audit "Comprehensive security vulnerability scanning"
# Complexity: 10/10 (keywords: security, critical)
# Base thinking: "ultrathink"

Creates:
- Agents:
  - vulnerability-scanner [thinking: "ultrathink"]
  - threat-analyzer [thinking: "ultrathink"]
  - security-reporter [thinking: "think harder"]
- Commands:
  - /security-audit [thinking: "ultrathink"]
  - /security-scan [thinking: "ultrathink"]
  - /security-report [thinking: "think harder"]
- Docs: docs/workflows/security-audit.md
```

### Template 6: Simple Utility Workflow

```bash
/workflow file-rename "Simple batch file renaming utility"
# Complexity: 2/10 (keywords: simple, utility)
# Base thinking: none

Creates:
- Agents:
  - file-scanner [thinking: none]
  - rename-executor [thinking: none]
- Commands:
  - /file-rename [thinking: none]
  - /file-rename-preview [thinking: none]
- Docs: docs/workflows/file-rename.md
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
**Complexity Score**: $COMPLEXITY_SCORE/10
**Base Thinking Level**: $COMMAND_THINKING

### Documentation Updates (if project-level)
- README.md: Reorganized, $token-reduction% smaller
- CLAUDE.md: Optimized to $token-count tokens
- docs/: Restructured with $new-structure
- Note: Documentation skipped for user-level workflows

### Infrastructure Created

#### Agents (4) with Thinking Levels
- @$1-analyzer: Requirements analysis [thinking: $ANALYZER_THINKING]
- @$1-executor: Core execution [thinking: $EXECUTOR_THINKING]
- @$1-validator: Quality assurance [thinking: $VALIDATOR_THINKING]
- @$1-coordinator: Orchestration [thinking: $COORDINATOR_THINKING]

#### Commands (5) with Thinking Levels
- /$1: Main workflow entry [thinking: $COMMAND_THINKING]
- /$1-analyze: Deep analysis [thinking: $ANALYZE_THINKING]
- /$1-validate: Result validation [thinking: $VALIDATE_THINKING]
- /$1-status: Check progress [thinking: none]
- /$1-rollback: Undo changes [thinking: $ROLLBACK_THINKING]

### Thinking Level Assignment Rationale
Based on complexity score of $COMPLEXITY_SCORE:
- Detected keywords: [$DETECTED_KEYWORDS]
- Workflow pattern: [$PATTERN_TYPE]
- Agents assigned thinking levels based on their roles
- Commands assigned thinking based on operation complexity

### Usage Examples

\`\`\`bash
# Execute workflow (will $THINKING_DIRECTIVE the task)
/$1 "parameter"

# Deep analysis (will $ANALYZE_DIRECTIVE requirements)
/$1-analyze

# Check status (simple operation, no deep thinking)
/$1-status

# Rollback if needed (will $ROLLBACK_DIRECTIVE the rollback)
/$1-rollback
\`\`\`

### Performance Metrics
- Setup Time: $time
- Token Optimization: $before → $after tokens
- Workflow Complexity: $complexity-score
- Thinking Budget: [$TOTAL_THINKING_OPERATIONS operations with extended thinking]

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