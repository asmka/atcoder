N = int(input())
l = []
for i in range(N):
    S, P = input().split()
    l.append([S, int(P), i+1])

l.sort(key=lambda x: [x[0], -x[1]])
for s, p, i in l:
    print(i)



