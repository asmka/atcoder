N, Q = map(int, input().split())
a = list(map(int, input().split()))
x = []
k = []
for _ in range(Q):
    xi, ki = map(int, input().split())
    x.append(xi)
    k.append(ki)

x_dict = {}
for i, ai in enumerate(a):
    if ai in x_dict:
        num = len(x_dict[ai]) + 1
        x_dict[ai][num] = i + 1
    else:
        x_dict[ai] = {1: i + 1}

for i in range(Q):
    ans: int
    if x[i] not in x_dict:
        ans = -1
    elif k[i] in x_dict[x[i]]:
        ans = x_dict[x[i]][k[i]]
    else:
        ans = -1
    print(ans)
