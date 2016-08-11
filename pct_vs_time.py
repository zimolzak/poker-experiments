from deuces.deuces import Card, Deck
from convenience import who_wins, pr
from copy import deepcopy

p1 = [Card.new('As'), Card.new('Ac')]
p2 = [Card.new('Ad'), Card.new('Kd')]

def draw_sure(deck, n, exclusions):
    drawn = []
    while len(drawn) < n:
        c = deck.draw()
        if c in exclusions + drawn:
            continue
        drawn.append(c)
    return drawn

def find_pcts(p1, p2, start_b = [], iter = 10000):
    win_record = []
    for i in range(iter):
        deck = Deck()
        need = 5 - len(start_b)
        b2 = draw_sure(deck, need, p1+p2+start_b)
        win_record.append(who_wins(start_b + b2, p1, p2, printout = False))
    return [win_record.count(1) / float(len(win_record)), 
            win_record.count(2) / float(len(win_record))
    ]

Card.print_pretty_cards(p1)
Card.print_pretty_cards(p2)
main_deck = Deck()
board = []

for ncards in [0, 3, 1, 1]:
    add_to_board = draw_sure(main_deck, ncards, p1 + p2 + board)
    pr(add_to_board)
    board = board + add_to_board
    print find_pcts(p1, p2, start_b = board)
