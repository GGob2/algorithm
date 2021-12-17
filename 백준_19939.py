ball, box = map(int, input().split())

minimum = (box*(box+1)) // 2 

if minimum > ball:
    print(-1)

elif (ball - minimum) % box == 0:
    print(box-1)

else:
    print(box)

    