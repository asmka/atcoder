N = int(input())
S = input()


ans = N+1

# ...
wnum = S.count('.')
# ###
bnum = S.count('#')

# ...###
wcnt = 0
bcnt = 0
for i, s in enumerate(S):
    l_wnum = wcnt
    l_bnum = bcnt
    r_wnum = wnum - l_wnum
    step = l_bnum + r_wnum
    if step < ans:
        ans = step

    #print('i: ', i)
    if s == '.':
        wcnt += 1
    else:
        bcnt += 1

# ...
if bnum < ans:
    ans = bnum

print(ans)

