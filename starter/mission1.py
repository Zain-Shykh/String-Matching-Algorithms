"""Mission 1 — The Crow's Alarm (KMP).   Run: python mission1.py"""
from matchers import compute_prefix_function, kmp_resume
from utils import read_chunks

FILE = "../data/crow_log.txt"
ALARM = "KAKAKA"

pi = compute_prefix_function(ALARM)
print("pi =", pi)

all_shifts = []
# TODO: loop over read_chunks(FILE, 4096). Keep track of q and of the offset
#       (how many characters came before this chunk). Call kmp_resume on each chunk.

print("Alarm count:", len(all_shifts))
print("First 10 shifts:", all_shifts[:10])
