# usage: python one_time_eval.py as8sqdtc

from deuces.deuces import Card
from convenience import find_pcts, pr, str2cards
import sys

cards_str = sys.argv[1]
board_str = ''
if len(sys.argv) > 2:
    board_str = sys.argv[2]

cards = str2cards(cards_str)
board = str2cards(board_str)

assert len(cards) == 4
p1 = cards[0:2]
p2 = cards[2:4]

pr(p1)
pr(p2)
print find_pcts(p1, p2, board, iter = 10000)
