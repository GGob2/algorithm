a, b = map(int, input().split())
b += 1
result = [True] * b

for i in range(2, int(b ** 0.5)+1):
    if result[i]:
        for j in range(2*i, b, i):
            result[j] = False

for k in range(a, b):
    if k > 1 and result[k] == True:
        print(k)


