from convenience_hole import add_margins, range_plot, top_hands_pct
from sys import argv
fc2 = 1326
p = float(argv[1])

print "Top",  p, 'pct of hands =', fc2 * (p / 100.0), 'hands'

thp = top_hands_pct(p)
t = {'pairs':0, 'suited':0, 'unsuited':0}
mul = {'pairs':6, 'suited':4, 'unsuited':12}
for h in thp:
    if h[0] == h[1]:
        t['pairs'] += 1
    elif 's' in h:
        t['suited'] += 1
    else:
        t['unsuited'] += 1

running_tot = 0
for k in 'pairs suited unsuited'.split():
    print t[k], k, '*', mul[k], '=', t[k] * mul[k]
    running_tot += t[k] * mul[k]
print "Actual number", running_tot, '=', round(running_tot / float(fc2), 4) * 100

print add_margins(range_plot(thp))
