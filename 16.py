def F(n):
    if n == 0:
        return 0
    elif n> 0 and n%2==0:
        return F(n//10) + n%10
    elif n%2!=0:
        return F(n//10)
summ = 0
for i in range(10**9, 2*(10**9)+1):
    n = i
    if F(n) == 0:
        summ +=1
        print(summ, n)


print("16 номер ", summ)