"""Mission 3 — The Copycat Slayer (Rabin-Karp).   Run: python mission3.py"""
import os
from utils import read_text

MANUAL = "../data/hashira_manual.txt"
FOLDER = "../data/trainee_reports"
K = 40          # window length in characters
D = 256

def clean_text(t):
    out = []
    for ch in t.lower():
        out.append(ch if ch.isalnum() else " ")
    return " ".join("".join(out).split())

def copy_detect(manual, report, k=K, d=D, q=1_000_000_007):
    n, r = len(manual), len(report)
    if r < k or n < k:
        return 0.0
    h = pow(d, k - 1, q)

    # 1. hash every k-window of the manual: hash -> list of shifts
    table = {}
    t = 0
    for i in range(k):
        t = (d * t + ord(manual[i])) % q
    for s in range(n - k + 1):
        table.setdefault(t, []).append(s)
        if s < n - k:
            t = (d * (t - ord(manual[s]) * h) + ord(manual[s + k])) % q

    # 2. roll across the report; verify hits char by char
    diff = [0] * (r + 1)   # difference array: +1 at window start, -1 after window end
    t = 0
    for i in range(k):
        t = (d * t + ord(report[i])) % q
    for s in range(r - k + 1):
        for ms in table.get(t, ()):
            j = 0
            while j < k and manual[ms + j] == report[s + j]:
                j += 1
            if j == k:
                diff[s] += 1
                diff[s + k] -= 1
                break
        if s < r - k:
            t = (d * (t - ord(report[s]) * h) + ord(report[s + k])) % q

    # 3. count covered characters
    covered = run = 0
    for i in range(r):
        run += diff[i]
        if run > 0:
            covered += 1
    return covered / r * 100

manual = clean_text(read_text(MANUAL))
scores = []
for name in sorted(os.listdir(FOLDER)):
    report = clean_text(read_text(os.path.join(FOLDER, name)))
    scores.append((copy_detect(manual, report), name.replace("report_", "").replace(".txt", "")))

print("Similarity ranking (highest first):")
for rank, (sim, who) in enumerate(sorted(scores, reverse=True), 1):
    print(f"{rank}. {who.capitalize():<8} {sim:6.2f}%")
