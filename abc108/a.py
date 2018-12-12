K = int(input())
ans = 0
if K%2 == 1:
    ans = int(K/2) * int(K/2 + 1)
else:
    ans = int(K/2) * int(K/2)
print(ans)
