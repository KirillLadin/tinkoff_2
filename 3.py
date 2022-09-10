n = int(input())
data = input().split()
a_min = int(data[0])
a_max = int(data[1])
ans = a_min - a_max
for i in range(2, n):
    a = int(data[i])
    if i % 2 == 0:
        a_min = min(a_min, a)
        ans += a
    else:
        a_max = max(a_max, a)
        ans -= a
if a_max > a_min:
    ans = ans + 2 * (a_max - a_min)
print(ans)



