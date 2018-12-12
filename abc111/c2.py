import collections

n = int(input())
v = list(map(int, input().split()))

v_odd = []
for i in range(0, n, 2):
    v_odd.append(v[i])
v_even = []
for i in range(1, n, 2):
    v_even.append(v[i])

odd_dic = collections.Counter(v_odd)
odd_sort = sorted(odd_dic.items(), key=lambda x: -x[1])
odd_maxkey = odd_sort[0][0]
odd_cnt1 = odd_sort[0][1]
if len(odd_sort) > 1:
    odd_cnt2 = odd_sort[1][1]
else:
    odd_cnt2 = 0

even_dic = collections.Counter(v_even)
even_sort = sorted(even_dic.items(), key=lambda x: -x[1])
even_maxkey = even_sort[0][0]
even_cnt1 = even_sort[0][1]
if len(even_sort) > 1:
    even_cnt2 = even_sort[1][1]
else:
    even_cnt2 = 0

ans = len(v_odd) + len(v_even)
if odd_maxkey == even_maxkey:
    ans -= max(odd_cnt1 + even_cnt2, odd_cnt2 + even_cnt1)
else:
    ans -= odd_cnt1 + even_cnt1


#print(odd_cnt1)
#print(odd_cnt2)
#print(even_cnt1)
#print(even_cnt2)

print(ans)

