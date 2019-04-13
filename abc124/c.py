S = input()

ans = len(S)+1
# 010...
cnt = 0
for i in range(len(S)):
    if i%2 == 0:
        color = '0'
    else:
        color = '1'
    if S[i] != color:
        cnt += 1
if cnt < ans:
    ans = cnt

# 101...
cnt = 0
for i in range(len(S)):
    if i%2 == 0:
        color = '1'
    else:
        color = '0'
    if S[i] != color:
        cnt += 1
if cnt < ans:
    ans = cnt

print(ans)

