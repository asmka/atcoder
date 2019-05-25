r, D, xt = map(int, input().split())

x = xt
for i in range(10):
    x = r*x - D
    print(x)

