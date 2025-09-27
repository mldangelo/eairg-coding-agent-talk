# AI Coding Agents Research Topics

## Key Research Areas for Engineering AI Research Group

• **Verifiable Reward Engineering** - Developing crisp, binary feedback mechanisms for code generation tasks beyond compile/test/lint to include performance, security, and maintainability metrics

• **Manager-Worker Agent Architectures** - Optimizing the allocation between fast models (high throughput, simple tasks) and smart models (complex reasoning, coordination) for wall-clock time efficiency

• **Trace-Level Evaluation Systems** - Building evaluation frameworks that score plans, tool chains, and intermediate steps rather than just final outputs, with emphasis on penalizing silent failures

• **Adaptive Planning and Backtracking** - Creating agents that can dynamically revise plans, backtrack from failures, and generate partial-order execution strategies instead of linear scripts

• **Unified Action Schema Standards** - Developing vendor-neutral JSON schemas for tool calls, results, diffs, and test outcomes to enable cross-platform agent interoperability

• **Capability Token Security Models** - Implementing fine-grained permission systems that scope secrets and API access per tool, per task, with automatic expiration and audit trails

• **Policy Synthesis and Human-in-the-Loop** - Enabling agents to propose minimum permission allowlists for tasks while requiring human approval for security-sensitive operations

• **Agentic Benchmark Extensions** - Enhancing evaluation frameworks like SWE-bench with shell access, edit verification, and real-world deployment constraints

• **Reward Hacking Detection and Mitigation** - Developing mutation testing, property-based checks, and hidden holdout tests to prevent agents from gaming evaluation metrics

• **Red-Team Agent Architectures** - Building specialized agents focused on prompt injection attacks against tool schemas and discovering reward hacking exploits

• **Synthetic Data Generation for Code Training** - Leveraging massive compute budgets to generate high-quality training data for code agents using verification loops

• **Replayable Trace Infrastructure** - Creating persistent logging systems for tool calls, diffs, and verification results that enable deterministic replay and audit of agent decisions