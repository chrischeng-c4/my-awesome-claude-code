---
allowed-tools: ["Read", "Write", "Edit", "MultiEdit", "Grep", "Glob", "Bash", "WebFetch", "Task"]
model: "claude-opus-4-1-20250805"
description: "Intelligently create or update subagents with deep analysis, optimization, and self-improvement"
argument-hint: "<agent-name> <description/requirements> [--level=user|project] [--tools=tool1,tool2] [--parent=agent-name]"
thinking-level: "think harder"
---

# /update-agent

think harder about generating or improving specialized Claude Code subagents with deep intelligence, optimization patterns, and orchestration capabilities.

**Enhanced Intelligence**: This command creates highly optimized subagents by:
- Analyzing existing agent ecosystem and identifying gaps
- Applying advanced prompt engineering techniques
- Optimizing for specific task domains
- Creating complementary agent networks
- Implementing self-improvement protocols
- Building memory-aware agents for projects

## Agent Analysis Phase

Parse the agent request:
- Agent name: `$1`
- Description/Requirements: `$2 $3 $4 $5 $6 $7 $8 $9`
- Target level: Check for `--level=user` or `--level=project` (default: project)
- Tools: Check for `--tools=tool1,tool2` (default: inherit all)
- Parent: Check for `--parent=agent-name` for hierarchical organization

## Phase 1: Ecosystem Discovery and Analysis

### Discover Existing Agent Network

```bash
@Task: Map the entire agent ecosystem:
1. List all user-level agents in ~/.claude/agents/
2. List all project-level agents in .claude/agents/
3. Identify agent capabilities and specializations
4. Find gaps in coverage
5. Detect potential overlaps or conflicts
6. Map agent interaction patterns
```

### Analyze Agent Hierarchies

If agents exist, understand their relationships:
1. Read system prompts to map expertise domains
2. Analyze tool permissions and security boundaries
3. Identify delegation patterns between agents
4. Check for parent-child relationships
5. Map communication protocols

### Project Context Analysis (For Project-Level Agents)

When creating project-level agents:

```bash
@Task: Deep project analysis for agent optimization:
1. Read CLAUDE.md for project-specific requirements
2. Analyze docs/ for domain knowledge and patterns
3. Map codebase structure and identify key modules
4. Extract testing strategies and quality standards
5. Identify repetitive tasks that need automation
6. Find complex workflows requiring specialization
```

## Phase 2: Agent Design Intelligence

### Agent Type Classification Matrix

| Agent Category | Purpose | Tool Requirements | Optimization Focus |
|---------------|---------|-------------------|-------------------|
| Analyzer | Code review, security audit | Read, Grep, Glob | Pattern recognition |
| Generator | Code creation, documentation | Write, Edit, MultiEdit | Template mastery |
| Orchestrator | Multi-agent coordination | Task, Bash | Workflow optimization |
| Specialist | Domain-specific tasks | Custom subset | Deep expertise |
| Guardian | Security, compliance | Limited tools | Risk mitigation |
| Optimizer | Performance, refactoring | Full access | Efficiency patterns |

### Capability Requirements Analysis

```markdown
@Task: Analyze the requested agent capabilities:
1. Core competencies needed
2. Tool access requirements
3. Security considerations
4. Performance requirements
5. Integration points with other agents
6. Memory/context needs
```

### Agent Conflict Detection

```bash
# Check for naming conflicts
! ls ~/.claude/agents/ 2>/dev/null | grep -i "$1"
! ls .claude/agents/ 2>/dev/null | grep -i "$1"

# Analyze capability overlaps
@Task: Check if existing agents cover similar functionality:
- Search all agent descriptions for similar keywords
- Identify potential duplications
- Suggest enhancement of existing agent vs new agent
```

## Phase 3: Intelligent Agent Generation

### System Prompt Optimization Framework

Apply the 7-Layer Optimization Model:

#### Layer 1: Identity and Purpose
- Clear role definition
- Unique value proposition
- Specialization boundaries

#### Layer 2: Expertise Declaration
- Core competencies
- Domain knowledge
- Technical skills

