n = int(input())

for i in range(n):
    j = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort(reverse=True)
    
    result = 0
    
    for k in range(j-2):
        result = max(result, num_list[k] - num_list[k+2])
    
    print(result)