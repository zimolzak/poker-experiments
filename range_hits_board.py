from convenience_hole import all_hands_in_range, add_margins, range_plot
from convenience import pr
from deuces.deuces import Card, Evaluator

e = Evaluator()
rank_class_keys = ['Straight Flush', 'Four of a Kind', 'Full House', 'Flush',
                   'Straight', 'Three of a Kind', 'Two Pair',
                   'Overpair', 'Top Pair', '1.5 Pair', 'Middle Pair', 'Weak Pair',
                   'High Card']
rc_counts = {}

## Input vars:
board = [Card.new('Qs'), Card.new('Td'), Card.new('4c')]
range_list = ['AA', 'KK', 'QQ', 'AK', 'AKs', 'KQ', 'KQs', 'JJ', '33', '22', 'A4', '99']

## tricky ones highlighted:
##  1   2    3    4       5        6     7          8                9
## sf quad boat flush straight trip set 2p overp tp 1.5p mp wp overc ah nmh
##                             ^^^^^^^^    ^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^

print "Range:", range_list
print "Board:",
pr(board)
print
print add_margins(range_plot(range_list))

def increment_dict(d, k):
    if k in d.keys():
        d[k] += 1
    else:
        d[k] = 1
    return d

def distinguish_pairs(hole, board):
    # assumes no trips or set
    hrs = [Card.get_rank_int(c) for c in hole]
    brs = [Card.get_rank_int(c) for c in board]
    brs.sort(reverse = True) # high card is index 0
    if hrs[0] == max(brs) or hrs[1] == max(brs):
        return 'Top Pair'
    elif hrs[0] == hrs[1]: # pocket pair
        if max(hrs) > max(brs):
            return 'Overpair'
        elif brs[0] > hrs[0] > brs[1]:
            return '1.5 Pair'
        else:
            return 'Weak Pair'
    elif brs[1] == hrs[0] or brs[1] == hrs[1]:
        return 'Middle Pair'
    else:
        return 'Weak Pair'

#### main loop ####

lol = all_hands_in_range(range_list)
for L in lol:
    hr = e.evaluate(L, board)
    rc = e.get_rank_class(hr)
    s = e.class_to_string(rc)
    if s == 'Pair':
        s = distinguish_pairs(L, board)
    increment_dict(rc_counts, s)

#### print ####

def pad_to(n, s):
    while len(s) < n:
        s += ' '
    return s

print('\nResults\n========')
denom = float(sum(rc_counts.values()))
print int(denom), 'combos.\n'
for s in rank_class_keys:
    if s in rc_counts.keys():
        n = rc_counts[s]
        print pad_to(15, s), n, '\t', round(n / denom * 100, 2)
