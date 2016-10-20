# usage: python one_time_eval.py hole_cards [board_cards]
# examples:
#        python one_time_eval.py as8sqdtc
#        python one_time_eval.py as8sqdtc     2skskd
#        python one_time_eval.py as8sqdtc3d3c 2skskd
#        python one_time_eval.py as8sqdtc3d3c 2skskd3h5s

from convenience import find_pcts_multi, pr, str2cards
import sys

## argv to strings
hole_cards_str = sys.argv[1]
board_str = ''
if len(sys.argv) > 2:
    board_str = sys.argv[2]

## strings to lists of Card objects
hole_cards = str2cards(hole_cards_str)
board = str2cards(board_str)

## hole card list to player list-of-lists
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
percents = find_pcts_multi(p, board, iter = 10000)
print [round(x, 4) for x in percents]
