a, b = map(int, input().split())
num_list = []

for i in range(a):
    num_list.append(int(input()))

start, end = 1, max(num_list)

while start <= end:
    mid = (start + end) // 2
    
    line = 0
    
    for i in num_list:
        line += i // mid
        
    if line >= b:
        start = mid + 1
    else:
        end = mid -1

print(end)