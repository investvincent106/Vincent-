# Task — Person Intake (No Data → No Opinion)

## But
Collecter les données **minimum viables** pour profiler une personne **sans hallucination**.

## Champs obligatoires
- `full_name`: Nom complet exact de la personne (ex: "Jane Dupont").
- `linked_profile_url`: **≥ 1 URL** publique (LinkedIn, site perso, Crunchbase, page presse...). Si aucune URL n’est fournie, **STOP**.
- `context_goal`: Contexte d’usage (prospection, recrutement, due diligence, veille).
- `do_not_infer`: `true` par défaut — **interdit d’inférer** un fait non sourcé.

## Règles d’entrée
1) Si `linked_profile_url` est vide → retourner un message court demandant l’URL. **Ne rien analyser**.
2) Normaliser l’URL (trim, https, sans tracking).
3) Logger les champs reçus dans `logs/person_intake/YYYYMMDD_HHMM_fullname.md`.

## Sortie attendue
Un bloc JSON compact pour orchestrateurs:
```json
{
  "full_name": "...",
  "linked_profile_url": ["https://..."],
  "context_goal": "...",
  "do_not_infer": true
}

---

**2) `vincent_chatgpt_pack_github_only/prompts/tasks/person_profile_report.md`**  
Gabarit de sortie **avec citations obligatoires** + **Confidence Score** par section.

```md
# Task — Person Profile Report (Citations-First)

## Règles globales (dures)
- **Aucun fait sans source**. Chaque point factuel doit référencer **≥ 1 URL**.
- Conflit entre sources → marquer **[Conflit]** et formuler une question de clarification.
- Donner un **Confidence Score** par section: `low` | `medium` | `high`.

## Structure de sortie (Markdown)

## Identité
- **Nom**: …
- **Alias/Variantes**: …
- **Citations**: [URL1], [URL2]
- **Confidence**: high|medium|low

## Rôle actuel
- **Poste**: …
- **Organisation**: …
- **Localisation**: …
- **Citations**: […]
- **Confidence**: …

## Parcours (3 faits clés)
1) Fait #1 — **Citations**: […]
2) Fait #2 — **Citations**: […]
3) Fait #3 — **Citations**: […]
- **Confidence (section)**: …

## Signals (12–18 derniers mois)
- Dernières actus publiques / posts / talks — **Citations**: […]
- **Confidence**: …

## Risques & Ambiguïtés
- Points flous, homonymes, dates contradictoires — **Citations**: […]
- **Confidence**: …

## Accroche LinkedIn sur-mesure (optionnel)
> 2–3 lignes contextualisées, **ne pas affirmer** de fait non cité.

## Citations (liste exhaustive)
- [1] …
- [2] …

## Meta
- Généré le: {{ISO8601}}
- Orchestrateur: person_profile
- Policy: no-source-no-output
