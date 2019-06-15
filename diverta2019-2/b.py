N = int(input())
d = {}
xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy.append([x, y])

for x1, y1 in xy:
    for x2, y2 in xy:
        if x1 == x2 and y1 == y2:
            continue
        dis = (x2-x1, y2-y1)
        if dis not in d:
            d[dis] = 1
        else:
            d[dis] += 1

ans = 0
if N == 1:
    ans = 1
else:
    ans = N - max(d.values())
print(ans)
