N, P = map(int, input().split())
S = input()

r_circ = []
v = 1
while True:
    r = v % P
    if r in r_circ:
        break
    r_circ.append(r)
    v *= 10

ans = 0
if P in (2, 5):
    for i, s in enumerate(S):
        if int(s) % P == 0:
            ans += i+1
else:
    pr = 0
    rcntmap = [0] * P
    rcntmap[0] = 1  # r - 0 patten
    for i in reversed(range(len(S))):
        d = int(S[i])
        r = (d * r_circ[(len(S)-1-i) % len(r_circ)] + pr) % P
        #r = int(S[i:]) % P
        ans += rcntmap[r]
    
        rcntmap[r] += 1
        pr = r

print(ans)
