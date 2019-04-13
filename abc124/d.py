(N, K) = map(int, input().split())
S = input()

fpos_list = []
ps = ''
for i in range(len(S)):
    if ps != S[i]:
        fpos_list.append([i, S[i]])
        ps = S[i]

ans = 0
for i in range(len(fpos_list)):
    bp = fpos_list[i][0]
    bs = fpos_list[i][1]
    l = 0
    if bs == '0':
        ep = N
        if i+2*K < len(fpos_list):
            ep = fpos_list[i+2*K][0]
        l = ep-bp
    else:
        ep = N
        if i+1+2*K < len(fpos_list):
            ep = fpos_list[i+1+2*K][0]
        l = ep-bp
    if l > ans:
        ans = l
    # debug
    #print('i: ', i)
    #print('bp: ', bp)
    #print('bs: ', bs)
    #print('l: ', l)

print(ans)
