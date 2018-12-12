N = int(input())
p = []
for i in range(N):
    p.append(int(input()))

ans = sum(p) - max(p)//2

print(ans)

