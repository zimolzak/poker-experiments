from deuces.deuces import Card, Evaluator, Deck
import random

evaluator = Evaluator()

def str2cards(s):
    """Parse a string like 'as8sqdtc3d3c' to a simple (flat) list of
    deuces card objects (in reality integers).
    """
    assert len(s) % 2 == 0
    str_list = []
    cards = []
    for cardnum in range(len(s) / 2):
        str_list.append(s[cardnum * 2 : cardnum * 2 + 2])
    for i, si in enumerate(str_list):
        cstring = si[0].upper() + si[1].lower()
        cards.append(Card.new(cstring))
    return cards

def reduce_h(hand):
    """Reduce a hand like [As, Th] to a string like ATo."""
    assert(type(hand) == list)
    assert(len(hand) == 2)
    assert(type(hand[0]) == type(hand[1]) == int)
    hand.sort(reverse=True)
    hand_str = Card.int_to_str(hand[0])[0] + Card.int_to_str(hand[1])[0]
    if Card.get_suit_int(hand[0]) == Card.get_suit_int(hand[1]):
        hand_str += 's'
    else:
        hand_str += 'o'
    return hand_str

def pr(x):
    """Simply abbreviation for pretty printing in deuces. Expects list."""
    Card.print_pretty_cards(x)

def ring_winners(b, players):
    """Given a board and a list-of-lists of hole cards, what is the list
    of indices of the winning players, and what string describes the
    winning hand?
    """
    winners = []
    winrank = ''
    s = [evaluator.evaluate(b, p) for p in players]
    for i, rank in enumerate(s):
        if rank == min(s):
            winners.append(i)
            winrank = evaluator.class_to_string(evaluator.get_rank_class(rank))
    return [winners, winrank]

def _who_wins(b, p1, p2, printout = True):
    if printout:
        [pr(h) for h in [b, p1, p2]]
    s = [evaluator.evaluate(b, p) for p in [p1, p2]]
    r = [evaluator.class_to_string(evaluator.get_rank_class(x)) for x in s]
    if s[1] > s[0]:
        t = "P1 wins"
        winning_player = 1
    elif s[1] < s[0]:
        t = "P2 wins"
        winning_player = 2
    else:
        t = "push"
        winning_player = 0
    if printout:
        print ', '.join(map(str, s) + map(str, r) + [t])
    return winning_player

def draw_sure(deck, n, exclusions):
    """Draw n cards from a deck but skip any cards listed in
    exclusions. Please note this func always returns a list, unlike
    native deuces draw function.
    """
    drawn = []
    while len(drawn) < n:
        c = deck.draw()
        if c in exclusions + drawn:
            continue
        drawn.append(c)
    return drawn

def find_pcts(p1, p2, start_b = [], iter = 10000):
    """Given 2 players' hole cards and an optional board in any state,
    what is each player's chance of winning?
    """
    win_record = []
    for i in range(iter):
        deck = Deck()
        need = 5 - len(start_b)
        b2 = draw_sure(deck, need, p1+p2+start_b)
        win_record.append(_who_wins(start_b + b2, p1, p2, printout = False))
    return [win_record.count(1) / float(len(win_record)), 
            win_record.count(2) / float(len(win_record))
    ]

#### FIXME - CRAPPY COPY PASTE

from itertools import combinations

all52 = Deck.GetFullDeck()
all_hole_explicit = []
for h in combinations(all52, 2):
    all_hole_explicit += [list(h)]
deck_choose_2 = len(all_hole_explicit)
assert deck_choose_2 == 1326


def all_hole_cards():
    """Enumerate all 2-card combos, lumping them together based on suited
    or off-suit.

    Example:
    AA   AA   AA   AKs  AK   AQs ... AA   AA   AK   AKs  AK   AK   AQ ...
    Which reflects:
    AsAh AsAd AsAc AsKs AsKh AsQs    AhAd AhAc AhKs AhKh AhKd AhKc AhQs
    """
    for hole in all_hole_explicit:
        s = reduce_h(hole)
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
    assert sum(Table.values()) == deck_choose_2
    return [Table, cells]



