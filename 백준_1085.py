x, y, w, h = map(int, input().split())

result_x = 0
result_y = 0

if w / 2 >= x:
    result_x = abs(0-x)
else:
    result_x = w - x

if h / 2 >= y:
    result_y = abs(0-y)
else:
    result_y = h - y

print(min(result_x, result_y))