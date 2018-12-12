(N, K) = map(int, input().split())
a = list(map(int, input().split()))
 
btyarr = [0 for i in range(N*(N+1)//2)]
cnt = 0
for i in range(N):
    bty = 0
    for j in range(i, N):
        bty += a[j]
        btyarr[cnt] = bty
        cnt += 1
 
#print(cnt)
#print(len(btyarr))
 
l = len(btyarr)
s = 0
e = l
for i in range(40, -1, -1):
    b = 1 << i
    cnt = 0
    for j in range(s, e):
        if btyarr[j] & b:
            tmp = btyarr[s+cnt]
            btyarr[s+cnt] = btyarr[j]
            btyarr[j] = tmp
            cnt += 1
    if cnt >= K:
        e = s + cnt

#for i in range(len(btyarr)):
#    for j in range(30, -1, -1):
#        b = 1 << j
#        if btyarr[i] & b:
#            chb = 1
#        else:
#            chb = 0
#        print(chb, end="")
#    print("")
 
ans = btyarr[s]
for i in range(K):
    ans &= btyarr[i]
 
print(ans)
