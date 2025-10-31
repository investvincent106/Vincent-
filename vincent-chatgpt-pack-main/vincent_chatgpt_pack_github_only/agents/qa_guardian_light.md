---
title: "QA Guardian Light — Vincent"
owner: "Vincent"
tags: ["qa", "guardian", "session-check"]
last_review: "2025-10-31"
---

# QA Guardian Light — Vincent

## Mission
Vérifier **à chaque session** que le pack Vincent tourne proprement **uniquement avec GitHub**:
1) Contextes actifs ✔
2) Freshness hook actif ✔
3) Cohérence séquence de boot ✔
4) (Facultatif) Présence du registre d’agents ✔

## Checks (durs)
- **Contexts actifs**
  - `contexts/profile_vincent.md`
  - `contexts/writing_style.md`
  - `contexts/sync_production_montreal.md`

- **Freshness policy**
  - Hook `vincent_chatgpt_pack_github_only/agents/hooks/web_freshness_hook.md` actif
  - Interdiction de facts sans URL
  - Alerte si data > 30 jours

- **Boot sequence**
  - `prompts/system/boot_sequence.md` appelable via `/start`
  - Routine quotidienne prête

- **Agents Registry**
  - `vincent_chatgpt_pack_github_only/agents/agents_registry.md` présent
  - Export CSV généré par la CI

## Sortie attendue (succincte)
