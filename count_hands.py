from convenience_hole import HR, deck_choose_2, numbers_of_hole_cards, numbers_of_hole_cards_random

print "According to theory\n========"
[Table, cells] = numbers_of_hole_cards()
for s in cells:
    print s, Table[s], '\t',
print
print
print sum(Table.values())
print
print

print "According to table 'HR'\n========"
HR_tot = sum([row['n'] for row in HR])
float_tot = 0
for s in cells:
    for row in HR:
        if row['h'] == s:
            n_hands = float(row['n']) / HR_tot * deck_choose_2
            float_tot += n_hands
            print s, round(n_hands, 1), '\t',
print
print
print float_tot
print
print

print "According to random\n========"
T2 = numbers_of_hole_cards_random(100000) # 115591080
T2_tot = sum(T2.values())
float_tot = 0
for s in cells:
    n_hands = float(T2[s]) / T2_tot * deck_choose_2
    float_tot += n_hands
    print s, round(n_hands, 1), '\t',
print
print
print float_tot
