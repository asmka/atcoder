(H, W) = map(int, input().split())
A = []
for i in range(H):
    A.append(input())


def fillDistance(d, h, w):
    # up
    ch = h - 1
    cd = 1
    while ch >= 0 and cd < d[ch][w]: 
        d[ch][w] = cd
        ch -= 1
        cd += 1
    # down
    ch = h + 1
    cd = 1
    while ch < H and cd < d[ch][w]: 
        d[ch][w] = cd
        ch += 1
        cd += 1
    # right and updown
    cw = w+1
    cd = 1
    while cw < W and cd < d[h][cw]:
        d[h][cw] = cd
        # up
        ch = h - 1
        cdd = cd + 1
        while ch >= 0 and cdd < d[ch][cw]: 
            d[ch][cw] = cdd
            ch -= 1
            cdd += 1
        # down
        ch = h + 1
        cdd = cd + 1
        while ch < H and cdd < d[ch][cw]: 
            d[ch][cw] = cdd
            ch += 1
            cdd += 1
        cd += 1
        cw += 1
    # left and updown
    cw = w-1
    cd = 1
    while cw >= 0 and cd < d[h][cw]:
        d[h][cw] = cd
        # up
        ch = h - 1
        cdd = cd + 1
        while ch >= 0 and cdd < d[ch][cw]: 
            d[ch][cw] = cdd
            ch -= 1
            cdd += 1
        # down
        ch = h + 1
        cdd = cd + 1
        while ch < H and cdd < d[ch][cw]: 
            d[ch][cw] = cdd
            ch += 1
            cdd += 1
        cd += 1
        cw -= 1
    #print(d)


d = [[10000 for j in range(W)] for i in range(H)]
for h in range(H):
    for w in range(W):
        if A[h][w] == '#':
            d[h][w] = 0
for h in range(H):
    for w in range(W):
        if A[h][w] == '#':
            #print('call fill', h, w)
            fillDistance(d, h, w)
                
#print(d)
ans = -1
for h in range(H):
    for w in range(W):
        if d[h][w] > ans:
            ans = d[h][w]
print(ans)
