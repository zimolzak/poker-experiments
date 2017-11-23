from convenience_hole import all_hands_in_range
from convenience import pr
from deuces.deuces import Card, Evaluator

e = Evaluator()

board = [Card.new('Qs'), Card.new('Jd'), Card.new('2c')]
range_list = ['AA', 'KK', 'QQ', 'AK', 'AKs']


## tricky ones highlighted:
##  1   2    3    4       5        6     7          8             9
## sf quad boat flush straight trip set 2p overp tp 1.5p mp wp ah nmh
##                             ^^^^^^^^    ^^^^^^^^^^^^^^^^^^^ ^^^^^^

print "Range:", range_list
print "Board:",
pr(board)
hr_list = [0] * 10
lol = all_hands_in_range(range_list)
for L in lol:
    hr = e.evaluate(L, board)
    rc = e.get_rank_class(hr)
    hr_list[rc] += 1


print('\nResults\n========')
print hr_list
for i in range(1,10):
    print e.class_to_string(i), hr_list[i]
