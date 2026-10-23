#!/usr/bin/env python3
"""Compile un fichier Lean 4 et retourne VERIFIED ou FAILED avec un diagnostic.

Usage : python3 scripts/verify.py [fichier.lean]   (défaut : Proofs/Generated.lean)
Code de sortie : 0 si VERIFIED, 1 si FAILED.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("Proofs/Generated.lean")
TIMEOUT = 600  # secondes

FORBIDDEN = re.compile(r"\b(sorry|admit|axiom)\b")
DIAG = re.compile(r"^(?P<file>[^:\n]+):(?P<line>\d+):(?P<col>\d+): (?P<sev>error|warning): (?P<msg>.*)$")


def strip_comments(src: str) -> str:
    src = re.sub(r"/-.*?-/", "", src, flags=re.S)
    return re.sub(r"--.*", "", src)


def fail(diagnostic: list[str], proof: str = "") -> None:
    print("STATUT : FAILED")
    if proof:
        print("PREUVE :\n" + proof)
    print("DIAGNOSTIC :")
    for d in diagnostic:
        print("  - " + d)
    sys.exit(1)


def main() -> None:
    path = (ROOT / TARGET).resolve()
    if not path.exists():
        fail([f"Fichier introuvable : {TARGET}"])
    proof = path.read_text(encoding="utf-8")

    issues = []
    for n, line in enumerate(strip_comments(proof).splitlines(), 1):
        m = FORBIDDEN.search(line)
        if m:
            issues.append(f"{TARGET}:{n}: mot interdit `{m.group(1)}`")

    if shutil.which("lake") is None:
        fail(["`lake` introuvable : installer Lean via elan (https://github.com/leanprover/elan)."], proof)

    try:
        res = subprocess.run(
            ["lake", "env", "lean", str(path)],
            cwd=ROOT, capture_output=True, text=True, timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        fail([f"Timeout après {TIMEOUT}s (preuve trop lente ou cache Mathlib manquant : `lake exe cache get`)."], proof)

    output = res.stdout + res.stderr
    errors, other = [], []
    for line in output.splitlines():
        m = DIAG.match(line)
        if m and m["sev"] == "error":
            errors.append(f"{m['file']}:{m['line']}:{m['col']}: {m['msg']}")
        elif m and "sorry" in m["msg"]:
            issues.append(f"{m['file']}:{m['line']}: {m['msg']}")
        elif line.strip() and not m and res.returncode != 0:
            other.append(line.strip())

    if res.returncode != 0 or errors or issues:
        fail(errors + issues + (other[:10] if not errors else []) or ["Échec sans message (voir `lake build`)."], proof)

    print("STATUT : VERIFIED")
    print("PREUVE :\n" + proof)
    print("DIAGNOSTIC :\n  - Compilation réussie, aucun sorry/admit/axiom.")


if __name__ == "__main__":
    main()
