N = int(input())
p = list(map(int, input().split()))

psort = [0] * N
for i in range(N):
    psort[i] = p[i]
psort.sort()

cnt = 0
for i in range(N):
    if p[i] != psort[i]:
        cnt += 1

if cnt <= 2:
    print('YES')
else:
    print('NO')

