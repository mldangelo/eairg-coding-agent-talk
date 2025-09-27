# A Technical Survey of Modern Coding Agents

### Course Module: 1

### Audience: Advanced Software Engineers, AI/ML Practitioners

---

## Chapter 1: From Chatbots to Agents: A Paradigm Shift

For years, the primary interface for interacting with Large Language Models (LLMs) has been conversational chat. However, a new paradigm has emerged: the **agentic model**. A coding agent is not merely a passive respondent; it is an active participant in the development lifecycle.

**Definition:** A coding agent is an LLM-powered system that can autonomously or semi-autonomously understand high-level goals, create and reason through multi-step plans, and execute actions using a predefined set of tools to interact with a software development environment.

The fundamental process that governs these agents is the **agentic loop**. While implementations vary, the core stages are universal:

1.  **Observe:** Gather state and context from the environment (user prompt, file contents, tool outputs).
2.  **Orient/Think:** Analyze the context, consult internal instructions (the system prompt), and formulate a plan.
3.  **Decide:** Select a specific action or tool to execute from the plan.
4.  **Act:** Execute the chosen action (e.g., call an API, run a command).

The loop repeats, feeding the result of the _Act_ phase back into the _Observe_ phase, until the high-level goal is achieved.

---

## Chapter 2: The Anatomy of a Modern Coding Agent

To understand the landscape, we must first dissect the components that constitute a typical agent. We will use Gemini CLI and Claude Code as our reference implementations.

```mermaid
graph TD
    subgraph Agent Core
        A[Component 1: The Brain (LLM)];
        B[Component 3: The Orchestrator];
        C[Component 5: The Memory];
    end

    subgraph Environment Interface
        D[Component 2: The Senses (Context Gathering)];
        E[Component 4: The Hands (Toolset)];
        F[Component 6: The Guardian (Security)];
    end

    A <--> B;
    B <--> C;
    B --> E;
    D --> B;
    F -- Mediates --> E;
```

### **Component 1: The "Brain" - The Large Language Model (LLM)**

This is the reasoning engine. Its quality determines the agent's ability to plan, reason, and correctly use tools.

- **Key Capabilities:**
  - **Instruction Following:** The ability to adhere to the complex rules laid out in the system prompt.
  - **Function Calling / Tool Use:** The model must be specifically fine-tuned to reliably output structured data (e.g., JSON) for invoking tools.
  - **Reasoning & Planning:** The capacity to break down a complex task like "refactor this module" into a logical sequence of tool calls.
  - **Large Context Window:** Essential for providing the model with sufficient context (code files, API definitions, conversation history).
- **Examples:** Google's Gemini family, Anthropic's Claude family.

### **Component 2: The "Senses" - Context Gathering**

An agent is only as good as its understanding of the environment. This component is responsible for feeding the LLM the right information.

- **Techniques:**
  - **Explicit User Input:** The user's prompt, including `@-mentioned` files.
  - **Automated Environment Scanning:** Reading key files on startup (`.git` to find the project root, `package.json` for dependencies, `GEMINI.md` or `CLAUDE.md` for project-specific instructions).
  - **Tool-Based Sensing:** Using its own tools (`list_directory`, `search_file_content`) to actively explore the environment in response to a prompt.
  - **IDE Integration:** A key differentiator for some agents. Accessing the IDE's state provides high-fidelity context like cursor position, selected text, and open files (as seen in Gemini CLI's VS Code companion).

### **Component 3: The "Orchestrator" - The Agentic Loop Runner**

This is the core software that drives the agent.

- **Responsibilities:**
  - Assembling the full prompt (System Prompt + User Prompt + Context).
  - Making the API call to the LLM.
  - Parsing the LLM's response, distinguishing between text output and tool calls.
  - Dispatching tool calls to the appropriate execution logic.
  - Managing the conversation state and history.
- **Architectural Example (Gemini CLI):** The logic is split between `packages/cli` (which handles the UI loop) and `packages/core` (which contains the `GeminiClient` that manages the interaction with the API and tools).

### **Component 4: The "Hands" - The Toolset & Actuators**

Tools are how the agent affects the world. A robust and well-designed toolset is critical.

