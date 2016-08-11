from deuces.deuces import Card, Deck
from convenience import who_wins

p1 = [Card.new('As'), Card.new('Ac')]
p2 = [Card.new('Ad'), Card.new('Kd')]
win_record = []

for i in range(100000):
    deck = Deck()
    b = []
    while len(b) < 5:
        c = deck.draw()
        if c in p1 or c in p2:
            continue
        b.append(c)
    win_record.append(who_wins(b, p1, p2, printout = False))

Card.print_pretty_cards(p1)
print win_record.count(1) / float(len(win_record))
Card.print_pretty_cards(p2)
print win_record.count(2) / float(len(win_record))
