MOD = 1000000007

N, K = map(int, input().split())

if N == 1:
    print(K)
    exit()

uv = {}
for i in range(N-1):
    a, b = map(int, input().split())
    if a in uv:
        uv[a].append(b)
    else:
        uv[a] = [b]

    if b in uv:
        uv[b].append(a)
    else:
        uv[b] = [a]

f = None
for u in uv:
    if len(uv[u]) == 1:
        f = u
        break

ans = 1
b = [False] * (N+1)
ulist = [[f, 0]]
while ulist:
    u, pNum = ulist[-1]
    ulist.pop()
    b[u] = True
    
    uPtn = K - pNum
    ans = ans*uPtn % MOD

    cnt = 1
    if pNum == 0:
        cnt = 0
    for v in uv[u]:
        if b[v]:
            continue
        ulist.append([v, 1 + cnt])
        cnt += 1

print(ans) 
