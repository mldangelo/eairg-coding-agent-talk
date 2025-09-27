---
layout: cover
---

# Deconstructing the Modern AI Coding Agent

### A Technical Survey for the Engineering AI Research Group (EAIRG)

<div class="pt-12">
  <span class="px-2 py-1 rounded">Saturday, September 27, 2025</span>
</div>

<!--
Welcome, everyone. Thank you for coming. Today, we're going to take a deep, technical dive into the world of AI coding agents.

We'll move beyond the hype and dissect how these tools actually work, what their core components are, and where this technology is headed. My goal is for you to leave with a solid framework for understanding and evaluating any coding agent you encounter.
-->

---

## layout: default

# Agenda

1.  **The Paradigm Shift:** From Chatbots to Tool-Using Agents.
2.  **Anatomy of an Agent:** A look under the hood at the core components.
3.  **Architectural Deep Dive:** Comparing Gemini CLI and Claude Code.
4.  **The "AI 2027" Lens:** Contextualizing today's agents in a future timeline.
5.  **The Evolving Role of the Human Developer.**
6.  **Future Directions & Open Problems.**

<!--
Here's our roadmap for the talk. We'll start with the foundational concepts, move into a detailed breakdown of the architecture, look at some real-world examples, place them in a future context, and then discuss what it all means for us as engineers.
-->

---

## layout: section

# 1. The Paradigm Shift

From Conversational AI to Agentic Systems

<!--
Let's begin by defining what we're even talking about. The leap from a simple chatbot to an agent is a significant one.
-->

---

## layout: default

# Beyond Chat

For years, our interaction with LLMs has been primarily conversational. We are now in a new paradigm: **the agentic model**.

**A coding agent is not a passive respondent; it is an active participant in the development lifecycle.**

It can:

- Understand high-level goals.
- Create and reason through multi-step plans.
- Execute actions using a predefined set of tools.

<br>

The fundamental process is the **Agentic Loop**.

<!--
A standard chatbot is stateless and can't *do* anything. An agent, on the other hand, has goals, tools, and the ability to act. This is the key distinction. It's not just about generating text; it's about taking action to achieve a goal.
-->

---

## layout: default

# The Agentic Loop

The core cycle that governs all modern coding agents.

```mermaid
graph TD
    A(Observe) --> B(Orient / Think);
    B --> C(Decide);
    C --> D(Act);
    D -- Feedback --> A;

    subgraph Environment
        direction LR
        Prompt
        Files
        Tool Outputs
    end

    subgraph Agent
        direction LR
        A
        B
        C
        D
    end

    Environment -- Input --> A
    D -- Output --> Environment
```

<!--
This is the most important conceptual slide of the talk. I want you to walk through each step.
1. **Observe:** The agent gathers information. This is the user's prompt, but also file contents, the output from a previous tool, etc.
2. **Orient/Think:** The agent processes this information against its core instructions—the system prompt—and formulates a plan.
3. **Decide:** It selects a concrete action from that plan, like 'I will use the read_file tool on app.py'.
4. **Act:** It executes the tool.
Crucially, the result of the 'Act' phase—success, failure, or data—is fed directly back into the next 'Observe' phase. This feedback mechanism is what makes it a true loop and allows the agent to perform complex, multi-step tasks.
-->

---

## layout: section

# 2. Anatomy of an Agent

The Core Components

<!--
So, how do you build a system that can execute this loop? Let's break it down into a functional anatomy. We can think of any agent as being composed of these six conceptual parts.
-->

---

## layout: default

# The Six Core Components

We can dissect any modern agent into six conceptual components.

```mermaid
graph TD
    subgraph Agent Core
        A[1. The Brain (LLM)];
        B[3. The Orchestrator];
        C[5. The Memory];
    end

    subgraph Environment Interface
        D[2. The Senses (Context)];
        E[4. The Hands (Tools)];
        F[6. The Guardian (Security)];
    end

    A <--> B;
    B <--> C;
    B --> E;
    D --> B;
    F -- Mediates --> E;
```

<!--
This diagram provides a mental model. The 'Agent Core' is the internal processing, while the 'Environment Interface' is how it interacts with the outside world—your computer. We'll go through each of these in more detail.
-->

---

## layout: two-cols

# The Agent's Mind

**1. The Brain (LLM)**

- The central reasoning and planning engine (e.g., Gemini, Claude).
- Success depends on its instruction-following, tool-use fine-tuning, and reasoning capabilities.

**3. The Orchestrator**

- The software that runs the agentic loop.
- Assembles prompts, parses LLM output, dispatches tool calls, and manages state.
- _Example: Gemini CLI's `packages/core/src/core/client.ts`_

