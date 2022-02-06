T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    ans = "No"
    if s >= a * 2 and (s - a * 2) & a == 0:
        ans = "Yes"
    print(ans)
