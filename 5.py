# c=0
# m=0
# for A1 in range(0,1000):
#     A=[i for i in range(A1,A1+49)]
#     for n in range(0,400):
#         s=bin(n)[2::]
#         ost=bin(n%4)[2::]
#         s=s+ost
#         r=int(s,2)
#         if r in A:
#             c+=1
#     m=max(c, m)
#     c=0
# print(m)

c=0

# for n in range(250_000_000,1789456124//2):
#     if n % 4 > 1: r=n*4 + n%4
#     else: r = n*2 + n%2
#     if 1000000000<=r and r<=1789456123:
#         c+=1
# print(c)
#
# a = 0
# for i in range(1000000000,1789456124,1):
#     i = bin(i)[2:]
#     if (int(i[:-2],2) % 4 == int(i[-2:],2) and i[-2] != "0" ) or (int(i[:-1],2) % 4 == int(i[-1:],2) ):
#         a  += 1
# print(a)

# c=0
#
# for n in range(250_000_000,1789456124//2):
#     r=int(bin(n)[2:]+bin(n%4)[2:],2)
#     if 1000000000<=r and r<=1789456123:
#         c+=1
# print(c)
#
# for t in range(100,1000):
#     s = 0
#     i = bin(t)[2:]
#     while s != 3:
#         if i.count("1")== i.count("0"):
#             i += i[-1]
#         elif i.count("1") < i.count("0"):
#             i += "1"
#         elif i.count("1") > i.count("0"):
#             i += "0"
#         s+=1
#     if int(i,2) % 4 == 0:
#         print(t)
#
# for t in range(2,10000):
#     s = 0
#     chet = []
#     nechet = []
#     i = bin(t)[2:]
#     for x in range(len(i)):
#         if (x+1) % 2 == 0:
#             chet.append(i[x])
#         else:
#             nechet.append(i[x])
#     if abs(chet.count("1") - nechet.count("0") )== 5:
#         print(t)
#
# for t in range(2,10000000):
#     i = bin(t)[2:]
#     i = i[:-1]+ i[1]+i[1]
#     if int(i,2) > 92:
#         print(t)
#         break

for t in range(2,10000000):
    i = bin(t)[2:]
    i += i[-2]+ i[1]
    if int(i,2) > 150:
        print(t)
        break
