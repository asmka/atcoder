A, B = map(int, input().split())

ans = 0
if A <= 5:
    ans = 0
elif A >= 13:
    ans = B
else:
    ans = B//2

print(ans)

