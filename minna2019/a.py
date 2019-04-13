(N, K) = map(int, input().split())

ans = ''
if K <= (N+1)//2:
    ans = 'YES'
else:
    ans = 'No'

print(ans)
