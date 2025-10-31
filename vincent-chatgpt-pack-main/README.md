# Vincent — Repo Sync (ChatGPT Booster Pack)

Ce repo améliore immédiatement la qualité de tes échanges avec ChatGPT.

## Ce qu’il y a dedans
- **contexts/** : infos sur toi (profil), Sync Production Montréal, style d’écriture, glossaire.  
- **prompts/** :
  - `system/` (règles globales)
  - `tasks/` (email polish, brief, notes→actions, proposal)
  - `agents/` (Planner, Writer, Researcher en YAML)
- **playbooks/** : connexion, routine 10 min, discovery, QA.
- **examples/** : email avant/après, brief, notes.
- **.github/workflows/docs-ci.yml** : lint Markdown.

## Connexion en 2 minutes
1. Dans ChatGPT → **Connecter des connaissances** → **GitHub**.  
2. Ajouter : `Minot-Prod/vincent-chatgpt-pack`.  
3. Dans ChatGPT :  
   > Active `contexts/profile_vincent.md`, `contexts/sync_production_montreal.md`, `contexts/writing_style.md`.

---

### 🚀 Démarrage Officiel
Ouvre **`prompts/system/init_vincent.md`** et suis les 3 étapes.  
> C’est le point d’entrée unique : contexte → effet wow → routine.

---

## 3 scénarios “effet wow”
1. **Email polish** → `prompts/tasks/email_polish.md` + `examples/email_before_after.md` (FR + EN, 1 CTA)  
2. **Brief client** → `prompts/tasks/brief_generator.md` (notes → brief structuré)  
3. **Notes → Actions** → `prompts/tasks/meeting_notes_to_actions.md` (5 actions max + risques)

---

## Routine quotidienne (10 min)
`playbooks/02_daily_workflow_sync_prod.md` : priorités du jour, 1 email clé, 1 risque à surveiller → mini-standup clair.

---

## KPI semaine 1
- Temps gagné / jour : **15–30 min**  
- Allers-retours mails : **–40 %**  
- Clarté perçue par pairs / clients : **+30 %**

---

## Maintenance
- Les fichiers `.md` sont lintés par CI.  
- Mets à jour `contexts/profile_vincent.md` si nécessaire.

## Licence
MIT
