from itertools import combinations
from deuces.deuces import Card, Evaluator, Deck
from nuts import nut_hand

### What are the theoretical and actual nut hands (on the flop), given
### a certain number of players?

evaluator = Evaluator()

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

print "nut_hand,flop_leader,num_players"

for num_players in range(2,7):
    for i in range(5000):
        deck = Deck()
        flop = deck.draw(3)
        rank_clasess= []
        for p in range(num_players):
            player = deck.draw(4)
            realrank = omaha_eval(player, flop)
            rank_clasess.append(r2c(realrank))
        winner = min(rank_clasess)
        print nut_hand(flop) + "," + str(winner) + ' ' + evaluator.class_to_string(winner) + "," + str(num_players)
