N = int(input())
a = list(map(int, input().split()))

avg = sum(a)/N

ans = 0
tmpmin = abs(a[0]-avg)
for i in range(1, N):
    if abs(a[i]-avg) < tmpmin:
        tmpmin = abs(a[i]-avg)
        ans = i

print(ans)
    




