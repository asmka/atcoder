N, A, B, C, D = map(int, input().split())
S = input()

needOver = False
if C > D:
    needOver = True

ans = 'Yes'
overPos = 0
if needOver:
    canOver = False
    for i in range(B-1, D):
        if S[i-1] == '.' and S[i] == '.' and S[i+1] == '.':
            canOver = True
            break
    if not canOver:
        ans = 'No'

for i in range(A+1-1, C):
    if S[i-1] == '#' and S[i] == '#':
        ans = 'No'
        break

for i in range(B+1-1, D):
    if S[i-1] == '#' and S[i] == '#':
        ans = 'No'
        break

print(ans)
