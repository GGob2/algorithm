n = int(input())

num_list = list(map(int, input().split()))
check_list = [0] * 1000001
arrow = 0

for i in range(n):
    if check_list[num_list[i]] == 0:
        arrow += 1
        check_list[num_list[i] -1] += 1
    else:
        check_list[num_list[i]] -= 1
        check_list[num_list[i] -1] += 1    

print(arrow)
    
        
    
        
