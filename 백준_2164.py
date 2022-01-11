from collections import deque
n = int(input())

num_list = deque([i for i in range(1, n+1)])

while len(num_list) != 1:
    num_list.popleft()
    temp = num_list.popleft()
    num_list.append(temp)



print(num_list[0])