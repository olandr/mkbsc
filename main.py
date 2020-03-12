#!/usr/bin/env python3

from mkbsc import MultiplayerGame, iterate_until_isomorphic, \
                  export, to_string, from_string, to_file, from_file

#states
L = ["0", "1", "*", "win", "lose"]
#initial state
L0 = "0"
#action alphabet
Sigma = (("r", "w"), ("r","w"))
#action labeled transitions
Delta = [
    ("0", ("r", "r"), "0"),
    ("0", ("r", "w"), "1"),
    ("0", ("w", "r"), "1"),
    ("0", ("w", "w"), "*"),

    ("1", ("r", "r"), "1"),
    ("1", ("r", "w"), "win"),
    ("1", ("w", "r"), "win"),
    ("1", ("w", "w"), "*"),

    ("*", ("r", "r"), "*"),
    ("*", ("r", "w"), "*"),
    ("*", ("w", "r"), "*"),
    ("*", ("w", "w"), "*"),


]
#observation partitioning
Obs = [
    [["0", "*", "1"], ["win"], ["lose"]],
    [["0", "1", "*"], ["win"], ["lose"]]
]

#G is a MultiplayerGame-object, and so are GK and GK0
#G = MultiplayerGame.create(L, L0, Sigma, Delta, Obs)
G = from_file("stuff")
GK = G.KBSC()
export(GK, "GK")


'''
(log2, GK2, iso_type2) = iterate_until_isomorphic(G, limit=2, print_size=False, verbose=True)
export(GK2, "GK2")
print(log2, GK2, iso_type2)
(log3, GK3, iso_type3) = iterate_until_isomorphic(G, limit=3, print_size=False, verbose=True)
export(GK3, "GK3")
print(log3, GK3, iso_type3)

(logi, GKi, iso_typei) = iterate_until_isomorphic(G, limit=-1, print_size=False, verbose=True)
export(GKi, "GKi")
print(logi, GKi, iso_typei)
'''
