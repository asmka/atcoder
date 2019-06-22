A, B, C, D = map(int, input().split())

Cprimes = {}
Dprimes = {}

tmpC = C
d = 2
while tmpC > 1:
    if tmpC % d == 0:
        if d in Cprimes:
            Cprimes[d] += 1
        else:
            Cprimes[d] = 1
        tmpC //= d
    else:
        d += 1
    
tmpD = D
d = 2
while tmpD > 1:
    if tmpD % d == 0:
        if d in Dprimes:
            Dprimes[d] += 1
        else:
            Dprimes[d] = 1
        tmpD //= d
    else:
        d += 1

comPrimes = {}
for k in Cprimes:
    comPrimes[k] = Cprimes[k]
for k in Dprimes:
    if k in comPrimes:
        if comPrimes[k] < Dprimes[k]:
            comPrimes[k] = Dprimes[k]
    else:
        comPrimes[k] = Dprimes[k]

comVal = 1
for k in comPrimes:
    comVal *= k**comPrimes[k]

#print(Cprimes)
#print(Dprimes)
#print(comPrimes)
#print(comVal)

CdivNum = B//C - (A-1)//C
DdivNum = B//D - (A-1)//D
comDivNum = B//comVal - (A-1)//comVal
ans = B-(A-1)
ans -= CdivNum
ans -= DdivNum
ans += comDivNum

print(ans)
