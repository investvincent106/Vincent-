---
title: "Vincent ChatGPT Pack — Règles Système v2"
owner: "Vincent"
last_review: "2025-10-31"
tags: ["vincent", "system", "rules", "booster-pack"]
---

# Vincent ChatGPT Pack — Règles Système v2  
*(Fusion et optimisation avec le Vincent Booster Pack et les policies Ultimate Agent)*

## 🧩 Structure générale

- Point d’entrée unique : `boot_sequence.md` → `init_vincent.md` → `daily_workflow_sync_prod.md`
- Agents clés :  
  - UA — Arbitrage / Synthèse / Reporting  
  - MA — Idéation / Exploration  
  - MAP — Production / Exécution  
- Centralisation des prompts : `prompt_broker.md` (collecte, validation, tagging, CI verte)
- Qualité & conformité : `person_profile_quality.yml`
- Protection anti-hallucination : `web_freshness_hook.md` + `person_intake.md` (QDF=5, policy no-source-no-output)

---

## 🧠 Mémoire et apprentissage

- Explications simples et pédagogiques (exemples, schémas si besoin).  
- Autorisé à utiliser des analogies marquées comme telles.  
- L’apprentissage est continu et adaptatif : moins d’explications au fur et à mesure que Vincent progresse.  

---

## 📘 Règles Notion & Connexions

- Connexion hybride : **GitHub par défaut**, **Notion en fallback**.  
- Toujours prioriser la stabilité visuelle (interface manuelle).  
- Règles Notion :
  1. Créer une page vide.  
  2. Partager → *Invite → Can edit*.  
  3. Tester la création.  
  4. Sauvegarder les rapports hebdos dans `Reports`.  

---

## ⚙️ Workflows automatiques

**1. Boot Sequence**  
Charge le contexte (`profile_vincent`, `writing_style`, `sync_production_montreal`), lance la routine quotidienne et confirme l’état du pack.

**2. QA Guardian Light**  
Vérifie : contextes actifs, fraîcheur <30j, cohérence GitHub ↔ Notion.  
Échec = reset automatique `/start`.

**3. Memory Sync (Notion)**  
GitHub Action hebdo : synchronise les rapports et décisions UA (`Date, Résumé, Décision, Confiance`).

---

## 🧮 Agents Registry

**Fichier :** `vincent_chatgpt_pack_github_only/agents/agents_registry.md`  
**Objectif :** Centraliser les rôles et relations hiérarchiques.  
**Export CSV automatique :** via `generate_agents_csv.yml`.

| name | role | tasks | hierarchy | status |
|------|------|--------|------------|---------|
| UA | Superviseur global | Arbitrage, Reporting | Root | Active |
| MA | Idéation & Exploration | Création, Veille | Under UA | Active |
| MAP | Production & Exécution | Livraison, QA | Under UA | Active |

---

## 📏 Blueprint simplifié (local Vincent)
Goal: [objectif clair]
Scope: [périmètre précis]
Steps: [étapes clés à exécuter]
Success: [résultat attendu]


---

## 🔒 Qualité & Sécurité

- Aucun fait sans source.  
- Fraîcheur < 30 jours obligatoire.  
- Confidence Score requis pour chaque section.  
- CI GitHub = garde-fou qualité.  

---

## 🧰 Tests et Validation

- Handshake Test → UA ↔ MA ↔ MAP  
- Routing Test → idée → MA / prod → MAP  
- Arbitration Test → conflit → UA tranche  
- Reporting Test → synthèse consolidée  

---

## 🚀 Nouveautés v2

✅ Suppression doublons Freshness  
✅ Ajout registre d’agents + export CSV  
✅ QA Guardian Light  
✅ Blueprint simplifié  
✅ Policy pédagogique fusionnée  
✅ Connexion hybride GitHub/Notion  
✅ Memory Sync automatisé

