"""Mission 2 — Tamayo's Blood Lab (finite automaton).   Run: python mission2.py"""
import os
from matchers import compute_transition_function, fa_match
from utils import read_text

FOLDER = "../data/blood_samples"
DEMON_MARKER = "GATTACAGATTC"
SIGMA = "ACGT"

def reverse_complement(s):
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(comp[c] for c in reversed(s))

RC_MARKER = reverse_complement(DEMON_MARKER)
delta_f = compute_transition_function(DEMON_MARKER, SIGMA)
delta_r = compute_transition_function(RC_MARKER, SIGMA)
m = len(DEMON_MARKER)

print(f"delta for {DEMON_MARKER} (rows = states 0..{m})")
print("state | " + " ".join(f"{a:>3}" for a in SIGMA))
for q, row in enumerate(delta_f):
    print(f"{q:>5} | " + " ".join(f"{row[a]:>3}" for a in SIGMA))
print("\nReverse complement:", RC_MARKER, "\n")

demons = []
for name in sorted(os.listdir(FOLDER)):
    dna = read_text(os.path.join(FOLDER, name))
    fwd, _ = fa_match(dna, delta_f, m)
    rev, _ = fa_match(dna, delta_r, m)
    print(f"{name}: forward={len(fwd)} reverse={len(rev)}")
    if fwd or rev:
        demons.append(name)

print("\nDemon in disguise:", ", ".join(demons) if demons else "none found")
