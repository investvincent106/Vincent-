---
title: "Prompt Broker — Vincent Pack"
owner: "Max"
last_review: "2025-10-31"
tags: ["vincent", "broker", "prompts", "workflow"]
---

## Orchestration (extrait)

### Person Profile — Execution Order
1) Intake → `prompts/tasks/person_intake.md`
2) Freshness (QDF=5) → `policies/web_freshness_layer_v2.1.md`
3) **One‑Shot Confident** → `policies/question_minimization_v1.md`
4) Render → `prompts/tasks/person_profile_report.md`

### Meta Tags
- `Policy: web-freshness-v2.1`
- `Policy: question-minimization-v1`
