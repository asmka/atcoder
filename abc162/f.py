N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 2 for i in range(N)]
dp[0][0] = 0
dp[0][1] = A[0]
dp[1][0] = 0
dp[1][1] = max(A[0:2])
for i in range(2, N-1):
    if i%2 == 0:
        dp[i][0] = max(dp[i-1][1], dp[i-2][0] + A[i])
        dp[i][1] = dp[i-2][1] + A[i]
    else:
        dp[i][0] = max(dp[i-1][0], dp[i-2][0] + A[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][1] + A[i])

if N%2 == 0:
    ans = max(dp[N-2][1], dp[N-3][1] + A[N-1])
else:
    ans = max(dp[N-2][1], dp[N-3][0] + A[N-1])
print(ans)
