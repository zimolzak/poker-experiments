from math import sqrt

## p = u / (52-5) ; o = (1-p) / p ; o=u
## http://www.wolframalpha.com/input/?i=solve+p+%3D+u+%2F+(52-5)+;+o+%3D+(1-p)+%2F+p+;+o%3Du
## p = ((1-p)/p)/(52-5)
## 47p^2 + p - 1 = 0

def print_outs(n_outs, maxiter):
    proportion = n_outs / float(maxiter)
    odds = (1 - proportion) / proportion
    print(n_outs, "outs\t", round(proportion, 3), '\t',
          round(odds, 3), "\tto 1")
    return odds

for n_outs in range(1,17):
    print_outs(n_outs, 52 - 5)
print()

print('numerically:')
x = 6.36
step = 0.001
odds = 7
while x <= odds :
    odds = print_outs(x, 52-5)
    x += step

print()

print('closed form:')
print('(3 * sqrt(21) - 1) / 2')
magic = (3 * sqrt(21) - 1) / 2
print_outs(magic, 52-5)
