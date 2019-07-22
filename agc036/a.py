S = int(input())

# x1y2 - x2y1 = S
# (x1, y1) = (1e9, 1)
# 1e9y2 - x2 = S

x0 = 0
y0 = 0
x1 = 10**9
y1 = 1
y2 = (S-1) // x1 + 1
x2 = x1*y2 - S

print(x0, y0, x1, y1, x2, y2)
