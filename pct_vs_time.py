from deuces.deuces import Card, Deck
from convenience import who_wins, pr
from copy import deepcopy

p1 = [Card.new('As'), Card.new('Ac')]
p2 = [Card.new('Ad'), Card.new('Kd')]

def find_pcts(p1, p2, start_b = [], iter = 10000):
    win_record = []
    for i in range(iter):
        deck = Deck()
        b = deepcopy(start_b)
        while len(b) < 5:
            c = deck.draw()
            if c in p1 + p2 + b:
                continue
            b.append(c)
        win_record.append(who_wins(b, p1, p2, printout = False))
    return [win_record.count(1) / float(len(win_record)), 
            win_record.count(2) / float(len(win_record))
    ]

Card.print_pretty_cards(p1)
Card.print_pretty_cards(p2)
print find_pcts(p1, p2)
