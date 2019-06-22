N, K = map(int, input().split())

ans = []

if N == 2 and K > 0:
    ans = []
elif (1+N-2)*(N-2)//2 < K:
    ans = []
else:
    for i in range(2, N+1):
        ans.append([1, i])
    cnt = (1+N-2)*(N-2)//2

    for u in range(2, N):
        if cnt == K:
            break
        for v in range(u+1, N+1):
            if cnt == K:
                break
            ans.append([u, v])
            cnt -= 1
   
if ans:
    print(len(ans))
    for u, v in ans:
        print(u, v)
else:
    print(-1)
