N = int(input())
H = list(map(int, input().split()))

ans = H[0]
for h in H[1:]:
    if h <= ans:
        break
    ans = h

print(ans)
