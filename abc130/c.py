W, H, x, y = map(int, input().split())

if x*2 == W and y*2 == H:
    cnt = 1
else:
    cnt = 0

print(W*H/2, cnt)
