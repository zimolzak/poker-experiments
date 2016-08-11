from deuces.deuces import Card, Deck
from convenience import draw_sure, find_pcts, pr

p1 = [Card.new('As'), Card.new('Ac')]
p2 = [Card.new('Js'), Card.new('Qs')]

print 'iter,stage,pct'

for i in range(20):

    main_deck = Deck()
    board = []

    for j, ncards in enumerate([0, 3, 1, 1]):
        row = [i, j]
        add_to_board = draw_sure(main_deck, ncards, p1 + p2 + board)
        board = board + add_to_board
        ps = find_pcts(p1, p2, start_b = board)
        row.append(ps[0])
        print ','.join(map(str,row))
    
