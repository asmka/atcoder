S = input()
Q = int(input())

buf = [0] * (3*(10**5)+10)
for i, s in enumerate(S):
    buf[i] = s

is_reverse = False
first = 0
last = len(S) - 1

def add_top(c):
    global buf
    global first
    if is_reverse:
        first += 1
    else:
        first -= 1
    buf[first] = c

def add_tail(c):
    global buf
    global last
    if is_reverse:
        last -= 1
    else:
        last += 1
    buf[last] = c

for i in range(Q):
    Query = input().split()
    t = int(Query[0])
    if t == 1:
        is_reverse = not is_reverse
        first, last = last, first
    else:
        f = int(Query[1])
        c = Query[2]
        if f == 1:
            add_top(c)
        else:
            add_tail(c)

ans_list = []
p = first
while True:
    ans_list.append(buf[p])
    if p == last:
        break
    if is_reverse:
        p -= 1
    else:
        p += 1
ans = ''.join(ans_list)
print(ans) 
