from pokermodules.convenience_hole import HR, deck_choose_2, numbers_of_hole_cards, numbers_of_hole_cards_random

standard_order = [] # Becomes list of strings ['AA', 'KK', 'QQ', ... 'AKs', ...]
ranks = 'AKQJT98765432'
for c in ranks:
    standard_order += [c+c] #pairs
for a in ranks:
    for b in ranks:
        if ranks.index(a) >= ranks.index(b):
            continue
        standard_order += [a+b+'s'] #suited
for a in ranks:
    for b in ranks:
        if ranks.index(a) >= ranks.index(b):
            continue
        standard_order += [a+b] #off suit

print "According to theory\n========"
[Table, cells] = numbers_of_hole_cards()
for s in standard_order:
    print s, Table[s], '\t',
print
print
print sum(Table.values())
print
print

print "According to table 'HR'\n========"
HR_tot = sum([row['n'] for row in HR])
float_tot = 0
for s in standard_order:
    for row in HR:
        if row['h'] == s:
            n_hands = float(row['n']) / HR_tot * deck_choose_2
            float_tot += n_hands
            print s, round(n_hands, 2), '    ',
print
print
print float_tot
print
print

print "According to random\n========"
T2 = numbers_of_hole_cards_random(100000) # or try 115591080!
T2_tot = sum(T2.values())
float_tot = 0
for s in standard_order:
    n_hands = float(T2[s]) / T2_tot * deck_choose_2
    float_tot += n_hands
    print s, round(n_hands, 1), '\t',
print
print
print float_tot
