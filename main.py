#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = ["start", "draw", "0", "1", "a", "b", "aab", "abb", "A", "B"]
#initial state
L0 = "start"
#action alphabet
Sigma = (("0a", "1a"), ("0b", "1b"))
#action labeled transitions
Delta = [
    ("start", ("0a", "0b"),  "0"),
    ("start", ("0a", "1b"),  "b"),
    ("start", ("1a", "0b"),  "a"),
    ("start", ("1a", "1b"),  "0"),

    ("0", ("0a", "0b"),  "1"),
    ("0", ("0a", "1b"),  "B"),
    ("0", ("1a", "0b"),  "A"),
    ("0", ("1a", "1b"),  "1"),

    ("a", ("0a", "0b"),  "1"),
    ("a", ("0a", "1b"),  "abb"),
    ("a", ("1a", "0b"),  "A"),
    ("a", ("1a", "1b"),  "A"),

    ("b", ("0a", "0b"),  "1"),
    ("b", ("0a", "1b"),  "B"),
    ("b", ("1a", "0b"),  "aab"),
    ("b", ("1a", "1b"),  "B"),

    ("1", ("0a", "0b"),  "draw"),
    ("1", ("0a", "1b"),  "B"),
    ("1", ("1a", "0b"),  "A"),
    ("1", ("1a", "1b"),  "draw"),

    ("abb", ("0a", "0b"),  "B"),
    ("abb", ("0a", "1b"),  "B"),
    ("abb", ("1a", "0b"),  "draw"),
    ("abb", ("1a", "1b"),  "B"),

    ("aab", ("0a", "0b"),  "A"),
    ("aab", ("0a", "1b"),  "draw"),
    ("aab", ("1a", "0b"),  "A"),
    ("aab", ("1a", "1b"),  "A")

]
#observation partitioning
Obs = [
    [["start"], ["draw", "0", "1"], ["b"], ["a", "abb"], ["aab"], ["A"], ["B"]],
    [["start"], ["draw", "0", "1"], ["a"], ["b", "aab"], ["abb"], ["A"], ["B"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)

GK = G.KBSC()
export(GK, "GK")

#(log2, GK2, iso_type2) = iterate_until_isomorphic(G, limit=2, print_size=False, verbose=True)
#export(GK2, "GK2")
