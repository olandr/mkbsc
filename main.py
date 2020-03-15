#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = ["0", "1", "2", "win"]
#initial state
L0 = "0"
#action alphabet
Sigma = (("0", "+1"), ("0","+1"))
#action labeled transitions
Delta = [
    ("0", ("0", "0"), "0"),
    ("0", ("0", "+1"), "1"),
    ("0", ("+1", "0"), "1"),
    ("0", ("+1", "+1"), "2"),

    ("1", ("0", "0"), "1"),
    ("1", ("0", "+1"), "2"),
    ("1", ("+1", "0"), "2"),
    ("1", ("+1", "+1"), "win"),

    ("2", ("0", "0"), "2"),
    ("2", ("0", "+1"), "win"),
    ("2", ("+1", "0"), "win"),
    ("2", ("+1", "+1"), "win"),


]
#observation partitioning
Obs = [
    [["0"], ["1", "2"], ["win"]],
    [["0"], ["1"], ["2"], ["win"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
export(G, "G")
GK = G.KBSC()
export(GK, "GK")



(log2, GK2, iso_type2) = iterate_until_isomorphic(G, limit=2, print_size=False, verbose=True)
export(GK2, "GK2")
print(log2, GK2, iso_type2)

'''
(log3, GK3, iso_type3) = iterate_until_isomorphic(G, limit=3, print_size=False, verbose=True)
export(GK3, "GK3")
print(log3, GK3, iso_type3)

'''
(logi, GKi, iso_typei) = iterate_until_isomorphic(G, limit=-1, print_size=False, verbose=True)
export(GKi, "GKi")
print(logi, GKi, iso_typei)
