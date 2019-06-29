import math
A, B, C, D = map(int, input().split())

## b = qa + r
#b = C
#a = D
#r = C%D
#while r != 0:
#    b = a
#    a = r
#    r = b%a
#gcd = a
gcd = math.gcd(C, D)
CDlcm = C*D//gcd

total = B-(A-1)
Cmuls = B//C - (A-1)//C
Dmuls = B//D - (A-1)//D
CDmuls = B//CDlcm - (A-1)//CDlcm
ans = total - Cmuls - Dmuls + CDmuls
print(ans)
