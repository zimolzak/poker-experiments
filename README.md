Poker Experiments
========

Just me playing around with `deuces` for Python.

Usage
--------

`make` to render a PDF of how common are various poker hands, and the
"flow" of several heads-up situations over the course of several
streets; and a text file of several tables, in particular pertinent to
nut hands.

`python omaha.py` to practice rapidly mentally figuring out what is
the nut hand.

`python one_time_eval.py as8sqdtc`

Index
--------
* Completely user-facing
    * omaha.py
    * one_time_eval.py
    * test.py
    * outs_odds_quiz.py
    * outs_loop.sh
* Usually called by makefile
    * ring_game.py (multi-proc, > ringwinners > R > txt)
    * poker-stats.py (> hand_ranks > R > pdf)
    * flop_turn_river.py (> progression > R)
    * theo_actual_nut.py (freq_of_nut > R > txt)
    * pct_vs_time.py (multi-proc, > aavjqs > R > pdf)
* Purely library
    * nuts.py
    * convenience.py

Depends on
--------
* R
* ggplot2
* deuces

Example
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


![Example R plot](https://dl.dropboxusercontent.com/u/38640281/github_img/poker-rplot.png)

          Flush  Four of a Kind      Full House       High Card            Pair 
          0.202           0.031           0.138          50.037          42.176 
       Straight  Straight Flush Three of a Kind        Two Pair 
          0.411           0.002           2.128           4.875 
