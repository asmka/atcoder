H, W = map(int, input().split())
s = []
for i in range(H):
    s.append(input())

is_white = True
st = []
st.append([False, H-1, W-1, 0])
dp = [[1000] * W for i in range(H)]

for h in reversed(range(H)):
    for w in reversed(range(W)):
        if h == H-1 and w == W-1:
            if s[h][w] == '#':
                dp[h][w] = 1
            else:
                dp[h][w] = 0
            continue

        if w+1 < W:
            cnt = dp[h][w+1]
            if s[h][w] == '#' and s[h][w+1] == '.':
                cnt += 1
            if cnt < dp[h][w]:
                dp[h][w] = cnt

        if h+1 < H:
            cnt = dp[h+1][w]
            if s[h][w] == '#' and s[h+1][w] == '.':
                cnt += 1
            if cnt < dp[h][w]:
                dp[h][w] = cnt

print(dp[0][0])
