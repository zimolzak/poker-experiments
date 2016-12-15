# usage: python one_time_eval.py hole_cards [board_cards]
# examples:
#        python one_time_eval.py as8sqdtc
#        python one_time_eval.py as8sqdtc     2skskd
#        python one_time_eval.py as8sqdtc3d3c 2skskd
#        python one_time_eval.py as8sqdtc3d3c 2skskd3h5s

import sys
import time
from convenience import find_pcts_multi, pr, str2cards

## argv to strings
hole_cards_str = sys.argv[1]
board_str = ''
if len(sys.argv) > 2:
    board_str = sys.argv[2]

## strings to lists of Card objects
n_range_villains = 0
pct_range = False
if 'p' in hole_cards_str:
    assert hole_cards_str[-1] == 'p'
    assert hole_cards_str.count('p') == 1
    pct_str = hole_cards_str[4:] # everything after 1st 4 ch = pct
    hole_cards_str = hole_cards_str[:4] # 1st 4 ch are hole cards
    print 'met preconditions'
    pct_range = int(pct_str[:pct_str.find('p')]) # parse the pct
    n_range_villains = 1
hole_cards = str2cards(hole_cards_str)
board = str2cards(board_str)
assert len(board) <= 5

## hole card (flat) list to player list-of-lists
assert len(hole_cards) % 2 == 0
n_players = len(hole_cards) / 2
assert n_players + n_range_villains > 1
p = []
print "Players' hole cards:"
for i in range(n_players):
    pi = hole_cards[i * 2 : i * 2 + 2]
    print "  " + str(i+1) + ':',
    pr(pi)
    p.append(pi)
if n_range_villains:
    print "...versus top", pct_range, "% of hands"

print "Board:",
pr(board)
n_hands = 35000
start = time.time()
percents = find_pcts_multi(p, board, iter = n_hands, vs_range = pct_range)
end = time.time()
print "Equities by player:", [round(x, 4) for x in percents]
sec = round(end - start, 1)
rate = int(n_hands / (end - start))
print "{} hands in {} sec. {} per sec.".format(n_hands, sec, rate)
