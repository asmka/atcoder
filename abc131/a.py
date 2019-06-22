S = input()

ans = 'Good'
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        ans = 'Bad'
        break

print(ans)
