from deuces.deuces import Card, Deck
from convenience import draw_sure, find_pcts, pr

p1 = [Card.new('As'), Card.new('Ac')]
p2 = [Card.new('Ad'), Card.new('Kd')]

Card.print_pretty_cards(p1)
Card.print_pretty_cards(p2)
main_deck = Deck()
board = []

for ncards in [0, 3, 1, 1]:
    add_to_board = draw_sure(main_deck, ncards, p1 + p2 + board)
    pr(add_to_board)
    board = board + add_to_board
    print find_pcts(p1, p2, start_b = board)
