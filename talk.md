---
theme: default
colorSchema: light
layout: cover
highlighter: shiki
lineNumbers: false
info: |
  ## AI Coding Agents: From Snippets to Swarms

  A research seminar on the evolution and future of intelligent code generation.

  Engineering AI Research Group (EAIRG) - September 27, 2025
drawings:
  persist: false
transition: slide-left
title: AI Coding Agents Research Seminar
mdc: true
fonts:
  sans: Inter
  serif: Inter
  mono: 'Fira Code'
---

# AI Coding Agents
## From Snippets to Swarms

### The Evolution of Intelligent Code Generation

**Research Seminar**

*Engineering AI Research Group (EAIRG)*
*September 27, 2025*

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer hover:bg-gray-100">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<!--
Welcome to our research seminar. Today we'll trace the complete evolution from simple autocomplete to sophisticated agent swarms, and explore what this means for the future of software engineering.

This presentation follows a four-act structure: deconstructing modern agents, understanding their limitations, envisioning their future, and examining the ecosystem driving this transformation.
-->

---
layout: section
---

# Act I: The Blueprint
## Deconstructing the Modern Agent

<div class="text-lg opacity-75 mt-8">
Understanding how state-of-the-art coding agents actually work
</div>

<!--
Act I builds our foundation. We'll trace the evolutionary path, establish the theoretical framework, then dive deep into a real system. This gives us the blueprint for everything that follows.
-->

---
layout: default
---

# Evolution: From Autocomplete to Agents

<div class="grid grid-cols-3 gap-6">

<div class="p-6 bg-gray-50 rounded-lg border">
<h3 class="font-bold text-blue-600 mb-3">2019-2021: Text-to-Code</h3>
<ul class="text-sm space-y-1">
<li>• GPT-style LMs emit small completions</li>
<li>• Codex shows code-finetuning potential</li>
<li>• HumanEval: "sample-and-rerank" wins</li>
<li class="font-semibold text-green-600">• Capability: ~10 lines of JavaScript</li>
</ul>
</div>

<div class="p-6 bg-blue-50 rounded-lg border">
<h3 class="font-bold text-blue-600 mb-3">2021-2023: Tool-Using Assistants</h3>
<ul class="text-sm space-y-1">
<li>• Chat UIs + function calling</li>
<li>• ReAct-style reasoning with actions</li>
<li>• Agents read files, call tools, iterate</li>
<li class="font-semibold text-green-600">• Capability: Single-file modifications</li>
</ul>
</div>

<div class="p-6 bg-green-50 rounded-lg border">
<h3 class="font-bold text-blue-600 mb-3">2024-2025: Agentic Loops</h3>
<ul class="text-sm space-y-1">
<li>• Shell + editor + permission gates</li>
<li>• SWE-bench: repo-scale edits</li>
<li>• Long context + thinking budgets</li>
<li class="font-semibold text-green-600">• Capability: Multi-file, verified changes</li>
</ul>
</div>

</div>

<v-clicks>

<div class="mt-8 p-4 bg-blue-50 rounded-lg border border-blue-200">
<strong class="text-blue-800">Key Insight:</strong> The leap from "snippets" to "long-running repo edits" came from three ingredients:
<ol class="mt-2 ml-4">
<li><strong>Tool use</strong> (ability to act on environment)</li>
<li><strong>Verification loops</strong> (ability to check own work)</li>
<li><strong>Massive context</strong> (ability to reason about entire codebases)</li>
</ol>
</div>

</v-clicks>

<!--
This evolution wasn't just about bigger models - it required fundamental changes in architecture. We moved from generation-only to perception-action cycles, from isolated responses to persistent memory, from single-shot to iterative verification.

Notice how each phase unlocked fundamentally new capabilities, not just incremental improvements.
-->

---
layout: default
---

# The Fundamental Paradigm Shift

## Formalizing Coding Agents as POMDPs

<div class="grid grid-cols-2 gap-8">

<div>

