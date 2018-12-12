N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

A.sort()

arr = []
arr.append(A[0])
arr.append(A[-1])
Atop = 1
Abtm = len(A) - 2
ans = arr[-1]-arr[0]
for i in range(len(A)-2):
    (Ai, ai) = (Atop, 0)
    if abs(A[Atop]-arr[-1]) > abs(A[Ai]-arr[ai]):
        (Ai, ai) = (Atop, -1)
    if abs(A[Abtm]-arr[0]) > abs(A[Ai]-arr[ai]):
        (Ai, ai) = (Abtm, 0)
    if abs(A[Abtm]-arr[-1]) > abs(A[Ai]-arr[ai]):
        (Ai, ai) = (Abtm, -1)

    #print('A[Ai]: ', A[Ai])
    #print(arr)
    ans += abs(A[Ai]-arr[ai])
    if ai == -1:
        arr[-1] = A[Ai]
    else:
        arr[0] = A[Ai]

    if Ai == Atop:
        Atop += 1
    else:
        Abtm -= 1


print(ans)

