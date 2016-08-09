from itertools import combinations
from deuces.deuces import Card, Evaluator, Deck
from nuts import nut_hand

evaluator = Evaluator()
deck = Deck()
flop = deck.draw(3)

def omaha_eval(hole, board):
    assert(len(hole)) == 4
    ranks = []
    for ph in combinations(hole, 2):
        thisrank = evaluator.evaluate(list(ph), board)
        ranks.append(thisrank)
    return min(ranks)

def r2t(x):
    return evaluator.class_to_string(evaluator.get_rank_class(x))

def r2c(x):
    return evaluator.get_rank_class(x)

def list_to_pretty_str(card_ints):
    output = " "
    for i in range(len(card_ints)):
        c = card_ints[i]
        if i != len(card_ints) - 1:
            output += Card.int_to_pretty_str(c) + ","
        else:
            output += Card.int_to_pretty_str(c) + " "
    return output

print list_to_pretty_str(flop)

rank_clasess= []
for i in range(6):
    player = deck.draw(4)
    realrank = omaha_eval(player, flop)
    print list_to_pretty_str(player), r2t(realrank)
    rank_clasess.append(r2c(realrank))

print
print "nuts = ", nut_hand(flop), ". win = ", evaluator.class_to_string(min(rank_clasess))
