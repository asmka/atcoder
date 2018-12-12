S = input()

minnum = 1000
for i in range(len(S)):
    num = abs(753-int(S[i:i+3]))
    if num < minnum:
        minnum = num

print(minnum)

