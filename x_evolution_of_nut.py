from deuces.deuces import Card, Deck
from pokermodules.nuts import nut_hand

### How does the nut hand evolve over several streets?

print "flop,turn,river"

for i in range(10000):
    deck = Deck()
    flop = deck.draw(3)
    turn = [deck.draw(1)]
    river = [deck.draw(1)]
    def f(x):
        return nut_hand(x).replace('.', '')
    progression = map(f, [flop, flop + turn, flop + turn + river])
    print ','.join(progression)
