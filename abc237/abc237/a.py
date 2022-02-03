N = int(input())

ans = "No"
if N >= -pow(2, 31) and N < pow(2, 31):
    ans = "Yes"
print(ans)
