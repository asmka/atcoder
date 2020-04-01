N, A, B = map(int, input().split())

d = B-A
if d%2 == 1:
    d = min((B + (N-B)*2 + 1) - A, B - (A - (A-1)*2 - 1))

ans = d//2
print(ans)
