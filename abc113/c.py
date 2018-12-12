(N, M) = map(int, input().split())

P = []
Y = []
pyd = {}
for i in range(M):
    (p, y) = map(int, input().split())
    if p in pyd:
        pyd[p].append([y, i])
    else:
        pyd[p] = [[y, i]]

ans = []
for k in pyd:
    pyd[k].sort(key=lambda x:x[0])
    for i in range(len(pyd[k])):
        htag = str(k)
        while len(htag) < 6:
            htag = '0' + htag
        ltag = str(i+1)
        while len(ltag) < 6:
            ltag = '0' + ltag
        tag = htag + ltag
        ans.append([pyd[k][i][1], tag])

ans.sort(key=lambda x:x[0])
for a in ans:
    print(a[1])

