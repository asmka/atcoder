N = int(input())

primes = {}

for i in range(2, N+1):
    tmpN = i
    n = 2
    while tmpN > 1:
        while tmpN%n == 0:
            tmpN //= n
            if n in primes:
                primes[n] += 1
            else:
                primes[n] = 1
        n += 1

kumi5 = 0
kumi3 = 0
kumi75 = 0
kumi25 = 0
kumi15 = 0
for key in primes.keys():
    if primes[key] >= 74:
        kumi75 += 1
    if primes[key] >= 24:
        kumi25 += 1
    if primes[key] >= 14:
        kumi15 += 1
    if primes[key] >= 4:
        kumi5 += 1
    if primes[key] >= 2:
        kumi3 += 1


ans = 0
if kumi5 >= 2 and kumi3 >= 3:
    ans += (kumi5 * (kumi5-1) // 2) * (kumi3-2)

if kumi75 >= 1:
    ans += kumi75

if kumi25 >= 1 and kumi3 >= 2:
    ans += kumi25 * (kumi3-1)

if kumi15 >= 1 and kumi5 >= 2:
    ans += kumi15 * (kumi5-1)

print(ans)



