n = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

result = 0

for i in range(n-1):
    result += num_list[i]
    num_list[i+1] += num_list[i]

print(result + num_list[-1]) 