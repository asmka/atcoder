N = int(input())

def rec(p, ptn, ans):
    if len(ptn) > 0 and int(ptn) <= int(N) and '3' in ptn and '5' in ptn and '7' in ptn:
        ans[0] += 1

    if p >= len(str(N)):
        return
    else:
        for n in ('3', '5', '7'):
            ptn += n
            rec(p+1, ptn, ans)
            ptn = ptn[:-1]

ans = [0]
rec(0, "", ans)

print(ans[0])


