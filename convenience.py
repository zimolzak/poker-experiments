from deuces.deuces import Card, Evaluator

evaluator = Evaluator()

def pr(x):
    Card.print_pretty_cards(x)

def who_wins(b, p1, p2):
    [pr(h) for h in [b, p1, p2]]
    s = [evaluator.evaluate(b, p) for p in [p1, p2]]
    r = [evaluator.class_to_string(evaluator.get_rank_class(x)) for x in s]
    if s[1] > s[0]:
        t = "P1 wins"
    elif s[1] < s[0]:
        t = "P2 wins"
    else:
        t = "push"
    print ', '.join(map(str, s) + map(str, r) + [t])
