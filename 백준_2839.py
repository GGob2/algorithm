N = int(input())
result = 0

while N >= 0:
    if N % 5 == 0:
        result += (N//5)
        print(result)
        break;
    N -= 3
    result += 1
else:
        print(-1)
    

    