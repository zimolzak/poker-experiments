from deuces.deuces import Deck, Card
from convenience import ring_winners

### Takes about 38 sec on Intel Core i5 at 3.1 GHz. 

for n in range(75000):
    deck = Deck()

    ## Deal the hole cards
    ring = []
    for i in range(9):
        p = deck.draw(2)
        p.sort(reverse=True)
        ring.append(p)

    ## Deal board
    board = deck.draw(5)

    ## Show down
    [winners, winrank] = ring_winners(board, ring)
    for i, hole in enumerate(ring):
        hole_str = Card.int_to_str(hole[0])[0] + Card.int_to_str(hole[1])[0]
        if Card.get_suit_int(hole[0]) == Card.get_suit_int(hole[1]):
            hole_str += 's'
        else:
            hole_str += 'o'
        wl = ''
        if i in winners:
            wl = 'w'
        else:
            wl = 'l'
        print hole_str + ',' + winrank + ',' + wl + ',' + str(n) + ',' + str(i)
