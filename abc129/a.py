P, Q, R = map(int, input().split())

ans = P+Q if P+Q < R+Q else R+Q
ans = P+R if P+R < ans else ans
print(ans)
