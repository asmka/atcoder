a, b, c = map(int, input().split())

ans = 'No'
if c-a-b < 2:
    ans = 'No'
elif 4*a*b < (c-a-b)**2:
    ans = 'Yes'

print(ans)

