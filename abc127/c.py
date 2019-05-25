N, M = map(int, input().split())

cl = [0 for i in range(N+1)]
for i in range(M):
    L, R = map(int, input().split())
    cl[L-1] += 1
    cl[R] -= 1

ans = 0
cnt = 0
for i, c in enumerate(cl):
    cnt += c
    if cnt == M:
        ans += 1

#print(cl)
print(ans)


