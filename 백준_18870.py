import sys

input = sys.stdin.readline

N = input()

num_list = list((map(int, input().split())))
temp_num_list = sorted(list(set((num_list))), reverse=True)

num_dict = {}

for i in range(len(temp_num_list)):
    num_dict[str(temp_num_list[i])] = len(temp_num_list) - i -1

for j in num_list:
    print(num_dict[str(j)] , end=" ")