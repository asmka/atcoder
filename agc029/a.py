S = list(input())

cnt = 0
Bseq = 0
for i in range(len(S)-1):
    if S[i] == 'B':
        Bseq += 1
    else:
        Bseq = 0

    if S[i] == 'B' and S[i+1] == 'W':
        S[i] = 'W'
        S[i+1] = 'B'
        cnt += Bseq
        Bseq = Bseq-1

ans = cnt
print(ans)

