l, r = input().split()
result = 0
if len(l) != len(r):
    result = 0
else:
    for i in range(len(l)):
        if l[i] == "8" and r[i] == "8":
            result += 1
        elif l[i] != r[i]:
            break
print(result)
