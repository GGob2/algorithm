n = int(input())

temp = 0
result = 0

for i in range(n, 0, -1):
    temp = 0
    temp += i
    for j in str(i):
        temp += int(j)
    
    if temp == n:
        result = i

print(result)



