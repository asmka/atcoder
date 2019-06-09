N = int(input())
W = list(map(int, input().split()))

ans = 100000
for i in range(1, N):
    tmp = abs(sum(W[:i+1]) - sum(W[i+1:]))
    if tmp < ans:
        ans = tmp
    
print(ans)