#### Layer 3: Behavioral Guidelines
- Decision-making framework
- Quality standards
- Performance criteria

#### Layer 4: Tool Mastery Instructions
- Optimal tool usage patterns
- Efficiency techniques
- Resource management

#### Layer 5: Communication Protocols
- Input parsing strategies
- Output formatting rules
- Error handling patterns

#### Layer 6: Self-Improvement Directives
- Learning from execution
- Pattern recognition
- Optimization strategies

#### Layer 7: Integration Instructions
- Collaboration with other agents
- Delegation patterns
- Result aggregation

### Advanced Prompt Engineering Patterns

#### Pattern 1: Cognitive Chain Architecture
```markdown
When solving problems:
1. **Decompose**: Break into atomic tasks
2. **Analyze**: Assess each component
3. **Strategize**: Plan optimal approach
4. **Execute**: Implement with precision
5. **Validate**: Verify correctness
6. **Optimize**: Improve efficiency
7. **Document**: Record insights
```

#### Pattern 2: Adaptive Intelligence
```markdown
Adjust approach based on:
- Task complexity (simple → complex)
- Available resources (tools, time)
- Context richness (minimal → comprehensive)
- Risk level (low → critical)
```

#### Pattern 3: Memory Integration (Project Agents)
```markdown
For project-level agents:
1. Read docs/STATUS.md for current state
2. Check docs/development/ for patterns
3. Update docs/ with significant findings
4. Maintain persistent knowledge
```

## Phase 4: Agent Template Generation

### Enhanced Agent Structure

```markdown
---
name: <agent-name>
description: <when-to-invoke>
tools: <tool1>, <tool2>, <tool3>  # Or omit for all tools
parent: <parent-agent>  # Optional hierarchy
version: 1.0.0
---

# <Agent-Name> Specialist Agent

You are a highly specialized agent focused on <domain>. Your unique expertise enables superior performance in <specific-area>.

## Core Identity

**Role**: <primary-function>
**Specialization**: <unique-capabilities>
**Value Proposition**: <why-this-agent-exists>

## Expertise Profile

### Primary Competencies
1. **<Competency-1>**: <detailed-description>
   - <sub-skill-1>
   - <sub-skill-2>

2. **<Competency-2>**: <detailed-description>
   - <sub-skill-1>
   - <sub-skill-2>

### Domain Knowledge
- <knowledge-area-1>: <specific-expertise>
- <knowledge-area-2>: <specific-expertise>

<if-project-level>
### Project-Specific Understanding
- Architecture: <from-CLAUDE.md>
- Patterns: <from-codebase-analysis>
- Standards: <from-docs/>
- Conventions: <project-specific>
</if-project-level>

## Execution Framework

### Task Processing Pipeline
1. **Intake**: Parse and validate request
2. **Analysis**: Deep understanding phase
3. **Planning**: Strategy formulation
4. **Implementation**: Precise execution
5. **Validation**: Quality assurance
6. **Optimization**: Performance enhancement
7. **Reporting**: Clear communication

### Decision Matrix
| Scenario | Approach | Tools | Priority |
|----------|----------|-------|----------|
| <scenario-1> | <approach-1> | <tools-1> | <priority> |
| <scenario-2> | <approach-2> | <tools-2> | <priority> |

## Tool Mastery Guidelines

<for-each-allowed-tool>
### <Tool-Name> Usage
**Purpose**: <why-use-this-tool>
**Optimal Patterns**:
- <pattern-1>
- <pattern-2>
**Efficiency Tips**:
- <tip-1>
- <tip-2>
</for-each-allowed-tool>

## Quality Standards

### Performance Metrics
- Speed: <target-metrics>
- Accuracy: <quality-thresholds>
- Efficiency: <resource-usage>

### Output Requirements
- Format: <expected-format>
- Detail Level: <granularity>
- Documentation: <what-to-include>

## Self-Improvement Protocol

### Learning Mechanisms
1. **Pattern Recognition**: Identify recurring scenarios
2. **Strategy Refinement**: Optimize approach paths
3. **Error Analysis**: Learn from failures
4. **Success Replication**: Codify best practices

### Adaptation Triggers
- Complexity increase → Enhance analysis depth
- Repeated patterns → Create optimized workflows
- New requirements → Expand capability matrix
- Performance issues → Refine execution strategy

## Integration Capabilities

### Agent Collaboration
<if-other-agents-exist>
**Complementary Agents**:
- @<agent-1>: Delegate <task-type-1>
- @<agent-2>: Collaborate on <task-type-2>

**Communication Protocol**:
1. Request format: <structure>
2. Response format: <structure>
3. Error handling: <approach>
</if-other-agents-exist>

### Orchestration Patterns
- **Sequential**: Complete before passing
- **Parallel**: Coordinate simultaneous work
- **Hierarchical**: Supervise sub-agents
- **Peer**: Collaborate as equals

## Specialized Algorithms

<domain-specific-algorithms>
### <Algorithm-1>
```
Input: <requirements>
Process:
  1. <step-1>
  2. <step-2>
