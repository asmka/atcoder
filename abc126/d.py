from queue import Queue

N = int(input())
d = {}
for i in range(N-1):
    u, v, w = map(int, input().split())
    if u in d:
        d[u].append([v, w])
    else:
        d[u] = [[v, w]]
    if v in d:
        d[v].append([u, w])
    else:
        d[v] = [[u, w]]

isChecked = [False for i in range(N)]
ans = [0 for i in range(N)]
q = Queue()
# [current v, sum length]
q.put([1, 0])
while not q.empty():
    v, l = q.get()
    if isChecked[v-1]:
        continue
    ans[v-1] = 0 if l%2 == 0 else 1
    isChecked[v-1] = True
    for u, w in d[v]:
        q.put([u, l+w])

for i in range(N):
    print(ans[i])
