n = int(input())

num_list = []
result = []
count = 1
test = True

for i in range(n):
    num = int(input())
    
    while count <= num:
        num_list.append(count)
        result.append("+")
        count += 1
    
    if num_list[-1] == num:
        num_list.pop()
        result.append("-")
    else:
        test = False

if test == True:
    for _ in result:
        print(_)
else:
    print("NO")

