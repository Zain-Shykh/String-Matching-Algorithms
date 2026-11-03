"""Mission 2 — Tamayo's Blood Lab (finite automaton).   Run: python mission2.py"""
import os
from matchers import compute_transition_function, fa_match
from utils import read_text

FOLDER = "../data/blood_samples"
DEMON_MARKER = "GATTACAGATTC"

def reverse_complement(s):
    # TODO: swap A<->T and C<->G, then reverse
    raise NotImplementedError

# TODO: build delta for DEMON_MARKER over "ACGT" and print it as a table (one row per state)
# TODO: build delta for the reverse complement too
# TODO: for every file in FOLDER, run fa_match with both tables and print
#       file name, forward matches, reverse matches
# TODO: print which sample belongs to the hidden demon
