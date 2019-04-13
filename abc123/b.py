dishlist = []
for i in range(5):
    dishlist.append(int(input()))

mind = 124
mini = 0
for i in range(len(dishlist)):
    d = (dishlist[i]-1) % 10
    if (d < mind):
        mind = d
        mini = i

dishlist[mini], dishlist[-1] = dishlist[-1], dishlist[mini]

ans = 0
for i in range(len(dishlist)):
    p = 0
    if (i < len(dishlist)-1):
        if (dishlist[i] % 10 != 0):
            p = 10 - (dishlist[i] % 10)
    ans += dishlist[i] + p 

print(ans)