def top_hands_pct(p):
    """Return list of the top p percent of hands, using the lookup table
    called 'HR' (short for Hand Rankings).
    """
    [Table, cells] = numbers_of_hole_cards()
    tot_hands = sum(Table.values())
    n_hands = tot_hands * (p / 100.0)
    # setup for loop
    hands_retrieved = 0
    hand_list = []
    for d in HR:
        hs = d['h']
        old_distance = abs(n_hands - hands_retrieved)
        new_distance = abs(n_hands - hands_retrieved - Table[hs])
        if new_distance < old_distance:
            hand_list += [hs]
            hands_retrieved += Table[hs]
    return hand_list

HR = [
{'h':'AA', 'e':2.32, 'n':521324},
{'h':'KK', 'e':1.67, 'n':522652},
{'h':'QQ', 'e':1.22, 'n':520663},
{'h':'JJ', 'e':0.86, 'n':521866},
{'h':'AKs', 'e':0.78, 'n':348364},
{'h':'AQs', 'e':0.59, 'n':348759},
{'h':'TT', 'e':0.58, 'n':520705},
{'h':'AK', 'e':0.51, 'n':1048008},
{'h':'AJs', 'e':0.44, 'n':348126},
{'h':'KQs', 'e':0.39, 'n':346772},
{'h':'99', 'e':0.38, 'n':522454},
{'h':'ATs', 'e':0.32, 'n':348013},
{'h':'AQ', 'e':0.31, 'n':1042962},
{'h':'KJs', 'e':0.29, 'n':346582},
{'h':'88', 'e':0.25, 'n':521972},
{'h':'QJs', 'e':0.23, 'n':348870},
{'h':'KTs', 'e':0.20, 'n':348774},
{'h':'A9s', 'e':0.19, 'n':348992},
{'h':'AJ', 'e':0.19, 'n':1045857},
{'h':'QTs', 'e':0.17, 'n':346115},
{'h':'KQ', 'e':0.16, 'n':1045069},
{'h':'77', 'e':0.16, 'n':524345},
{'h':'JTs', 'e':0.15, 'n':348235},
{'h':'A8s', 'e':0.10, 'n':349431},
{'h':'K9s', 'e':0.09, 'n':348286},
{'h':'AT', 'e':0.08, 'n':1047289},
{'h':'A5s', 'e':0.08, 'n':348544},
{'h':'A7s', 'e':0.08, 'n':349949},
{'h':'KJ', 'e':0.08, 'n':1047098},
{'h':'66', 'e':0.07, 'n':520946},
{'h':'T9s', 'e':0.05, 'n':348264},
{'h':'A4s', 'e':0.05, 'n':347862},
{'h':'Q9s', 'e':0.05, 'n':348760},
{'h':'J9s', 'e':0.04, 'n':349965},
{'h':'QJ', 'e':0.03, 'n':1044338},
{'h':'A6s', 'e':0.03, 'n':347677},
{'h':'55', 'e':0.02, 'n':521945},
{'h':'A3s', 'e':0.02, 'n':347895},
{'h':'K8s', 'e':0.01, 'n':350401},
{'h':'KT', 'e':0.01, 'n':1045392},
{'h':'98s', 'e':0.00, 'n':348759},
{'h':'T8s', 'e':-0.00, 'n':347443},
{'h':'K7s', 'e':-0.00, 'n':348341},
{'h':'A2s', 'e':0.00, 'n':347318},
{'h':'87s', 'e':-0.02, 'n':348348},
{'h':'QT', 'e':-0.02, 'n':1047827},
{'h':'Q8s', 'e':-0.02, 'n':348381},
{'h':'44', 'e':-0.03, 'n':523398},
{'h':'A9', 'e':-0.03, 'n':1047672},
{'h':'J8s', 'e':-0.03, 'n':348046},
{'h':'76s', 'e':-0.03, 'n':347540},
{'h':'JT', 'e':-0.03, 'n':1043812},
{'h':'97s', 'e':-0.04, 'n':350158},
{'h':'K6s', 'e':-0.04, 'n':347029},
{'h':'K5s', 'e':-0.05, 'n':349320},
{'h':'K4s', 'e':-0.05, 'n':348681},
{'h':'T7s', 'e':-0.05, 'n':347638},
{'h':'Q7s', 'e':-0.06, 'n':348073},
{'h':'K9', 'e':-0.07, 'n':1045630},
{'h':'65s', 'e':-0.07, 'n':348590},
{'h':'T9', 'e':-0.07, 'n':1045306},
{'h':'86s', 'e':-0.07, 'n':348374},
{'h':'A8', 'e':-0.07, 'n':1042209},
{'h':'J7s', 'e':-0.07, 'n':345009},
{'h':'33', 'e':-0.07, 'n':522632},
{'h':'54s', 'e':-0.08, 'n':348260},
{'h':'Q6s', 'e':-0.08, 'n':349068},
{'h':'K3s', 'e':-0.08, 'n':348865},
{'h':'Q9', 'e':-0.08, 'n':1049468},
{'h':'75s', 'e':-0.09, 'n':349781},
{'h':'22', 'e':-0.09, 'n':524131},
{'h':'J9', 'e':-0.09, 'n':1044150},
{'h':'64s', 'e':-0.09, 'n':349689},
{'h':'Q5s', 'e':-0.09, 'n':350110},
{'h':'K2s', 'e':-0.09, 'n':349276},
{'h':'96s', 'e':-0.09, 'n':349514},
{'h':'Q3s', 'e':-0.10, 'n':348009},
{'h':'J8', 'e':-0.10, 'n':1046506},
{'h':'98', 'e':-0.10, 'n':1044759},
{'h':'T8', 'e':-0.10, 'n':1048779},
{'h':'97', 'e':-0.10, 'n':1046152},
{'h':'A7', 'e':-0.10, 'n':1046587},
{'h':'T7', 'e':-0.10, 'n':1044950},
{'h':'Q4s', 'e':-0.10, 'n':348979},
{'h':'Q8', 'e':-0.11, 'n':1048251},
{'h':'J5s', 'e':-0.11, 'n':348923},
{'h':'T6', 'e':-0.11, 'n':1043014},
{'h':'75', 'e':-0.11, 'n':1047447},
{'h':'J4s', 'e':-0.11, 'n':347508},
{'h':'74s', 'e':-0.11, 'n':350325},
{'h':'K8', 'e':-0.11, 'n':1048167},
{'h':'86', 'e':-0.11, 'n':1047524},
{'h':'53s', 'e':-0.11, 'n':346930},
{'h':'K7', 'e':-0.11, 'n':1043698},
{'h':'63s', 'e':-0.11, 'n':346449},
{'h':'J6s', 'e':-0.11, 'n':347570},
{'h':'85', 'e':-0.11, 'n':1048159},
{'h':'T6s', 'e':-0.11, 'n':348875},
{'h':'76', 'e':-0.11, 'n':1046722},
{'h':'A6', 'e':-0.12, 'n':1046762},
{'h':'T2', 'e':-0.12, 'n':1047032},
{'h':'95s', 'e':-0.12, 'n':348477},
{'h':'84', 'e':-0.12, 'n':1046266},
{'h':'62', 'e':-0.12, 'n':1049495},
{'h':'T5s', 'e':-0.12, 'n':348928},
{'h':'95', 'e':-0.12, 'n':1044601},
{'h':'A5', 'e':-0.12, 'n':1046285},
{'h':'Q7', 'e':-0.12, 'n':1046099},
{'h':'T5', 'e':-0.12, 'n':1048428},
{'h':'87', 'e':-0.12, 'n':1044635},
{'h':'83', 'e':-0.12, 'n':1048550},
{'h':'65', 'e':-0.12, 'n':1045971},
{'h':'Q2s', 'e':-0.12, 'n':348912},
{'h':'94', 'e':-0.12, 'n':1047422},
{'h':'74', 'e':-0.12, 'n':1043278},
{'h':'54', 'e':-0.12, 'n':1046435},
{'h':'A4', 'e':-0.12, 'n':1046931},
{'h':'T4', 'e':-0.12, 'n':1047976},
{'h':'82', 'e':-0.12, 'n':1043638},
{'h':'64', 'e':-0.12, 'n':1043079},
{'h':'42', 'e':-0.12, 'n':1043357},
{'h':'J7', 'e':-0.12, 'n':1046565},
{'h':'93', 'e':-0.12, 'n':1045989},
{'h':'85s', 'e':-0.12, 'n':347928},
{'h':'73', 'e':-0.12, 'n':1047020},
{'h':'53', 'e':-0.12, 'n':1047022},
{'h':'T3', 'e':-0.12, 'n':1043908},
{'h':'63', 'e':-0.12, 'n':1044818},
{'h':'K6', 'e':-0.12, 'n':1045039},
{'h':'J6', 'e':-0.12, 'n':1045991},
{'h':'96', 'e':-0.12, 'n':1047156},
{'h':'92', 'e':-0.12, 'n':1049342},
{'h':'72', 'e':-0.12, 'n':1046167},
{'h':'52', 'e':-0.12, 'n':1049213},
{'h':'Q4', 'e':-0.13, 'n':1045087},
{'h':'K5', 'e':-0.13, 'n':1047359},
{'h':'J5', 'e':-0.13, 'n':1047697},
{'h':'43s', 'e':-0.13, 'n':348802},
{'h':'Q3', 'e':-0.13, 'n':1047649},
{'h':'43', 'e':-0.13, 'n':1047900},
{'h':'K4', 'e':-0.13, 'n':1046562},
{'h':'J4', 'e':-0.13, 'n':1048129},
{'h':'T4s', 'e':-0.13, 'n':350639},
{'h':'Q6', 'e':-0.13, 'n':1046958},
{'h':'Q2', 'e':-0.13, 'n':1046353},
{'h':'J3s', 'e':-0.13, 'n':349254},
{'h':'J3', 'e':-0.13, 'n':1046204},
{'h':'T3s', 'e':-0.13, 'n':349673},
{'h':'A3', 'e':-0.13, 'n':1046970},
{'h':'Q5', 'e':-0.13, 'n':1047946},
{'h':'J2', 'e':-0.13, 'n':1045715},
{'h':'84s', 'e':-0.13, 'n':349390},
{'h':'82s', 'e':-0.14, 'n':348622},
{'h':'42s', 'e':-0.14, 'n':350591},
{'h':'93s', 'e':-0.14, 'n':348835},
{'h':'73s', 'e':-0.14, 'n':349007},
{'h':'K3', 'e':-0.14, 'n':1045968},
{'h':'J2s', 'e':-0.14, 'n':348259},
{'h':'92s', 'e':-0.14, 'n':347868},
{'h':'52s', 'e':-0.14, 'n':348401},
{'h':'K2', 'e':-0.14, 'n':1048521},
{'h':'T2s', 'e':-0.14, 'n':349612},
{'h':'62s', 'e':-0.14, 'n':348033},
{'h':'32', 'e':-0.14, 'n':1044956},
{'h':'A2', 'e':-0.15, 'n':1047979},
{'h':'83s', 'e':-0.15, 'n':349355},
{'h':'94s', 'e':-0.15, 'n':348259},
{'h':'72s', 'e':-0.15, 'n':348368},
{'h':'32s', 'e':-0.15, 'n':349794},
]
#### END FIXME


def find_pcts_multi(P, start_b = [], iter = 10000, vs_range = None):
    """Given a list-of-lists of players' hole cards and an optional board
    in any state, what is each player's chance of winning?
    """
    wins_per_player = [0] * len(P)
    all_hole = reduce(lambda x,y: x+y, P) # do once if static
    if vs_range:
        assert len(P) == 1
        range_list = top_hands_pct(vs_range)
        wins_per_player = [0] * 2
    for i in range(iter):
        deck = Deck()
        need = 5 - len(start_b)
        if vs_range:
            villain_hole = random.choice(top_hands_pct(vs_range))
            ### add on to P ### FIXME left off here.
            all_hole = reduce(lambda x,y: x+y, P) # do each time if dynamic
        b2 = draw_sure(deck, need, all_hole+start_b)
        s = [evaluator.evaluate(start_b+b2, h) for h in P]
        for i, e in enumerate(s):
            if e == min(s):
                wins_per_player[i] += 1
    return [float(x) / sum(wins_per_player) for x in wins_per_player]
