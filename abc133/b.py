import math

def checkDisInt(y, z):
    disSum = 0
    for i in range(D):
        disSum += (y[i] - z[i])**2
    if int(math.sqrt(disSum))**2 == disSum:
        return True
    return False

N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if checkDisInt(X[i], X[j]):
            ans += 1

print(ans)
