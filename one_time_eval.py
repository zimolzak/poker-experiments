# usage: python one_time_eval.py as8sqdtc

from deuces.deuces import Card
from convenience import find_pcts, pr
import sys

s = sys.argv[1]
assert len(s) == 8
cards = [s[0:2], s[2:4], s[4:6], s[6:8]]
for i, ci in enumerate(cards):
    cards[i] = ci[0].upper() + ci[1].lower()

p1 = [Card.new(cards[0]), Card.new(cards[1])]
p2 = [Card.new(cards[2]), Card.new(cards[3])]
pr(p1)
pr(p2)
print find_pcts(p1, p2, start_b = [], iter = 10000)
