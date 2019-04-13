N = int(input())
H = list(map(int, input().split()))

ans = 1
for i in range(1, N):
    if H[i] >= max(H[0:i]):
        ans += 1

print(ans)
