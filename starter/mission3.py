"""Mission 3 — The Copycat Slayer (Rabin-Karp).   Run: python mission3.py"""
import os
from utils import read_text

MANUAL = "../data/hashira_manual.txt"
FOLDER = "../data/trainee_reports"
K = 40          # window length in characters
D = 256

def clean_text(t):
    # TODO: lowercase, turn punctuation into spaces, collapse runs of spaces into one
    raise NotImplementedError

def copy_detect(manual, report, k=K, d=D, q=1_000_000_007):
    """TODO:
      1. Rolling-hash every k-character window of `manual`; store hash -> list of shifts.
      2. Roll the hash across `report`. On a hit, compare characters yourself
         (write the loop, no == on slices).
      3. Mark every report character covered by a verified window.
      4. similarity = covered characters / len(report) * 100
    Return similarity_percent."""
    raise NotImplementedError

# TODO: clean the manual and every report, run copy_detect on each report,
#       print each trainee's similarity and rank all five (highest first).
