# print("1ая задача - ижабедквг")
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if (((x or y)<= (y and z)) and ((w==x) or (w<= (not(z))))) == 1:
#                     print(x, y, z, w)
import sys

# print("2ая задача - zxyw")
# print("3яя задача - 74")
# print("4ая задача - 11011101100")
# k= 0
# print ("5ая задача - разобрать")
# print("6ая задача - 47")
# print("7ая задача - 20")
# qq = [[1,3,5],[0,2,4],[1,3,5],[0,2],[1,3,5],[0,2,4],[1,3,5]]
# s= 0
# count = 0
# for x1 in range(1,7):
#     for x2 in qq[x1]:
#             for x3 in qq[x2]:
#                 for x4 in qq[x3]:
#                     for x5 in qq[x4]:
#                         for x6 in qq[x5]:
#                             for x7 in qq[x6]:
#                                 for x8 in qq[x7]:
#                                     for x9 in qq[x8]:
#                                         for x10 in qq[x9]:
#                                             for x11 in qq[x10]:
#                                                 for x12 in qq[x11]:
#                                                     for x13 in qq[x12]:
#                                                         for x14 in qq[x13]:
#                                                             for x15 in qq[x14]:
#                                                                 for x16 in qq[x15]:
#
#                                                                     count += 1
# print(count)
#
# q = open("24.txt")
# c = q.readline()
# t = [-2]*10044
# v = [-2]*10044
# j=0
# a = 0
# for x in range(len(c)):
#     if c[x] == "C":
#         j+=1
#     if c[x] == "D":
#         j-=1
#     if c[x] == "D" or c[x] == "C":
#         if t[j + 5044] == -2:
#             t[j +5044] = x
#         v[j+5044] = x
# for x in range(10044):
#     a = max(v[x]-t[x],a)
# print(a)

# while j<len(cstr):
#     i=0
#     while i < len(cstr):
#         if cstr[i]>= dstr[i] and cstr[i-1]<dstr[i]:
#             lenstr = dstr[i]-cstr[j]
#         i+=1
#     j+=1
#     for x2 in range(x+lenstr+1,len(c)):
#         if c[x:x2].count("C") == c[x:x2].count("D"):
#             lenstr = x2-x

# v = 0
# q = open("27-B.txt")
# r = [int(x) for x in q.readlines()]
# k = r[0]
# n = r[1]
# r = r[2:]
# # for i in range(n):
# #     for j in range(i+2*k,n):
# #         if (r[i]*r[j])%100000 == 0:
# #             v+=1
# p=[0]*6
# for i in range(6):
#     p[i]=[0]*6
# for i in range(2*k,n):
#     a = r[i-2*k]
#     m = 0
#     u = 0
#     while a%2==0 and m<5:
#         a=a//2
#         m+=1
#     while a%5==0 and u<5:
#         a=a//5
#         u+=1
#     p[m][u]+=1
#     a = r[i]
#     m = 0
#     u = 0
#     while a%2==0 and m<5:
#         a=a//2
#         m+=1
#     while a%5==0 and u<5:
#         a=a//5
#         u+=1
#     for j in range(5-m,6):
#         for x in range(5-u,6):
#             v+=p[j][x]
# print(v)
#
# vladimir = 0
# zero = 0
# c = 0
# count = 0
# f = open("26.txt")
# r = f.readlines()
# n = int(r[0])
# r = r[1:]
# for x in range(n):
#     r[x] = r[x].split()
#     r[x][0] = int(r[x][0])
#     r[x][1] = int(r[x][1])
# r.sort()
# g = [0]*30
# for x in range(n):
#
#     if x == 0:
#         t = 0
#     else:
#         t = r[x-1][0]
#     while t< r[x][0]:
#         zero = 0
#         for z in range(30):
#             if g[z] > t:
#                 zero +=1
#         if zero <= 14:
#             vladimir +=1
#         t+=1
#     c=0
#     for y in range(30):
#         if g[y] <= r[x][0]:
#             g[y]=r[x][0]+r[x][1]
#             c+=1
#             break
#     if c == 0:
#         count+=1
#
# while t< 1440:
#     zero = 0
#     for z in range(30):
#         if g[z] > t:
#             zero +=1
#     if zero <= 14:
#         vladimir +=1
#     t+=1
# print(count,vladimir)


