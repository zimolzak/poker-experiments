from pokermodules.convenience import reduce_h

def pto(pct):
    """Percentage to odds converter. Take a number like 35, return what
    odds it represents (x-to-one odds).
    """
    return (1 - pct / 100.0) / (pct / 100.0)

def playing(hand, position, style):
    """Should we play a given hand in a given situation? The hand argument
    can be either a list of 'deuces' cards (integers), or a string
    like 'JTo', 'JTs', 'JT', where the latter is assumed to be
    off-suit.
    """
    play_pct = {
        'average': {'early': 4.1, 'middle': 10.7, 'late': 20.4, 'button': 35.8},
        'tight': {'early': 3.0, 'middle': 8.9, 'late': 17.2, 'button': 34.3},
        'loose': {'early': 4.7, 'middle': 12.4, 'late': 24.0, 'button': 43.5},
        'short': {'early': 4.7, 'middle': 13.0, 'late': 23.7, 'button': 42.0}
    } # source: inferred from Phil Gordon
    my_pct = play_pct[style][position]
    if type(hand) == list:
        my_str = reduce_h(hand).replace('o','')
    elif type(hand) == str:
        my_str = hand.replace('o','')
    return my_str in top_hands_pct(my_pct)

def strategy(hand, style='tight'):
    """http://www.philnolimits.com/uploads/8/1/8/9/8189328/nl_starting_hands.pdf"""
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

