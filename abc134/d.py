N = int(input())
a = list(map(int, input().split()))

b = [0] * N
for i in range(N-1, -1, -1):
    s = 0
    k = i + (i+1)
    while k < N:
        s += b[k]
        k += (i+1)

    if s % 2 == a[i]:
        b[i] = 0
    else:
        b[i] = 1

print(b.count(1))
bv = []
for i in range(N):
    if b[i] == 1:
        bv.append(i+1)
if bv:
    print(' '.join(map(str, bv)))
