(N, K) = map(int, input().split())
h = []
for i in range(N):
    h.append(int(input()))

h.sort()
ans = 10**9 + 100
for i in range(N-K+1):
    d = abs(h[i]-h[i+K-1])
    if d < ans:
        ans = d
    
print(ans)


