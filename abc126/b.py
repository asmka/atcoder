S = input()

f = int(S[0])*10 + int(S[1])
b = int(S[2])*10 + int(S[3])
ans = ''
if (1<=f and f<=12) and (1<=b and b<=12):
    ans = 'AMBIGUOUS'
elif (1<=f and f<=12):
    ans = 'MMYY'
elif (1<=b and b<=12):
    ans = 'YYMM'
else:
    ans = 'NA'
print(ans)
