# lean-verifier
Recevoir un input en langage naturel ou une proposition mathématique.

Générer automatiquement du code Lean 4 avec Mathlib.

Exécuter Lean dans le terminal.

Analyser les erreurs et corriger le code.

Retourner un résultat VERIFIED ou FAILED, accompagné de la preuve et du diagnostic.

## Initialiser le projet
Après avoir installé Lean via elan, exécute :

        lake new claude-lean-project math
        cd claude-lean-project

        lake exe cache get

        mkdir -p .claude/agents Proofs

## Exemple de prompt:

        Utilise l'agent lean-verifier pour démontrer que pour tous les entiers naturels a et b, a + b = b + a. Génère le code Lean, exécute-le avec Mathlib, corrige les erreurs éventuelles et retourne le rapport de vérification.


## Le code Lean attendu pourrait ressembler à :

        import Mathlib

        theorem addition_commutative (a b : Nat) :
            a + b = b + a := by
        omega

## print axioms addition_commutative


Si l'exécution et le contrôle des axiomes réussissent, l'agent peut retourner un rapport du type :

        {
        "status": "VERIFIED",
        "theorem": "addition_commutative",
        "attempts": 1,
        "compiler_exit_code": 0,
        "proof": "omega",
        "axiom_check": "PASSED"
        }


C'est un exemple de réponse attendue, pas le résultat d'une exécution réelle.