(L, N) = map(int, input().split())
X = [0 for i in range(N)]
sumld = [0 for i in range(N)]
sumrd = [0 for i in range(N)]
for i in range(N):
    X[i] = int(input())
    sumld[i] = X[i]*2 if i == 0 else sumld[i-1] + X[i]*2
for i in range(N):
    sumrd[N-1-i] = (L-X[N-1-i])*2 if i == 0 else sumrd[N-1-i+1] + (L-X[N-1-i])*2
#print('X: ', X)
#print('sumld: ', sumld)
#print('sumrd: ', sumrd)

ans = 0
if N == 1:
    ans = max(X[0], L-X[0])
else:
    dmax = 0
    for i in range(1, N):
        l = (N-1+i)%N
        r = i
        lnum = l+1
        rnum = N-lnum
        #print('l: ', l)
        #print('r: ', r)
        #print('lnum: ', lnum)
        #print('rnum: ', rnum)

        # start from l
        d = 0
        # end at l
        if lnum > rnum:
            d = sumld[l] + sumrd[r] - X[l]
            if lnum-rnum > 1:
                d -= sumld[l-rnum-1]
        # end at r
        else:
            d = sumld[l] + sumrd[r] - X[l]
            if rnum-lnum > 0:
                d -= sumrd[r+lnum]
        #print('d from l: ', d)
        if d > dmax:
            dmax = d

        # start from r
        d = 0
        # end at l
        if lnum >= rnum:
            d = sumld[l] + sumrd[r] - (L-X[r])
            if lnum-rnum > 0:
                d -= sumld[l-rnum]
        # end at r
        else:
            d = sumld[l] + sumrd[r] - (L-X[r])
            if rnum-lnum > 1:
                d -= sumrd[r+lnum+1]
        #print('d from r: ', d)
        if d > dmax:
            dmax = d
    ans = dmax

print(ans)
