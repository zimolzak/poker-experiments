# usage: python one_time_eval.py as8sqdtc

from deuces.deuces import Card
from convenience import find_pcts, pr
import sys

s = sys.argv[1]
#board_str = []
#if len(sys.argv) > 2:
#    board_str = sys.argv[2]

def str2cards(s):
    assert len(s) % 2 == 0
    str_list = []
    cards = []
    for cardnum in range(len(s) / 2):
        str_list.append(s[cardnum * 2 : cardnum * 2 + 2])
    for i, si in enumerate(str_list):
        cstring = si[0].upper() + si[1].lower()
        cards.append(Card.new(cstring))
    return cards

cards = str2cards(s)

assert len(cards) == 4
p1 = cards[0:2]
p2 = cards[2:4]

pr(p1)
pr(p2)
print find_pcts(p1, p2, start_b = [], iter = 10000)
