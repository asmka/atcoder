N = int(input())
BA = [[0] * 2 for i in range(N)]
for i in range(N):
    A, B = map(int, input().split())
    BA[i][0] = B
    BA[i][1] = A

BA.sort()
t = 0
ans = 'Yes'
#print(BA)
for ba in BA:
    B = ba[0]
    A = ba[1]
    t += A
    if t > B:
        ans = 'No'
        break

print(ans)
    
