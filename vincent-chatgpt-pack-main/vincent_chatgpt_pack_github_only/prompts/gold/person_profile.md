# Prompt Gold — Person Profile (Citations-First)

intents:
  - "person_profile"
tags:
  - "profil"
  - "linkedin"
  - "due_diligence"
triggers:
  - "analyse le profil de"
  - "qui est"
  - "parcours de"
  - "linkedin de"

## Instruction
- Appeler `agents/router_person_profile.md`.
- Si l’utilisateur n’a pas fourni d’URL → présenter un mini-form: 
  "Donne-moi au moins **1 URL publique** (LinkedIn, site, Crunchbase). Sans URL, je ne peux pas garantir la véracité."

## Contrainte
- Policy: **no-source-no-output**, citations obligatoires, confidence scores par section.

## Format attendu
- Rapport selon `prompts/tasks/person_profile_report.md`.
- Liste `issues` si des faits ont été rejetés.
