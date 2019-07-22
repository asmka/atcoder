N = int(input())
A = []
sA = []
for i in range(N):
    a = int(input())
    A.append(a)
    sA.append(a)

sA.sort(reverse=True)

f = sA[0]
s = sA[1]

for i in range(N):
    if A[i] == f:
        print(s)
    else:
        print(f)
