L, R = map(int, input().split())

MOD = 2019

v = []
if R+1 - L < MOD:
    for i in range(L, R+1):
        v.append(i % MOD)
else:
    v = list(range(0, MOD))
v.sort()

ans = MOD+1
for i in range(len(v)):
    for j in range(i+1, len(v)):
        tmp = v[i] * v[j] % MOD
        if tmp < ans:
            ans = tmp

print(ans)
