(N, T) = map(int, input().split())
c = []
for i in range(N):
    (tmpc, tmpt) = map(int, input().split())
    if tmpt <= T:
        c.append(tmpc)

if len(c) == 0:
    ans = 'TLE'
else:
    ans = min(c)

print(ans)


