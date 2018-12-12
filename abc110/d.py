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

for i in range(2, MAX_SQRT+1):
    if prime_flag[i]:
        while M%i == 0:
            if i in prime_dic:
                prime_dic[i] += 1
            else:
                prime_dic[i] = 1
            M = int(M/i)

if M > 1:
    prime_dic[M] = 1

print(prime_flag)
print(prime_dic)

