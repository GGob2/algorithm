n = int(input())

num_list = [i for i in range(1, n+1)]

while len(num_list) > 1:
    print(num_list.pop(0), end=" ")
    num_list.append(num_list.pop(0))
print(num_list[0]) 
