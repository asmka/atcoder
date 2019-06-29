N, M = map(int, input().split())

uv = {}
for i in range(M):
    u, v = map(int, input().split())
    if not u in uv:
        uv[u] = [v]
    else:
        uv[u].append(v)
    

S, T = map(int, input().split())

b = [[False] * (10**5+1) for i in range(3)]
us = [S]
b[-1][S] = True
cnt = 0
while us:
    cnt += 1
    for i in range(3):
        tmpus = []
        for u in us:
            if u in uv:
                for v in uv[u]:
                    if b[i][v] is False:
                        b[i][v] = True
                        tmpus.append(v)
        us = tmpus

    if T in us:
        print(cnt)
        break

if not T in us:
    print(-1)

            
        
