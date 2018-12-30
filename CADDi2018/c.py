import math
(N, P) = map(int, input().split())

p = P
primes = {}
d = 2
maxd = int(math.sqrt(P))

while d <= maxd and p > 1:
    while p%d == 0:
        if d not in primes:
            primes[d] = 1
        else:
            primes[d] += 1
        p = p//d
    d += 1
if p > 1:
    primes[p] = 1
#print(primes)

ans = 1
for k in primes:
    n = primes[k]//N
    if n > 0:
        ans *= k**n

print(ans)