- **Tool Categories:**
  - **Filesystem (Read):** `read_file`, `list_directory`, `glob`, `search_file_content`
  - **Filesystem (Write):** `write_file`, `replace`
  - **Code Execution:** `run_shell_command`
  - **External Knowledge:** `google_web_search`, `web_fetch`
  - **Internal State:** `save_memory`, `list_todos`
- **Implementation:** Each tool has a schema (often JSON Schema) that is provided to the LLM in the system prompt. The agent's orchestrator uses this schema to validate tool calls from the model before execution.

### **Component 5: The "Memory" - State & History Management**

An agent must remember the past to inform the future.

- **Short-Term Memory:** The full transcript of the current session, including all prompts, responses, and tool call/result pairs. This is passed to the LLM with every turn.
- **The Compaction Problem:** As the conversation grows, the history exceeds the LLM's context window. Agents solve this with a **summarization strategy**. Gemini CLI's `client.ts` contains logic to use the LLM to summarize the beginning of a long conversation, replacing many old messages with a single summary message.
- **Long-Term Memory:**
  - **Project-Specific:** `GEMINI.md` or `CLAUDE.md` files act as a persistent "memory" for a specific workspace.
  - **User-Specific:** A mechanism (e.g., `/memory` command) to store user preferences or facts across sessions.

### **Component 6: The "Guardian" - Security & Sandboxing**

This is arguably the most important component for user trust and safety.

- **Techniques:**
  - **Permission Models:** The orchestrator intercepts "dangerous" tool calls (`write_file`, `run_shell_command`) and requires explicit user confirmation before execution.
  - **Sandboxing:** Executing shell commands within a container (Docker/Podman) to isolate them from the host filesystem and network. Both Gemini CLI and Claude Code support this.
  - **Network Policy:** Using container firewalls (like `iptables` in Claude Code's devcontainer) to restrict which domains the agent can contact.
  - **Static Analysis:** Pre-parsing shell commands to block known dangerous patterns (e.g., `rm -rf /`).

---

## Chapter 3: Architectural Patterns & Ecosystem Survey

Coding agents are not a monolith. They exist in several distinct architectural patterns.

| Category                       | Primary Environment      | Key Characteristics                                                                                                | Examples                                           |
| :----------------------------- | :----------------------- | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| **Integrated Terminal Agents** | Your Local Terminal      | Self-contained, manages its own agentic loop, deep filesystem/shell integration.                                   | **Gemini CLI**, **Claude Code**, Aider, Mentat     |
| **IDE-Integrated Agents**      | Your IDE (e.g., VS Code) | Access to rich IDE context (AST, diagnostics, cursor), UI-driven, often acts on selected code blocks.              | GitHub Copilot, Cursor                             |
| **Agent Frameworks (SDKs)**    | Your Application Code    | **Not end-user tools.** Libraries for _building_ other agents. Provide abstractions for tools, memory, and chains. | LangChain, LlamaIndex, CrewAI                      |
| **Cloud-Native Agents**        | Remote Cloud Environment | Often have their own sandboxed browser/shell. May not have direct local file access. Good for web-based tasks.     | Devin (as reported), various web automation agents |

---

## Chapter 4: Future Directions & Open Problems

The field of coding agents is evolving rapidly. The next generation of tools will need to solve several key challenges:

1.  **Advanced Planning & Reasoning:** Moving from sequential tool use to complex, graph-based plans where the agent can evaluate multiple paths and backtrack.

2.  **Self-Improvement & Meta-Cognition:** Can an agent analyze its own failures and modify its internal system prompt or tool definitions to improve its performance over time?

3.  **The UX of Agency:** How do we build user interfaces that can effectively display and manage complex, long-running, asynchronous agentic tasks without overwhelming the user? The simple request-response model of a chat window is insufficient.

4.  **Multi-Agent Collaboration:** The concept of specialized agents (e.g., a "Database Agent," a "Frontend Agent," a "Testing Agent") collaborating on a single repository. This requires robust protocols for inter-agent communication and shared state management.

5.  **The "Last Mile" Problem:** While agents are excellent at scaffolding and routine tasks, they often struggle with the final, nuanced details required for production-ready code. Bridging this gap is the ultimate challenge.
