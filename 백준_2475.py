num_list = list(map(int, input().split()))
temp = 0
result = 0
for i in num_list:
    temp += i * i
result = temp % 10
print(result)