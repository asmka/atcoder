n = int(input())
v = list(map(int, input().split()))

v_odd = []
for i in range(0, n, 2):
    v_odd.append(v[i])
v_even = []
for i in range(1, n, 2):
    v_even.append(v[i])

v_odd.sort()
v_even.sort()

ans = 0

cnt = 0
max_cnt = 1
for i in range(len(v_odd)):
    if i == 0:
        cnt = 1
    else:
        if v_odd[i] == v_odd[i-1]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 1
ans += len(v_odd) - max_cnt

cnt = 0
max_cnt = 1
for i in range(len(v_even)):
    if i == 0:
        cnt = 1
    else:
        if v_even[i] == v_even[i-1]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 1
ans += len(v_even) - max_cnt

print(ans)
    


