(N, K) = map(int, input().split())
usedflg = [False for i in range(N)]
tdic = {}
d = []
for i in range(N):
    (tmp_t, tmp_d) = map(int, input().split())
    if tmp_t not in tdic:
        tdic[tmp_t] = [tmp_d, i]
    else:
        tdic[tmp_t].append([tmp_d, i])
    d.append([tmp_d, i])

d.sort(reverse=True)

gp = 0
ans = []
ansk = 0

for k in tdic:
    md = max(tdic[k])
    usedflg[md[1]] = True
    gp += md[0]
    ansk += 1
    ans.append(md)
ans.sort(reverse=True)

while ansk > K:
    gp -= ansk[-1][0]
    ans.pop()
    ansk -= 1
   
di = 0
while len(ans) < K:
    while d[di][1] != False:
        di += 1
    d[di][1] = True



