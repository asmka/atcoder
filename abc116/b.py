s = int(input())

seta = set()
seta.add(s)

p = s
c = s
i = 2
while True:
    if p%2 == 0:
        c = p//2
    else:
        c = 3*p+1

    if c in seta:
        break
    else:
        seta.add(c)

    p = c
    i += 1

print(i)

