
## Multi-agent Lean verification workflow

This project uses two specialized agents:

### latex-to-lean

Responsibilities:
- Convert LaTeX mathematical expressions to Lean 4.
- Preserve the original mathematical meaning.
- Identify assumptions and ambiguities.
- Validate Lean syntax and types.
- Save output to Proofs/Converted.lean.

### lean-verifier

Responsibilities:
- Generate formal proofs.
- Execute Lean 4 with Mathlib.
- Debug proof failures.
- Check axiom dependencies.
- Return verification results.

## Agent orchestration

For LaTeX inputs:

1. Delegate LaTeX formalization to latex-to-lean.
2. Obtain the generated Lean proposition.
3. Ask the user to confirm the formalization
   if there are unresolved ambiguities.
4. Delegate proof generation to lean-verifier.
5. Keep the formalized proposition unchanged.
6. Execute Lean verification.
7. Return the final report.

## Verification statuses

CONVERTED:
  LaTeX successfully translated into Lean.

TYPE_CHECKED:
  Lean accepts the proposition as well-typed.

VERIFIED:
  Lean kernel accepts the proof and its axioms
  satisfy the project's approved axiom policy.

FAILED:
  Compilation or proof verification failed.

INCONCLUSIVE:
  Verification could not be completed.
