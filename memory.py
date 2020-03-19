#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = ["start", 0, 1, "win", "lose"]
#initial state
L0 = "start"
#action alphabet
Sigma = (("0", "t", "-1"), ("0", "t", "-1"))
#action labeled transitions
Delta = [
    ("start", ("-1", "-1"),   "lose"),
    ("start", ("-1", "0"),    0),
    ("start", ("-1", "t"),    1),
    ("start", ("0", "-1"),    0),
    ("start", ("0", "0"),     0),
    ("start", ("0", "t"),     0),
    ("start", ("t", "-1"),    1),
    ("start", ("t", "0"),     0),
    ("start", ("t", "t"),     1),

    (0, ("-1", "-1"),         "lose"),
    (0, ("-1", "0"),          0),
    (0, ("0", "-1"),          0),
    (0, ("0", "0"),           0),
    (0, ("-1", "t"),          1),
    (0, ("0", "t"),           1),
    (0, ("t", "-1"),          1),
    (0, ("t", "0"),           1),
    (0, ("t", "t"),           1),

    (1, ("-1", "-1"),         "win"),
    (1, ("-1", "0"),          0),
    (1, ("-1", "t"),          0),
    (1, ("0", "-1"),          0),
    (1, ("0", "0"),           0),
    (1, ("0", "t"),           0),
    (1, ("t", "-1"),          0),
    (1, ("t", "0"),           0),
    (1, ("t", "t"),           0),
]
#observation partitioning
Obs = [
    [["start"], [0, 1], ["win"], ["lose"]],
    [["start"], [0, 1], ["win"], ["lose"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)

GK = G.KBSC()
export(GK, "memory_GK")

(log2, GK2, iso_type2) = iterate_until_isomorphic(G, limit=-1, print_size=False, verbose=True)
export(GK2, "memory_GK2")
print(log2, GK2, iso_type2)
