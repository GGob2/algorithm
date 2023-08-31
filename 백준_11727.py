import sys

input = sys.stdin.readline

n = int(input())

num_list = [0 for _ in range(1001)]

num_list[0] = 1
num_list[1] = 3
num_list[2] = 5

for i in range(3, n+1):
    num_list[i]= (num_list[i-2] * 2) + num_list[i-1]

print(num_list[n-1]%10007)