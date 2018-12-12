(H, W, K) = map(int, input().split())
DIVISOR = 1000000007

# the number of horizonal line pattens at moving from line i to line j
hlineptn = [[0 for j in range(W)] for i in range(W)]

# calculate the number of horizonal line patterns
for hlinedig in range(1 << (W-1)):
    # convert digit to bit
    bitlist = [0 for i in range(W-1)]
    for i in range(len(bitlist)):
        if hlinedig & 1 << ((W-2)-i):
            bitlist[i] = 1

    # check illegal horizonal line
    illegalflg = False
    for i in range(len(bitlist)-1):
        if bitlist[i] and bitlist[i+1]:
            illegalflg = True
            break
    if illegalflg:
        continue

    # loop for before line
    for i in range(W):
        # move to left
        if i-1 >= 0 and bitlist[i-1]:
            hlineptn[i][i-1] += 1
        # move to right
        elif i+1 < W and bitlist[i]:
            hlineptn[i][i+1] += 1
        # move to current
        else:
            hlineptn[i][i] += 1

# calculate the number of move patterns from line 0
# and divide it by DIVISOR to get division remainder
mvptn = [[0 for w in range(W)] for h in range(H+1)]
mvptn[0][0] = 1
for h in range(1, H+1):
    for w in range(W):
        # from above left line
        if w-1 >= 0:
            mvptn[h][w] += mvptn[h-1][w-1] * hlineptn[w-1][w]
        # from above current line
        mvptn[h][w] += mvptn[h-1][w] * hlineptn[w][w]
        # from above right line
        if w+1 < W:
            mvptn[h][w] += mvptn[h-1][w+1] * hlineptn[w+1][w]

        # format to division remainder
        if mvptn[h][w] > DIVISOR:
            mvptn[h][w] %= DIVISOR

ans = mvptn[H][K-1]
print(ans)

