S = input()
d = {}

ans = 'Yes'
for i in range(len(S)):
    if S[i] in d:
        d[S[i]] += 1
    else:
        d[S[i]] = 1

    if d[S[i]] > 2:
        ans = 'No'
        break

if len(d) != 2:
    ans = 'No'

print(ans)
