from deuces.deuces import Card, Deck
from convenience import draw_sure, find_pcts
from random import randint

### Given some interesting matchups (AA vs {AKs KQs JQs} and AKo vs
### 77), show the way the win percentages evolve over several possible
### streets.

### find_pcts() does 10,000 iterations by default. And we call it 4 *
### 20 * 4 times = 3.2 million iters altogether. 4 showdowns (graph) *
### 20 hands (lines on each graph) * 4 streets (points on each line).
### Takes rather a while. 5 min on Intel Core i5 at 3.1 GHz (really
### only uses 1 core though). In other words, one call of find_pcts()
### takes about 1 sec. Seems maybe 15 - 20 min on MacBook Pro 2.7 GHz
### Intel Core i7?
###
### Now with 4 processes, 1:30 on Core i5 3.1 GHz. 8 million iters.
### Implies about 8900 per sec. 4 min on MacBook Pro 2.7 GHz Intel
### Core i7.

myid = randint(1,999) * 100
            
p1 = [Card.new('As'), Card.new('Ac')]

villain = {'jqs' : [Card.new('Js'), Card.new('Qs')] ,
           'aks' : [Card.new('Ad'), Card.new('Kd')] ,
           'kqs' : [Card.new('Ks'), Card.new('Qs')]
}

for villain_str, p2 in villain.iteritems():
    for i in range(5):
        main_deck = Deck()
        board = []
        for j, ncards in enumerate([0, 3, 1, 1]):
            row = [villain_str, i + myid, j]
            add_to_board = draw_sure(main_deck, ncards, p1 + p2 + board)
            board = board + add_to_board
            ps = find_pcts(p1, p2, start_b = board)
            row.append(ps[0])
            print ','.join(map(str,row))

## crummy cut n paste follows

p1 = [Card.new('As'), Card.new('Kc')]
p2 = [Card.new('7h'), Card.new('7d')]
villain_str = 'AKo v 77'
for i in range(5):
    main_deck = Deck()
    board = []
    for j, ncards in enumerate([0, 3, 1, 1]):
        row = [villain_str, i + myid, j]
        add_to_board = draw_sure(main_deck, ncards, p1 + p2 + board)
        board = board + add_to_board
        ps = find_pcts(p1, p2, start_b = board)
        row.append(ps[0])
        print ','.join(map(str,row))