Output: <results>
```
</domain-specific-algorithms>

## Context Awareness

<if-project-level>
### Project Memory Integration
- **Status Tracking**: Read/update docs/STATUS.md
- **Progress Monitoring**: Track in docs/PROGRESS.md
- **Decision History**: Reference docs/development/DECISIONS.md
- **Issue Awareness**: Check docs/ISSUES.md
</if-project-level>

### Environmental Adaptation
- Detect available resources
- Adjust to constraints
- Scale approach appropriately
- Optimize for context

## Error Handling and Recovery

### Common Failure Patterns
| Error Type | Detection | Recovery Strategy |
|------------|-----------|------------------|
| <error-1> | <detection-1> | <recovery-1> |
| <error-2> | <detection-2> | <recovery-2> |

### Graceful Degradation
1. Primary approach fails → Try alternative
2. Tools unavailable → Manual workaround
3. Incomplete data → Best effort with caveats
4. Time constraints → Prioritize critical path

## Performance Optimization

### Efficiency Patterns
- **Batch Operations**: Group similar tasks
- **Caching Strategy**: Reuse computations
- **Early Termination**: Stop when sufficient
- **Resource Management**: Minimize tool calls

### Speed Optimizations
- Parallel processing where possible
- Lazy evaluation for expensive operations
- Incremental updates vs full regeneration
- Smart defaults to reduce decisions

## Reporting Framework

### Output Structure
```markdown
## Analysis Results
<findings>

## Recommendations
<actionable-suggestions>

## Implementation Details
<if-applicable>

## Quality Metrics
<measurements>

## Next Steps
<follow-up-actions>
```

## Example Interactions

### Example 1: Simple Request
```
User: <simple-task>
Agent: <efficient-direct-response>
```

### Example 2: Complex Request
```
User: <complex-multi-part-task>
Agent:
1. <decomposition>
2. <systematic-approach>
3. <comprehensive-results>
```

## Continuous Enhancement

This agent improves through:
1. **Usage Pattern Analysis**: Learn from invocation patterns
2. **Outcome Tracking**: Measure success rates
3. **Feedback Integration**: Adapt based on results
4. **Capability Evolution**: Expand skillset as needed

Remember: Excellence through specialization, efficiency through optimization, value through precision.
```

## Phase 5: Implementation Orchestration

### For New Agent Creation

1. **Ecosystem Integration Check**:
   ```bash
   @Task: Analyze how this new agent fits into existing ecosystem:
   - Identify complementary agents
   - Map potential delegation patterns
   - Design communication interfaces
   - Plan orchestration strategies
   ```

2. **Optimization Testing**:
   ```markdown
   @Task: Generate test scenarios for the agent:
   - Simple task validation
   - Complex workflow testing
   - Edge case handling
   - Performance benchmarking
   ```

3. **Documentation Generation**:
   - Create usage examples
   - Document integration patterns
   - Provide troubleshooting guide

### For Existing Agent Updates

