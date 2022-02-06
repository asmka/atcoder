N = int(input())
A = list(map(int, input().split()))

seq = [0, 360]
slope = 0
for _, a in enumerate(A):
    deg = (360 + slope - a) % 360
    seq.append(deg)
    slope = deg
seq.sort()

ans = 0
for i in range(1, len(seq)):
    cdeg = seq[i] - seq[i - 1]
    if cdeg > ans:
        ans = cdeg

print(ans)
