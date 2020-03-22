S = input()

def is_rotate(s: str) -> bool:
    is_r = True
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            is_r = False
    #print(s, is_r)
    return is_r

N = len(S)
ans = 'No'
if is_rotate(S) and is_rotate(S[:(N-1)//2]) and is_rotate(S[(N+3)//2 - 1:]):
    ans = 'Yes'

print(ans)
