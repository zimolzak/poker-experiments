from convenience import *
deck = Deck()
P = [deck.draw(2), deck.draw(2)]
pr(P[0])
pr(P[1])
print find_pcts_multi(P)
situation = [[Card.new('Jh'), Card.new('As')],
             [Card.new('7s'), Card.new('Jc')],
             [Card.new('Ks'), Card.new('5d')]]
pr(situation[0])
pr(situation[1])
pr(situation[2])
print find_pcts_multi(situation)
