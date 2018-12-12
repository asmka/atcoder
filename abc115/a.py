D = int(input())
#(a, b) = map(int, input().split())

ans = ""
if D == 25:
    ans = "Christmas"
elif D == 24:
    ans = "Christmas Eve"
elif D == 23: 
    ans = "Christmas Eve Eve"
elif D == 22: 
    ans = "Christmas Eve Eve Eve"

print(ans)
