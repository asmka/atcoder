A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = []
y = []
c = []

cand = []
for i in range(M):
    lx, ly, lc = map(int, input().split())
    x.append(lx)
    y.append(ly)
    c.append(lc)

cand.append(min(a)+min(b))
for i in range(M):
    cand.append(a[x[i]-1] + b[y[i]-1] - c[i])

ans = min(cand)
print(ans)
