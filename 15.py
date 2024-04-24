
# для строки
# for x in [k*0.25 for k in range(-10000,10000)]:
#     p = 10<=x<=40
#     q = 5<=x<=15
#     r = 35<= x <=50
#     a = 0 #если большее то 1
#     f = (a or p) or (q <= r)
#     if f!=1 :  #обратное от a
#         print(round(x))
#
# #для множества
# for x in [k*0.25 for k in range(-10000,10000)]:
#     p = x in [2,4,6,8,10,12,14,16,18,20]
#     q = x in [3,6,9,12,15,18,20,24,27,30]
#     r = 35<= x <=50
#     a = 1 #если меньшее то 0
#     f = (a <= p) and ((not q) <= (not(a)))
#     if f!=0 :  #обратное от a
#         print(x)
#
# for A in range(1000):
#     p = True
#     for x in range(1000):
#         f = (x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))
#         if f == False:
#             p = False
#             break
#     if p == True:
#         print(A)
#         break
# def f(x, a):
#     p = set([i * 2 for i in range(1, 11)])
#     q = set([i * 3 for i in range(1, 11)])
#     return ((x in p) <= (x in a)) or ((not (x in a)) <= (not(x in q)))
# a = set()
# for x in range(2000):
#     if not(f(x, a)):
#         a.add(x)
# print(sum(a))
#
# def f(x, a):
#     p = set([i for i in range(10, 31)])
#     q = set([i for i in range(20, 41)])
#     return (not(x in a)) <= ((x in p) <= (not(x in q)))
# a = set()
# for x in range(1,50,2):
#     if not(f(x, a)):
#         a.add(x)
# print(len(a))
#
# for alen in range(1,100):
#     for alef in range(50):
#         count = 0
#         for x in range(-100,400):
#             if (not(alef<=x/2<=alef+alen)) <= ((10<=x/2<=30) <= (not(20<=x/2<=40))):
#                 count+=1
#         if count == 500:
#             print(alen,alef)
# summ = 0
# for a in range(100):
#     p = True
#     for x in range(100):
#         for y in range(100):
#             f = ((x < a) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= a))
#             if f == False:
#                 p = False
#                 break
#     if p == True:
#         summ+=1
# print(summ)

# summ = 0
# for a in range(100):
#     p = True
#     for x in range(100):
#         for y in range(100):
#             f = (((2*x)+(3*y)) < 30 ) or ((x + y) >= a)
#             if f == False:
#                 p = False
#                 break
#     if p == True:
#         if summ < a : summ = a
# print(summ)

# t = 0
# for a in range(1,1000):
#     count = 0
#     for n in range(1,1000):
#         if ((not(n%a == 0)) <= ((n%6==0) <=  (not(n%4==0)))) == 1:
#             count+=1
#     if count == 999:
#         t = a
# print(t)

for A in range(1000):
    p = True
    for x in range(1000):
        f = (x & A != 0) <= ((x & 36 == 0) <= (x & 6 != 0))
        if f == False:
            p = False
            break
    if p == True:
        print(A)

# for A in range(1000):
#     p = True
#     for x in range(1000):
#         f = (x & 49 != 0) <= ((x & 41 == 0) <= (x & A != 0))
#         if f == False:
#             p = False
#             break
#     if p == True:
#         print(A)
#         break
#
# y = []
# for x in [k*0.25 for k in range(-10000,10000)]:
#     p = x in [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
#     q = x in [30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65]
#     a = x in y
#     f = (not(a)) <= (p <= (not(q)))
#     if f!=1 :
#         y.append(x)
# print(max(y)-min(y))