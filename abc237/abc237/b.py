from typing import List

H, W = map(int, input().split())

A: List[List[int]] = []
for _ in range(H):
    A.append(list(map(int, input().split())))

for w in range(W):
    Bw: List[int] = []
    for h in range(H):
        Bw.append(A[h][w])
    print(*Bw)
