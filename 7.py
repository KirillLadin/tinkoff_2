def f(s):
    d = dict()
    pos = 0
    for c in s:
        if c not in d:
            d[c] = [pos]
        else:
            d[c].append(pos)
        pos += 1
    s = sorted(s)
    res = 0
    pos = 0
    for c in s:
        if len(d[c]) == 1:
            a = d[c][0]
            if a >= pos:
                res += d[c][0] - pos
            else:
                res += len(s) - pos + d[c][0]
            pos = d[c][0]
        else:
            lst = d[c]
            min = len(s) + 1
            for l in lst:
                if l < min:
                    min = l
            if pos < min:
                res += min - pos
            else:
                res += len(s) - pos + min
            pos = min
            d[c].remove(min)
    return res




s = input()
n = int(input())
res = []
for i in range(0, n):
    start, end = map(int, input().split())
    res.append(f(s[start - 1: end]))
for r in res:
    print(r)

