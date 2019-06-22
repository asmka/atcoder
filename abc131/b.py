N, L = map(int, input().split())

taste = [0] * N
for i in range(N):
    taste[i] = L+i

taste.sort()
ans = 0
if 0 in taste:
    ans = sum(taste)
elif taste[0] > 0:
    ans = sum(taste) - taste[0]
else:
    ans = sum(taste) - taste[-1]

print(ans)
