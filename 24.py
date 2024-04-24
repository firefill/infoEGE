# f = open("24.txt")
# maximum = 0
# lines = f.readline()
# for i in range(len(lines)):
#     for g in range(i+1+maximum,len(lines)):
#         s = lines[i:g]
#         if s.count("A") <= 2 and s.count("B") <= 2 :
#             if len(s)> maximum:
#                 maximum = len(s)
#         else:
#             break
# print(maximum)
#
#
# A = [-1]
# B = [-1]
# for i in range(len(lines)):
#     if lines[i]=="A":
#         A.append(i)
#     if lines[i]=="B":
#         B.append(i)
# A.append(len(lines))
# B.append(len(lines))
# maximum = 0
# for i in range(len(A)-3):
#     if lines[A[i]+1:A[i+3]].count("B") <= 2 and maximum < A[i+3] - A[i] -1:
#         maximum = A[i+3] - A[i] -1
# for i in range(len(B)-3):
#     if lines[B[i]+1:B[i+3]].count("A") <= 2 and maximum < B[i+3] - B[i] -1:
#         maximum = B[i+3] - B[i] -1
# print(maximum)
#
#
# alf = "UVWXYZ"
# c = 100
# f = open("24.txt")
# lines = f.readline()
# for i in range(len(lines)):
#     for g in range(i+c+1,len(lines)):
#         if lines[i:g].count("U") <= 100 and lines[i:g].count("V") <= 100 and lines[i:g].count("X") <= 100 and lines[i:g].count("Y") <= 100 and lines[i:g].count("Z") <= 100 and lines[i:g].count("W") <= 100:
#             c+=1
#         else:
#             break
# print(c)

f = open("24_9753.txt")
r = f.readline()
summ = 150
for x in range(len(r)):
    for y in range(x+summ+1, len(r)):
        if summ < len(r[x:y]):
            if r[x:y].count('Y') <= 150:
                summ = len(r[x:y])
            else:
                break
print(summ)
