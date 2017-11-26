from deuces.deuces import Card, Evaluator, Deck

### Simulate a bunch of random 5 card groups and find out what are the
### most common hands that they make.

evaluator = Evaluator()

for i in range(100000):
    deck = Deck()
    b = deck.draw(3)
    p = deck.draw(2)
    rank = evaluator.evaluate(b, p)
    text = evaluator.class_to_string(evaluator.get_rank_class(rank))
    print str(rank) + "\t" + text

