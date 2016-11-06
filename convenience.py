from deuces.deuces import Card, Evaluator, Deck

evaluator = Evaluator()

def str2cards(s):
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
    Card.print_pretty_cards(x)

def ring_winners(b, players):
    winners = []
    winrank = ''
    s = [evaluator.evaluate(b, p) for p in players]
    for i, rank in enumerate(s):
        if rank == min(s):
            winners.append(i)
            winrank = evaluator.class_to_string(evaluator.get_rank_class(rank))
    return [winners, winrank]

def who_wins(b, p1, p2, printout = True):
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
    # exclusions is a list. please note this func always returns list.
    drawn = []
    while len(drawn) < n:
        c = deck.draw()
        if c in exclusions + drawn:
            continue
        drawn.append(c)
    return drawn

def find_pcts(p1, p2, start_b = [], iter = 10000):
    win_record = []
    for i in range(iter):
        deck = Deck()
        need = 5 - len(start_b)
        b2 = draw_sure(deck, need, p1+p2+start_b)
        win_record.append(who_wins(start_b + b2, p1, p2, printout = False))
    return [win_record.count(1) / float(len(win_record)), 
            win_record.count(2) / float(len(win_record))
    ]

def find_pcts_multi(P, start_b = [], iter = 10000):
    wins_per_player = [0] * len(P)
    all_hole = reduce(lambda x,y: x+y, P)
    for i in range(iter):
        deck = Deck()
        need = 5 - len(start_b)
        b2 = draw_sure(deck, need, all_hole+start_b)
        s = [evaluator.evaluate(start_b+b2, h) for h in P]
        for i, e in enumerate(s):
            if e == min(s):
                wins_per_player[i] += 1
    return [float(x) / sum(wins_per_player) for x in wins_per_player]
