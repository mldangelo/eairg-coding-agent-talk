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

# Why Now: The Leap to Repo-Scale

<v-clicks>

- Tool execution: deterministic shell/editor tools with typed I/O
- Verification: compile/lint/test gates after every change
- Context: long windows + retrieval over symbol graphs

</v-clicks>

```json
{
  "tool": "apply_patch",
  "input_schema": {
    "type": "object",
    "properties": {
      "diff": {"type": "string"},
      "idempotency_key": {"type": "string"}
    },
    "required": ["diff"]
  },
  "errors": ["E_PARSE", "E_CONFLICT", "E_POLICY"]
}
```

<div class="mt-3 text-xs text-gray-600">Typed tools + explicit error codes enable safe retries and recovery.</div>

<!--
Anchor the audience: capability jumps track addition of tools, verification, and long context. Sets expectations.
-->

---

# Minimal Viable Agent Loop

```python
def run(issue, tools, budget_steps=8, budget_seconds=600):
    plan = planner(issue)
    t0 = now()
    for step in range(budget_steps):
        if now() - t0 > budget_seconds:
            return failure("E_BUDGET_TIME", plan=plan)
        action = plan.next()
        out = tools.invoke(action)
        if out.error:
            # structured errors: E_PARSE, E_CONFLICT, E_POLICY
            plan = planner.revise(plan, feedback=out.error)
            continue
        v = verifier.check(repo_state(), out.artifacts)
        if v.passed:
            if plan.done():
                return success(plan=plan, trace=v.trace)
            plan = planner.revise(plan, feedback=v.results)
        else:
            plan = planner.revise(plan, feedback=v.failures)
    return failure("E_BUDGET_STEPS", plan=plan)
```

<div class="mt-3 text-xs text-gray-600">Short loops, explicit budgets, structured errors, verifier‑driven revision.</div>

<!--
Emphasize that the loop is simple by design; reliability comes from safeguards and verification, not long chains of thought alone.
-->

---

# Production Architecture (5 Components)

<v-clicks>

1. Planner — step plan + acceptance tests
2. Actor — repo edits, test runs, artifact capture
3. Verifier — policy engine, SAST, secrets, hidden tests
4. Repo Memory — symbol graph, embeddings, change history
5. Safety Guard — file allowlists, code-owner approvals

</v-clicks>

```jsonc
// policy.json (example)
{
  "deny": [
    {"rule": "no_main_commits", "when": {"branch": "main"}},
    {"rule": "limit_diff_size", "max_changed_lines": 400},
    {"rule": "tests_required", "when": {"changed_paths": ["src/**"]}}
  ],
  "require_checks": ["compile", "lint", "unit", "secrets", "sast"]
}
```

<div class="mt-3 text-xs text-gray-600">Priorities: typed schemas, deterministic tools, JSONL traces, replayable runs.</div>

<!--
Map directly to the larger talk’s playbook; this is the deployable skeleton.
-->

---

# What Works Today

<v-clicks>

- Code changes where tests define behavior; stable CI; reproducible builds
- Structured chores: refactors, config, dependency bumps with policy gates
- DevOps tasks in sandboxes via CLI tools with explicit allowlists
- Public benchmarks with repository edits; prefer Verified subsets for clarity

</v-clicks>

<div class="mt-4 text-xs text-gray-600">Preconditions: hermetic env (container), deterministic toolchain, reliable tests.</div>

<!--
Avoid overpromising; highlight verifiability as the common thread for wins.
-->

---

# What Breaks (Fast)

<v-clicks>

- Stale repo model → proposes edits to non-existent paths
- Untyped tool I/O → silent coercion and lossy parsing
- Non-idempotent tools → duplicate patches, corrupted state
- Flaky tests → non-stationary reward signal, spurious regressions
- Privilege mistakes → editing protected files, leaking secrets

</v-clicks>

```jsonc
// Tool design checklist
{
  "idempotency": true,
  "schema": "json-schema://tool/v1",
  "errors": ["E_PARSE", "E_TIMEOUT", "E_CONFLICT", "E_POLICY"],
  "stderr_as_error": true,
  "dry_run": true
}
```

<div class="mt-3 text-xs text-gray-600">Prefer explicit schemas, retries with backoff/jitter, and no-op defaults on error.</div>

<!--
Name the sharp edges succinctly; pair with concrete mitigations.
-->

---

# Evaluation That Predicts Shipping

<v-clicks>

- Metrics: success_rate, intervention_rate, redo_ratio, compile_error_rate
- Gate on verifiable signals: compile/lint/unit/property/fuzz tests
- Benchmarks: prioritize "Verified" subsets; treat broader sets with caution
- Trace review: replay runs; label failure modes → fixes

</v-clicks>

```text
success_rate          = successes / total
intervention_rate     = human_interventions / runs
redo_ratio            = total_tool_calls / unique_steps
compile_error_rate    = compile_failures / runs
```

```json
{"ts":"2025-09-27T13:14:20Z","run_id":"r_123","step":3,"tool":"apply_patch","ok":true,"lines":42}
{"ts":"2025-09-27T13:14:27Z","run_id":"r_123","step":4,"tool":"run_tests","ok":false,"error":"E_FAIL_TEST","failing":["tests/foo.spec.js::bar"]}
```

<div class="mt-3 text-xs text-gray-600">Evaluate the process, not just the final diff.</div>

<!--
Steer away from leaderboard chasing; align eval with deployment reality.
-->

---

# Deployment Playbook (90 Days)

<v-clicks>

- Phase 1: edit-only or bash-only agents; PRs always; CI must pass
- Phase 2: policy-verified PRs; human review; measure defect density
- Phase 3: merge-on-green within allowlists; auto-rollback on SLO breach
- Data loop: log traces; weekly model/tool updates from labeled failures

</v-clicks>

```yaml
# gate.yaml
require:
  checks: [compile, lint, unit, secrets, sast]
  reviewers: ["CODEOWNERS"]
limits:
  changed_lines: 400
  new_files: 10
allowlist:
  - "src/**"
  - "configs/**"
```

<div class="mt-3 text-xs text-gray-600">Route by verifiability/cost; small models for exploration, large for commit paths.</div>

<!--
Make it concrete and time-bound; emphasize staged risk and continuous learning.
-->

---

# Operational Controls

<v-clicks>

- Branch protection + policy engine (deny on missing checks/oversized diffs)
- Secrets scan + SAST as hard gates; deny shells with wildcard writes
- Sandbox: one container per run; user namespace remap; no host mounts
- Observability: signed JSONL traces; deterministic replays

</v-clicks>

```bash
docker run --rm \
  --network=none \
  --pids-limit=512 \
  --memory=2g --cpus=2 \
  --read-only -v /tmp:/tmp:rw \
  --security-opt no-new-privileges \
  --security-opt seccomp=seccomp.json \
  agent-runner:latest
```

<div class="mt-3 text-xs text-gray-600">Contain blast radius first; then optimize capabilities.</div>

<!--
Short list that prevents 80% of incidents; matches the big-deck guidance.
-->

---
layout: center
---
# Operational Invariants

<v-clicks>

- Loops are short, budgeted, and verifier-driven
- Tools are typed, idempotent, and deterministic by default
- Evaluation is process-level with replayable traces
- Controls enforce least privilege and merge-on-green discipline

</v-clicks>

<!--
Close with crisp action bias; invite discussion if time remains.
-->
