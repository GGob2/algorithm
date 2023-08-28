import sys
n = int(sys.stdin.readline())

result = set()

for i in range(n):
    command_line = sys.stdin.readline().split()
    command = command_line[0]

    if len(command_line) > 1:
        num = int(command_line[1])

    if command == "add":
        if num not in result:
            result.add(num)
    
    if command == "remove":
        if num in result:
            result.discard(num)
    
    if command == "check":
        if num in result:
            print(1)
        else:
            print(0)
    
    if command == "toggle":
        if num in result:
            result.discard(num)
        else:
            result.add(num)
    
    if command == "all":
        result = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    
    if command == "empty":
        result = set()