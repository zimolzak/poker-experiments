# usage: python one_time_eval.py as8sqdtc
# usage: python one_time_eval.py as8sqdtc 2skskd

from convenience import find_pcts, pr, str2cards
import sys

## argv to strings
hole_cards_str = sys.argv[1]
board_str = ''
if len(sys.argv) > 2:
    board_str = sys.argv[2]

## strings to lists of Card objects
hole_cards = str2cards(hole_cards_str)
board = str2cards(board_str)

## card list to player list-of-lists
assert len(hole_cards) % 2 == 0
n_players = len(hole_cards) / 2
assert n_players > 1
p = []
for i in range(n_players):
    pi = hole_cards[i * 2 : i * 2 + 2]
    pr(pi)
    p.append(pi)

print "Board",
pr(board)
print find_pcts(p[0], p[1], board, iter = 10000)
