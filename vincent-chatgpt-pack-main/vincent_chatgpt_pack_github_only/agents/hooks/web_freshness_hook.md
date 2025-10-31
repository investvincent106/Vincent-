---
title: "Web Freshness Hook — Person Profile"
owner: "Max"
last_review: "2025-10-30"
tags: ["hook", "freshness", "prospection"]
goal: "Brancher automatiquement la policy web-freshness avant toute génération de rapport de personne."
scope: "Agents Broker/Router — analyses de personnes uniquement."
acceptance: "Intake OK, fraîcheur <30j, citations présentes, Confidence par section, tag Policy en Meta."
---

### Hook — Exécution standard
1) **Intake** → `vincent_chatgpt_pack_github_only/prompts/tasks/person_intake.md`
2) **Freshness** (QDF=5) → appliquer la policy `policies/web_freshness_layer_v2.1.md`
3) **Report** → `vincent_chatgpt_pack_github_only/prompts/tasks/person_profile_report.md`

### Règles du hook
- Si `linked_profile_url` manquant → STOP + message court demandant l’URL.
- Si dernière mise à jour détectée > 30j → avertir + demander confirmation explicite avant de continuer.
- Refuser toute affirmation **sans URL**.
- Ajouter `Policy: web-freshness-v2.1` dans **Meta** du rapport.
