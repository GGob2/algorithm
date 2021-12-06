n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))

num_list.sort(reverse=True)

result = sum(num_list)
free = 0 
for j in range(2, n, 3):
    free += num_list[j]

print(result - free)