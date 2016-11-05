from deuces.deuces import Evaluator, Deck
from convenience import pr, draw_sure

e = Evaluator()
deck = Deck()
hole = deck.draw(2)
pr(hole)

rc = [None] * 2

board = deck.draw(3)
pr(board)
rc[0] = e.get_rank_class(e.evaluate(hole, board))
print e.class_to_string(rc[0])

hits = 0
maxiter = 52 - 5

for i in range(maxiter):
    newdeck = Deck()
    riv = draw_sure(newdeck, 1, board + hole)
#    pr(riv)
    board = board + riv
    rc[1] = e.get_rank_class(e.evaluate(hole, board))
#    print e.class_to_string(rc[1])
    if rc[0] > rc[1]:
        hits = hits + 1

print hits / float(maxiter)

### fixme adding all kinds of crap to board. decl new var called flop
