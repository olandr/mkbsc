#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = ["0", "1", "win"]
#initial state
L0 = "0"
#action alphabet
Sigma = (("0", "t", "-1"), ("0", "t", "-1"))
#action labeled transitions
Delta = [
    ("0", ("-1", "-1"),   "0"),
    ("0", ("-1", "0"),   "0"),
    ("0", ("-1", "t"),   "1"),
    ("0", ("0", "-1"),   "0"),
    ("0", ("0", "0"),   "0"),
    ("0", ("0", "t"),   "0"),
    ("0", ("t", "-1"),   "1"),
    ("0", ("t", "0"),   "0"),
    ("0", ("t", "t"),   "1"),

    ("1", ("-1", "-1"),   "win"),
    ("1", ("-1", "0"),   "0"),
    ("1", ("-1", "t"),   "0"),
    ("1", ("0", "-1"),   "0"),
    ("1", ("0", "0"),   "0"),
    ("1", ("0", "t"),   "0"),
    ("1", ("t", "-1"),   "0"),
    ("1", ("t", "0"),   "0"),
    ("1", ("t", "t"),   "0"),
]
#observation partitioning
Obs = [
    [["0", "1"], ["win"]],
    [["0", "1"], ["win"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)

GK = G.KBSC()
export(GK, "GK")

#(log2, GK2, iso_type2) = iterate_until_isomorphic(G, limit=2, print_size=False, verbose=True)
#export(GK2, "GK2")
#print(log2, GK2, iso_type2)
