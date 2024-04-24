#
#
# from functools import lru_cache
# def moves(h):
#     if h % 2 == 0: return h+1, h*1.5
#     else: return h+1, h*2
# @lru_cache(None)
# def game(h):
#     if h>=108: return "W"
#     if any(game(m) == "W" for m in moves(h)):return "P1"
#     if all(game(m) == "P1" for m in moves(h)):return "B1"
#     if any(game(m) == "B1" for m in moves(h)):return "P2"
#     if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):return "B2"
#
# for s in range(1,200):
#     if game(s) == 'B2':
#         print(s, game(s))
#19statgrad answer = 70
#20statgrad answer = 2729
#21statgrad answer = 52

from functools import lru_cache
def moves(h):
    m=[]
    for k in range(2,s+1):
        if h%k==0:
            m.append(h-h//k)
    return m
@lru_cache(None)
def game(h):
    if any(m<13 for m in moves(h)): return "W"
    if all(game(m) == "W" for m in moves(h)):return "P1"
    if any(game(m) == "P1" for m in moves(h)):return "B1"
    if all(game(m) == "B1" or game(m) =="W" for m in moves(h)) and any(game(m) == "B1"  for m in moves(h)):return "P2"

for s in range(13,200):
    if game(s) == 'P2':
        print(s, game(s))
#15
#39 83