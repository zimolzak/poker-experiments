from math import log
from deuces.deuces import Card

def suited3(hand):
    L = [0] * 4
    Lc = []
    for c in hand:
        suit = int(log(Card.get_suit_int(c), 2))
        L[suit] += 1
    if max(L) >= 3:
        suit_to_pull = 2 ** L.index(max(L))
        for c in hand:
            if Card.get_suit_int(c) == suit_to_pull:
                Lc.append(c)
    return Lc

def poss_straight(hand):
    """Specifically, are there >= three cards, AND can you add exactly two
    to form a straight?
    """
    if len(hand) < 3:
        return False
    Lr = hand2ranks(hand)
    for i in range(len(Lr) - 2):
        if Lr[i+2] - Lr[i] <= 4:
            return True
    return False

def hand2ranks(h):
    Lr = []
    for c in h:
        Lr.append(Card.get_rank_int(c))
    Lr.sort()
    return Lr

def trips_or_pair(hand, or_quads = False):
    Lr = hand2ranks(hand)
    for i in range(13):
        if Lr.count(i) == 2 or Lr.count(i) == 3:
            return True
        if Lr.count(i) == 4 and or_quads == True:
            return True
    return False

def flush_is_nuts(hand):
    nptq = not trips_or_pair(hand, or_quads=True)
    S = suited3(hand)
    are_suited = len(S) >= 3
    no_str = not poss_straight(S)
    return nptq and are_suited and no_str

def straight_is_nuts(hand):
    return not trips_or_pair(hand, or_quads=True) and \
        poss_straight(hand) and \
        len(suited3(hand)) < 3

def trips_is_nuts(hand):
    return not trips_or_pair(hand, or_quads=True) and \
        not poss_straight(hand) and \
        len(suited3(hand)) < 3

def nut_hand(hand):
    if poss_straight(suited3(hand)):
        return 'Straight flush.'
    elif trips_or_pair(hand):
        return 'Four of a kind.'
    elif flush_is_nuts(hand):
        return 'Flush.'
    elif straight_is_nuts(hand):
        return 'Straight.'
    elif trips_is_nuts(hand):
        return 'Three of a kind.'
    else:
        return 'Something else?'