ant = []
for i in range(5):
    ant.append(int(input()))
k = int(input())

ans = 'Yay!'
if (ant[-1] - ant[0] > k):
    ans = ':('

print(ans)
