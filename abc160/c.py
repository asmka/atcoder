K, N = map(int, input().split())
A = list(map(int, input().split()))

dlist = []
for i in range(N):
    if i == 0:
        dlist.append(A[i]+K - A[i-1])
    else:
        dlist.append(A[i] - A[i-1])

ans = K - max(dlist)
print(ans)
