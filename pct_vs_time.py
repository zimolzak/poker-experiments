from deuces.deuces import Card, Evaluator, Deck
from convenience import who_wins

evaluator = Evaluator()

p1 = [Card.new('As'), Card.new('Ac')]
p2 = [Card.new('Ad'), Card.new('Kd')]

for i in range(10):
    deck = Deck()
    b = deck.draw(5)
    who_wins(b, p1, p2)
