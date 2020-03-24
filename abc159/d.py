N = int(input())
A = list(map(int, input().split()))

def comb2(n):
    if n < 2:
        return 0
    return n*(n-1)//2

cntd = {}
for i in range(N):
    if A[i] in cntd:
        cntd[A[i]] += 1
    else:
        cntd[A[i]] = 1

sum_comb = 0
for k, v in cntd.items():
    sum_comb += comb2(v)

#print(cntd)
#print(sum_comb)
for i in range(N):
    k = A[i]
    ans = sum_comb - comb2(cntd[k]) + comb2(cntd[k]-1)
    print(ans)
