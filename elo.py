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

def update_table(a, b, winner, table):
    assert winner == a or winner == b
    if winner == a:
        ascore = 1
        bscore = 0
    else:
        ascore = 0
        bscore = 1
    ex = expected(table[a], table[b])
    ea = elo(table[a], ex, ascore)
    eb = elo(table[b], ex, bscore)
    table[a] = ea
    table[b] = eb
    return table

for i in range(100):
    # choose 2 opponents
    a = random.randint(0, maxidx)
    b = a
    while b == a:
        b = random.randint(0, maxidx)
    # draw variate for each opponent and compare
    a_s = random.uniform(*ranges[a])
    b_s = random.uniform(*ranges[b])
    winner = None
    if a_s > b_s:
        print a, "wins", b, "loses", 
        winner = a
    else:
        print b, "wins", a, "loses", 
        winner = b
    # do the update
    elos = update_table(a, b, winner, elos)
    # print
    print map(lambda x: round(x, 1), elos)