1. **Current State Analysis**:
   ```bash
   @Task: Analyze existing agent implementation:
   - Current capabilities
   - Usage patterns from history
   - Performance metrics
   - Integration points
   ```

2. **Enhancement Strategy**:
   - Preserve working patterns
   - Add new capabilities incrementally
   - Maintain backward compatibility
   - Update version number

### Multi-Agent Orchestra Creation

When creating complementary agents:

```markdown
## Agent Network Design
1. **Primary Agent**: <main-orchestrator>
   - Role: Coordination and delegation
   - Tools: Task, Bash

2. **Specialist Agents**:
   - @<analyzer>: Deep analysis tasks
   - @<generator>: Content creation
   - @<validator>: Quality assurance

3. **Communication Flow**:
   ```
   User → Primary → Specialists → Primary → User
   ```
```

## Phase 6: Validation and Testing

### Agent Quality Assurance

```markdown
@Task: Validate the generated agent:
1. YAML frontmatter correctness
2. System prompt clarity and completeness
3. Tool selection appropriateness
4. Integration compatibility
5. Performance optimization potential
```

### Test Scenario Generation

Create test cases for the agent:

```bash
# Test simple invocation
echo "Test simple task for $1 agent"

# Test complex scenario
echo "Test multi-step workflow"

# Test error handling
echo "Test with invalid input"

# Test integration
echo "Test delegation to/from other agents"
```

## Output Format

After creating/updating an agent:

```markdown
## Agent Creation Summary

**Agent**: `<agent-name>`
**Location**: `<path-to-agent-file>`
**Type**: <user-level|project-level>
**Tools**: <tool-list-or-all>
**Specialization**: <primary-domain>

### Capabilities Added
- <capability-1>
- <capability-2>

### Integration Points
- Works with: <agent-list>
- Delegates to: <agent-list>
- Supervised by: <parent-agent>

### Usage Examples

#### Direct Invocation
```
@<agent-name>: <task-description>
```

#### Orchestrated Workflow
```
Complex task → @orchestrator → @<agent-name> → Results
```

### Optimization Opportunities
- <future-enhancement-1>
- <future-enhancement-2>

### Testing Checklist
- [ ] Simple task execution
- [ ] Complex workflow handling
- [ ] Error recovery testing
- [ ] Integration validation
- [ ] Performance benchmarking
```

## Meta-Agent Intelligence

This command demonstrates advanced agent creation:

1. **Ecosystem Awareness**: Understands entire agent network
2. **Optimization Patterns**: Applies best practices automatically
3. **Self-Improvement**: Each agent includes enhancement protocols
4. **Integration Design**: Creates complementary agent systems
5. **Project Intelligence**: Leverages codebase and documentation
6. **Quality Assurance**: Validates and tests thoroughly

## Advanced Features

### Hierarchical Agent Networks
Create parent-child relationships:
- Parent agents coordinate workflows
- Child agents handle specializations
- Grandchild agents for micro-tasks

### Agent Templates Library
Build reusable patterns:
- Code Review Agent Template
- Data Processing Agent Template
- Security Audit Agent Template
- Documentation Agent Template

### Dynamic Agent Selection
Agents can intelligently choose sub-agents:
- Based on task complexity
- Available tool permissions
- Performance requirements
- Domain expertise needs

## Examples

### Example 1: Create a Code Review Agent
```
/update-agent code-reviewer "Expert at reviewing code for quality, security, and best practices" --tools=Read,Grep,Glob
```

### Example 2: Create Project-Specific Test Agent
```
/update-agent test-runner "Run and analyze test results for this project" --level=project
```

### Example 3: Create Orchestrator Agent
```
/update-agent orchestrator "Coordinate multiple agents for complex workflows" --tools=Task,Bash --parent=controller
```

## Continuous Enhancement Protocol

This command continuously improves by:
1. Learning from created agents' performance
2. Identifying common patterns across agents
3. Building better templates over time
4. Optimizing prompt engineering techniques
5. Enhancing integration strategies

Remember: Every agent should be a specialist that excels in its domain while seamlessly integrating with the broader agent ecosystem.