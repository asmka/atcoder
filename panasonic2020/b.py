import fractions
H, W = map(int, input().split())

ans = 1
if H == 1 or W == 1:
    ans = 1
else:
    ans = H*W//2
    if H%2 == 1 and W%2 == 1:
        ans += 1
print(ans)
