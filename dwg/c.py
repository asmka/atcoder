N = int(input())
S = input()
Q = int(input())
kL = list(map(int, input().split()))

ans = []
Dcnt = [0 for i in range(len(kL))]
Mcnt = [0 for i in range(len(kL))]
DMcnt = [0 for i in range(len(kL))]
DMCcnt = [0 for i in range(len(kL))]
for i in range(len(S)):
    for j in range(len(kL)):
        k = kL[j]
        if i-k >= 0 and S[i-k] == 'D':
            Dcnt[j] -= 1
            DMcnt[j] -= Mcnt[j]
        elif i-k >= 0 and S[i-k] == 'M':
            Mcnt[j] -= 1

        if S[i] == 'D':
            Dcnt[j] += 1
        elif S[i] == 'M':
            Mcnt[j] += 1
            DMcnt[j] += Dcnt[j]
        elif S[i] == 'C':
            DMCcnt[j] += DMcnt[j]
    
for a in DMCcnt:
    print(a)
            
