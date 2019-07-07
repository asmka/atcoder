N = int(input())
A = list(map(int, input().split()))

# A[i] = ans[i]/2 + ans[i+1]/2
ans = [0] * N

# A[i] = ans[i]/2 + ans[i+1]/2
# ans[i] =  2A[i] - ans[i+1]
# A[i+1] = ans[i+1]/2 + ans[i+2]/2
# ans[i+1] =  2A[i+1] - ans[i+2]
for i in range(N):
    if i%2 == 0:
        tmp = -1
    else:
        tmp = 1
    tmp *= A[i] * 2
    ans[0] -= tmp
ans[0] //= 2

for i in range(1, N):
    ans[-i] = A[-i] * 2 - ans[-i+1]

print(' '.join(map(str, ans)))
