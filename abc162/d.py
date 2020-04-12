N = int(input())
S = input()

rn = S.count('R')
gn = S.count('G')
bn = S.count('B')

eqn = 0
for i in range(N):
    for j in range(i+1, N):
        k = j + (j-i)
        if k < N and S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
            eqn += 1

ans = rn * gn * bn - eqn

print(ans)
