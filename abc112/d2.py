import math
(N, M) = map(int, input().split())

msq = int(math.sqrt(M))
if N == 1:
    ans = M
else:
    for i in range(M, 0, -1):
        if M%i == 0:
            tmp = M - i*(N-1)
            if tmp > 0 and tmp%i == 0:
                ans = i
                break

print(ans)
