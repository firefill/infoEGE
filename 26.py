# a =[]
# with open('26statgrad1.txt', 'r') as file:
#     lines = file.readlines()
#     lines = lines[1:]
#     for line in lines:
#         x, y = map(int, line.split())
#         a.append((y,x))
# a.sort()
# start = a[0][0] +15
# k = 1
# i = 1
# while i < len(a):
#     if a[i][1] >= start:
#         k +=1
#         old = start - 15
#         start = a[i][0]+15
#         p = i
#     i+=1
# i = p
# start = old + 15
# print(k)
# while i < len(a):
#     if a[i][1] >= start:
#         start = a[i][1]
#     i+=1
# print(start - old)
#
# f = open('26.txt', 'r')
# a = f.readlines()
# count = int(a[0])
# a=a[1:]
# w1 = [0]
# w2 = [0]
# welcome = 0
# welcome2 = 0
# b = []
# for i in range(len(a)):
#     x, y, z = map(int, a[i].split())
#     b.append((x,y,z))
# b.sort()
# for i in range(len(b)):
#     if len(w1)>1:
#         if b[i][0]>=w1[0]:
#             w1=w1[1:]
#     if len(w2) > 1:
#         if b[i][0]>=w2[0]:
#             w2=w2[1:]
#
#     if b[i][2] ==0:
#         if len(w1)>len(w2) and len(w2) < 12:
#             w2.append(max(w2[-1],b[i][0])+b[i][1])
#             welcome2+=1
#         elif len(w2)>=len(w1) and len(w1) < 12:
#             w1.append(max(w1[-1],b[i][0])+b[i][1])
#             welcome+=1
#         else:
#             continue
#     if b[i][2] == 1:
#         if len(w1) >=12:
#             continue
#         else:
#             w1.append(max(w1[-1],b[i][0])+b[i][1])
#             welcome+=1
#     if b[i][2] == 2:
#         if len(w2) >=12:
#             continue
#         else:
#             w2.append(max(w2[-1],b[i][0])+b[i][1])
#             welcome2+=1
# print(welcome, count-welcome-welcome2)
#
#
#
f = open('26_7626.txt')
r = f.readlines()
k  = int(r[0])
count = 0
number = 0
n = int(r[1])
s = []
l = [0]*(k+1)
r = r[2:]
for i in range(len(r)):
    x,y = map(int,r[i].split())
    s.append((x,y))
s.sort()

for i in range(len(s)):
    for g in range(1,k+1):
        if l[g] < s[i][0]:
            l[g] = s[i][1]
            count+=1
            number = g
            break
print(count)
print(number)


