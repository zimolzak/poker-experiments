Poker Experiments
========

Just me playing around with `deuces` for Python.

Includes **tools** like an equity calculator, how a range hits a
board, and finding top x% of hands. Does a number **analyses** often
using Monte Carlo methods, on such topics as how often the nut hand
evolves or is realized per street. Has some **quizzes** for drilling
the response to various boards.

Usage
--------
* User-facing, print to standard output (Do `make test` to try out
  these and the interactive ones.)

    * `python one_time_eval.py as8sqdtc` (equity calculator)

    * `python range_hits_board.py` (Currently hardcoded analysis of
      how Q♠ T♦ 4♣ hits a board of deuces plus any two broadways. Will
      later take command line arguments.

    * `python range.py 15` (plot a preflop range)

    * `python count_hands.py` (convince self there are 1326 hands, 169
      classes)

    * `python3 fun_with_outs_odds.py` (just math trivia)

* User-facing, output to files

    * `make` to render (most interstingly) a text file `output.txt` of
      multiple tables. Also a PDF of how common are various poker
      hands, and the "flow" of several heads-up situations over the
      course of several streets.

    * `make tournament; make tournament.png` gets you a nice PNG graph
      of some hands that beat some other hands.

* User-facing, interactive

    * `python omaha_nuts_quiz.py` to practice rapidly mentally figuring out what
      is the nut hand.

    * `python outs_odds_quiz.py` or `source outs_loop.sh` to practice
      calculating outs and drawing odds.

* Usually called by makefile

    * best_hole_cards.py (multi-proc, > best_hole_cards > R > txt).
      Big csv. Each proc takes about 1 min on my macbook (2.7ghz i7).
      Winning cards/hand if all 9 players show down.

    * most_common_hands.py (> hand_ranks > R > pdf). How often do 5
      random cards make two pair, three of a kind, etc.?

    * evolution_of_nut.py (> evolution_of_nut > R > txt)

    * theo_actual_nut.py (theo_actual_nut > R > txt)

    * pct_vs_time.py (multi-proc, > pct_vs_time > R > pdf). Long
      compute. How equity can change by street for certain matchups.

    * tournament.py, filt.py. What if you could assign an Elo rating
      to a pair of hole cards and decide who is conclusively better
      than whom? What if you showed a directed graph of big
      favorites/dogs? Would there be any cycles?

* Purely library

    * nuts.py

    * convenience.py

    * future.py (generally dumping ground of functions not currently
      used)

    * convenience_hole.py

    * elo.py

Depends on
--------

* R

* ggplot2

* deuces




Examples
========

range.py
--------

`python range.py 15`

    Top 15.0 pct of hands = 198.9 hands
    9 pairs * 6 = 54
    18 suited * 4 = 72
    6 unsuited * 12 = 72
    Actual number 198 = 14.93
      A K Q J T 9 8 7 6 5 4 3 2
    A * * * * * * * * . * * . .
    K * * * * * * . . . . . . .
    Q * * * * * * . . . . . . .
    J * * . * * . . . . . . . .
    T * . . . * * . . . . . . .
    9 . . . . . * . . . . . . .
    8 . . . . . . * . . . . . .
    7 . . . . . . . * . . . . .
    6 . . . . . . . . * . . . .
    5 . . . . . . . . . . . . .
    4 . . . . . . . . . . . . .
    3 . . . . . . . . . . . . .
    2 . . . . . . . . . . . . .

one_time_eval.py (equity calculator)
--------

`python one_time_eval.py 3c4ckdqd 4d9s7d`

      [ 3 ♣ ] , [ 4 ♣ ]  
      [ K ♦ ] , [ Q ♦ ]  
    Board   [ 4 ♦ ] , [ 9 ♠ ] , [ 7 ♦ ]  
    [0.459, 0.541]

outs_odds_quiz.py
--------

      [ A ♠ ] , [ T ♣ ]  
      [ 2 ♦ ] , [ T ♦ ] , [ J ♠ ]  
    
    Starting with Pair
    5 outs, which are:
      [ A ♣ ] , [ T ♠ ] , [ A ❤ ] , [ T ❤ ] , [ A ♦ ]  
        3 outs to Two Pair
        2 outs to Three of a Kind
    Proportion: 0.106
    8.4 to 1

most_common_hands.py
--------

![Example R plot](https://dl.dropboxusercontent.com/u/38640281/github_img/poker-rplot.png)

          Flush  Four of a Kind      Full House       High Card            Pair 
          0.202           0.031           0.138          50.037          42.176 
       Straight  Straight Flush Three of a Kind        Two Pair 
          0.411           0.002           2.128           4.875 

omaha_nuts_quiz.py (quiz about the nut hand)
--------

      [ Q ♣ ] , [ A ❤ ] , [ 4 ❤ ]  
    Think hard... 
    Nuts: Three of a kind.
      [ Q ♣ ] , [ A ❤ ] , [ 4 ❤ ] , [ Q ♦ ]  
    Think hard... 
    Nuts: Four of a kind.
      [ Q ♣ ] , [ A ❤ ] , [ 4 ❤ ] , [ Q ♦ ] , [ K ♣ ]  
    Think hard... 
    Nuts: Four of a kind.
