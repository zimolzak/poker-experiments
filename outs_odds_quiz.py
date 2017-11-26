from deuces.deuces import Evaluator, Deck, Card
from pokermodules.convenience import pr, draw_sure
from itertools import combinations
from sys import argv

if '--test' in argv:
    pause = False
else:
    pause = True

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

flop = deck.draw(3)
pr(flop)
h_rc_flop = e.get_rank_class(e.evaluate(hole, flop))

if pause:
    dummy = raw_input('Think hard... ')
print
print "Starting with", e.class_to_string(h_rc_flop)

## start simulating turn cards, counting outs

n_outs = 0
maxiter = 52 - 5  # runs every turn card remaining in deck
outs = []

# You have five outs. Five outs to WHAT HANDS? Two outs get you trips,
# and three outs get you two pair. Setup a dict that lets us answer
# this question.
outs_hands = {}
for i in range(1,10): # rank classes are [1 .. 9]
    outs_hands[e.class_to_string(i)] = 0

for i in range(maxiter):
    turn = deck.draw(1) # runs every card in deck
    h_rc_turn = e.get_rank_class(e.evaluate(hole, flop + [turn]))

    hero_win_flop = 0
    hero_win_turn = 0
    hero_denom = 0.0
    villain_deck = deck_without(flop + hole + [turn])
    for v_tuple in combinations(villain_deck, 2):
        villain = list(v_tuple)
        hero_denom = hero_denom + 1
        v_rc_flop = e.get_rank_class(e.evaluate(villain, flop))
        v_rc_turn = e.get_rank_class(e.evaluate(villain, flop + [turn]))
        if h_rc_flop < v_rc_flop:
            hero_win_flop = hero_win_flop + 1
        if h_rc_turn < v_rc_turn:
            hero_win_turn = hero_win_turn + 1
    Pf = round(hero_win_flop / hero_denom, 3)
    Pt = round(hero_win_turn / hero_denom, 3)
    if Pt > Pf:
        n_outs = n_outs + 1
        outs.append(turn)
        outs_hands[e.class_to_string(h_rc_turn)] += 1
    
print n_outs, "outs, which are:"
pr(outs)

for k, v in outs_hands.iteritems():
    if v == 0:
        continue
    print "    {} outs to {}".format(v, k)

proportion = n_outs / float(maxiter)
print "Proportion:", round(proportion, 3)
print round((1 - proportion) / proportion, 1), "to 1"
