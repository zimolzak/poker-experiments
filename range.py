from future import add_margins, range_plot, top_hands_pct
from sys import argv
print add_margins(range_plot(top_hands_pct(float(argv[1]))))