def f(a,b):
    if b == 0: return 0
    if b>0 and b%2==0: return 2*f(a,b//2)
    if b%2 != 0: return a + f(a,b-1)
for y in range(100000):
    for x in range(y-1):
        if f(x,y) == 89999:
            print(x,y)
            break
#301

# f = open("17.txt")
# s = [x[:-1] for x in f.readlines()]
# z = [int(x) for x in f.readlines()]
# maxc = 0
# minc = 100000
# for j in range(len(z)):
#     if s[j][-3:] == "652":
#         if maxc < z[j]:
#             maxc == z[j]
#         if minc > z[j]:
#             minc = z[j]
# maxsumm = 0
# count = 0
# for x in range(len(s)-3):
#     if (len(s[x]) == 5)+(len(s[x+1]) == 5) + (len(s[x+2]) == 5) + (len(s[x+3]) == 5) > (len(s[x]) == 4)+(len(s[x+1]) == 4) + (len(s[x+2]) == 4) + (len(s[x+3]) == 4) :
#         if ((int(s[x])%3 == 0) + (int(s[x+1])%3 == 0) + (int(s[x+2])%3 == 0) + (int(s[x+3])%3 == 0)) == ((int(s[x])%7 == 0) +(int(s[x+1])%7 == 0) +(int(s[x+2])%7 == 0) +(int(s[x+3])%7 == 0)):
#             if int(s[x])+ int(s[x+1]) + int(s[x+2]) + int(s[x+3]) > 2*(maxc+minc):
#                 count +=1
#                 if maxsumm < int(s[x])+ int(s[x+1]) + int(s[x+2]) + int(s[x+3]) :
#                     maxsumm = int(s[x])+ int(s[x+1]) + int(s[x+2]) + int(s[x+3])
# print(count,maxsumm)



# r=241609
# while r % 9517 !=0:
#     r +=1
# s = []
# star=[]
# for x in range(r,10**9, 9517):
#     if str(x)[0] == "2":
#         if str(x)[-1] == "9" :
#             if str(x)[-3] == "6":
#                 if str(x)[1:-3].count("41") >= 1:
#                     s.append(x)
#                 if str(x)[1:-3].count("41") == 1:
#                     star.append(x)
#
# print(s)
# print(star)
# maxs = 0
# s = 80
# for x in range(s):
#     for y in range(s):
#         for z in range(s):
#             ch1 = 1 + 2*s + 6*s**2 + z*s**3 + 4*s**4 + 5*s**5 + 7*s**6 + x*s**7 + 3*s**8 + 8*s**9 + 9*s**10
#             ch2 = 1 + 0*s + 9*s**2 + 4*s**3 + y*s**4 + 5*s**5 + 5*s**6 + 3*s**7 + z*s**8 + 7*s**9 + 8*s**10
#             if (ch1*ch2)%79 == 0 :
#                 maxs = max(maxs,z+y*s+x*s**2)
# print(maxs)

# count = 0
# for a in range(0,2**20):
#     flag = True
#     for x in range(1000):
#         if not((x&57476 == 0) <= ((x&90753 != 0) <= (x&a != 0))):
#             flag=False
#             break
#     if flag :
#         count+=1
# print(count)
# print('0'+bin(57665)[2:])
# print(bin(83265)[2:])
# print(bin(2**20)[2:])
# print(2**18)

# def f(x,y,n):
#     if x%2==0:
#         n+=1
#     if x>y or n>4:return 0
#     if x==y: return 1
#     if x<y: return f(x+1,y,n)+f(x*2,y,n)
# print(f(1,19,0))