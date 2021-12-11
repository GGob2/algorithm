n = int(input())

for i in range(n):
    t = int(input())
    num_list = list(map(int, input().split()))
    
    result = 0
    max = 0

    for j in range(len(num_list) -1, -1, -1):
        if(num_list[j] > max):
            max = num_list[j]
        else:
            result += max -num_list[j]
    
    print(result)
        
            