a, b = map(int, input().split())

if a != 0:
    if b >= 45:
        b = b - 45
    else:
        a = a - 1
        b = b + 15
else:
    if b >= 45:
        b = b - 45
    else:
        a = 23
        b = b + 15
print(a, b)