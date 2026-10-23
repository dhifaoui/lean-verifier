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

## latex-to-lean converter
Prompt à envoyer à Claude Code

        Utilise l'agent latex-to-lean pour convertir
        la formule suivante en Lean 4 :

        \forall n \in \mathbb{N},\quad
        \sum_{k=0}^{n} k = \frac{n(n+1)}{2}

## input-output:

Input LaTeX


        \[
        \forall a,b \in \mathbb{N},\quad a+b=b+a
        \]

output LEAN


        import Mathlib

        def additionStatement : Prop :=
        ∀ a b : Nat, a + b = b + a

        #check additionStatement