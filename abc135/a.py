A, B = map(int, input().split())

if A > B:
    tmp = A
    A = B
    B = tmp

if (B - A) % 2 == 0:
    print(B - (B - A) // 2)
else:
    print('IMPOSSIBLE')
    

