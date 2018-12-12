N = int(input())
x = []
y = []
h = []
for i in range(N):
    (tmp_x, tmp_y, tmp_h) = map(int, input().split())
    x.append(tmp_x)
    y.append(tmp_y)
    h.append(tmp_h)

def CalcHigh(cx, cy, px, py, ph):
    ch = ph + abs(cx-px) + abs(cy-py)
    return ch

for i in range(101):
    for j in range(101):
        ch = 0
        for k in range(N):
            if h[k] > 0:
                ch = CalcHigh(i, j, x[k], y[k], h[k])

        flag = True
        for k in range(N):
            if ch > 0:
                if h[k] == 0:
                    if CalcHigh(i, j, x[k], y[k], h[k]) < ch:
                        flag = False
                        break
                else:
                    if CalcHigh(i, j, x[k], y[k], h[k]) != ch:
                        flag = False
                        break

        if flag == True:
            ans = (i, j, ch)
            break

print(ans[0], ans[1], ans[2])



