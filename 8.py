# from itertools import *
# c1 = '1357'
# c2 = '2468'
# count = 0
# for i in product(c1,c2,c1,c2,c1,c2,c1,c2,c1,c2,c1):
#     s = ''.join(i)
#     if s.count('1') < 5 and s.count('2') < 5 and s.count('3') < 5 and s.count('4') < 5 and s.count('5') < 5 and s.count('6') < 5 and s.count('7') < 5 and s.count('8') < 5:
#         count += 1
# print(count * 2)


def f(n) :
    s = str(n)
    if len(s) == 12:
        return 1
    a =[]
    for i in range (9) :
        if(n%10+i)%2==0 and i>n%10:
            a.append (int (s + str (i)))
    for i in range (9) :
        if (n% 10 + i) % 2 != 0 and i<n%10:
            a.append (int (s + str (i)))
    return sum(f(i) for i in a)
print(sum(f(1) for i in range(1, 9)))


