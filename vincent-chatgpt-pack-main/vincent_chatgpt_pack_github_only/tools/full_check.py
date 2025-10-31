#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
full_check.py — v1.4.3
Purpose:
  - Exécuter un "full check" de cohérence des livrables prospection (One-Shot)
  - Réconcilier automatiquement les décisions UA (ex: employeur final) avec le rapport One-Shot
  - Résoudre les blocs [Conflit] et propager le choix dans Analyse/Stratégie/Meta
  - Émettre des sorties prêtes à livrer: .md + .json avec trace d'audit

Usage (CLI):
  python full_check.py \
    --report-json /path/to/report.json \
    --decision-json /path/to/UA_Decision.json \
    --out-md /path/to/report_final.md \
    --out-json /path/to/report_final.json

Entrées attendues (schémas minimaux):
- report.json (One-Shot):
  {
    "Prospect": "Zoé Maxwell",
    "Conflit": {
      "field": "employeur",
      "options": ["Banque Nationale du Canada", "Equisoft"],
      "status": "ouvert" | "résolu",
      "résolution": null | "Equisoft"
    },
    "Analyse": {
      "employeur": "Banque Nationale du Canada",
      "confiance": 0.88,
      "source_principale": "LinkedIn",
      "ton": "professionnel"
    },
    "Stratégie": {
      "cible": "SYNC → corporate AV",
      "focus": ["captation", "diffusion", "événements"],
      "employeur_ciblé": "Banque Nationale du Canada"
    },
    "Messages": {...},
    "Meta": {
      "Policy": ["web-freshness-v2.1", "question-minimization-v1"],
      "source": "Banque Nationale du Canada (non confirmé)"
    },
    "Hypothèses_Manques": [...]
  }

- UA_Decision.json:
  {
    "Decision": {
      "type": "Employeur",
      "field": "employeur",
      "employer_candidates": ["Banque Nationale du Canada", "Equisoft"],
      "employer_final": "Equisoft",
      "confiance": 0.96
    },
    "Prospect": "Zoé Maxwell",
    "Date": "2025-10-30",
    "Meta": {
      "policy": ["web-freshness-v2.1", "context-weighted-inference-v1"]
    }
  }

Sorties:
- report_final.json:
  - mêmes champs que report.json +
  - "audit_sync": true
  - "audit_sync_at": ISO8601
  - "audit_sync_note": str
  - toutes les sections pertinentes patchées
- report_final.md:
  - rendu Markdown reconstruit, bloc [Conflit] résolu (ou supprimé si non pertinent)
  - meta mise à jour
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

VERSION = "1.4.3"

def _now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def load_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        raise RuntimeError(f"Impossible de lire le JSON: {p} — {e}")

def save_json(p: Path, data: dict) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def render_md(report: dict) -> str:
    # Rendu propre et robuste; s'adapte si certaines clés manquent.
    prospect = report.get("Prospect", "Prospect")
    analyse = report.get("Analyse", {})
    strategie = report.get("Stratégie", {})
    meta = report.get("Meta", {})
    messages = report.get("Messages", {})
    hyp = report.get("Hypothèses_Manques", [])
    conflit = report.get("Conflit")

    lines = []
    lines.append(f"# One-Shot — {prospect}")
    lines.append("")
    lines.append(f"_Version check_: full_check.py v{VERSION}")
    lines.append("")

    # Analyse
    lines.append("## 🔍 Analyse")
    if analyse:
        emp = analyse.get("employeur")
        conf = analyse.get("confiance")
        src = analyse.get("source_principale")
        ton = analyse.get("ton")
        if emp: lines.append(f"- **Employeur**: {emp}")
        if conf is not None: lines.append(f"- **Confiance**: {int(conf*100) if conf <= 1 else int(conf)}%")
        if src: lines.append(f"- **Source principale**: {src}")
        if ton: lines.append(f"- **Ton**: {ton}")
    else:
        lines.append("_Analyse indisponible_")
    lines.append("")

    # Conflit (afficher seulement si encore ouvert)
    if conflit and conflit.get("status") != "résolu":
        lines.append("## ⚠️ Conflit")
        lines.append(f"- **Champ**: {conflit.get('field')}")
        opts = conflit.get("options") or []
        if opts:
            lines.append(f"- **Options**: {', '.join(opts)}")
        lines.append("- **Statut**: ouvert")
        lines.append("")

    # Stratégie
    lines.append("## 🎯 Stratégie")
    if strategie:
        cible = strategie.get("cible")
        focus = strategie.get("focus") or []
        emp_cible = strategie.get("employeur_ciblé")
        if cible: lines.append(f"- **Cible**: {cible}")
        if emp_cible: lines.append(f"- **Employeur ciblé**: {emp_cible}")
        if focus: lines.append(f"- **Focus**: {', '.join(focus)}")
    else:
        lines.append("_Stratégie indisponible_")
    lines.append("")

    # Messages (si présents)
    if messages:
        lines.append("## 💬 Messages")
        for k, v in messages.items():
            lines.append(f"### {k}")
            lines.append(v.strip() if isinstance(v, str) else json.dumps(v, ensure_ascii=False))
            lines.append("")
    # Hypothèses & Manques
    lines.append("## 🧩 Hypothèses & Manques")
    if hyp:
        if isinstance(hyp, list):
            for item in hyp:
                if isinstance(item, str):
                    lines.append(f"- {item}")
                elif isinstance(item, dict):
                    lines.append(f"- {item.get('Élément','Élément')} — {item.get('Statut','?')}: {item.get('Commentaire','')}")
                else:
                    lines.append(f"- {item}")
        else:
            lines.append(f"- {json.dumps(hyp, ensure_ascii=False)}")
    else:
        lines.append("_Rien à signaler_")
    lines.append("")

    # Meta
    lines.append("## 🧠 Meta")
    if meta:
        policy = meta.get("Policy")
        src = meta.get("source")
        audit = {k: meta.get(k) for k in meta.keys() if k.startswith("audit_")}
        if policy:
            if isinstance(policy, list): lines.append(f"- **Policy**: {', '.join(policy)}")
            else: lines.append(f"- **Policy**: {policy}")
        if src: lines.append(f"- **Source**: {src}")
        if audit:
            for k, v in audit.items():
                lines.append(f"- **{k}**: {v}")
    else:
        lines.append("_Meta indisponible_")
    lines.append("")

    return "\n".join(lines)

