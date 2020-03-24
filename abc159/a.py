n, m = map(int, input().split())

#nC2
#mC2

ans = 0
if n >= 2:
    ans += n*(n-1)//2
if m >= 2:
    ans += m*(m-1)//2

print(ans)
