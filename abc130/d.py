import bisect

N, K = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * N
s[0] = a[0]
for i in range(1, N):
    s[i] = s[i-1] + a[i]

cnt = 0
for i in range(N):
    q = K
    if i > 0:
        q += s[i-1]
    p = bisect.bisect_left(s, q, i, len(s))
    cnt += N - p

print(cnt)

