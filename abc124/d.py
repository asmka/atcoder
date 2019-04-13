(N, K) = map(int, input().split())
S = input()

ans = 0
fpos = []
p = '0'
for i in range(len(S)):
    if p == '0' and S[i] == '1':
        fpos.append(i)
    if p == '1' and S[i] == '0':
        fi = len(fpos) - 1 - K
        if fi >= 0:
            l = (i-1) - (fpos[fi]-1)
            if l > ans:
                ans = l
    p = S[i]
#print('ans: ', ans)
            
# top
p = '1'
cnt = 0
for i in range(len(S)):
    if p == '0' and S[i] == '1':
        cnt += 1
    if p == '1' and S[i] == '0':
        if cnt == K:
            l = i
            if l > ans:
                ans = l
            break
    if i == len(S) - 1:
        l = len(S)
        if l > ans:
            ans = l
        break
    p = S[i]

# tail
p = '1'
cnt = 0
for i in range(len(S)-1, -1, -1):
    if p == '0' and S[i] == '1':
        cnt += 1
    if p == '1' and S[i] == '0':
        if cnt == K:
            l = (len(S)-1) - i
            if l > ans:
                ans = l
            break
    if i == 0:
        l = len(S)
        if l > ans:
            ans = l
        break
    p = S[i]

print(ans)
