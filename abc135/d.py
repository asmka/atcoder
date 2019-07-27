MOD = 10**9 + 7
S = input()
dp = [[0] * 13 for i in range(len(S))]

rs = [[0] * 10 for i in range(len(S))]
for i in reversed(range(len(S))):
    if i == len(S) - 1:
        for j in range(10):
            rs[i][j] = j % 13
        continue

    for j in range(10):
        rs[i][j] = rs[i+1][j] * 10 % 13


for i in reversed(range(len(S))):
    if i == len(S) - 1:
        if S[i] == '?':
            for v in range(10):
                r = v % 13
                dp[i][r] += 1
        else:
            v = int(S[i])
            r = v % 13
            dp[i][r] += 1
        continue

    if S[i] == '?':
        for v in range(10):
            for r in range(13):
                s = (rs[i][v] + r) % 13
                dp[i][s] += dp[i+1][r]
                dp[i][s] %= MOD
    else:
        v = int(S[i])
        for r in range(13):
            s = (rs[i][v] + r) % 13
            dp[i][s] += dp[i+1][r]
            dp[i][s] %= MOD

print(dp[0][5])
