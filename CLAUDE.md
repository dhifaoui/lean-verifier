
# Lean Verification Project

This project uses Lean 4 and Mathlib to formally
verify mathematical propositions.

## Agent delegation

Delegate Lean proof generation and verification
tasks to the lean-verifier subagent.

## Requirements

- Use Lean 4 and Mathlib.
- Execute generated Lean code.
- Never claim a proof is valid without verification.
- Do not modify approved theorem statements.
- Reject proofs using unapproved axioms.
- Report errors and failed verification attempts.

## Verification command

lake env lean Proofs/Generated.lean

## Exemple de prompt:

Utilise l'agent lean-verifier pour démontrer que pour tous les entiers naturels a et b, a + b = b + a. Génère le code Lean, exécute-le avec Mathlib, corrige les erreurs éventuelles et retourne le rapport de vérification.