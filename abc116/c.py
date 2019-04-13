N = int(input())
h = list(map(int, input().split()))

opcnt = 0
pmh = 0
for i in range(N):
    if h[i] >= pmh:
        opcnt += h[i] - pmh
    pmh = h[i]

print(opcnt)
