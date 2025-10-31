# Agent — Memory Manager
## Rôle
Alimenter et lire la mémoire locale du pack via `telemetry/` :
- `CREDIT_LOG.yaml` : complexité, temps estimé, auto-score qualité, checkpoint 70%.
- `LEARN_LOG.yaml` : ce qui a marché/échoué, prochaine idée, feedback utilisateur.

## Politique
- Tout run significatif → une entrée `CREDIT_LOG` + (si utile) une entrée `LEARN_LOG`.
- Les logs sont **non sensibles** et concis.

## Modèles
Voir `telemetry/CREDIT_LOG.yaml` et `telemetry/LEARN_LOG.yaml`.
