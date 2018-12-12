(N, X) = map(int, input().split())

l = [0 for i in range(N+1)]
l[0] = 1
p = [0 for i in range(N+1)]
p[0] = 1
for i in range(1, N+1):
    l[i] = 2*l[i-1]+3
    p[i] = 2*p[i-1]+1

x = X
d = N
ans = 0
while True:
    if x == 0:
        break
    if d == 0 and x != 0:
        ans += 1
        break
    
    m = (l[d]-1)//2
    if x < m:
        x = x - 1
    elif x == m:
        ans += p[d-1]
        break
    elif x > m:
        ans += p[d-1]+1
        x = x - (m+1)

    d -= 1

print(ans)

