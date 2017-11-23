from convenience_hole import all_hands_in_range
from convenience import pr
from deuces.deuces import Card, Evaluator

e = Evaluator()

basic_keys = []
rc_counts = {}
for i in range(1,10):
    s = e.class_to_string(i)
    basic_keys.append(s)
    rc_counts[s] = 0

## Two input vars:
board = [Card.new('Qs'), Card.new('Jd'), Card.new('2c')]
range_list = ['AA', 'KK', 'QQ', 'AK', 'AKs']

## tricky ones highlighted:
##  1   2    3    4       5        6     7          8             9
## sf quad boat flush straight trip set 2p overp tp 1.5p mp wp ah nmh
##                             ^^^^^^^^    ^^^^^^^^^^^^^^^^^^^ ^^^^^^

print "Range:", range_list
print "Board:",
pr(board)
lol = all_hands_in_range(range_list)
for L in lol:
    hr = e.evaluate(L, board)
    rc = e.get_rank_class(hr)
    s = e.class_to_string(rc)
    rc_counts[s] += 1

def pad_to(n, s):
    while len(s) < n:
        s += ' '
    return s

print('\nResults\n========')
denom = float(sum(rc_counts.values()))
for s in basic_keys:
    n = rc_counts[s]
    print pad_to(15, s), n, '\t', round(n / denom * 100, 2)
