(H, W) = map(int, input().split())
a = []
for i in range(H):
    a.append(list(map(int, input().split())))
#print("a: ")
#print(a)

odd_flag = []
for i in range(len(a)):
    odd_flag.append(list())
    for j in range(len(a[i])):
        if a[i][j]%2 != 0:
            odd_flag[i].append(True)
        else:
            odd_flag[i].append(False)
#print("odd_flag: ")
#print(odd_flag)

odd_sum = 0
for i in range(len(odd_flag)):
    odd_sum += odd_flag[i].count(True)
#print(odd_sum)

def move(h, w):
    if h%2 == 0:
        if w == W-1:
            return (h+1, w)
        else:
            return (h, w+1)
    else:
        if w == 0:
            return (h+1, w)
        else:
            return (h, w-1)

s_h = 0
s_w = 0
N = 0
ope_list = []
move_flag = False
while odd_sum >= 2:
    # 移動先到着
    if move_flag is True and odd_flag[s_h][s_w] is True:
        move_flag = False
        (s_h, s_w) = move(s_h, s_w)
        odd_sum -= 2
    # 移動中
    elif move_flag is True and odd_flag[s_h][s_w] is False:
        ope = ""
        ope += str(s_h+1) + " " + str(s_w+1) + " "
        (s_h, s_w) = move(s_h, s_w)
        ope += str(s_h+1) + " " + str(s_w+1) + "\n"
        ope_list.append(ope)
        N += 1
    # 移動すべきものなし
    elif move_flag is False and odd_flag[s_h][s_w] is False:
        (s_h, s_w) = move(s_h, s_w)
    # 移動元到着
    elif move_flag is False and odd_flag[s_h][s_w] is True:
        move_flag = True
        ope = ""
        ope += str(s_h+1) + " " + str(s_w+1) + " "
        (s_h, s_w) = move(s_h, s_w)
        ope += str(s_h+1) + " " + str(s_w+1) + "\n"
        ope_list.append(ope)
        N += 1

print(N)
for i in range(len(ope_list)):
    print(ope_list[i], end="")
    print("\n")

