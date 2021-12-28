n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))
result = 1
max_value = num_list[-1]

for j in range(len(num_list)-1, -1, -1):
    if max_value < num_list[j]:
        result += 1
        max_value = num_list[j]

print(result)