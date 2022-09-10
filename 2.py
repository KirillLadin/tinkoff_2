N = int(input())
d = dict()
for i in range(0, N):
    names = input().split()
    names.sort()
    s = names[0] + names[1] + names[2]
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
max = 0
for s in d:
    if d[s] > max:
        max = d[s]
print(max)
