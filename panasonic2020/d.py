N = int(input())

cset = [chr(ord('a')+i) for i in range(N)]
sset = ['a'] * N
def rec(di, usedci):
    if di >= len(sset):
        print(''.join(sset))
        return
    for i in range(usedci+1):
        sset[di] = cset[i]
        rec(di+1, usedci)
    sset[di] = cset[usedci+1]
    rec(di+1, usedci+1)

rec(1, 0)
