N = int(input())

a = [i for i in range(N+1)]

for i in range(3, N+1, 3):
    a[i] = 0

for i in range(5, N+1, 5):
    a[i] = 0

ans = sum(a)
print(ans)
