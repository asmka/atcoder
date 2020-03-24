def check_pickedup(M: int, V: int, P: int, A: list, accum_score: list, i: int) -> bool:
    is_pickedup = False
    return True

def main():
    N, M, V, P = map(int, input().split())
    A = list(map(int, input().split()))
    
    A.sort(reverse=True)
    th_score = A[P-1]
    
    accum_score = [A[0]] * N
    for i in (1, N):
        accum_score[i] = accum_score[i-1] + A[i]
    
    # Reduce N-V scores each judge
    ans = 0
    was_checked = {}
    for i, a in enumerate(A):
        # Check a will be picked up
        if a in was_checked:
            ans += 1
            continue
        if check_pickedup(M, V, P, A, accum_score, i):
            ans += 1
            was_checked[a] = True
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
