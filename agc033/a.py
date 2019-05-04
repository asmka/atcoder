(H, W) = map(int, input().split())
A = []
for i in range(H):
    A.append(input())

F = [[False for w in range(W)] for h in range(H)]
blackList = []
for h in range(H):
    for w in range(W):
        if A[h][w] == '#':
            F[h][w] = True
            blackList.append((h, w))

ans = -1
while blackList:
    #print('blackList: ', blackList)
    ans += 1
    nextBlack = []
    for (h, w) in blackList:
        if h-1 >= 0 and F[h-1][w] == False:
            F[h-1][w] = True
            nextBlack.append((h-1, w))
        if h+1 < H and F[h+1][w] == False:
            F[h+1][w] = True
            nextBlack.append((h+1, w))
        if w-1 >= 0 and F[h][w-1] == False:
            F[h][w-1] = True
            nextBlack.append((h, w-1))
        if w+1 < W and F[h][w+1] == False:
            F[h][w+1] = True
            nextBlack.append((h, w+1))
    #print('nextBlack: ', nextBlack)
    blackList = nextBlack

print(ans)
