N, M = map(int, input().split())
A = list(map(int, input().split()))

A_sum = sum(A) 
cnt = 0
for i, a in enumerate(A):
    if a*(4*M) >= A_sum:
        cnt += 1

print("Yes" if cnt >= M else "No")
