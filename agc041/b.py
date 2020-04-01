def check_pickedup(N: int, M: int, V: int, P: int, A: list, accum_score: list, i: int) -> bool:
    th_score = A[P-1]
    if A[i] >= th_score:
        return True
    sum_surplus = (accum_score[i-1] - (accum_score[P-2] if P-2 >=0 else 0)) - ((i-1)-(P-2))*A[i]
    #print('i: ', i)
    #print('th_score: ', th_score)
    #print('sum_surplus: ', sum_surplus)
    #print('th_score - A[i]: ', th_score - A[i])
    if th_score - A[i] <= M and sum_surplus <= M*(N-V):
        return True
    return False

def main():
    N, M, V, P = map(int, input().split())
    A = list(map(int, input().split()))
    
    A.sort(reverse=True)
    
    accum_score = [A[0]] * N
    for i in range(1, N):
        accum_score[i] = accum_score[i-1] + A[i]
    
    # Reduce N-V scores each judge
    ans = 0
    was_checked = {}
    for i, a in enumerate(A):
        # Check a will be picked up
        if a in was_checked:
            ans += 1
            continue
        if check_pickedup(N, M, V, P, A, accum_score, i):
            ans += 1
            was_checked[a] = True
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
