---
title: "Template — Task (Vincent)"
owner: "Max"
last_review: "2025-10-30"
tags: ["template","task","execution"]
goal: "Modèle minimal pour décrire une tâche exécutable et mesurable."
scope: "Tâches ≤ 1 jour; dépendances listées; artefacts .md/.csv; pas d’info sensible."
acceptance: "DoD clair, owner, deadline ISO, liens artefacts; CI verte."
---

---
title: "Template — Task (Vincent)"
owner: "Max"
last_review: "2025-10-29"
tags: ["template","task","execution"]
goal: "Fournir un modèle minimal pour décrire une tâche exécutable et mesurable."
scope: "Tâches ≤ 1 jour; dépendances listées; artefacts en .md/.csv; pas d’info sensible."
acceptance: "La tâche inclut DoD clair, owner, échéance ISO, et liens vers artefacts; passage CI vert."
---

# Template — Task

goal: "Ex: générer une séquence d'emails de relance B2B (FR/EN)"
scope: "Ex: 1 ICP, 3 emails (J1/J3/J7), objections standards, ton Sync"
acceptance:
- "3 emails FR + 3 EN"
- "Object + CTA + variations A/B"
- "Références prompts: prompts/gold/sales.md, prompts/gold/email_marketing.md"

related_prompts:
- "prompts/gold/sales.md"
- "prompts/gold/email_marketing.md"

telemetry_ref:
  credit_log: "telemetry/CREDIT_LOG.yaml"
  learn_log: "telemetry/LEARN_LOG.yaml"

notes:
- "Adapter au secteur (SaaS, service pro, ecom) et à la persona ICP."
- "Respect RGPD/anti-spam. Ton: pro, clair, humain."
