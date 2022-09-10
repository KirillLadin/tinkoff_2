x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())
if x1_2 > x1_1:
    w = x2_2 - x1_1
else:
    w = x2_1 - x1_2
if y2_2 > y2_1:
    h = y2_2 - y1_1
else:
    h = y2_1 - y1_2
print(max(h, w) ** 2)
