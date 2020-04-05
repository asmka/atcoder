N, K = map(int, input().split())

x = N
d = N-K
if d > 0:
    x = K + d%K
ans = min(x, abs(x-K), abs(x-K-K))
print(ans)
