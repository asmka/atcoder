aaS = input()

ans = 'Yes'
buf = S
while buf:
    if len(buf) < 2 or not 'hi' in buf[-2:]:
        ans = 'No'
        break
    buf = buf[0:-2]

print(ans)