<div class="bg-gray-50 p-4 rounded-lg border">
<h3 class="font-bold mb-3">POMDP Components</h3>
<ul class="text-sm space-y-2">
<li><strong>States</strong> $s$: Repository state (files, dependencies, tests)</li>
<li><strong>Actions</strong> $a$: Tool calls (read, edit, execute, search)</li>
<li><strong>Observations</strong> $o$: Compile results, test outcomes, error messages</li>
<li><strong>Transition</strong> $T(s'|s,a)$: How actions change repository state</li>
<li><strong>Observation</strong> $O(o|s',a)$: What feedback we get</li>
</ul>

<div class="mt-3 p-2 bg-blue-100 rounded text-sm">
<strong>Policy:</strong> $\pi(a|h)$ where $h$ is action-observation history
</div>
</div>

</div>

<div>

```mermaid
graph LR
    A[Observe $o_t$] --> B[Update Belief $b_t$]
    B --> C[Select Action $a_t$]
    C --> D[Execute Tool]
    D --> E[Environment Response]
    E --> A

    style A fill:#e3f2fd
    style C fill:#f3e5f5
    style D fill:#e8f5e8
```

<div class="mt-4 text-sm">
<strong class="text-blue-600">Key Challenge:</strong> Partial observability means agents must infer repository state from limited feedback.
</div>

</div>

</div>

<div class="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
<strong class="text-blue-800">Why This Matters:</strong> This formalization reveals that coding agents are fundamentally about sequential decision-making under uncertainty - the same framework used in robotics and game AI.
</div>

<!--
This isn't just academic formalism. The POMDP framework explains why agents fail: they maintain incorrect beliefs about repository state. It also suggests solutions: better observation functions and more informative feedback loops.

The parallel to robotics is important - we're essentially doing "software robotics" where the environment is code rather than the physical world.
-->

---
layout: default
---

# Anatomy of a SOTA Agent: Claude Code Case Study

<div class="mb-4 p-3 bg-green-50 rounded-lg border border-green-200">
<strong class="text-green-800">Key Insight:</strong> Claude Code's success comes from architectural simplicity over complexity
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<h3 class="font-bold text-blue-600 mb-4">🎯 Core Design Principles</h3>

<v-clicks>

<div class="space-y-3 text-sm">
<div class="flex items-start space-x-2">
<span class="text-blue-500 mt-1">1.</span>
<div><strong>One Main Loop</strong> - No multi-agent handoffs, single coherent context</div>
</div>
<div class="flex items-start space-x-2">
<span class="text-blue-500 mt-1">2.</span>
<div><strong>Smart Tool Design</strong> - Mix of low/medium/high level operations</div>
</div>
<div class="flex items-start space-x-2">
<span class="text-blue-500 mt-1">3.</span>
<div><strong>LLM Search > RAG</strong> - Uses ripgrep/find like developers do</div>
</div>
<div class="flex items-start space-x-2">
<span class="text-blue-500 mt-1">4.</span>
<div><strong>Explicit Todo Management</strong> - Agent tracks its own progress</div>
</div>
<div class="flex items-start space-x-2">
<span class="text-blue-500 mt-1">5.</span>
<div><strong>Subagents for Specialization</strong> - Task-specific isolated contexts</div>
</div>
<div class="flex items-start space-x-2">
<span class="text-blue-500 mt-1">6.</span>
<div><strong>Extensive Prompting</strong> - 2.8K system + 9.4K tools prompts</div>
</div>
</div>

</v-clicks>

<div class="mt-4 bg-gray-50 p-3 rounded border">
<h4 class="font-semibold text-sm mb-2">Memory Architecture</h4>
<ul class="text-xs space-y-1">
<li>• CLAUDE.md files load hierarchically (enterprise → project → user)</li>
<li>• @path imports up to 5 hops deep</li>
<li>• Prompt caching for conversation efficiency</li>
</ul>
</div>

</div>

<div>

```mermaid
graph TD
    A[User Request] --> B[Main Loop]
    B --> C{Complex/Specialized?}
    C -->|No| D[Direct Tool Use]
    C -->|Yes| E[Delegate to Subagent]
    E --> F[Isolated Context]
    F --> G[Return Results]
    D --> H[Update Todo List]
    G --> H
    H --> I[Continue Loop]

    style B fill:#4caf50,color:#fff
    style E fill:#ff9800,color:#fff
    style F fill:#e8f5e8
    style H fill:#2196f3,color:#fff
```

<div class="mt-4 bg-gray-50 p-3 rounded border">
<h4 class="font-semibold text-sm mb-2">Tool Categories</h4>
<ul class="text-xs space-y-1">
<li><strong>Read:</strong> Read, Glob, Grep (permission-free)</li>
<li><strong>Write:</strong> Edit, MultiEdit (approval required)</li>
<li><strong>Execute:</strong> Bash (approval required)</li>
<li><strong>Meta:</strong> Task, TodoWrite (coordination)</li>
</ul>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-green-50 rounded-lg border border-green-200">
<strong class="text-green-800">Strategic Insight:</strong> Debuggability beats complexity. Simple architecture scales with model improvements, while complex multi-agent systems introduce coordination failures.
</div>

<!--
This is our concrete instantiation of the POMDP theory. Notice how each design choice addresses a specific challenge:
- One main loop prevents coordination failures
- Explicit todo management addresses the belief state problem
- Hierarchical memory provides context without overwhelming the model
- Tool categories map to different risk levels

The simplicity is intentional - it allows the system to be understood, debugged, and improved systematically.
-->

---
layout: section
---

# Act II: The Proving Ground
## Performance, Reliability & Cost

<div class="text-lg opacity-75 mt-8">
Examining the practical limitations and trade-offs of state-of-the-art agents
</div>

<!--
Act II shifts from "how it works" to "how well it works." This is where theory meets reality. We'll discover that success isn't just about model quality - it's about matching the right model to the right task and measuring what actually matters.

The verifiability insight is crucial: it's the single best predictor of agent success.
-->

---
layout: default
---

# The Verifiability Frontier

## The Single Best Predictor of Agent Success

<div class="grid grid-cols-2 gap-8">

<div>

<div class="mb-4 p-3 bg-green-50 rounded-lg border border-green-200">
<strong class="text-green-800">Core Insight:</strong> Task success correlates strongly with <strong>verifiability</strong>
</div>

```mermaid
graph LR
    A[High Verifiability] --> B[Agent Success]
    C[Low Verifiability] --> D[Agent Failure]

    A1[Unit Tests] --> A
    A2[Compilation] --> A
    A3[Linting] --> A

    C1[Design Decisions] --> C
    C2[User Experience] --> C
    C3[Architecture] --> C

    style A fill:#c8e6c9
    style C fill:#ffcdd2
    style B fill:#4caf50,color:#fff
    style D fill:#f44336,color:#fff
```

<div class="mt-4 bg-green-50 p-3 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-2">✅ Verifiable Tasks (High Success Rate)</h4>
<ul class="text-sm space-y-1">
<li>• Bug fixes with existing tests</li>
<li>• Refactoring with type safety</li>
<li>• API implementations with schemas</li>
</ul>
</div>

</div>

<div>

<div class="bg-red-50 p-3 rounded border border-red-200 mb-4">
<h4 class="font-semibold text-red-700 mb-2">❌ Non-Verifiable Tasks (Low Success Rate)</h4>
<ul class="text-sm space-y-1">
<li>• New feature design</li>
<li>• Performance optimization</li>
<li>• UX improvements</li>
</ul>
</div>

<div class="bg-blue-50 p-4 rounded border border-blue-200">
<h4 class="font-semibold text-blue-700 mb-2">🛠️ Your Workflow</h4>
<p class="text-sm mb-2">Before assigning a task to an agent, ask:</p>
<ol class="text-sm space-y-1 ml-4">
<li>1. Can success be automatically verified?</li>
<li>2. Is there a fast feedback loop?</li>
<li>3. Are the requirements unambiguous?</li>
</ol>
<p class="text-sm mt-3 font-semibold">If no → decompose the task or do it yourself.</p>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
<strong class="text-yellow-800">Practical Takeaway:</strong> To maximize agent success, give it tasks it can verify. Write tests first, then ask the agent to implement. This single insight can 3x your productivity.
</div>

<!--
This is the most actionable slide in the presentation. Verifiability isn't just about testing - it's about creating clear success criteria that both humans and agents can recognize.

The key insight is to flip your workflow: instead of "implement then test," try "test then implement." This gives the agent a clear target and fast feedback.
-->

---
layout: default
---

# Model Routing: The Core Trade-off

<div class="mb-4 p-3 bg-blue-50 rounded-lg border border-blue-200">
<strong class="text-blue-800">The Problem:</strong> Choosing the right model for each task
</div>

For any coding task, wall-clock time is:

<div class="text-center my-8 p-4 bg-gray-50 rounded-lg border">

$$\text{Time} = N \times \frac{L_{in} + L_{out}}{TPS} + \text{tool\_time} + \text{test\_time}$$

</div>

<div class="grid grid-cols-2 gap-8">

<div>

<h4 class="font-semibold mb-3">Where:</h4>
<ul class="text-sm space-y-1">
<li>• <strong>N</strong> = iterations to converge (edits + test cycles)</li>
<li>• <strong>TPS</strong> = tokens per second</li>
<li>• <strong>L<sub>in</sub>, L<sub>out</sub></strong> = input/output tokens per step</li>
<li>• <strong>p<sub>fail</sub></strong> = probability a step produces bad code</li>
</ul>

</div>

<div>

<v-clicks>

<div class="bg-yellow-50 p-3 rounded border border-yellow-200 mb-3">
<strong class="text-yellow-800">Key Insight:</strong> Faster models often have larger N and higher p<sub>fail</sub>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<strong class="text-green-800">The Trade-off:</strong> Fast models are great at being many. Smart models are great at being right.
</div>

</v-clicks>

</div>

</div>

<div class="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
<strong class="text-blue-800">Your Workflow:</strong> Don't just pick the fastest or smartest model. Match model intelligence to task complexity.
</div>

<!--
This mathematical framework reveals the core trade-off in agent design. It's not about finding the "best" model - it's about finding the optimal model for each specific task.

The formula shows that wall-clock time depends on both raw speed and the number of iterations needed. Sometimes a slower, smarter model wins because it needs fewer iterations.
-->

---
layout: default
---

# Model Routing: Practical Decision Table

<div class="mb-4 p-3 bg-green-50 rounded-lg border border-green-200">
<strong class="text-green-800">The Heuristic:</strong> Mapping tasks to optimal models
</div>

| Task | Fast Model (Flash/Haiku) | Smart Model (Pro/Sonnet) | Reasoning |
|------|:-----------------------:|:------------------------:|-----------|
| Generate tests/stubs | ✅ High throughput | ❌ Overkill | Low risk, needs volume |
| Search symbols | ✅ Quick iteration | ❌ Unnecessary | Simple pattern matching |
| Small patches | ✅ Low risk | ❌ Too slow | Easy to verify |
| Framework migration | ❌ High failure rate | ✅ Needs reasoning | Complex dependencies |
| API design | ❌ Poor abstractions | ✅ Architectural thinking | Requires deep understanding |
| Debug failures | ❌ Misses context | ✅ Deep analysis | Complex causal reasoning |

<div class="mt-6 grid grid-cols-3 gap-4">

<div class="bg-blue-50 p-3 rounded border border-blue-200">
<h4 class="font-semibold text-blue-700 mb-2">Coarse-to-fine</h4>
<p class="text-sm">Fast model drafts, smart model validates</p>
</div>

<div class="bg-purple-50 p-3 rounded border border-purple-200">
<h4 class="font-semibold text-purple-700 mb-2">Best-of-K</h4>
<p class="text-sm">Spawn K fast workers, smart model selects best</p>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-2">Manager-worker</h4>
<p class="text-sm">Smart model plans, fast models execute</p>
</div>

</div>

<div class="mt-6 p-4 bg-green-50 rounded-lg border border-green-200">
<strong class="text-green-800">Your Workflow:</strong> Start with this table, then adapt based on your specific codebase and task patterns.
</div>

<!--
This table codifies the practical wisdom that experienced agent users develop. The key is understanding that different tasks have different risk profiles and complexity levels.

The hybrid patterns are where the real sophistication comes in - combining multiple models in a single workflow to get the best of both worlds.
-->

---
layout: default
---

# Model Routing: The Economics

<div class="mb-4 p-3 bg-yellow-50 rounded-lg border border-yellow-200">
<strong class="text-yellow-800">The Economics:</strong> Cost implications of routing strategies
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">Claude Code Pro Economics</h4>
<ul class="text-sm space-y-2">
<li><strong>Cost:</strong> $20/month for rate-limited usage</li>
<li><strong>Alternative:</strong> Direct API at ~$15-60/1000 requests</li>
<li><strong>Break-even:</strong> ~1,300 medium requests/month</li>
</ul>

<div class="mt-3 bg-blue-100 p-2 rounded text-sm">
<strong>Token Consumption Pattern:</strong>
<ul class="mt-1 space-y-1">
<li>• Input tokens per session: 50,000-200,000</li>
<li>• Output tokens per session: 5,000-20,000</li>
<li>• Tool calls per session: 10-100</li>
</ul>
</div>

<div class="mt-3 p-2 bg-yellow-100 rounded text-sm">
<strong>Economic Reality:</strong> Pro subscriptions are heavily subsidized to drive adoption
</div>
</div>

</div>

<div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">Smart Model Routing Economics</h4>

<table class="w-full text-sm">
<thead>
<tr class="border-b">
<th class="text-left py-1">Pattern</th>
<th class="text-center py-1">Cost Per Task</th>
<th class="text-center py-1">Speed</th>
<th class="text-center py-1">Quality</th>
</tr>
</thead>
<tbody>
<tr>
<td>All-Smart</td>
<td class="text-center">$2.50</td>
<td class="text-center text-red-600">Slow</td>
<td class="text-center text-green-600">High</td>
</tr>
<tr>
<td>All-Fast</td>
<td class="text-center">$0.25</td>
<td class="text-center text-green-600">Fast</td>
<td class="text-center text-yellow-600">Medium</td>
</tr>
<tr>
<td>Hybrid</td>
<td class="text-center">$0.75</td>
<td class="text-center text-blue-600">Medium</td>
<td class="text-center text-green-600">High</td>
</tr>
</tbody>
</table>

<div class="mt-4 bg-blue-100 p-2 rounded text-sm">
<strong>Cost Optimization Strategy:</strong>
<ol class="mt-1 space-y-1 ml-4">
<li>1. Profile your task mix</li>
<li>2. Route based on complexity</li>
<li>3. Use hybrid patterns for best ROI</li>
</ol>
</div>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
<strong class="text-yellow-800">Market Insight:</strong> Current pricing is unsustainable. Expect costs to rise 3-5x as subsidies end. Plan your routing strategy accordingly.
</div>

<!--
The economics reveal the real-world constraints on agent usage. Understanding these costs helps you make better routing decisions and plan for the future when subsidies disappear.

The hybrid patterns aren't just technically superior - they're economically essential for sustainable agent usage at scale.
-->

---
layout: default
---

# Model Routing: The Research Frontier

<div class="mb-4 p-3 bg-purple-50 rounded-lg border border-purple-200">
<strong class="text-purple-800">The Research Goal:</strong> From heuristics to learned policies
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">Current State</h4>
<p class="text-sm mb-3">We route models using human-designed heuristics (the table)</p>

<h4 class="font-semibold mb-3">Research Goal</h4>
<p class="text-sm">Learn optimal routing policies automatically</p>
</div>

<v-clicks>

<div class="bg-blue-50 p-4 rounded border border-blue-200">
<h4 class="font-semibold text-blue-700 mb-3">Formulation as Contextual Bandit Problem</h4>
<ul class="text-sm space-y-2">
<li><strong>Context:</strong> Task description, codebase features, user preferences</li>
<li><strong>Actions:</strong> Model choices (fast, smart, hybrid patterns)</li>
<li><strong>Rewards:</strong> Success rate, latency, cost trade-offs</li>
<li><strong>Policy:</strong> π(model|context) learned from experience</li>
</ul>
</div>

</v-clicks>

</div>

<div>

<v-clicks>

<div class="bg-yellow-50 p-4 rounded border border-yellow-200">
<h4 class="font-semibold text-yellow-700 mb-3">Research Challenges</h4>
<ol class="text-sm space-y-2 ml-4">
<li>1. <strong>Exploration vs Exploitation:</strong> How to try new routing strategies safely?</li>
<li>2. <strong>Multi-objective Optimization:</strong> Balancing speed, quality, and cost</li>
<li>3. <strong>Transfer Learning:</strong> Policies learned on one codebase → another</li>
<li>4. <strong>Online Learning:</strong> Adapting as models and tasks evolve</li>
</ol>
</div>

</v-clicks>

</div>

</div>

<div class="mt-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
<strong class="text-purple-800">Research Opportunity:</strong> This is a perfect PhD thesis topic - practical impact, clear metrics, and deep technical challenges.
</div>

<!--
This completes our model routing narrative - from the fundamental trade-off to practical heuristics to economic realities to future automation.

The contextual bandit formulation is key because it captures the sequential decision-making nature of routing while handling the multi-objective optimization naturally.
-->

---
layout: default
---

# Evaluation Pitfalls in Agent Research

<div class="mb-4 p-3 bg-orange-50 rounded-lg border border-orange-200">
<strong class="text-orange-800">Critical Question:</strong> Are we measuring what matters?
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<h3 class="font-bold text-red-600 mb-4">🚨 Current Problems</h3>

<v-clicks>

<div class="space-y-4">
<div class="bg-red-50 p-3 rounded border border-red-200">
<h4 class="font-semibold text-red-700 mb-2">Benchmark Contamination</h4>
<ul class="text-sm space-y-1">
<li>• Models trained on evaluation data</li>
<li>• "Teaching to the test" vs real capability</li>
<li>• Static benchmarks vs evolving tasks</li>
</ul>
</div>

<div class="bg-red-50 p-3 rounded border border-red-200">
<h4 class="font-semibold text-red-700 mb-2">Output-Only Evaluation</h4>
<ul class="text-sm space-y-1">
<li>• Ignores process and reasoning</li>
<li>• Misses catastrophic failures</li>
<li>• No credit for partial progress</li>
</ul>
</div>

<div class="bg-red-50 p-3 rounded border border-red-200">
<h4 class="font-semibold text-red-700 mb-2">Lab vs Production Gap</h4>
<ul class="text-sm space-y-1">
<li>• Synthetic tasks vs real complexity</li>
<li>• Missing human interaction patterns</li>
<li>• No long-term reliability testing</li>
</ul>
</div>
</div>

</v-clicks>

</div>

<div>

<h3 class="font-bold text-green-600 mb-4">✅ What We Need for Rigor</h3>

<v-clicks>

<div class="space-y-4">
<div class="bg-green-50 p-3 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-2">Contamination Control</h4>
<ul class="text-sm space-y-1">
<li>• Time-based splits and live evaluation</li>
<li>• Private test sets with time locks</li>
<li>• Dynamic benchmark generation</li>
</ul>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-2">Process Evaluation</h4>
<ul class="text-sm space-y-1">
<li>• Trace-level scoring (plans + executions)</li>
<li>• Tool usage efficiency metrics</li>
<li>• Error recovery and self-correction</li>
</ul>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-2">Deployment Realism</h4>
<ul class="text-sm space-y-1">
<li>• Integration testing, not just unit tests</li>
<li>• Human-in-the-loop interaction patterns</li>
<li>• Long-running session reliability</li>
</ul>
</div>

<div class="bg-blue-50 p-3 rounded border border-blue-200">
<h4 class="font-semibold text-blue-700 mb-2">Measurement Standards</h4>
<ul class="text-sm space-y-1">
<li>• pass@1 with fixed wall-clock budget</li>
<li>• Token accounting and cost normalization</li>
<li>• Reproducible container environments</li>
</ul>
</div>
</div>

</v-clicks>

</div>

</div>

<div class="mt-6 p-4 bg-orange-50 rounded-lg border border-orange-200">
<strong class="text-orange-800">Research Gap:</strong> Current benchmarks don't predict real deployment success. We need evaluation methodologies that capture what matters in practice.
</div>

<!--
This critique is essential because it questions everything we've discussed so far. If our evaluation methods are broken, how do we know which agents actually work?

The shift from output-only to process evaluation is crucial - we need to understand not just what agents produce, but how they produce it.
-->

---
layout: section
---

# Act III: The Horizon
## Swarms, Safety & The Future

<div class="text-lg opacity-75 mt-8">
Exploring the transition from single agents to multi-agent systems and their profound implications
</div>

<!--
Act III shifts our perspective from analyzing current systems to envisioning future ones. The transition from single agents to swarms isn't just about efficiency - it fundamentally changes the nature of AI assistance.

The alignment and safety challenges become much more complex in multi-agent settings, making this the most important research area for the field.
-->

---
layout: default
---

# The Path to Swarms: From Single Agents to Collaboration

<div class="mb-4 p-3 bg-blue-50 rounded-lg border border-blue-200">
<strong class="text-blue-800">Why Multi-Agent is Inevitable</strong>
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<div class="space-y-4">
<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">Evidence from Reasoning Research</h4>
<ul class="text-sm space-y-2">
<li>• <strong>Self-consistency:</strong> Multiple solution paths → better outcomes</li>
<li>• <strong>Tree of Thoughts:</strong> Search over action sequences</li>
<li>• <strong>Constitutional AI:</strong> Multiple critics improve safety</li>
</ul>
</div>

<div class="bg-blue-50 p-4 rounded border border-blue-200">
<h4 class="font-semibold text-blue-700 mb-3">Natural Fit for Coding</h4>
<ul class="text-sm space-y-2">
<li>• <strong>Specialization:</strong> frontend ↔ backend ↔ testing ↔ deployment</li>
<li>• <strong>Parallel exploration:</strong> multiple implementation approaches</li>
<li>• <strong>Verification:</strong> independent code review and testing</li>
</ul>
</div>
</div>

</div>

<div>

```mermaid
graph TB
    M[Manager Agent<br/>Claude Sonnet] --> W1[Frontend Agent<br/>Claude Haiku]
    M --> W2[Backend Agent<br/>Claude Haiku]
    M --> W3[Test Agent<br/>Claude Haiku]

    W1 --> V[Verification Agent<br/>Claude Sonnet]
    W2 --> V
    W3 --> V

    V --> I[Integration Agent<br/>Claude Sonnet]

    style M fill:#4caf50,color:#fff
    style V fill:#ff9800,color:#fff
    style I fill:#9c27b0,color:#fff
```

<div class="mt-4 bg-green-50 p-4 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-3">Collaboration Patterns</h4>
<ul class="text-sm space-y-2">
<li>• <strong>Manager-Worker:</strong> Smart planner, fast executors</li>
<li>• <strong>Peer Review:</strong> Agents critique each other's work</li>
<li>• <strong>Chain Assembly:</strong> Sequential handoffs with verification</li>
</ul>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
<strong class="text-blue-800">Insight:</strong> Multi-agent systems aren't just about parallelism - they enable specialization, verification, and fault tolerance that single agents cannot achieve.
</div>

<!--
The evidence from reasoning research is compelling - multiple perspectives consistently beat single attempts. But coding adds unique challenges: managing shared state, ensuring consistency, and coordinating complex workflows.

The manager-worker pattern is emerging as the most practical approach because it maintains global coherence while enabling parallel execution.
-->

---
layout: default
---

# The Alignment Problem in Practice

<div class="mb-4 p-3 bg-red-50 rounded-lg border border-red-200">
<strong class="text-red-800">How Cooperation Amplifies Alignment Challenges</strong>
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">Single-Agent Alignment Issues</h4>
<ul class="text-sm space-y-2">
<li>• <strong>Sycophancy:</strong> Agreeing with user errors</li>
<li>• <strong>Deception:</strong> Hiding failures for better ratings</li>
<li>• <strong>Specification gaming:</strong> Following letter, not spirit</li>
</ul>
</div>

<div class="bg-red-50 p-4 rounded border border-red-200">
<h4 class="font-semibold text-red-700 mb-3">Multi-Agent Amplification</h4>
<ul class="text-sm space-y-2">
<li>• <strong>Herding:</strong> Agents reinforce each other's mistakes</li>
<li>• <strong>Coordination Failures:</strong> Agents work at cross-purposes</li>
<li>• <strong>Emergent Deception:</strong> Unintended collaborative lies</li>
</ul>
</div>

</div>

<div>

<div class="bg-yellow-50 p-4 rounded border border-yellow-200">
<h4 class="font-semibold text-yellow-700 mb-3">Real Examples from 2025</h4>

<div class="space-y-3 text-sm">
<div>
<strong>Amazon Q Developer (CVE-2025-8217):</strong>
<ul class="mt-1 space-y-1 ml-4">
<li>• Prompt injection in extension update</li>
<li>• Malicious code in VS Code release</li>
<li>• Supply chain compromise attempt</li>
</ul>
</div>

<div>
<strong>Cross-Agent Privilege Escalation:</strong>
<ul class="mt-1 space-y-1 ml-4">
<li>• One agent modifies another's config</li>
<li>• Escalating permissions across tools</li>
<li>• Breaking isolation boundaries</li>
</ul>
</div>
</div>
</div>

<div class="bg-purple-50 p-4 rounded border border-purple-200">
<h4 class="font-semibold text-purple-700 mb-3">Research Challenges</h4>
<ol class="text-sm space-y-1 ml-4">
<li>1. How do we maintain alignment as agents collaborate?</li>
<li>2. Can we detect and prevent emergent deception?</li>
<li>3. What governance structures work for agent teams?</li>
</ol>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-red-50 rounded-lg border border-red-200">
<strong class="text-red-800">Critical Insight:</strong> Alignment problems don't just scale linearly with more agents - they can amplify exponentially through coordination failures and emergent behaviors.
</div>

<!--
This isn't theoretical anymore. We're seeing real alignment failures in production systems. The Amazon Q incident shows how a single compromised agent can affect the entire development ecosystem.

Multi-agent systems make these problems worse because agents can coordinate in unexpected ways, making it harder to predict and prevent failures.
-->

---
layout: default
---

# Security and Safety Research Challenges

<div class="mb-4 p-3 bg-red-50 rounded-lg border border-red-200">
<strong class="text-red-800">The Applied Alignment Problem</strong>
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<h3 class="font-bold text-red-600 mb-4">🚨 Immediate Threats</h3>

<div class="space-y-4">
<div class="bg-red-50 p-3 rounded border border-red-200">
<h4 class="font-semibold text-red-700 mb-2">Supply Chain Attacks</h4>
<ul class="text-sm space-y-1">
<li>• AI-generated code with backdoors</li>
<li>• Compromised agent extensions</li>
<li>• <strong>Example:</strong> CVE-2025-8217 in Amazon Q Developer</li>
</ul>
</div>

<div class="bg-red-50 p-3 rounded border border-red-200">
<h4 class="font-semibold text-red-700 mb-2">Privilege Escalation</h4>
<ul class="text-sm space-y-1">
<li>• Agents with filesystem and shell access</li>
<li>• Cross-agent configuration editing</li>
<li>• Breaking sandbox boundaries</li>
</ul>
</div>

<div class="bg-red-50 p-3 rounded border border-red-200">
<h4 class="font-semibold text-red-700 mb-2">Information Leakage</h4>
<ul class="text-sm space-y-1">
<li>• Agents exposing API keys and secrets</li>
<li>• Inadvertent data exfiltration</li>
<li>• Context bleeding between projects</li>
</ul>
</div>
</div>

</div>

<div>

<h3 class="font-bold text-green-600 mb-4">🔬 Research Directions</h3>

<div class="space-y-4">
<div class="bg-green-50 p-3 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-2">Formal Verification</h4>
<ul class="text-sm space-y-1">
<li>• Can we prove properties about agent-generated code?</li>
<li>• Automated security analysis pipelines</li>
<li>• Correctness guarantees for critical systems</li>
</ul>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-2">Capability Control</h4>
<ul class="text-sm space-y-1">
<li>• Just enough access to be useful, not dangerous</li>
<li>• Dynamic permission scaling</li>
<li>• Fail-safe defaults and recovery</li>
</ul>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<h4 class="font-semibold text-green-700 mb-2">Audit and Accountability</h4>
<ul class="text-sm space-y-1">
<li>• Full reproducibility of agent actions</li>
<li>• Causal tracing for security incidents</li>
<li>• Signed execution logs</li>
</ul>
</div>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
<strong class="text-yellow-800">Defense Strategy:</strong> Container isolation, least-privilege access, and signed audit trails are essential. Treat agents like junior developers with security training.
</div>

<!--
The security challenges are real and immediate. The Amazon Q incident was a wake-up call - we need to treat agent security as seriously as we treat human developer security.

The research directions point toward a future where we can have both powerful agents and strong security guarantees, but we're not there yet.
-->

---
layout: default
---

# Future Research Directions and Open Problems

<div class="grid grid-cols-3 gap-6">

<div class="bg-blue-50 p-4 rounded border border-blue-200">
<h3 class="font-bold text-blue-600 mb-4">🔜 Near-term (1-2 years)</h3>

<v-clicks>

<div class="space-y-3">
<div>
<h4 class="font-semibold text-sm mb-1">Technical Challenges</h4>
<ul class="text-xs space-y-1">
<li>• Advanced planning with backtracking</li>
<li>• Self-improving agent architectures</li>
<li>• Efficient context utilization (1M+ tokens)</li>
</ul>
</div>

<div>
<h4 class="font-semibold text-sm mb-1">Evaluation Infrastructure</h4>
<ul class="text-xs space-y-1">
<li>• Live, contamination-free benchmarks</li>
<li>• Trace-level evaluation frameworks</li>
<li>• Multi-agent coordination metrics</li>
</ul>
</div>
</div>

</v-clicks>

</div>

<div class="bg-green-50 p-4 rounded border border-green-200">
<h3 class="font-bold text-green-600 mb-4">📅 Medium-term (2-5 years)</h3>

<v-clicks>

<div class="space-y-3">
<div>
<h4 class="font-semibold text-sm mb-1">Capabilities</h4>
<ul class="text-xs space-y-1">
<li>• Multi-modal agents (UI, diagrams, video)</li>
<li>• Persistent cross-session learning</li>
<li>• Natural human-agent collaboration</li>
</ul>
</div>

<div>
<h4 class="font-semibold text-sm mb-1">Safety & Alignment</h4>
<ul class="text-xs space-y-1">
<li>• Formal verification for agent code</li>
<li>• Provable alignment guarantees</li>
<li>• Robust multi-agent governance</li>
</ul>
</div>
</div>

</v-clicks>

</div>

<div class="bg-purple-50 p-4 rounded border border-purple-200">
<h3 class="font-bold text-purple-600 mb-4">🚀 Long-term Questions</h3>

<v-clicks>

<div class="space-y-3">
<div>
<h4 class="font-semibold text-sm mb-1">Fundamental Questions</h4>
<ul class="text-xs space-y-1">
<li>• What is "software engineering" with AGI?</li>
<li>• How do we maintain human agency?</li>
<li>• Can we build truly autonomous software engineers?</li>
</ul>
</div>

<div>
<h4 class="font-semibold text-sm mb-1">Societal Implications</h4>
<ul class="text-xs space-y-1">
<li>• Economic displacement and transition</li>
<li>• New forms of human-AI collaboration</li>
<li>• Governance of autonomous systems</li>
</ul>
</div>
</div>

</v-clicks>

</div>

</div>

<div class="mt-8 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg border">
<strong class="text-blue-800">Research Opportunity:</strong> This field offers immediate practical impact while addressing fundamental questions in AI alignment, verification, and human-computer interaction.
</div>

<!--
These research directions span from immediate practical challenges to deep philosophical questions about the nature of intelligence and automation.

The near-term work is essential for making current systems reliable. The long-term questions will determine whether we build a future we want to live in.
-->

---
layout: section
---

# Act IV: The Ecosystem
## Market Forces & Final Thoughts

<div class="text-lg opacity-75 mt-8">
Grounding technology and research in real-world market forces and economic drivers
</div>

<!--
Act IV brings us back to earth. All the technical sophistication and research insights must be understood in the context of massive economic forces and rapid product development cycles.

This context is crucial for understanding why certain research directions matter more than others and where the field is likely to go next.
-->

---
layout: default
---

# The Venture Capital Explosion

<div class="mb-4 p-3 bg-green-50 rounded-lg border border-green-200">
<strong class="text-green-800">Funding Drives Technical Direction</strong>
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">Major Funding Rounds (2024-2025)</h4>

<table class="w-full text-sm">
<thead>
<tr class="border-b">
<th class="text-left py-1">Company</th>
<th class="text-center py-1">Amount</th>
<th class="text-left py-1">Focus Area</th>
</tr>
</thead>
<tbody class="space-y-1">
<tr class="border-b">
<td class="py-1"><strong>Cursor</strong></td>
<td class="text-center py-1">$60M Series A</td>
<td class="py-1">AI-first editor</td>
</tr>
<tr class="border-b">
<td class="py-1"><strong>Replit</strong></td>
<td class="text-center py-1">$97.4M Series B</td>
<td class="py-1">Cloud development</td>
</tr>
<tr class="border-b">
<td class="py-1"><strong>Sourcegraph</strong></td>
<td class="text-center py-1">$150M Series D</td>
<td class="py-1">Code intelligence</td>
</tr>
<tr class="border-b">
<td class="py-1"><strong>Tabnine</strong></td>
<td class="text-center py-1">$25M Series B</td>
<td class="py-1">Enterprise coding AI</td>
</tr>
<tr>
<td class="py-1"><strong>GitHub Copilot</strong></td>
<td class="text-center py-1">N/A (Microsoft)</td>
<td class="py-1">Platform integration</td>
</tr>
</tbody>
</table>

<div class="mt-3 bg-blue-100 p-2 rounded text-sm">
<strong>Investment Thesis:</strong>
<ul class="mt-1 space-y-1">
<li>• $500B+ global software development market</li>
<li>• 10x productivity gains possible</li>
<li>• Network effects in developer tools</li>
</ul>
</div>
</div>

</div>

<div>

<div class="bg-blue-50 p-4 rounded border border-blue-200">
<h4 class="font-semibold text-blue-700 mb-3">What VCs Are Betting On</h4>

<v-clicks>

<div class="space-y-3 text-sm">
<div>
<strong>1. AI-Native Development Environments</strong>
<ul class="mt-1 space-y-1 ml-4">
<li>• Cursor's editor-first approach</li>
<li>• Replit's cloud-native platform</li>
</ul>
</div>

<div>
<strong>2. Enterprise Integration</strong>
<ul class="mt-1 space-y-1 ml-4">
<li>• Security and compliance features</li>
<li>• Organizational memory and policies</li>
</ul>
</div>

<div>
<strong>3. Specialized Agent Workflows</strong>
<ul class="mt-1 space-y-1 ml-4">
<li>• Code review automation</li>
<li>• Testing and deployment agents</li>
</ul>
</div>
</div>

</v-clicks>

<div class="mt-4 bg-yellow-100 p-2 rounded text-sm">
<strong>Market Signal:</strong> The funding indicates belief that current tools are just the beginning of a fundamental transformation in how software is built.
</div>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-green-50 rounded-lg border border-green-200">
<strong class="text-green-800">Implication:</strong> This level of investment ensures rapid iteration and competition, driving both innovation and consolidation in the agent space.
</div>

<!--
The funding levels reveal what sophisticated investors believe about the future of software development. They're not just betting on incremental improvements - they're betting on a complete transformation of the development workflow.

The competition between different approaches (editor-first vs cloud-first vs enterprise-first) will drive rapid innovation.
-->

---
layout: default
---

# Major Product Releases Timeline

<div class="mb-4 p-3 bg-blue-50 rounded-lg border border-blue-200">
<strong class="text-blue-800">September 2025: A Watershed Month</strong>
</div>

<div class="grid grid-cols-2 gap-8">

<div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">September 2025 Developments</h4>

<div class="space-y-3 text-sm">
<div>
<strong class="text-blue-600">GPT-5-Codex</strong> (Sept 15):
<ul class="mt-1 space-y-1 ml-4">
<li>• First coding-specific GPT-5 variant</li>
<li>• Dynamic thinking time (up to 7 hours)</li>
<li>• 51.3% on refactoring evals vs 33.9% for GPT-5</li>
<li>• Integrated code review workflows</li>
</ul>
</div>

<div>
<strong class="text-blue-600">GitHub Copilot CLI</strong> (Sept 25):
<ul class="mt-1 space-y-1 ml-4">
<li>• Public preview with GitHub Models</li>
<li>• Defaults to Claude Sonnet 4, supports GPT-5</li>
<li>• Shared billing with existing Copilot plans</li>
</ul>
</div>

<div>
<strong class="text-blue-600">Cross-Agent Security Research</strong> (Sept 24):
<ul class="mt-1 space-y-1 ml-4">
<li>• Johann Rehberger's privilege escalation findings</li>
<li>• Industry wake-up call for container isolation</li>
</ul>
</div>
</div>
</div>

</div>

<div>

<div class="bg-blue-50 p-4 rounded border border-blue-200">
<h4 class="font-semibold text-blue-700 mb-3">Key Trends Emerging</h4>

<v-clicks>

<div class="space-y-3 text-sm">
<div>
<strong>1. Model Specialization:</strong>
<ul class="mt-1 space-y-1 ml-4">
<li>• Coding-specific fine-tuning becoming standard</li>
<li>• Task-specific thinking budgets</li>
</ul>
</div>

<div>
<strong>2. Platform Convergence:</strong>
<ul class="mt-1 space-y-1 ml-4">
<li>• Multiple model backends in single tools</li>
<li>• Cross-platform agent workflows</li>
</ul>
</div>

<div>
<strong>3. Security Maturation:</strong>
<ul class="mt-1 space-y-1 ml-4">
<li>• Real incidents driving better practices</li>
<li>• Industry-wide security standards emerging</li>
</ul>
</div>
</div>

</v-clicks>

<div class="mt-4 bg-yellow-100 p-2 rounded text-sm">
<strong>Market Insight:</strong> The rapid release cycle indicates this field is still in the "land grab" phase, with major players competing for developer mindshare.
</div>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
<strong class="text-blue-800">Strategic Takeaway:</strong> For researchers and practitioners, this rapid evolution means staying current is essential. What's state-of-the-art today may be obsolete in six months.
</div>

<!--
September 2025 was a watershed month that perfectly illustrates how fast this field is moving. Three major developments in 10 days shows the pace of innovation.

The convergence trends are particularly important - the field is moving toward multi-model, multi-platform systems rather than single-vendor solutions.
-->

---
layout: default
---

# Discussion Questions

<div class="grid grid-cols-2 gap-8">

<div class="bg-purple-50 p-6 rounded-lg border border-purple-200">
<h3 class="font-bold text-purple-600 mb-4">🤔 For Researchers</h3>

<v-clicks>

<div class="space-y-3 text-sm">
<div>
<strong>1. Evaluation:</strong> How do we create benchmarks that predict real-world agent success?
</div>

<div>
<strong>2. Multi-Agent Coordination:</strong> What are the fundamental limits of agent collaboration?
</div>

<div>
<strong>3. Alignment:</strong> Can we prove alignment properties for agent-generated code?
</div>

<div>
<strong>4. Capability Control:</strong> How do we give agents just enough power to be useful but not dangerous?
</div>
</div>

</v-clicks>

</div>

<div class="bg-blue-50 p-6 rounded-lg border border-blue-200">
<h3 class="font-bold text-blue-600 mb-4">🛠️ For Practitioners</h3>

<v-clicks>

<div class="space-y-3 text-sm">
<div>
<strong>1. Adoption Strategy:</strong> Which agent should you integrate into your workflow first?
</div>

<div>
<strong>2. Task Selection:</strong> How do you identify which tasks to automate vs keep human?
</div>

<div>
<strong>3. Security Posture:</strong> What security practices are essential when using coding agents?
</div>

<div>
<strong>4. ROI Measurement:</strong> How do you measure the true productivity impact of agents?
</div>
</div>

</v-clicks>

</div>

</div>

<div class="mt-8 p-6 bg-gradient-to-r from-purple-50 to-blue-50 rounded-lg border">
<strong class="text-purple-800">Meta-Question:</strong> Are we building the future we want? How do we ensure that increasingly capable agents serve human flourishing rather than replace human agency?
</div>

<!--
These discussion questions are designed to bridge the gap between the research insights and practical applications we've covered.

The meta-question is perhaps the most important - as we build increasingly sophisticated agent systems, we need to consciously design them to augment rather than replace human capability and creativity.
-->

---
layout: default
---

# References & Further Reading

<div class="grid grid-cols-2 gap-6 text-sm">

<div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">📖 Foundational Papers</h4>
<ul class="space-y-2">
<li>• <strong>METR:</strong> "Measuring AI Ability to Complete Long Tasks" (2024)</li>
<li>• <strong>SWE-bench:</strong> "Can Language Models Resolve Real-World GitHub Issues?" (2024)</li>
<li>• <strong>Sleeper Agents:</strong> "Training Deceptive LLMs" (2024)</li>
</ul>
</div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">🔬 AI Safety Research</h4>
<ul class="space-y-2">
<li>• <strong>Among Us:</strong> "A Sandbox for Agentic Deception" (2024)</li>
<li>• <strong>AI Agents and Painted Facades</strong> (2024)</li>
</ul>
</div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">🏗️ System Architecture</h4>
<ul class="space-y-2">
<li>• <strong>Basic Systems Architecture for AI Agents</strong> (2024)</li>
</ul>
</div>

</div>

<div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">🏭 Industry Analysis</h4>
<ul class="space-y-2">
<li>• <strong>AI 2027:</strong> "Forecasting Superhuman Coders" (LessWrong, 2024)</li>
<li>• <strong>Claude Code Deep Dive:</strong> MinusX analysis (2025)</li>
<li>• <strong>GPT-5-Codex Analysis:</strong> Simon Willison's blog (Sept 2025)</li>
<li>• <strong>Cross-Agent Security Research:</strong> Johann Rehberger (Sept 2025)</li>
<li>• <strong>Amazon Q Security Advisory:</strong> CVE-2025-8217</li>
</ul>
</div>

<div class="bg-gray-50 p-4 rounded border">
<h4 class="font-semibold mb-3">📊 Benchmarks & Evaluation</h4>
<ul class="space-y-2">
<li>• <strong>SWE-bench Pro, SWE-bench-Live</strong></li>
<li>• <strong>LiveCodeBench, RepoQA</strong></li>
<li>• <strong>SWE-bench Critiques:</strong> "Illusion" and "UTBoost" papers</li>
</ul>
</div>

<div class="bg-blue-50 p-4 rounded border border-blue-200">
<h4 class="font-semibold text-blue-700 mb-3">🌐 Essential Resources</h4>
<ul class="space-y-2">
<li>• <strong>Simon Willison's Blog:</strong> AI-assisted programming tag</li>
<li>• <strong>swyx's AI Engineering Guide</strong></li>
<li>• <strong>Hacker News:</strong> Search "coding agents"</li>
<li>• <strong>r/MachineLearning:</strong> Academic discussions</li>
<li>• <strong>AI Engineering Communities:</strong> Real-time insights</li>
</ul>
</div>

</div>

</div>

<div class="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200 text-center">
<strong class="text-blue-800">Stay Current:</strong> This field evolves daily. Follow security researchers, read vendor blogs, and test new releases carefully.
</div>

---
layout: default
---

# From Stumbling to Superhuman: The 2027 Checklist

<div class="mb-6 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg border">
<strong class="text-blue-800">To bridge the capability gap from today's "stumbling agents" to reliable "superhuman teammates," we need:</strong>
</div>

<v-clicks>

<div class="grid grid-cols-2 gap-6">

<div class="space-y-4">
<div class="flex items-start space-x-3">
<span class="text-2xl">1️⃣</span>
<div>
<strong class="text-blue-600">Robust Planning</strong>
<p class="text-sm mt-1">Move from linear scripts to partial-order plans with backtracking capabilities</p>
</div>
</div>

<div class="flex items-start space-x-3">
<span class="text-2xl">2️⃣</span>
<div>
<strong class="text-blue-600">Verified Edits</strong>
<p class="text-sm mt-1">Property checks, automated test synthesis, and formal verification of agent actions</p>
</div>
</div>

<div class="flex items-start space-x-3">
<span class="text-2xl">3️⃣</span>
<div>
<strong class="text-blue-600">Secure Observability</strong>
<p class="text-sm mt-1">Signed traces with replay guarantees and full audit capabilities</p>
</div>
</div>
</div>

<div class="space-y-4">
<div class="flex items-start space-x-3">
<span class="text-2xl">4️⃣</span>
<div>
<strong class="text-blue-600">Intelligent Memory</strong>
<p class="text-sm mt-1">Work diaries and persistent learning, not just conversation dumps</p>
</div>
</div>

<div class="flex items-start space-x-3">
<span class="text-2xl">5️⃣</span>
<div>
<strong class="text-blue-600">Adaptive Model Routing</strong>
<p class="text-sm mt-1">Smart selection between fast and intelligent models based on task complexity</p>
</div>
</div>

<div class="flex items-start space-x-3">
<span class="text-2xl">6️⃣</span>
<div>
<strong class="text-blue-600">Multi-Agent Coordination</strong>
<p class="text-sm mt-1">Specialized teams with shared context and verified handoffs</p>
</div>
</div>
</div>

</div>

</v-clicks>

<div class="mt-8 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg border">
<strong class="text-blue-800">The Path Forward:</strong> Co-design the LLM "brain" with the entire agentic scaffold - success comes from the system, not just the model
</div>

---
layout: default
---

# Call to Action

<div class="grid grid-cols-2 gap-8">

<div class="bg-blue-50 p-6 rounded-lg border border-blue-200">
<h3 class="font-bold text-blue-600 mb-4">For Practitioners</h3>
<ul class="space-y-2 text-sm">
<li>• Pick one local agent, one cloud agent</li>
<li>• Instrument traces and ship evaluations</li>
<li>• Start a policy file and enforce it</li>
<li>• Contribute to MCP servers and tool ecosystems</li>
</ul>

<div class="mt-4 pt-4 border-t border-blue-200">
<h4 class="font-semibold text-blue-700 mb-2">For Researchers</h4>
<ul class="space-y-2 text-sm">
<li>• Focus on trace-level evaluation methodologies</li>
<li>• Study agent failure modes systematically</li>
<li>• Build better verification primitives</li>
<li>• Design multi-agent coordination protocols</li>
</ul>
</div>
</div>

<div class="bg-purple-50 p-6 rounded-lg border border-purple-200">
<h3 class="font-bold text-purple-600 mb-4">Key Insights to Remember</h3>

<div class="space-y-4 text-sm">
<blockquote class="bg-white p-3 rounded border-l-4 border-purple-300 italic">
"Long context helps you read more. Tests help you know."
</blockquote>

<blockquote class="bg-white p-3 rounded border-l-4 border-purple-300 italic">
"Fast models are great at being many. Smart models are great at being right."
</blockquote>

<blockquote class="bg-white p-3 rounded border-l-4 border-purple-300 italic">
"If you cannot replay the trace, you cannot trust the change."
</blockquote>

<blockquote class="bg-white p-3 rounded border-l-4 border-purple-300 italic">
"Benchmarks measure outputs. Production measures verified diffs."
</blockquote>
</div>
</div>

</div>

---
layout: end
---

# Thank You

<div class="text-center">
<h2 class="text-3xl font-bold mb-8">Questions & Discussion</h2>

<div class="text-6xl mb-6">🤖</div>
<div class="text-2xl mb-8 text-gray-700">From snippets to swarms: the future is agentic</div>

<div class="grid grid-cols-3 gap-8 max-w-4xl mx-auto">
<div class="bg-blue-50 p-4 rounded-lg border border-blue-200">
<div class="font-bold text-blue-600 mb-2">Try Today</div>
<div class="text-sm space-y-1">
<div>Claude Code, Gemini CLI</div>
<div>Cursor, GitHub Copilot</div>
</div>
</div>

<div class="bg-green-50 p-4 rounded-lg border border-green-200">
<div class="font-bold text-green-600 mb-2">Research</div>
<div class="text-sm space-y-1">
<div>SWE-bench, HumanEval</div>
<div>Multi-agent coordination</div>
</div>
</div>

<div class="bg-purple-50 p-4 rounded-lg border border-purple-200">
<div class="font-bold text-purple-600 mb-2">Build</div>
<div class="text-sm space-y-1">
<div>MCP servers</div>
<div>Trace evaluation tools</div>
</div>
</div>
</div>

<div class="mt-12 text-gray-600">
<div>Engineering AI Research Group (EAIRG)</div>
<div>September 27, 2025</div>
</div>
</div>

<!--
We've traced the complete evolution from simple autocomplete to sophisticated agent systems, explored the current challenges with "stumbling agents," and outlined the path toward reliable, parallel agent systems.

Key insights:
1. Evolution required tool use + verification + context, not just bigger models
2. Speed vs intelligence tradeoffs create natural routing strategies
3. The future is many competent agents, not one perfect agent
4. Success comes from the entire agentic scaffold, not just the LLM
5. We're building the foundation for AGI through coding agent research

This is a critical moment - the decisions we make about agent architecture, safety, and evaluation will shape the future of human-AI collaboration.
-->