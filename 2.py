# print("x w y z u")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 for u in range(2):
#                     if (((x <= y) and (z == (not(w)) )) <= (u == (x or z))) == 0:
#                         print(x, w, y, z, u)

# print("x w y z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x == y) <= ((not(z)) or w )) == (not((w <= x) or (y<= z)))) == 1:
#                     print(x, w, y, z)
print("x w y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and not(y) ) or (x == z) or not(w)) == 0:
                    print(x, w, y, z)
