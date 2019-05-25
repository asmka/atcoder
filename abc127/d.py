import math
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

CB = []
for i in range(M):
    B, C = map(int, input().split())
    CB.append([C, B])
CB.sort(reverse=True)

p = 0
for C, B in CB:
    while p < len(A) and A[p] >= C:
        p += 1
    if p >= len(A):
        break
    for i in range(B):
        if p >= len(A):
            break
        if A[p] < C:
            A[p] = C
            p += 1
        else:
            break
print(sum(A))
