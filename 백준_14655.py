n = int(input())

num = list(map(int, input().split()))
result = 0
for i in range(len(num)):
    if num[i] < 0:
        num[i] = num[i] * (-1)
    result += num[i]

print(result * 2)

