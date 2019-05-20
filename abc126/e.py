from queue import Queue

N, M = map(int, input().split())
d = {}
for i in range(1, N+1):
    d[i] = []
for i in range(M):
    x, y, z = map(int, input().split())
    d[x].append(y)
    d[y].append(x)

isChecked = [False for i in range(N)]
ans = 0
for k in d:
    if isChecked[k-1]:
        continue
    ans += 1
    q = Queue()
    q.put(k)
    while not q.empty():
        v = q.get()
        if isChecked[v-1]:
            continue
        isChecked[v-1] = True
        for u in d[v]:
            q.put(u)

print(ans)
