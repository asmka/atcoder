(X, Y, Z, K) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = list(reversed(sorted(A)))
B = list(reversed(sorted(B)))
C = list(reversed(sorted(C)))

Atmp = [A[0]]
Btmp = [B[0]]
Ctmp = [C[0]]

x, y, z = 1, 1, 1
while x*y*z < K:
    l = [0, 0, 0]
    if (x < X):
        l[0] = A[x]
    if (y < Y):
        l[1] = B[y]
    if (z < Z):
        l[2] = C[z]
    maxi = 0
    maxl = 0
    minl = 10000000001
    for i in range(len(l)):
        if (l[i] > 0 and l[i] - l[i-1] < minl):
            maxi = i
            maxl = l[i]
            minl = l[i]-l[i-1]
    if (maxi == 0):
        Atmp.append(maxl)
        x += 1
    elif (maxi == 1):
        Btmp.append(maxl)
        y += 1
    elif (maxi == 2):
        Ctmp.append(maxl)
        z += 1

ansl = []
for a in Atmp:
    for b in Btmp:
        for c in Ctmp:
            ansl.append(a+b+c)
ansl = list(reversed(sorted(ansl)))

print(Atmp)
print(Btmp)
print(Ctmp)
print(ansl)

for i in range(K):
    print(ansl[i])
