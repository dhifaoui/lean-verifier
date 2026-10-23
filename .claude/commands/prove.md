---
description: Prouver une proposition en Lean 4 (génération, compilation, correction) et retourner VERIFIED ou FAILED
argument-hint: <proposition en langage naturel ou en Lean>
---

Proposition à prouver : $ARGUMENTS

Suis ce processus :

1. **Formaliser** la proposition en énoncé Lean 4 avec Mathlib. Si l'énoncé est ambigu, choisis une formalisation raisonnable et note-la pour le diagnostic.
2. **Écrire** l'énoncé et la preuve dans `Proofs/Generated.lean` (commence par `import Mathlib`).
3. **Compiler** avec `python3 scripts/verify.py`.
4. **Corriger** : en cas de FAILED, lis les erreurs, modifie la preuve (jamais l'énoncé pour le rendre plus facile), recompile. 5 itérations maximum.
5. **Vérification finale** : délègue au sous-agent `lean-verifier`.
6. **Répondre** dans ce format :

```
STATUT : VERIFIED | FAILED
PREUVE : <code Lean final>
DIAGNOSTIC : <erreurs rencontrées et corrections, ou cause de l'échec>
```
