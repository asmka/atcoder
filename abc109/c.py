(N, X) = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
    
ans = 0

diff = []
for i in range(len(x)-1):
    diff.append(x[i+1] - x[i])
#print("diff: ")
#print(diff)

base = min(diff)
for i in range(1, base+1):
    flag = True
    if base%i != 0:
        continue
    div = int(base/i)
    for j in range(len(diff)):
        if diff[j]%div != 0:
            flag = False
            break
    if flag == True:
        ans = div
        break

print(ans)

