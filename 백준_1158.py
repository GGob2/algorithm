a, b = map(int, input().split())

num_list = [i for i in range(1, a+1)]
result = []

temp = 0 
for j in range(a):
    temp += b-1
    if temp >= len(num_list):
        temp = temp % len(num_list)
    
    result.append(str(num_list.pop(temp)))

print("<"+ ", ".join(result[:])+">")
