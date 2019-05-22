M, K = map(int, input().split())

ans = []
if M == 0 or M == 1:
    if K == 0:
        for i in range(2**M):
            ans.append(str(i))
            ans.append(str(i))
    else:
        ans.append('-1')
elif K >= 2**M:
    ans.append('-1')
else:
    for i in range(2**M):
        if i != K:
            ans.append(str(i))
    ans.append(str(K))
    for i in reversed(range(2**M)):
        if i != K:
            ans.append(str(i))
    ans.append(str(K))

print(' '.join(ans))
