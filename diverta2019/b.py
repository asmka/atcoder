R, G, B, N = map(int, input().split())

ans = 0
rsum = 0
for r in range(0, N+1):
    if N < rsum:
        break
    rgsum = rsum
    for g in range(0, N+1):
        if N < rgsum:
            break
        left = N - rgsum 
        if left % B == 0:
            ans += 1
        rgsum += G
    rsum += R

print(ans)

