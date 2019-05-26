N, K = map(int, input().split())
V = list(map(int, input().split()))
INF_MIN = -(10**10)
l = [[INF_MIN] * (K+1) for i in range(N+1)]
r = [[INF_MIN] * (K+1) for i in range(N+1)]

pop_sum = 0
for i in range(N+1):
    if i == 0:
        pop_sum = 0
        l[i][0] = 0
        r[i][0] = 0
        popV = []
    else:
        pop_sum += V[i-1]
        popV = list(sorted(V[0:i]))
        l[i][0] = pop_sum
    for k in range(1, K+1):
        if not (k-1 < len(popV)) or popV[k-1] > 0:
            l[i][k] = l[i][k-1]
        else:
            l[i][k] = l[i][k-1] - popV[k-1]

pop_sum = 0
for i in range(N+1):
    if i == 0:
        pop_sum = 0
        r[i][0] = 0
        popV = []
    else:
        pop_sum += V[N-i]
        popV = list(sorted(V[N-i:N]))
        r[i][0] = pop_sum
    for k in range(1, K+1):
        if not (k-1 < len(popV)) or popV[k-1] > 0:
            r[i][k] = r[i][k-1]
        else:
            r[i][k] = r[i][k-1] - popV[k-1]

#print(l)
#print(r)

max_val = INF_MIN
imax = min(N, K)
for i in range(imax+1):
    for k in range(K-i+1):
        jmax = min(N-i, K-i-k)
        for j in range(jmax+1):
            val = l[i][k] + r[j][K-i-k-j]
            if val > max_val:
                max_val = val
                #print(i, j, k, l[i][k], r[j][K-i-k-j])


print(max_val)
