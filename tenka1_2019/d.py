N = int(input())
a = []
d = {}
for i in range(N):
    tmp = int(input)
    a.append(tmp)
    if tmp in d:
        d[tmp] = 1
    else:
        d[tmp] += 1
    



