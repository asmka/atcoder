L = input()

MOD = 10**9 + 7

d = [0] * len(L)
in_d = [0] * len(L)

for i in range(len(L)):
    if i == 0:
        d[i] = 1
        in_d[i] = 2
        continue

    # (0, 0), (0, 1), (1, 0)
    if L[i] == '1':
        d[i] = (d[i-1]*3 + in_d[i-1]*1) % MOD
        in_d[i] = in_d[i-1]*2 % MOD
    else:
        d[i] = d[i-1]*3 % MOD
        in_d[i] = in_d[i-1]*1 % MOD

d[-1] = (d[-1] + in_d[-1]) % MOD
print(d[-1])

