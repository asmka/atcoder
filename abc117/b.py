N = int(input())
L = list(map(int, input().split()))

ans = ''
if max(L) < sum(L) - max(L):
    ans = 'Yes'
else:
    ans = 'No'

print(ans)

