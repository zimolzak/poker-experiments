Poker Experiments
========

Just me playing around with `deuces` for Python.

Usage
--------
* Completely user-facing

    * `make` to render (most interstingly) a text file `output.txt` of
      multiple tables. Also a PDF of how common are various poker
      hands, and the "flow" of several heads-up situations over the
      course of several streets.

    * `python omaha.py` to practice rapidly mentally figuring out what
      is the nut hand.

    * `python one_time_eval.py as8sqdtc`
    * `python outs_odds_quiz.py` or `source outs_loop.sh`
    * `python range.py 15`
    * `python count_hands.py`
* Usually called by makefile
    * best_hole_cards.py (multi-proc, > best_hole_cards > R > txt). 
      Big csv. Each proc takes about 1 min on my macbook (2.7ghz i7).

    * most_common_hands.py (> hand_ranks > R > pdf)
    * evolution_of_nut.py (> evolution_of_nut > R > txt)
    * theo_actual_nut.py (theo_actual_nut > R > txt)
    * pct_vs_time.py (multi-proc, > pct_vs_time > R > pdf). Long compute.
* Purely library
    * nuts.py
    * convenience.py
    * future.py (generally dumping ground of functions not currently used)
    * convenience_hole.py

Depends on
--------
* R
* ggplot2
* deuces

Example of omaha.py
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

Example of most_common_hands.py
--------

![Example R plot](https://dl.dropboxusercontent.com/u/38640281/github_img/poker-rplot.png)

          Flush  Four of a Kind      Full House       High Card            Pair 
          0.202           0.031           0.138          50.037          42.176 
       Straight  Straight Flush Three of a Kind        Two Pair 
          0.411           0.002           2.128           4.875 
