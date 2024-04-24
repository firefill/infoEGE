# import sys
# sys.setrecursionlimit(2500)
# def f(n):
#     if n<11:
#         return n
#     if n>=11:
#         return n+f(n-1)
# print(f(2024)-f(2021))


# from functools import lru_cache
# def moves(h):
#     return h+1, h+4, h*3
# @lru_cache(None)
# def game(h):
#     if h>=88: return "W"
#     if any(game(m) == "W" for m in moves(h)):return "P1"
#     if all(game(m) == "P1" for m in moves(h)):return "B1"
#     if any(game(m) == "B1" for m in moves(h)):return "P2"
#     if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):return "B2"
#
# for s in range(1,200):
#     if game(s) == 'B2':
#         print(s, game(s))

#29
#25 28
#24 27229


# r = 30157
# summ = []
# while r % 2023 != 0:
#     r+=1
# for i in range(r, 10**8, 2023):
#     q = str(i)
#     if q[0]== "3":
#         if q[2] == "1":
#             if q[-1] == "7":
#                 if q[-2] == "5":
#                     summ.append((i,i//2023))
# print("25ая", *sorted(summ))

# f = open("26_9756.txt")
# r= f.readlines()
# n = int(r[0])
# r = r[1:]
# for x in range(n):
#     r[x]= list(map(int, r[x].split()))
# r = sorted(r)
# print(r)

