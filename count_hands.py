from convenience import reduce_h
from deuces.deuces import Card

ranks = 'A K Q J T 9 8 7 6 5 4 3 2'.split()

def all_cards():
    for r in ranks:
        for s in 'shdc':
            yield r+s

def all_hole_cards():
    seen = []
    for x in all_cards():
        for y in all_cards():
            if y == x:
                continue # no such thing as suited pair
            if x+y in seen or y+x in seen:
                continue # only count AsKh, not KhAs
            else:
                seen += [x+y]
                s = reduce_h([Card.new(x), Card.new(y)])
                if s[2] == 'o':
                    s = s[0:2]
                yield s

def numbers_of_hole_cards():
    Table = {}
    cells = [] # lets us do it in order
    for s in all_hole_cards():
        if s in Table.keys():
            Table[s] += 1
        else:
            cells += [s]
            Table[s] = 1
    assert sum(Table.values()) == 1326 # 52 choose 2
    return [Table, cells]

if __name__ == '__main__':
    [Table, cells] = numbers_of_hole_cards()
    for s in cells:
        print s, '\t', Table[s]
    print
    print sum(Table.values())