**5. The Memory**

- **Short-Term:** The conversation transcript.
- **Long-Term:** Vector DBs or summary files.
- **The Compaction Problem:** Solved by using the LLM to summarize early parts of a long conversation to fit within the context window.

::right::

# The Agent's Body

**2. The Senses (Context Gathering)**

- How the agent perceives its environment.
- Reads user prompts, `@-mentioned` files, and workspace files (`package.json`, `GEMINI.md`).

**4. The Hands (The Toolset)**

- How the agent acts upon the world.
- **Read-only tools:** `read_file`, `glob`, `web_search`
- **Mutative tools:** `replace`, `write_file`, `run_shell_command`

**6. The Guardian (Security)**

- The critical safety layer.
- Implements permission models, command validation, and sandboxing (Docker/Podman).

<!--
Here we break down the six components. For the 'Mind', emphasize that the Orchestrator is the actual code that *runs* the agent, while the LLM is the reasoning engine it calls. For 'Memory', the key technical challenge is the finite context window, which necessitates a compaction or summarization strategy.

For the 'Body', explain that the 'Senses' are about getting information *into* the prompt, and the 'Hands' are about taking action *based on* the prompt. The 'Guardian' is the crucial layer that sits between the agent's decision and the actual execution, preventing it from doing something dangerous without user consent.
-->

---

## layout: section

# 3. Architectural Deep Dive

Case Studies: Gemini CLI vs. Claude Code

<!--
Now let's make this concrete by looking at two real-world examples. We'll see how their different engineering choices reflect different priorities.
-->

---

## layout: two-cols

# Gemini CLI

- **Tech Stack:** TypeScript / Node.js Monorepo.
- **UI Framework:** **React / Ink**. A declarative, component-based UI running in the terminal.
- **Key Feature:** **Dual-Mode Architecture**.
  - **Interactive Mode:** A rich, stateful UI for conversational use.
  - **Non-Interactive Mode:** A streamlined flow for scripting and CI/CD (`gemini -p "..."`).
- **Extensibility:** Formal system via **MCP (Model Context Protocol)** and Extensions, designed for team-wide sharing and governance.

::right::

# Claude Code

- **Tech Stack:** Polyglot environment, with a heavy emphasis on a secure, containerized development process via **Devcontainers**.
- **UI Framework:** Appears to be a custom, highly-optimized text renderer.
- **Key Feature:** **Simplicity and Security**.
  - The entire development environment is defined and secured in the repository.
- **Extensibility:** Direct and simple.
  - **Markdown-defined slash commands** for prompts.
  - **Script-based hooks** for validation and automation.

<!--
This is the core comparison. For Gemini CLI, the keywords are 'TypeScript', 'React/Ink', 'Dual-Mode', and 'MCP'. This paints a picture of a scalable, versatile platform.

For Claude Code, the keywords are 'Devcontainer', 'Security', and 'Simple Extensibility' (scripts/Markdown). This paints a picture of a tool that prioritizes safety and individual developer empowerment.
-->

---

## layout: default

# Architectural Tradeoffs

| Feature           | Gemini CLI                                                                            | Claude Code                                                                         |
| :---------------- | :------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------- |
| **Architecture**  | **TypeScript Monorepo**<br>Scalable, maintainable, large ecosystem.                   | **Secure Devcontainer**<br>Highly secure, reproducible, more setup complexity.      |
| **UI**            | **React / Ink**<br>Rich, complex UIs are easier to build.                             | **Custom Renderer**<br>Potentially faster, dependency-free, harder to evolve.       |
| **Extensibility** | **Formal (MCP/Extensions)**<br>Powerful, scalable for teams, higher learning curve.   | **Informal (Scripts/Markdown)**<br>Extremely easy for individuals, less structured. |
| **Versatility**   | **Dual-Mode (Interactive/Scripting)**<br>Excellent for both human use and automation. | **Primarily Interactive**<br>Optimized for conversational development.              |

**Conclusion:** Gemini CLI is architected like a scalable, enterprise-ready platform. Claude Code is architected with a focus on ultimate security and developer-centric, rapid customization.

<!--
This slide summarizes the previous one. Don't just read the table. Explain the 'why'. For example, 'Gemini's choice of a formal MCP system for extensions makes it ideal for a large company that needs to govern and share tools, but it's more complex than Claude Code's approach of just dropping a script into a folder, which is faster for a single developer.' The conclusion at the bottom is the key takeaway.
-->

---

## layout: section

# 4. The "AI 2027" Lens

Contextualizing Today's Agents in a Speculative Future

