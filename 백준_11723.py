import sys
n = int(sys.stdin.readline())

result = []
result_v2 = [str(i)for i in range(1, 21)]

for i in range(n):
    command_line = sys.stdin.readline().split()
    
    command = command_line[0]
    if len(command_line) > 1:
        num = command_line[1]

    if command == "add":
        if num in result:
            pass
        else:
            result.append(num)
    
    if command == "check":
        if num in result:
            print(1)
        else:
            print(0)
    
    if command == "remove":
        if num in result:
            result.remove(num)
        else:
            pass
    
    if command == "toggle":
        if num in result:
            result.remove(num)
        else:
            result.append(num)
    
    if command == "all":
        result = result_v2
    
    if command == "empty":
        result = []



    

