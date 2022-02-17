a, b = map(int, input().split())
num_list = list(map(int, input().split()))
start, end = 1, max(num_list)

while start <= end:
    mid = (start + end) // 2
    
    tree = 0
    for i in num_list:
        if i >= mid:
            tree += i - mid
        
    if tree >= b:
        start = mid + 1
    else:
        end = mid -1

print(end)