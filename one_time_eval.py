from deuces.deuces import Card
from convenience import find_pcts
import sys

card_str = sys.argv[1]
assert len(card_str) == 8


p1 = [Card.new('As'), Card.new('Kc')]
p2 = [Card.new('7h'), Card.new('7d')]
print find_pcts(p1, p2, start_b = [], iter = 10000)
