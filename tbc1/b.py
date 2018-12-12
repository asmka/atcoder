(A, B, K) = map(int, input().split())


def ChgCookie(a, b) :
    if a%2 == 1:
        a = a-1

    (a, b) = (a//2, b+a//2)
    return (a, b)


for i in range(K):
    if i%2 == 0:
        (A, B) = ChgCookie(A, B)
        #print(A, B)
    else:
        (B, A) = ChgCookie(B, A)
        #print(A, B)

print(A, B)
