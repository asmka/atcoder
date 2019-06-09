N, M = map(int, input().split())

MOD = 1000000007

p = [0]*(N+1)
for i in range(M):
    a = int(input())
    p[a] = -1

p[N] = 1
if p[N-1] != -1:
    p[N-1] = 1

for i in range(N-2, -1, -1):
    if p[i] == -1:
        continue

    if p[i+1] == -1 and p[i+2] == -1:
        p[i] = -1
    elif p[i+1] == -1:
        p[i] = p[i+2]
    elif p[i+2] == -1:
        p[i] = p[i+1]
    else:
        p[i] = p[i+1] + p[i+2]

    if p[i] > 0:
        p[i] %= MOD

ans = p[0]
if ans < 0:
    ans = 0

print(ans)

