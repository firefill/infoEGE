#первый способ
# with open('9onestatgrad.txt', 'r') as file:
#     count = 0
#     for line in file:
#         n = list(map(int, line.split()))
#         n.sort()
#         if (n[0] + n[5])/2 > (sum(n)-n[0]-n[5])/4 and len(n)==len(set(n)):
#             count+=1
# print(count)
# # второй способ
# k=0
# f = open('9onestatgrad.txt', 'r')
# for s in f:
#     a=sorted([int(x) for x in s.split()])
#     a2 = sorted([x for x in a if a.count(x)==2])
#     a1=[x for x in a if a.count(x)==1]
#     if len(a2)==6 and len(a1)==1 and (a2[0]-a2[5])/2 < sum(a1):
#         k+=1
# print(k)

#задачи

f = open('9onestatgrad.txt')
e=[]
e1=[]
e2=[]
e3=[]
e4=[]
e5=[]
e6=[]
for s in f:
    s=[int(x) for x in s.split()]
    e.append(s)
    e1.append(s[0])
    e2.append(s[1])
    e3.append(s[2])
    e4.append(s[3])
    e5.append(s[4])
    e6.append(s[5])
k=[e1,e2,e3,e4,e5,e6]
c=0

count=0
for i in range(0,len(e)):
    n=e[i]
    for j in range(0,6):
        if n.count(n[j])== 2 :
            for x in range(0,6):
                if n.count(n[x])== 2 and n[j]!=n[x]:
                    c+=1
        if c == 1 :
            if n.count(max(n))== 1:
                if max(n)*min(n) > sum(n)-max(n)-min(n):
                    count+=1


print(count)





