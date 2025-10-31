---
title: "Prompt Broker — Vincent Pack"
owner: "Max"
last_review: "2025-10-30"
tags: ["vincent", "broker", "prompts", "workflow"]
goal: "Standardiser la collecte, le tri et la mise à jour des prompts utiles à la prospection et au reporting."
scope: "Sources GitHub/Notion; FR/EN; formats .md; aucune donnée sensible; sorties prêtes à copier-coller."
acceptance: "Prompts versionnés avec exemples; tags par use-case; lien canonique; CI verte."
---

## Mission du Prompt Broker
Ce module centralise la gestion des prompts partagés entre Vincent et Max.
Il sert de référentiel "single source of truth" pour les requêtes IA testées et validées.

### Responsabilités
- **Collecter** les prompts utilisés dans les outils internes.
- **Valider** les formulations efficaces avant publication.
- **Taguer** chaque prompt selon son usage précis (prospection, suivi, génération de contenu).
- **Assurer** la conformité au format Markdown standardisé.

### Bonnes pratiques
- Tous les prompts doivent être autoportants, avec contexte minimal.
- Mentionner la version IA testée (`GPT-5`, `Claude`, etc.).
- Éviter les placeholders vagues (ex. "insérer ici").
- Garder une trace des performances observées pour affiner les itérations.

---

## 🔗 Web Freshness Hook (auto)
**Objectif :** empêcher toute hallucination lors des analyses de personne, et **forcer** la fraîcheur (<30j) + **citations** + **Confidence**.

**Pipeline obligatoire (person profile)**
1) Intake → `vincent_chatgpt_pack_github_only/prompts/tasks/person_intake.md`
2) Freshness (QDF=5) → `vincent_chatgpt_pack_github_only/policies/web_freshness_layer_v2.1.md`
3) Report → `vincent_chatgpt_pack_github_only/prompts/tasks/person_profile_report.md`

**Règles d’exécution**
- Si `linked_profile_url` manquant → **STOP** + message demandant l’URL.
- Si fraîcheur > 30j → **avertir + demander confirmation** explicite avant de poursuivre.
- **Aucun fait sans URL.**
- Ajouter `Policy: web-freshness-v2.1` dans la **Meta** du rapport.

**Note :** Ce hook est appelé **avant tout rendu** de `person_profile_report.md`.
