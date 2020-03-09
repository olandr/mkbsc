#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = [0, 1, 10, 11, 12, 21]
#initial state
L0 = 0
#action alphabet
Sigma = (("0a", "1a"), ("0b", "1b"))
#action labeled transitions
Delta = [
    (0, ("0a", "0b"),   0),
    (0, ("0a", "1b"),   1),
    (0, ("1a", "0b"),  10),
    (0, ("1a", "1b"),  11),
    (1, ("1a", "0b"),  11),
    (10, ("0a", "1b"), 11)

]
#observation partitioning
Obs = [
    [[0,  1], [10, 11, 12], [21]],
    [[0, 10], [1, 11, 21], [12]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
GK = G.KBSC()
GK0 = GK.project(0)

#export the GK game to ./pictures/GK.png
export(GK, "GK")
export(GK0, "GK0")
