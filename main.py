#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = ["draw", "a", "b", "ab", "aa", "bb", "aab", "aabb", "abb", "A", "B"]
#initial state
L0 = "draw"
#action alphabet
Sigma = (("0a", "1a"), ("0b", "1b"))
#action labeled transitions
Delta = [
    ("draw", ("0a", "0b"),  "draw"),
    ("draw", ("0a", "1b"),  "b"),
    ("draw", ("1a", "0b"),  "a"),
    ("draw", ("1a", "1b"),  "ab"),

    ("a", ("0a", "0b"),  "a"),
    ("a", ("0a", "1b"),  "ab"),
    ("a", ("1a", "0b"),  "aa"),
    ("a", ("1a", "1b"),  "aab"),

    ("b", ("0a", "0b"),  "b"),
    ("b", ("0a", "1b"),  "bb"),
    ("b", ("1a", "0b"),  "ab"),
    ("b", ("1a", "1b"),  "abb"),

    ("ab", ("0a", "0b"),  "ab"),
    ("ab", ("0a", "1b"),  "abb"),
    ("ab", ("1a", "0b"),  "aab"),
    ("ab", ("1a", "1b"),  "aabb"),

    ("aa", ("0a", "0b"),  "aa"),
    ("aa", ("0a", "1b"),  "aab"),
    ("aa", ("1a", "0b"),  "A"),
    ("aa", ("1a", "1b"),  "A"),

    ("bb", ("0a", "0b"),  "bb"),
    ("bb", ("0a", "1b"),  "B"),
    ("bb", ("1a", "0b"),  "abb"),
    ("bb", ("1a", "1b"),  "B"),

    ("aab", ("0a", "0b"),  "A"),
    ("aab", ("0a", "1b"),  "draw"),
    ("aab", ("1a", "0b"),  "A"),
    ("aab", ("1a", "1b"),  "A"),

    ("abb", ("0a", "0b"),  "B"),
    ("abb", ("0a", "1b"),  "B"),
    ("abb", ("1a", "0b"),  "draw"),
    ("abb", ("1a", "1b"),  "B"),

    ("aabb", ("0a", "0b"),  "draw"),
    ("aabb", ("0a", "1b"),  "B"),
    ("aabb", ("1a", "0b"),  "A"),
    ("aabb", ("1a", "1b"),  "draw")
]
#observation partitioning
Obs = [
    [["draw", "b", "bb"], ["a", "ab", "abb"], ["aa", "aab", "aabb"], ["A"], ["B"]],
    [["draw", "a", "aa"], ["b", "ab", "aab"], ["bb", "abb", "aabb"], ["A"], ["B"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)

GK = G.KBSC()
export(GK, "GK")

(log, GK2, iso_type) = iterate_until_isomorphic(G, limit=2, print_size=False, verbose=True)
export(GK2, "GK2")
