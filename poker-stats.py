from deuces import Card, Evaluator, Deck

evaluator = Evaluator()

for i in range(10):
    deck = Deck()
    b = deck.draw(3)
    p = deck.draw(2)
    print evaluator.evaluate(b, p)
