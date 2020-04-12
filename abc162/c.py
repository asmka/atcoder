import math
K = int(input())

gcdmem = [[[0] * (K+1) for i in range(K+1)] for j in range(K+1)]

for a in range(1, K+1):
    for b in range(a, K+1):
        for c in range(b, K+1):
            if gcdmem[a][b][c] > 0:
                continue
            gcdab = math.gcd(a, b)
            gcdmem[a][b][c] = math.gcd(gcdab, c)

ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            s1, s2, s3 = sorted([a, b, c])
            ans += gcdmem[s1][s2][s3]

print(ans)
