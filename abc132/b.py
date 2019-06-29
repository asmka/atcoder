n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(1, n-1):
    ps = p[i-1:i+2]
    ps.sort()
    if p[i] == ps[1]:
        ans += 1

print(ans)
