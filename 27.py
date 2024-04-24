# A = open("27-A.txt")
# B = open("27-B.txt")
A = open("27stat-A.txt")
B = open("27stat-B.txt")

# способ 1

# c = A.readlines()
# k = int(c[0])
# u = []
# n = int(c[1])
# c = list(map(int,c[2:]))
# for x in range (len(c)-3*k):
#     for y in range (x+1, len(c)):
#         for z in range (max(y+1, x+3*k),len(c)):
#             u.append(c[x]+c[y]+c[z])
# print(max(u))

# способ 2
#
# c = A.readlines()
# k = int(c[0])
# v = 0
# n = int(c[1])
# c = list(map(int,c[2:]))
# for x in range (len(c)):
#     for y in range (x+1, len(c)):
#         for z in range (y+1,len(c)):
#             if z - x >= 3*k:
#                 v = max(v,c[x]+c[y]+c[z])
#
# print(v)

#способ 3 (не перебор)

# b = B.readlines()
# k = int(b[0])
# n = int(b[1])
# b = list(map(int,b[2:]))
# c = b[::-1]
# r = [0]
# for i in range(1,len(b)):
#     if b[i]>=b[r[-1]]:
#         r.append(i)
#     else:
#         r.append(r[-1])
# h = []
# z = r[-1]
# y = r[z-1]
# x = r[z-3*k]
# h.append(b[z]+b[y]+b[x])
# p = [0]
# for i in range(1,len(b)):
#     if c[i]>=c[p[-1]]:
#         p.append(i)
#     else:
#         p.append(p[-1])
#
# z = p[-1]
# y = p[z-1]
# x = p[z-3*k]
# h.append(c[z]+c[y]+c[x])
#
# y = r[-1]
# x = y
# while x>0:
#     x = r[x-1]
#     z = p[len(b)-(x+3*k)]
#     h.append(c[z]+b[y]+b[x])
#
# y = p[-1]
#
# z = y
# while z>0:
#     z = p[z-1]
#     x = r[len(b)-(z+3*k)]
#     h.append(c[z]+c[y]+b[x])
# print(max(h))

# y = 0
# f = open("27-A.txt")
# A = f.readlines()
# k = int(A[0])
# n = int(A[1])
# a = [int(x) for x in A[2:]]
# for i in range(n - 3*k):
#     for j in range(n):
#         if ( j!=i and j!=i+3*k ) and a[i]+a[j]+a[i+3*k]>y:
#             y = a[i]+a[j]+a[i+3*k]
# print(y)
#
#
# f = open("27-B.txt")
# A = f.readlines()
# b = []
# c = []
# y = []
# k = int(A[0])
# n = int(A[1])
# a = [int(x) for x in A[2:]]
# for x in range(n):
#     b.append((a[x], x))
# for i in range(n-3*k):
#     y.append((a[i] + a[i+3*k] , i , i+3*k))
# b.sort(reverse=True)
# y.sort(reverse=True)
# print(b[0][0] + y[0][0])
# print(b[:3])
# print(y[:3])
#

# f = open("27_rp.txt")
# a = f.readlines()
# k = int(a[0])
# summ = 0
# n = int(a[1])
# a = [int(x) for x in a[2:]]
# print(a)
# for i in range(len(a)):
#     for j in range(i+k, len(a)):
#         if summ < a[i]+a[j]:
#             summ = a[i]+a[j]
# print(summ)
#
#
# f = open("27_B_7627 (1).txt")
# a = f.readlines()
# k = int(a[0])
# n = int(a[1])
# c = []
# a = [int(x) for x in a[2:]]
# for x in range(len(a)):
#     c.append((a[x],x))
# c.sort(reverse=True)
# print(c[:100])
# print(k)
# print(9234919+9234916)
# b = [a[0]]
# for i in range(1,len(a)):
#     b.append(max(b[-1],a[i]))
# summ = 0
# for i in range(k,len(a)):
#     if summ < a[i]+b[i-k]:
#         summ = a[i]+b[i-k]
# print(summ)


# count = []
# f = open("27_B_9755.txt")
# r = f.readlines()
# k = int(r[0])
# n = int(r[1])
# r = [int(x) for x in r[2:]]
# a = [r[0]]
# b = [r[-1]]
# # for x in range(n):
# #     for y in range(x+k,n):
# #         for z in range(y+k,n):
# #             count.append(r[y]+r[z]+r[x])
# # print(min(count))
# for x in range(1,n):
#     if a[-1]>r[x]:
#         a.append(r[x])
#     else:
#         a.append(a[-1])
# for x in range(n-2,-1,-1):
#     if b[-1]>r[x]:
#         b.append(r[x])
#     else:
#         b.append(b[-1])
# b.reverse()
# for x in range(k,n-k):
#     count.append(b[x+k]+a[x-k]+r[x])
# print(min(count))


