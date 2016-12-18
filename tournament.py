from itertools import product
from deuces.deuces import Card
from convenience import pr

r = 'AKQJT98765432'

def all_169_hands():
    for x in product(r, r):
        if r.index(x[0]) < r.index(x[1]):
            yield ''.join(x) + 's'
        else:
            yield ''.join([x[1], x[0]])

def black_red(pxs, suits):
    assert len(suits) == 2
    if 's' in pxs:
        return [Card.new(pxs[0] + suits[0]), Card.new(pxs[1] + suits[0])]
    else:
        return [Card.new(pxs[0] + suits[0]), Card.new(pxs[1] + suits[1])]

def detailed_cards(color):
    assert color in ['black', 'red']
    if color == 'black':
        suits = 'sc'
    else:
        suits = 'hd'
    for ps in all_169_hands():
        p = black_red(ps, suits)
        yield p

for x in detailed_cards('black'):
    pr(x)
for x in detailed_cards('red'):
    pr(x)

