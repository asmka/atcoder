S = input()
T = input()

ans = "Yes"

def CheckDup(src, dest):
    dic = {}
    for i in range(len(src)):
        if src[i] in dic:
            if dic[src[i]] != dest[i]:
                return("No")
        else:
            dic[src[i]] = dest[i]
    return("Yes")

ans1 = CheckDup(S, T)
ans2 = CheckDup(T, S)

if ans1 == "No" or ans2 == "No":
    ans = "No"

print(ans)
