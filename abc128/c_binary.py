N, M = map(int, input().split())
onptns = []
for i in range(M):
    k, *s= list(map(int, input().split()))
    onptn = 0
    for i in s:
        onptn += 1 << (i - 1)
    onptns.append(onptn)
ps = list(map(int, input().split()))

ans = 0

s = 0
while s < (1 << N):
    ans += 1
    for onptn, p in zip(onptns, ps):
        if bin(s & onptn).count('1') % 2 != p:
            ans -= 1
            break
    s += 1

print(ans)
