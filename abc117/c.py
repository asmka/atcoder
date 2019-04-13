(N, M) = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

d = []
for i in range(1, len(X)):
    d.append(X[i] - X[i-1])
    
d.sort()

k = 0
if M-N > 0:
    k = M-N

print(sum(d[0:k]))


