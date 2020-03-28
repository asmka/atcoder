X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

ep = p[:X]
eq = q[:Y]
epq = ep + eq
epq.sort()

ans = sum(epq)
for i, mr in enumerate(r):
    if i >= len(epq):
        break

    if mr > epq[i]:
        ans += mr-epq[i]
    else:
        break

print(ans)
