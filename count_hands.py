from convenience_hole import HR, deck_choose_2, numbers_of_hole_cards

[Table, cells] = numbers_of_hole_cards()
for s in cells:
    print s, Table[s], '\t',
print
print
print sum(Table.values())
print
print

HR_tot = sum([row['n'] for row in HR])
float_tot = 0
for s in cells:
    for row in HR:
        if row['h'] == s:
            n_hands_HR = float(row['n']) / HR_tot * deck_choose_2
            float_tot += n_hands_HR
            print s, round(n_hands_HR, 1), '\t',
print
print
print float_tot
