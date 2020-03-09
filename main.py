#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = [0, 1, 2, 10, 11, 12, 20, 21, 22]
#initial state
L0 = 0
#action alphabet
Sigma = (("0a", "1a", "2a"), ("0b", "1b", "2b"))
#action labeled transitions
Delta = [
    (0, ("0a", "0b"),   0),
    (0, ("0a", "1b"),   1),
    (0, ("1a", "0b"),  10),
    (0, ("1a", "1b"),  11),
    (1, ("1a", "0b"),  11),
    (10, ("0a", "1b"), 11),
    (0, ("2a", "0b"),  20),
    (0, ("2a", "1b"),  21),
    (0, ("2a", "2b"),  22),
    (0, ("0a", "2b"),   2),
    (0, ("1a", "2b"),  12),
    (1, ("2a", "0b"),  21),
    (1, ("2a", "1b"),  22),
    (2, ("1a", "0b"),  12),
    (2, ("2a", "0b"),  22),
    (0, ("0a", "2b"),   2),
    (10, ("0a", "2b"), 12),
    (10, ("1a", "2b"), 22),
    (10, ("0a", "2b"), 12),
    (11, ("1a", "1b"), 22),
    (11, ("0a", "1b"), 12),
    (11, ("1a", "0b"), 21)



]
#observation partitioning
Obs = [
    [[0,  1, 2], [10, 11, 12], [20, 21, 22]],
    [[0, 10, 20], [1, 11, 21], [2, 12, 22]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
GK = G.KBSC()
GK0 = GK.project(0)

#export the GK game to ./pictures/GK.png
export(GK, "GK")
export(GK0, "GK0")
