import math
(N, M) = map(int, input().split())

MAX_SQRT = int(math.sqrt(M))
prime_flag = [True] * (MAX_SQRT+1)
prime_dic = {}

prime_flag[0] = False
prime_flag[1] = False

for i in range(2, MAX_SQRT+1):
    mul = 2
    while True:
        p = i * mul
        if p > MAX_SQRT:
            break
        prime_flag[p] = False
        mul += 1

TMPM = M
for i in range(2, MAX_SQRT+1):
    if prime_flag[i]:
        while TMPM%i == 0:
            if i in prime_dic:
                prime_dic[i] += 1
            else:
                prime_dic[i] = 1
            TMPM = int(TMPM/i)

if TMPM > 1 or len(prime_dic) == 0:
    prime_dic[TMPM] = 1

max_mul = 1
def Rec(mul, p):
    global max_mul
    if M//mul < N:
        return

    if p >= len(prime_dic):
        if mul > max_mul:
            max_mul = mul
        return

    k = list(prime_dic.keys())[p]
    v = list(prime_dic.values())[p]
    for i in range(v+1):
        Rec(mul*(k**i), p+1)

Rec(1, 0)
print(max_mul)

    
