r = 1430201
summ = []
while r % 3147 != 0:
    r+=1
for i in range(r, 10**10, 3147):
    q = str(i)
    if q[0]== "1":
        if q[-1] == "1":
            if q[-5] == "3":
                if q[-3] == "2":
                    if q[-4] == "0":
                        if q[-6] == "4":
                            summ.append(i)
                            print(i)
print("25ая", sorted(summ), len(summ))
