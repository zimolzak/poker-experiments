from deuces.deuces import Card, Evaluator, Deck

evaluator = Evaluator()

def pto(pct):
    """Percentage to odds converter. Take a number like 35, return what
    odds it represents (x-to-one odds).
    """
    return (1 - pct / 100.0) / (pct / 100.0)

def reduce(hand):
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

def strategy(hand, style='tight'):
    assert style == 'tight'
    #      a k q j t 9 8 7 6 5 4 3 2
    Mt = [[1,1,1,2,2,2,3,3,3,3,4,4,4], #a
          [1,1,2,3,3,3,4,4,5,5,5,5,5], #k
          [2,3,1,2,3,4,5,5,5,5,5,5,5], #q
          [2,3,3,1,3,4,5,5,5,5,5,5,5], #j
          [3,3,4,4,2,4,4,5,5,5,5,5,5], #t
          [3,5,5,5,5,2,4,5,5,5,5,5,5], #9
          [3,5,5,5,5,5,2,4,5,5,5,5,5], #8
          [4,5,5,5,5,5,5,2,4,5,5,5,5], #7
          [4,5,5,5,5,5,5,5,3,5,5,5,5], #6
          [4,5,5,5,5,5,5,5,5,3,5,5,5], #5
          [4,5,5,5,5,5,5,5,5,5,3,5,5], #4
          [4,5,5,5,5,5,5,5,5,5,5,3,5], #3
          [4,5,5,5,5,5,5,5,5,5,5,5,3], #2
          ]
    return Mt

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
