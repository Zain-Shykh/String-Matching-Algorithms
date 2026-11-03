"""BONUS — Breathing Styles Tournament (+10).   Run: python mission4.py"""
from matchers import *
from utils import Timer
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ARENA = ("a" * 100_000, "a" * 99 + "b")   # T, P
T, P = ARENA

results = {}
with Timer() as t:
    _, c = naive_match(T, P)
results["Naive"] = (c, t.seconds)
with Timer() as t:
    _, c, _ = rabin_karp_match(T, P, 256, 1_000_000_007)
results["Rabin-Karp"] = (c, t.seconds)
with Timer() as t:
    _, c = kmp_match(T, P)
results["KMP"] = (c, t.seconds)
with Timer() as t:
    delta = compute_transition_function(P, "ab")
    _, c = fa_match(T, delta, len(P))
results["Automaton"] = (c, t.seconds)

print(f"{'Technique':<12}{'Comparisons':>14}{'Time (s)':>12}")
for k, (c, s) in sorted(results.items(), key=lambda kv: kv[1][1]):
    print(f"{k:<12}{c:>14,}{s:>12.4f}")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
names = list(results)
ax[0].bar(names, [results[k][0] for k in names]); ax[0].set_title("Comparisons"); ax[0].set_yscale("log")
ax[1].bar(names, [results[k][1] for k in names]); ax[1].set_title("Time (s)")
plt.tight_layout(); plt.savefig("tournament.png")
print("Saved tournament.png")
