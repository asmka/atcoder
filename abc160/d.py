N, X, Y = map(int, input().split())

mind = [[N] * N for i in range(N)]
    
for i in range(N):
    for j in range(i+1, N):
        mind[i][j] = min(abs(j-i), abs((X-1)-i)+1+abs(j-(Y-1)), abs((Y-1)-i)+1+abs(j-(X-1)))

mindcnt = [0] * N
for i in range(N):
    for j in range(i+1, N):
        d = mind[i][j]
        mindcnt[d] += 1

for k in range(1, N):
    print(mindcnt[k])
