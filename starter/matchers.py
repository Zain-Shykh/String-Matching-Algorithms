"""
Demon Slayer Corps — The String Hunt
Your four techniques (matchers). Fill in every function marked TODO,
following the pseudocode from Lectures 7, 8 and 9.

Rules:
  * Shifts are 0-based: P occurs with shift s if T[s:s+m] == P.
  * Do NOT use str.find, the `in` operator on strings, str.count, re, or any other
    built-in search inside these functions. Compare characters one by one.
  * "comparisons" = how many times you compare one character of T with one character of P.

Check your work with:  python test_matchers.py
"""


def naive_match(T, P):
    """Lecture 7. Slide P over T one position at a time.
    Returns (shifts, comparisons)."""
    # TODO
    raise NotImplementedError


def rabin_karp_match(T, P, d=256, q=101):
    """Lecture 7. Use ord(ch) as the digit value of a character.
    On every hash hit, verify character by character.
    Returns (shifts, comparisons, spurious_hits)."""
    # TODO
    raise NotImplementedError


def compute_prefix_function(P):
    """Lecture 8. Returns the list pi, where pi[i] is the length of the longest
    proper prefix of P[0..i] that is also a suffix of it.
    Example: compute_prefix_function("ababaca") == [0, 0, 1, 2, 3, 0, 1]"""
    # TODO
    raise NotImplementedError


def kmp_resume(T, P, pi, q, offset):
    """Lecture 8, with one change: the matcher starts in state q instead of 0,
    and `offset` is the position of T[0] inside the whole file.
    This lets you feed a big file in chunks and carry q from one chunk to the next.
    After a full match, set q = pi[q - 1] so overlapping matches are found.
    Returns (q_at_the_end, shifts_found, comparisons)."""
    # TODO
    raise NotImplementedError


def kmp_match(T, P):
    """Whole-text KMP. Already done for you: it just calls kmp_resume once."""
    pi = compute_prefix_function(P)
    _, shifts, comparisons = kmp_resume(T, P, pi, 0, 0)
    return shifts, comparisons


def compute_transition_function(P, alphabet):
    """Lecture 9. Returns delta as a list of dicts: delta[q][a] = next state.
    There are len(P) + 1 states (0 .. m)."""
    # TODO
    raise NotImplementedError


def fa_match(T, delta, m):
    """Lecture 9. Start at q = 0 and do q = delta[q][T[i]] for every character.
    A character not in the alphabet sends you back to state 0.
    Returns (shifts, steps) where steps = number of table lookups."""
    # TODO
    raise NotImplementedError
