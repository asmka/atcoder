#import math
#MOD = 10**9 + 7
#N, K = map(int, input().split())
#
#gcdmem = [[0] * (K+1) for i in range(K+1)]
#for i in range(1, K+1):
#    for j in range(i, K+1):
#        gcd = math.gcd(i, j)
#        gcdmem[i][j] = gcdmem[j][i] = gcd
#
#print(ans)
