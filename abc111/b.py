N = int(input())

ans = N

while ans < 999:
    if int(ans/100) == int((ans%100)/10) and int(ans/100) == int(ans%10):
        break
    ans += 1

print(ans)


