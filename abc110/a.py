(A, B, C) = map(int, input().split())

ans = (A*10+B) + C

tmp = (A*10+C) + B
if tmp > ans:
    ans = tmp

tmp = (B*10+A) + C
if tmp > ans:
    ans = tmp

tmp = (B*10+C) + A
if tmp > ans:
    ans = tmp

tmp = (C*10+B) + A
if tmp > ans:
    ans = tmp

tmp = (C*10+A) + B
if tmp > ans:
    ans = tmp

print(ans)
