(N, M, X, Y) = map(int, input().split())
x = map(int, input().split())
y = map(int, input().split())

ans = "War"

max_x = max(x)
min_y = min(y)

if X+1 > max_x+1:
    min_z = X+1
else:
    min_z = max_x+1

if Y < min_y:
    max_z = Y
else:
    max_z = min_y

if min_z <= max_z:
    ans = "No War"

print(ans)

