N = int(input())
cap = []
for i in range(5):
    cap.append(int(input()))

d = min(cap)
ans = 5 + ((N-1)//d + 1) - 1

print(ans)
