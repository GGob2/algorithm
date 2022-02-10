n = int(input())

room_num = 1
count = 1

while n > room_num:
    room_num += 6 * count
    count += 1 

print(count)