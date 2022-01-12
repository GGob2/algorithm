n = int(input())
result = []

for i in range(n):
    a, b = input().split()
    result.append([a, b])

result.sort(key=lambda x:int(x[0]))


for j in range(n):
    print(result[j][0], result[j][1])
