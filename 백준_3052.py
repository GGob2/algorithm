result = []

for i in range(10):
    a = int(input())

    if (a % 42) in result:
        continue
    else:
        result.append(a%42)

print(len(result))
