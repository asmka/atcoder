abc = int(input())
a = abc // 100
b = abc // 10 % 10
c = abc % 10
bca = b * 100 + c * 10 + a
cab = c * 100 + a * 10 + b

ans = abc + bca + cab
print(ans)
