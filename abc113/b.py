N = int(input())

(T, A) = map(int, input().split())
H = list(map(int, input().split()))

mindiff = 1000000.0
ans = 0
for i in range(N):
    t = T-H[i]*0.006
    if abs(t-A) < mindiff:
        mindiff = abs(t-A)
        ans = i+1

print(ans)

