---
title: "Web Freshness Layer (v2.1) — Vincent Pack"
owner: "Max"
last_review: "2025-10-30"
tags: ["freshness", "prospection", "policy"]
goal: "Empêcher toute inférence non sourcée et forcer la vérification live (<30j) avant d’analyser un profil."
scope: "Analyses de personnes (prospection, due diligence, veille). GitHub-only + Web search."
acceptance: "URL(s) obligatoires, Policy: web-freshness-v2.1 dans la sortie, citations présentes, Confidence Score par section."
---

## 🔍 Web Freshness Layer (v2.1)

### Étapes
1. **Intake** — Appeler `prompts/tasks/person_intake.md` (No Data → No Opinion).
   - Exiger `linked_profile_url` (≥1).
   - Normaliser l’URL.
   - `do_not_infer: true`.

2. **Freshness Check (QDF=5)**
   - Lancer une recherche web ciblée sur `linked_profile_url`.
   - Si dernière mise à jour > 30 jours → prévenir et demander validation avant de continuer.

3. **Report** — Appeler `prompts/tasks/person_profile_report.md`.
   - **Aucun fait sans source** (≥1 URL par point).
   - Ajouter `Policy: web-freshness-v2.1` dans la section **Meta**.
   - Donner un **Confidence Score** par section.

### Exemple de meta attendu
```md
## Meta
- Généré le: 2025-10-30T00:00:00Z
- Orchestrateur: person_profile
- Policy: web-freshness-v2.1
```

### Note d’intégration
- Ce module est référencé par le Prompt Broker. Si besoin de fallback, répondre: 
  > "Merci d’indiquer au moins un lien public (LinkedIn, site, presse). Aucun profil ne sera généré sans source."
