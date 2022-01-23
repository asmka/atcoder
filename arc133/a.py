N = int(input())
A = list(map(int, input().split()))

x = A[0]
for i in range(1, N):
    if A[i] >= x:
        x = A[i]
    else:
        break

ans = []
for _, a in enumerate(A):
    if a != x:
        ans.append(a)

print(*ans)
