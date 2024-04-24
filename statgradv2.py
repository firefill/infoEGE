print("1ая задача - 14")
# print("x w y z u")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 for u in range(2):
#                     if (((x <= y) and (z == (not(w)) )) <= (u == (x or z))) == 0:
#                         print(x, w, y, z, u)
print("2ая wzyxu")
print("3ая m35")
from functools import lru_cache
print("4 номер 35")

c=0
m=0
for A1 in range(0,1000):
    A=[i for i in range(A1,A1+49)]
    for n in range(0,400):
        s=bin(n)[2::]
        ost=bin(n%4)[2::]
        s=s+ost
        r=int(s,2)
        if r in A:
            c+=1
    m=max(c, m)
    c=0
print("5 задача ",m)
#4 - 35
print("6ая задача - 59")
print("7 номер", 1024*768*12*0.8/(200*8*1024))

from itertools import *
c1 = '2468'
c2 = '1357'
count = 0
for i in product(c1,c2,c1,c2,c1,c2,c1,c2,c1,c2,c1):
    s = ''.join(i)
    if s.count('1') < 5 and s.count('2') < 5 and s.count('3') < 5 and s.count('4') < 5 and s.count('5') < 5 and s.count('6') < 5 and s.count('7') < 5 and s.count('8') < 5:
        count += 1
print("8ая задача ",count * 2)

#10 - 2214
k = 0
with open('9_stat.txt', 'r') as f:
    for line in f:
        numbers = [int(x) for x in line.split()]
        max_num = max(numbers)
        repeated_nums = [num for num in set(numbers) if numbers.count(num) > 1]
        repeated_sum = sum([num * numbers.count(num) for num in repeated_nums])

        if len(repeated_nums) > 0 and max_num not in repeated_nums and repeated_sum > max_num:
            k += 1
print("9ая ответ",k)
print("10 номер 2214")
print("11 номер 16640")
m=[]
for a1 in range(0,50):
    for a2 in range(0,50):
        for a3 in range(0,50):
            A='0'+'1'*a1+'2'*a2+'3'*a3+'0'
            B=A
            while '00' not in A:
                if '01' in A:
                    A=A.replace('01', '220', 1)
                if '02' in A:
                    A=A.replace('02', '1013', 1)
                if '03' in A:
                    A=A.replace('03', '120', 1)
            if A.count('1')==13 and A.count('2')==18:
                m.append(len(B))
print("12ая задача -",m)
print("13ая задача - 240")
c = []
for x in range(40):
    for y in range(40):
        t = 5*40**8+7*40**7+x*40**6+6*40**5+9*40**4+2*40**3+y*40**2+1*40*1+9
        if t % 39 == 0 and (y*40**1+x)**0.5==round((y*40**1+x)**0.5):
            c.append(y*40**1+x)
print("14 задача",max(c))
def f(x, a):
    return ((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0)
for a in range(1, 300):
    p = True
    for x in range(0, 300):
        if f(x, a) == False:
            p = False
            break
    if p == True:
        print("15 номер ",a)
        break




p = ["0","1","3","5","7","9"]
summ = 0
k = [0]*10
for k[0] in p:
    for k[1] in p:
        for k[2] in p:
            for k[3] in p:
                for k[4] in p:
                    for k[5] in p:
                        for k[6] in p:
                            for k[7] in p:
                                for k[8] in p:
                                    summ+=1
print("16 номер ", summ)

f = [int(i) for i in open("17.txt")]
m = 0
for i in range(0,len(f)):
    r = f[i]
    if str(r)[-3:]== "123" and m<r:
        m = r
k=0
summa = []
for i in range(0 , len(f)-2):
    if ((len(str(f[i]))==5) + (len(str(f[i+1]))==5)+(len(str(f[i+2]))==5)>=2 ) and ((f[i]%3==0) + (f[i+1]%3==0) + (f[i+2]%3==0) == 1) and (f[i]+f[i+1]+f[i+2]>m):
        k = k+1
        summa.append(f[i]+f[i+1]+f[i+2])
print("17 номер ",k,max(summa))

# def moves(h):
#     if h%2==0 and h%3==0: return h+1,h+(h/2), h+(h/3)
#     if h % 2 == 0: return h+1, h+(h/2)
#     if h % 3 == 0: return h+1, h+(h/3)
#     if h % 2 != 0 and h % 3 != 0: return h+1, h*2
# @lru_cache(None)
# def game(h):
#     if h>=96: return "W"
#     if any(game(m) == "W" for m in moves(h)):return "P1"
#     if all(game(m) == "P1" for m in moves(h)):return "B1"
#     if any(game(m) == "B1" for m in moves(h)):return "P2"
#     if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):return "B2"
#
# for s in range(1,700):
#     if game(s) == 'B1':
#         print(s, game(s))

print("19 задача - 48")
print("20 задача - 5762")
print("21 задача - 56")

def f(a,b,c):
    if c > 1: return 0
    if a > b+1: return 0
    if a ==b: return 1
    return f(a-1,b,c+1)+f(a*2,b,0)+f(a*3,b,0)


print("23",f(3,20, 0))

r = 1430201
summ = []
while r % 3147 != 0:
    r+=1
for i in range(r, 10**10, 3147):
    q = str(i)
    if q[0]== "1":
        if q[-1] == "1":
            if q[-6:-2] == "4302":
                summ.append(i)
print("25ая", sorted(summ), len(summ))


f = open('26.txt', 'r')
a = f.readlines()
count = int(a[0])
a=a[1:]
w1 = [0]
w2 = [0]
welcome = 0
welcome2 = 0
b = []
for i in range(len(a)):
    x, y, z = map(int, a[i].split())
    b.append((x,y,z))
b.sort()
for i in range(len(b)):
    if len(w1)>1:
        if b[i][0]>=w1[0]:
            w1=w1[1:]
    if len(w2) > 1:
        if b[i][0]>=w2[0]:
            w2=w2[1:]

    if b[i][2] ==0:
        if len(w1)>len(w2) and len(w2) < 12:
            w2.append(max(w2[-1],b[i][0])+b[i][1])
            welcome2+=1
        elif len(w2)>=len(w1) and len(w1) < 12:
            w1.append(max(w1[-1],b[i][0])+b[i][1])
            welcome+=1
        else:
            continue
    if b[i][2] == 1:
        if len(w1) >=12:
            continue
        else:
            w1.append(max(w1[-1],b[i][0])+b[i][1])
            welcome+=1
    if b[i][2] == 2:
        if len(w2) >=12:
            continue
        else:
            w2.append(max(w2[-1],b[i][0])+b[i][1])
            welcome2+=1
print("26ая задача",welcome, count-welcome-welcome2)

