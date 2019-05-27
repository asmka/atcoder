from heapq import heappush, heappop

N, Q = map(int, input().split())
tl = []
for i in range(N):
    S, T, X = map(int, input().split())
    tl.append([S-X-0.5, 'S', X])
    tl.append([T-X-0.5, 'T', X])
d = []
for i in range(Q):
    D = int(input())
    tl.append([D, 'D'])

tl.sort()
#print(tl)

ans = []
Xhp = []
dX = set()
for t in tl:
    mode = t[1]
    if mode == 'S':
        X = t[2]
        if X in dX:
            dX.remove(X)
        heappush(Xhp, X)
    elif mode == 'T':
        X = t[2]
        dX.add(X)
    else:
        while True:
            if not Xhp:
                ans.append(-1)
                break
            Xmin = heappop(Xhp)
            if Xmin in dX:
                dX.remove(Xmin)
                continue
            else:
                ans.append(Xmin)
                break

for a in ans:
    print(a) 
