N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = []
f = 0
l = N-1
s = 0

if N == 2:
    ans.append([A[l], A[f]])
    s = A[l] - A[f]
    f += 1
    l -= 1
else:
    hasPlus = True if A[N-2] >= 0 else False
    if hasPlus:
        # make minus
        ans.append([A[f], A[l]])
        s = A[f] - A[l]
        f += 1
        l -= 1
        while f <= l:
            if f == l or A[l-1] < 0:
                # choose plus make plus
                ans.append([A[l], s])
                s = A[l] - s
                l -= 1
                break
            # choose plus make minus
            ans.append([s, A[l]])
            s = s - A[l]
            l -= 1
    else:
        # make plus
        ans.append([A[l], A[f]])
        s = A[l] - A[f]
        f += 1
        l -= 1

# choose minus make plus
while f <= l:
    ans.append([s, A[l]])
    s = s - A[l]
    l -= 1

print(s)
for x, y in ans:
    print(x, y)
