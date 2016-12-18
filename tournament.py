from sys import argv
from itertools import product
from deuces.deuces import Card
from convenience import pr, find_pcts_multi, reduce_h

r = 'AKQJT98765432'

my_slice = int(argv[1])
tot_slice = int(argv[2])

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

#### slice up search space

dcb = []
for e in detailed_cards('black'):
    dcb.append(e)

len_slice = 1.0 / tot_slice * len(dcb)
print '// Length of slice', len_slice
start = int(len_slice * (my_slice - 1))
end = int(start + len_slice)
if my_slice == tot_slice:
    slice = dcb[start:]
else:
    slice = dcb[start:end]
print "// Start, end indices", start, end
print "// From hand", reduce_h(slice[0])
print "// ...to hand", reduce_h(slice[-1])
print

### do search

for x in product(slice, detailed_cards('red')):
    pcts = find_pcts_multi(list(x), iter=1000)
    if pcts[0] / pcts[1] > 1.5:
        print reduce_h(x[0]), '->', reduce_h(x[1])
    elif pcts[1] / pcts[0] > 1.5:
        print reduce_h(x[0]), '<-', reduce_h(x[1])