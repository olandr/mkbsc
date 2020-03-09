#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = ["start", "draw", "Alead", "Blead", "Awin", "Bwin"]
#initial state
L0 = "start"
#action alphabet
Sigma = (("0a", "1a"), ("0b", "1b"))
#action labeled transitions
Delta = [
    ("start", ("0a", "0b"), "draw"),
    ("start", ("0a", "1b"),  "Blead"),
    ("start", ("1a", "0b"),  "Alead"),

    ("draw", ("0a", "0b"), "draw"),
    ("draw", ("0a", "1b"), "Blead"),
    ("draw", ("1a", "0b"),  "Alead"),

    ("Alead", ("0a", "0b"), "Alead"),
    ("Alead", ("0a", "1b"), "draw"),
    ("Alead", ("1a", "0b"), "Awin"),

    ("Blead", ("0a", "0b"), "Blead"),
    ("Blead", ("1a", "0b"),  "draw"),
    ("Blead", ("0a", "1b"), "Bwin")

]
#observation partitioning
Obs = [
    [["start"], ["draw", "Alead", "Blead"], ["Awin"], ["Bwin"]],
    [["start"], ["draw", "Alead", "Blead"], ["Awin"], ["Bwin"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
GK = G.KBSC()
export(GK, "GK")

#(log, GK2, iso_type) = iterate_until_isomorphic(G, limit=2, print_size=False, verbose=True)
#export(GK2, "GK2")
