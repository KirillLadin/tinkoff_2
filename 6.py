def sort_key(item):
    return item[1]


n = int(input())
l = []
for i in range(0, n):
    s, f = map(int, input().split())
    l.append([s, f])
l = sorted(l, key=sort_key)
res = []
while len(l) > 0:
    elem = l[0]
    flag = True
    for r in res:
        if (r[0] < elem[0] < r[1]) or (elem[0] < r[0] < elem[1]) or (r[0] < elem[1] < r[1]) or (elem[0] < r[1] < elem[1]):
            flag = False
            l.remove(elem)
            break
    if flag:
        res.append(elem)
        l.remove(elem)
res = sorted(res, key=lambda e: (e[0], len(e)))
max = 0
curr_res = 1
curr = res[0][1]
for i in range(1, len(res)):
    if res[i][0] == curr:
        curr_res += 1
    else:
        if curr_res > max:
            max = curr_res
        curr_res = 1
    curr = res[i][1]
if curr_res > max:
    max = curr_res
print(max)

