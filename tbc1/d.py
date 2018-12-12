N = int(input())

ans = 'No'
k = 2
while True:
    kk = k*(k-1)
    if kk > N*2:
        ans = 'No'
        break
    elif kk == N*2:
        ans = 'Yes'
        break
    k += 1

print(ans)
if ans == 'Yes':
    print(k)
    psum = (k-1)*k//2
    tops = []
    for i in range(k):
        ntop = psum - (k-1-i)*(k-i)//2 + 1
        tops.append(ntop)
    for i in range(k):
        print(k-1, end=" ")
        # 1st
        for j in range(i):
            print(tops[j]+(i-j-1), end=" ")
        # 2nd
        for j in range(k-1-i):
            print(tops[i]+j, end=" ")
        print('')


# 1 2 3 4
# 1 5 6 7
# 2 5 8 9

