N = int(input())
d = list(map(int, input().split()))

d.sort()
ans = 0
if d[N//2] == d[N//2 - 1]:
    ans = 0
else:
    ans = d[N//2] - d[N//2 - 1]

print(ans)

