(N, K) = map(int, input().split())
A = list(map(int, input().split()))

k = K
d = 0
while k > 0:
    d += 1
    k = k >> 1

bset = 0x0
for i in reversed(range(d)):
    b = 0x1 << i
    bcnt0 = 0
    for j in range(len(A)):
        if A[j] & b == 0:
            bcnt0 += 1
    # 1
    if bcnt0 > len(A)//2 and bset | b <= K:
        bset |= b

    #print('b: ' + str(b))
    #print('bcnt0: ' + str(bcnt0))

X = bset
ans = 0
for i in range(len(A)):
    ans += A[i] ^ X

print(ans)
