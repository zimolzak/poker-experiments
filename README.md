Poker Experiments
========

Just me playing around with `deuces` for Python.

Usage
--------

`tup upd` to render a PDF of how common are various poker hands.

`python omaha.py` to practice rapidly mentally figuring out what is
the nut hand.

Depends on
--------

* R
* ggplot2
* tup
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
