H, W = map(int, input().split())

S = []
for i in range(H):
    S.append(input())

U = [[0] * W for h in range(H)]
D = [[0] * W for h in range(H)]
L = [[0] * W for h in range(H)]
R = [[0] * W for h in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] == 1:
            continue
        # up
        if h-1 < 0 or S[h-1][w] == '#':
            U[h][w] = 0
        else:
            U[h][w] = U[h-1][w] + 1
        # left
        if w-1 < 0 or S[h][w-1] == '#':
            L[h][w] = 0
        else:
            L[h][w] = L[h][w-1] + 1

for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
        if S[h][w] == 1:
            continue
        # down
        if h+1 >= H or S[h+1][w] == '#':
            D[h][w] = 0
        else:
            D[h][w] = D[h+1][w] + 1
        # right
        if w+1 >= W or S[h][w+1] == '#':
            R[h][w] = 0
        else:
            R[h][w] = R[h][w+1] + 1

ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        cnt = U[h][w] + L[h][w] + D[h][w] + R[h][w] + 1
        if cnt > ans:
            ans = cnt 

print(ans)
