N, M, V, P = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
th_score = A[P-1]

def is_pickedup(init_score: int) -> bool:
    return True

ans = 0
was_checked = {}
for i, a in enumerate(A):
    if a in was_checked:
        ans += 1
        continue
    if is_pickedup(a):
        ans += 1

print(ans)
