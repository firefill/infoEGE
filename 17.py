# f = open("17-1.txt")
# a = []
# for s in f :
#     a.append(int(s))
# k=0
# summa = []
# for i in range(0 , len(a)-1):
#     if (a[i]%7==0 and a[i+1]%17!=0) or (a[i+1]%7==0 and a[i]%17!=0):
#         k=k+1
#         summa.append(a[i]+a[i+1])
# print(k)
# print(min(summa))

# f = open("17-338.txt")
# a = []
# for s in f :
#     a.append(int(s))
# k=0
# minimum = min(a)
# summa = []
# for i in range(0 , len(a)-1):
#     if a[i]%117==min(a) or a[i+1]%117==min(a):
#         k=k+1
#         summa.append(a[i]+a[i+1])
# print(k)
# print(max(summa))


# f = open("17-339.txt")
# a = []
# m = []
# for s in f :
#     a.append(int(s))
#     if int(s)%19==0 and int(s)>0:
#         m.append(int(s))
# k=0
# summa = []
# for i in range(0 , len(a)-1):
#     if a[i]+a[i+1]<min(m):
#         k=k+1
#         summa.append(a[i]+a[i+1])
# print(k)
# print(max(summa))


# f = open("17-243.txt")
# a = []
# # m = ""
# for s in f :
#     a.append(int(s))
# for s in range(0,len(a)):
#     r = a[s]
#     if r%37==0:
#         while r>0:
#             m+=r%10
#             r//=10
# k=0
# print(s)
# summa = []
# for i in range(0 , len(a)-1):
#     if a[i]> m and a[i+1]>m:
#         k=k+1
#         summa.append(a[i]+a[i+1])
# print(k)
# print(max(summa))


# f = [int(i) for i in open("17-243.txt")]
# m = 0
# for i in range(0,len(f)):
#     r = f[i]
#     if r%49==0:
#         while r>0:
#             m+=r%10
#             r//=10
# k=0
# summa = []
# for i in range(0 , len(f)-1):
#     if (f[i]< m and f[i+1]%13==0 and f[i+1]>=m) or (f[i]%13==0 and f[i+1]<m and f[i]>=m) :
#         k=k+1
#         summa.append(f[i]+f[i+1])
# print(k)
# print(max(summa))

#
# f = [int(i) for i in open("17-3.txt")]
# m = 0
# for i in range(0,len(f)):
#     r = f[i]
#     if str(r)[-1] == "3" and m<r:
#         m = r
# k=0
# summa = []
# for i in range(0 , len(f)-1):
#     if ((str(f[i])[-1]=="3" and str(f[i+1])[-1]!="3") or (str(f[i+1])[-1]=="3" and str(f[i])[-1]!="3") ) and (f[i+1]**2)+(f[i]**2)>=m**2:
#         k = k+1
#         summa.append(f[i]+f[i+1])
# print(k)
# print(max(summa))




# f = [int(i) for i in open("17.txt")]
# m = 0
# for i in range(0,len(f)):
#     r = f[i]
#     if str(r)[-3:]== "123" and m<r:
#         m = r
# k=0
# summa = []
# for i in range(0 , len(f)-1):
#     if ((len(str(f[i]))==5 and len(str(f[i+1]))==5) or (len(str(f[i+1]))==5 and len(str(f[i+2]))==5) or (len(str(f[i]))==5 and len(str(f[i+2]))==5)) and ((f[i]%3==0 and f[i+1]%3!=0 and f[i+2]%3!=0) or (f[i]%3!=0 and f[i+1]%3==0 and f[i+2]%3!=0) or (f[i]%3!=0 and f[i+1]%3!=0 and f[i+2]%3==0)) and (f[i]+f[i+1]+f[i+2]> m):
#         k = k+1
#         summa.append(f[i]+f[i+1]+f[i+2])
# print(k)
# print(max(summa))

t = 0
f = open("17stattxt")
maxx = 0
maxik = []
a = [int(x) for x in f.readlines()]
for x in range(len(a)):
    if str(a[x])[-3:] == "238" and maxx < a[x]:
        maxx = a[x]

for i in range(len(a)-2):
    if 0 < ((len(str(a[i])) == 5) + (len(str(a[i+1])) ==5) + (len(str(a[i+2])) == 5)) <3:
        if ((a[i] % 3== 0) + (a[i+1] % 3==0 ) + (a[i+2] % 3 == 0)) > (a[i] % 5 == 0) + (a[i+1] % 5 == 0) + (a[i+2] % 5 == 0):
            if a[i]+a[i+1]+a[i+2] > maxx:
                maxik.append(a[i]+a[i+1]+a[i+2])
print(len(maxik), max(maxik))