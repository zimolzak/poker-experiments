from deuces.deuces import Evaluator, Deck, Card
from convenience import pr, draw_sure

e = Evaluator()
deck = Deck()
hole = deck.draw(2)
pr(hole)

def card_pairs_board(c, b):
    card_rank = Card.get_rank_int(c)
    board_ranks = map(Card.get_rank_int, b)
    return card_rank in board_ranks

def deck_without(cards):
    returnme = []
    for c in Deck.GetFullDeck():
        if c not in cards:
            returnme.append(c)
    return returnme

rc = [None] * 2

flop = deck.draw(3)
pr(flop)
rc[0] = e.get_rank_class(e.evaluate(hole, flop))
print e.class_to_string(rc[0])

n_outs = 0
maxiter = 52 - 5
outs = []

for i in range(maxiter):
    turn = deck.draw(1) # runs every card in deck
    rc[1] = e.get_rank_class(e.evaluate(hole, flop + [turn]))
    if rc[0] > rc[1] and not card_pairs_board(turn, flop):
        n_outs = n_outs + 1
        outs.append(turn)

print n_outs, "outs"
pr(outs)
proportion = n_outs / float(maxiter)
print round(proportion, 3)
print round((1 - proportion) / proportion, 1), "to 1"

## probably exclude any turn card that pairs to the board.
## would cover: 2pr to board, trips to board, quads to board.
## because only 4 card board, no chance of flush/str8 to board

# bug = test case

#   [ 6 h ] , [ J s ]  
#   [ 4 c ] , [ J d ] , [ 3 s ]  
# Pair
# 3 outs
#   [ 6 s ] , [ 6 d ] , [ 6 c ]  
# 0.064
# 14.7 to 1
