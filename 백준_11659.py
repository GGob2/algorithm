import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list_sum = [0]
sum_value = 0 

for j in num_list:
    sum_value += j
    num_list_sum.append(sum_value)

for i in range(m):
    a, b = map(int, input().split())
    print(num_list_sum[b] - num_list_sum[a-1])

