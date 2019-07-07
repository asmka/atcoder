N, A, B = map(int, input().split())

train = A*N
taxi = B

ans = train if train < taxi else taxi
print(ans)
