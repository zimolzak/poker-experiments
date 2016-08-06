from deuces.deuces import Card, Deck
from nuts import nut_hand

for i in range(15):
    deck = Deck()
    flop = deck.draw(3)
    turn = [deck.draw(1)]
    river = [deck.draw(1)]
    for board in [flop, flop + turn, flop + turn + river]:
        Card.print_pretty_cards(board)
        dummy = raw_input('Think hard... ')
        print "Nuts:", nut_hand(board)
    print