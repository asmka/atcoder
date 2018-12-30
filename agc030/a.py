(A, B, C) = map(int, input().split())
#N = int(input())

ans = 0
if C <= A+B+1:
    ans = B+C
else:
    ans = A+B+1 + B
    
print(ans)

