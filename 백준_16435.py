n, s = map(int, input().split())
    
fruit_list = list(map(int, input().split()))    

fruit_list.sort()

for j in range(len(fruit_list)):
    if fruit_list[j] <= s:
        s += 1
    else:
        break
print(s)
