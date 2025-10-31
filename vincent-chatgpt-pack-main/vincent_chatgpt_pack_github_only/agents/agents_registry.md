---
title: "Agents Registry — Vincent"
owner: "Vincent"
tags: ["agents", "registry", "org"]
last_review: "2025-10-31"
---

# Agents Registry — Vincent

Ce registre liste **tous les agents** utiles à Vincent, leur rôle, tâches et hiérarchie.
Source de vérité = **GitHub** (Pas de Notion/HubSpot requis).

> Format tabulaire ci-dessous = compatible export CSV auto (CI).

| name | role | tasks | hierarchy | status |
|------|------|------|-----------|--------|
| UA | Superviseur global | Arbitrage, Synthèse, Reporting | Root | Active |
| MA | Idéation & Exploration | Création d’idées, Veille ciblée | Under UA | Active |
| MAP | Production & Exécution | Livraison, QA, Packaging | Under UA | Active |

## Règles d’évolution
- Ajouter une ligne par nouvel agent (pas de colonnes custom).
- Garder `name` unique et stable.
- `status`: Active | Paused | Deprecated.

## Export CSV (automatique)
- Généré par `.github/workflows/generate_agents_csv.yml` → `reports/agents_registry.csv`
