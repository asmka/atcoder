N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in reversed(range(N)):
    if A[i+1] >= B[i]:
        cnt += B[i]
        continue
    else:
        cnt += A[i+1]
        B[i] -= A[i+1]
        if A[i] >= B[i]:
            cnt += B[i]
            A[i] -= B[i]
        else:
            cnt += A[i]
            A[i] -= A[i]
print(cnt)
