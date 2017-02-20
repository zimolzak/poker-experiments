#!/usr/bin/env python2
# https://github.com/rshk/elo/blob/master/elo.py
from __future__ import division
import random

def expected(A, B):
    """
    Calculate expected score of A in a match against B
    :param A: Elo rating for player A
    :param B: Elo rating for player B
    """
    return 1 / (1 + 10 ** ((B - A) / 400))

def elo(old, exp, score, k=32):
    """
    Calculate the new Elo rating for a player
    :param old: The previous Elo rating
    :param exp: The expected score for this match
    :param score: The actual score for this match
    :param k: The k-factor for Elo (default: 32)
    """
    return old + k * (score - exp)

ranges = [[0,6], [3, 8], [5, 10]]
maxidx = len(ranges) - 1
elos = [1000] * len(ranges)

## begin one game

a = random.randint(0, maxidx)
b = a
while b == a:
    b = random.randint(0, maxidx)

print a, b
print ranges[a], ranges[b]
a_s = random.uniform(*ranges[a])
b_s = random.uniform(*ranges[b])
print a_s, b_s

ascore = 0.5
bscore = 0.5
if a_s > b_s:
    print a, "wins"
    ascore = 1
    bscore = 0
else:
    print b, "wins"
    ascore = 0
    bscore = 1

ex = expected(elos[a], elos[b])
print "expected", ex
print a, "new", elo(elos[a], ex, ascore)
print b, "new", elo(elos[b], ex, bscore)
