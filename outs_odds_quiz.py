from deuces.deuces import Evaluator, Deck
from convenience import pr, draw_sure

e = Evaluator()
deck = Deck()
hole = deck.draw(2)
pr(hole)

rc = [None] * 2

flop = deck.draw(3)
pr(flop)
rc[0] = e.get_rank_class(e.evaluate(hole, flop))
print e.class_to_string(rc[0])

n_outs = 0
maxiter = 52 - 5
outs = []

for i in range(maxiter):
    riv = deck.draw(1)
    board = flop + [riv]
    rc[1] = e.get_rank_class(e.evaluate(hole, board))
    if rc[0] > rc[1]:
        n_outs = n_outs + 1
        outs.append(riv)

print n_outs, "outs"
pr(outs)
proportion = n_outs / float(maxiter)
print round(proportion, 3)
print round((1 - proportion) / proportion, 1), "to 1"