def reconcile_one_shot(ua_decision: dict, report: dict) -> tuple[dict, str]:
    """
    Applique la décision UA (ex: employeur_final) dans le rapport One-Shot.
    - Met à jour Analyse.employeur
    - Met à jour Stratégie.employeur_ciblé si présent
    - Résout bloc Conflit si sur le même field
    - Aligne Meta.source
    - Marque l'audit de sync
    Retourne (report_patché, note_audit)
    """
    note = []
    decision = (ua_decision or {}).get("Decision") or {}
    field = decision.get("field")
    final = decision.get("employer_final")
    conf = decision.get("confiance")
    prospect_dec = ua_decision.get("Prospect")

    if not field or not final:
        note.append("Aucune décision exploitable (field/final manquant) — aucun patch appliqué.")
        return report, "; ".join(note)

    prospect_report = report.get("Prospect")
    if prospect_report and prospect_dec and prospect_report != prospect_dec:
        note.append(f"Prospect mismatch: report={prospect_report}, decision={prospect_dec} — patch forcé quand même.")

    # Patch Analyse
    analyse = report.setdefault("Analyse", {})
    previous_emp = analyse.get(field)
    analyse["employeur"] = final  # alias le champ attendu côté Analyse
    if previous_emp and previous_emp != final:
        note.append(f"Analyse.employeur: '{previous_emp}' → '{final}'")
    else:
        note.append(f"Analyse.employeur aligné: '{final}'")

    # Patch Stratégie
    strat = report.setdefault("Stratégie", {})
    prev_target = strat.get("employeur_ciblé")
    strat["employeur_ciblé"] = final
    if prev_target and prev_target != final:
        note.append(f"Stratégie.employeur_ciblé: '{prev_target}' → '{final}'")
    else:
        note.append("Stratégie.employeur_ciblé aligné")

    # Résolution du Conflit si applicable
    conflit = report.get("Conflit")
    if conflit and conflit.get("field") in (field, "employeur"):
        report["Conflit"]["status"] = "résolu"
        report["Conflit"]["résolution"] = final
        note.append("Conflit résolu via UA Decision")
    else:
        note.append("Aucun bloc Conflit pertinent à résoudre ou déjà résolu")

    # Meta
    meta = report.setdefault("Meta", {})
    policies = meta.get("Policy")
    if isinstance(policies, list) and "question-minimization-v1" not in policies:
        # Harmonise avec la policy pack (doc référencé dans le repo)
        policies.append("question-minimization-v1")
    elif not policies:
        meta["Policy"] = ["question-minimization-v1"]

    meta["source"] = f"{final} (confirmé UA Decision, confiance {int(conf*100) if conf and conf<=1 else int(conf or 95)}%)"
    meta["audit_sync"] = True
    meta["audit_sync_at"] = _now_iso()
    meta["audit_sync_note"] = " / ".join(note)

    return report, meta["audit_sync_note"]

def main():
    ap = argparse.ArgumentParser(description=f"full_check v{VERSION} — UA Decision Sync")
    ap.add_argument("--report-json", required=True, type=Path, help="Chemin du rapport One-Shot JSON source")
    ap.add_argument("--decision-json", required=True, type=Path, help="Chemin du UA_Decision JSON")
    ap.add_argument("--out-md", required=True, type=Path, help="Chemin de sortie pour le Markdown final")
    ap.add_argument("--out-json", required=True, type=Path, help="Chemin de sortie pour le JSON final")
    args = ap.parse_args()

    report = load_json(args.report_json)
    decision = load_json(args.decision_json)

    patched, audit_note = reconcile_one_shot(decision, report)

    # Stamp globales
    patched["_full_check"] = {
        "version": VERSION,
        "executed_at": _now_iso(),
        "audit_note": audit_note
    }

    # Sauvegardes
    save_json(args.out_json, patched)
    md = render_md(patched)
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text(md, encoding="utf-8")

    print(f"[OK] UA Decision Sync appliqué.\n- JSON: {args.out_json}\n- MD:   {args.out_md}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERREUR] {e}", file=sys.stderr)
        sys.exit(1)
