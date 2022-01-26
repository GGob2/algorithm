n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    
    room_num = 1 + (c // a)
    floor = c % a
    
    if floor == 0:
        floor = a
        room_num -= 1

    print(floor*100+room_num)
