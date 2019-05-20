import math

N, K = map(int, input().split())

saip = 1/N
ans = 0
for i in range(1, N+1):
    prob = saip
    score = i
    while score < K:
        score *= 2
        prob *= 1/2
    ans += prob

print(ans)
