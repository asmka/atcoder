import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = {}
for i, a in enumerate(A):
    if a in d:
        d[a].append(i)
    else:
        d[a] = [i]

loop_cnt = 0
sp = []
p = 0
fp = 1
top = A[0]
while True:
    loop_cnt += 1
    while fp < N:
        np = bisect.bisect_left(d[top], fp)
        if np < len(d[top]):
            p = d[top][np] + 1
            fp = p+1
            if p < N:
                top = A[p]
        else:
            break
    if p >= N:
        break
    top = A[p]
    sp.append(p)
    fp = 0

k = K % loop_cnt - 1
if k == -1:
    exit()
p = sp[k]
s = []
while p < N:
    top = A[p]
    while True:
        np = bisect.bisect_left(d[top], p+1)
        if np < len(d[top]):
            p = d[top][np] + 1
            if p < N:
                top = A[p]
        else:
            break
    if p < N:
        s.append(top)
        p += 1

print(' '.join(map(str, s)))