<!--
Now let's zoom out. We've seen how these agents work today. Let's use a speculative article, 'AI 2027', as a lens to think about where this is all going.
-->

---

## layout: default

# Where We Are Today

The "AI 2027" scenario describes the state of agents in mid-2025. **This is an accurate description of today.**

> **"The agents are impressive in theory... but in practice unreliable. AI twitter is full of stories about tasks bungled in some particularly hilarious way."**

This is our current reality. The unreliability stems from potential failures at any point in the agentic loop: misinterpreting the prompt, lacking context, or using a tool incorrectly.

> **"Agent-1 is a scatterbrained employee who thrives under careful management."**

This perfectly defines the current human-agent interaction model. The human is the "manager" or "tech lead."

<!--
This is a powerful point to make. The future described in the article is, in many ways, already here. The 'Stumbling Agents' are not a future prediction; they are the tools we are using right now. This grounds the rest of the discussion in reality. Emphasize that the 'scatterbrained employee' analogy is perfect—it highlights both the power and the need for human oversight.
-->

---

## layout: default

# The Alignment Problem in Practice

The scenario highlights that "alignment" is not just an esoteric, long-term problem. It manifests as practical, near-term engineering challenges we already face.

- **Sycophancy:** The agent agrees with a flawed premise in your prompt rather than correcting you. It optimizes for agreeableness.

- **Hiding Failures:** An agent's `replace` tool call might fail silently. Without a verification step (like running a test), the agent may proceed as if the change succeeded, creating a divergence between its internal state and the real world.

- **The Core Issue:** The LLM is optimized to produce a _plausible-looking response_ or _syntactically correct tool call_, not to achieve _actual task success_. The entire agentic scaffold is built to bridge this critical gap.

<!--
This is a key insight for a technical audience. Alignment isn't just about rogue AI. It's about the everyday frustrations of using these tools. The 'Hiding Failures' point is a great example. The agent isn't being malicious; its training objective was just to output a valid tool call, and it did. It wasn't rewarded for *verifying* the outcome. This is why the self-correction loop, where an agent runs tests on its own code, is so important.
-->

---

## layout: section

# 5. The Evolving Role of the Human Developer

<!--
So what does this all mean for us, the engineers in the room? Our jobs aren't going away, but they are changing.
-->

---

## layout: default

# From Coder to "Agent Manager"

The most effective users of coding agents are not just writing prompts. They are internalizing the agentic loop and managing it like a system.

**The new critical skills are:**

1.  **Task Decomposition:** Breaking down high-level features into a sequence of agent-sized tasks.

2.  **Context Scaffolding:** Knowing exactly what information the agent needs to succeed and providing it efficiently.

3.  **Execution Supervision & Debugging:** Acting as the final quality gate for code changes and diagnosing _why_ an agent is failing, not just that it failed.

4.  **Systems Architecture:** Focusing on high-level design, component boundaries, and data flow, while delegating implementation boilerplate to the agent.

<!--
This slide is the call to action for the audience. Our value is moving up the abstraction ladder. We are moving from writing lines of code to designing systems and managing the AI agents that implement them. Emphasize that these are all skills that senior engineers and architects already have. This isn't a totally alien skill set; it's an evolution of our existing expertise.
-->

---

## layout: section

# 6. Future Directions & Open Problems

<!--
Finally, let's look at what's next. The path from today's 'Stumbling Agents' to the truly autonomous agents of the future is paved with fascinating engineering challenges.
-->

---

## layout: default

# The Road Ahead

The path from today's "Stumbling Agents" to the "Superhuman Coders" of the 2027 scenario requires solving several major challenges:

- **Advanced Planning:** Moving from linear tool use to complex, graph-based plans where the agent can evaluate multiple strategies and backtrack from failures.

- **Self-Improvement:** Creating agents that can analyze their own errors and permanently update their internal instructions or tool usage patterns.

- **The UX of Agency:** Designing interfaces that can manage long-running, asynchronous tasks and clearly visualize an agent's complex plan and execution status.

- **Multi-Agent Collaboration:** Developing protocols for specialized agents (e.g., a "Testing Agent" and a "Security Agent") to collaborate on a single codebase.

<!--
Briefly touch on each of these. For a technical audience, 'Advanced Planning' (e.g., graph-based planning vs. simple chains) and 'Multi-Agent Collaboration' (e.g., defining communication protocols) will be particularly interesting. The 'UX of Agency' is also a great point—a simple chat interface is not enough to manage a team of AIs working for hours on a complex task.
-->

---

layout: center
class: "text-center"

---

# Thank You

### Q&A

<!--
And that's the talk. Thank you.
-->
