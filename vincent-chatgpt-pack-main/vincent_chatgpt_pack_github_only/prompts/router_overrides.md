# Router Gold — Overrides (Priority Triggers)

## But
Court-circuiter l'index standard lorsque certaines phrases fortes sont détectées, afin de lancer le pipeline le plus fiable sans poser de questions.

## Priority Trigger — Person Profile
- **Détection (mots-clés)** :
  - "analyse le profil", "analyse cette personne", "profil linkedin de"
- **Action** :
  1) Charger `prompts/gold/person_profile.md` (qui appelle `agents/router_person_profile.md`).
  2) Exécuter la séquence Intake → Auto-URL → Freshness (QDF=5) → One‑Shot → Factcheck → Report.
  3) Forcer `Policy: web-freshness-v2.1` et `Policy: question-minimization-v1`.

## Notes
- Les overrides sont évalués **avant** `prompts/index_gold.json`.
- Si plusieurs overrides matchent, **Person Profile** est prioritaire sur `analysis.md` et `sales.md`.
