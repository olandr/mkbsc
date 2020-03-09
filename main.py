#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = ["draw", "Alead", "Blead", "Awin", "Bwin"]
#initial state
L0 = "draw"
#action alphabet
Sigma = (("-a", "a", "+a"), ("-b", "b", "+b"))
#action labeled transitions
Delta = [
    ("draw", ("+a", "b"),  "Alead"),
    ("draw", ("+a", "-b"),  "draw"),
    ("draw", ("+a", "+b"),  "draw"),

    ("draw", ("-a", "b"),  "draw"),
    ("draw", ("-a", "-b"),  "draw"),
    ("draw", ("-a", "+b"),  "draw"),

    ("draw", ("a", "b"),  "draw"),
    ("draw", ("a", "-b"),  "draw"),
    ("draw", ("a", "+b"),  "Blead"),

    ("Alead", ("+a", "b"),  "Awin"),
    ("Alead", ("+a", "-b"),  "Alead"),
    ("Alead", ("+a", "+b"),  "Awin"),

    ("Alead", ("-a", "b"),  "Alead"),
    ("Alead", ("-a", "-b"),  "Alead"),
    ("Alead", ("-a", "+b"),  "Alead"),

    ("Alead", ("a", "b"),  "Alead"),
    ("Alead", ("a", "-b"),  "draw"),
    ("Alead", ("a", "+b"),  "draw"),

    ("Blead", ("+a", "b"),  "draw"),
    ("Blead", ("+a", "-b"),  "Blead"),
    ("Blead", ("+a", "+b"),  "Bwin"),

    ("Blead", ("-a", "b"),  "draw"),
    ("Blead", ("-a", "-b"),  "Blead"),
    ("Blead", ("-a", "+b"),  "Blead"),

    ("Blead", ("a", "b"),  "Blead"),
    ("Blead", ("a", "-b"),  "Blead"),
    ("Blead", ("a", "+b"),  "Bwin")


]
#observation partitioning
Obs = [
    [["draw", "Alead", "Blead"], ["Awin"], ["Bwin"]],
    [["draw", "Alead", "Blead"], ["Awin"], ["Bwin"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
GK = G.KBSC()
export(GK, "GK")

(log, GK2, iso_type) = iterate_until_isomorphic(G, limit=2, print_size=False, verbose=True)
export(GK2, "GK2")
