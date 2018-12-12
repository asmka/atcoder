N = int(input())
W = []
head = ''
ans = "Yes"
for i in range(N):
    W.append(input())
while len(W) != 0:
    word = W[-1]
    W.pop()
    if word in W or (head != '' and word[-1] != head):
        ans = "No"
        break
    head = word[0]
print(ans)

