---
theme: default
colorSchema: light
layout: cover
highlighter: shiki
lineNumbers: false
title: AI Coding Agents — 5‑Minute Briefing
info: |
  A concise, pragmatic walkthrough of coding agents: what changed, what works, how to ship safely.
  Engineering AI Research Group (EAIRG) — Sept 27, 2025
transition: slide-left
mdc: true
fonts:
  sans: Inter
  serif: Inter
  mono: "Fira Code"
canvasWidth: 1280
aspectRatio: 16/9
class: text-center
---

# AI Coding Agents

## 5‑Minute Briefing

### From Snippets to Shipping

_EAIRG • Sept 27, 2025_

<div class="pt-8">
  <span @click="$slidev.nav.next" class="px-4 py-2 rounded cursor-pointer hover:bg-blue-50 text-blue-600 border border-blue-200">
    Press Space for next page →
  </span>
</div>

<!--
Goal: deliver the minimum set of concepts to evaluate, deploy, and govern coding agents in production.
Pace: ~30–40s per slide. Keep commentary crisp and actionable.
-->

---

## layout: default

# Why Now: The Leap to Repo-Scale

<v-clicks>

- Bigger models alone didn’t do it. The leap came from:
- Tool use — agents act via shell/editor/CLI with typed tools
- Verification loops — tests, linters, and policy gates close the loop
- Massive context — enough to reason across repos, not just files

</v-clicks>

<div class="mt-4 p-3 bg-blue-50 rounded border border-blue-200 text-sm">
Key shift: from single-shot completions to iterative perception–action–verification.
</div>

<!--
Anchor the audience: capability jumps track addition of tools, verification, and long context. Sets expectations.
-->

---

## layout: default

# Minimal Viable Agent Loop

<v-clicks>

- Planner — decomposes issue → steps + acceptance checks
- Actor — edits files, runs tests, captures artifacts
- Verifier — policy checks, SAST/secret scan, hidden tests
- Iterate until checks pass or budget is exhausted

</v-clicks>

<div class="mt-4 text-xs text-gray-600">
Tip: keep loops short; prioritize actions that increase verifiability per step.
</div>

<!--
Emphasize that the loop is simple by design; reliability comes from safeguards and verification, not long chains of thought alone.
-->

---

## layout: default

# Production Architecture (5 Components)

<v-clicks>

1. Planner — step plan + acceptance tests
2. Actor — repo edits, test runs, artifact capture
3. Verifier — policy engine, SAST, secrets, hidden tests
4. Repo Memory — symbol graph, embeddings, change history
5. Safety Guard — file allowlists, code-owner approvals

</v-clicks>

<div class="mt-4 p-3 bg-amber-50 rounded border border-amber-200 text-xs">
Engineering priorities: typed tool schemas, structured errors, JSONL traces, replay, cost-aware scheduling.
</div>

<!--
Map directly to the larger talk’s playbook; this is the deployable skeleton.
-->

---

## layout: default

# What Works Today

<v-clicks>

- Bug fixes with good tests; small features in well-scoped modules
- Repo chores: refactors, config, dependency bumps with CI gates
- DevOps and scripting in constrained sandboxes via CLI tools
- SWE-bench Verified shows repo-scale edits are attainable with loops

</v-clicks>

<div class="mt-4 text-xs text-gray-600">
Start narrow: maximize verifiable surfaces, minimize ambiguity and side effects.
</div>

<!--
Avoid overpromising; highlight verifiability as the common thread for wins.
-->

---

## layout: default

# What Breaks (Fast)

<v-clicks>

- Hallucinated files/paths; stale mental model of repo
- Brittle tools; untyped I/O; silent errors; non-idempotent ops
- Flaky tests obscure progress; long loops drift off-spec
- Security: unintended privilege, secret leakage, unsafe shell

</v-clicks>

<div class="mt-4 p-3 bg-rose-50 rounded border border-rose-200 text-xs">
Mitigations: typed schemas, retries with backoff, deterministic tools, container isolation, least privilege.
</div>

<!--
Name the sharp edges succinctly; pair with concrete mitigations.
-->

---

## layout: default

# Evaluation That Predicts Shipping

<v-clicks>

- Prefer process metrics over just outcomes: passes, retries, human interventions
- Gate on verifiable signals: compile/lint/unit/property/fuzz tests
- Benchmarks: prioritize SWE-bench Verified; treat Pro with caution
- Trace-level review: replay runs; label failure modes to drive fixes

</v-clicks>

<div class="mt-4 text-xs text-gray-600">
Decision rule: strong on Verified → Pro adds signal; never the reverse.
</div>

<!--
Steer away from leaderboard chasing; align eval with deployment reality.
-->

---

## layout: default

# Deployment Playbook (90 Days)

<v-clicks>

- Phase 1: Edit-only or bash-only with tests; PRs behind flags
- Phase 2: Policy-verified PRs; human review; track defect density
- Phase 3: Merge-on-green in allowlisted dirs; rollback on SLO breach
- Data loop: log everything; weekly RL/VR on your backlog distribution

</v-clicks>

<div class="mt-4 p-3 bg-green-50 rounded border border-green-200 text-xs">
Route by verifiability and cost; use small, fast models for exploration; large for commit paths.
</div>

<!--
Make it concrete and time-bound; emphasize staged risk and continuous learning.
-->

---

## layout: default

# Guardrails You Actually Need

<v-clicks>

- Policy engine: no commits to main; tests required; diff size limits
- Secrets and SAST gating; deny dangerous shells; approval gates
- Sandboxing: container per run; least privilege; network egress controls
- Observability: signed JSONL traces; replay runners; audit trails

</v-clicks>

<div class="mt-4 text-xs text-gray-600">
Security amplifies in multi-agent settings — contain blast radius first.
</div>

<!--
Short list that prevents 80% of incidents; matches the big-deck guidance.
-->

---

## layout: center

# The Takeaway

<v-clicks>

- It’s not magic — it’s loops, tools, and tests
- Ship a minimal loop with guardrails, then scale scope
- Evaluate processes, not just final diffs
- Optimize for verifiability, cost, and safety

</v-clicks>

<!--
Close with crisp action bias; invite discussion if time remains.
-->

