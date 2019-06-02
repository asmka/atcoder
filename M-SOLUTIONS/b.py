S = input()

ans = 'YES' if 15-len(S) + S.count('o') >= 8 else 'NO'
print(ans)
