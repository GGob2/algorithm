T = int(input())
A = 0
B = 0
C = 0

while T >= 0:
    if T % 10 != 0:
        print(-1)    
        break

    if (T // 300) >= 1:
        A += T // 300
        T -= (300 * (T // 300))
        
    if (T == 0):
        print(A, B, C)
        break;

    if T // 60 >= 1:
        B += T // 60
        T -= (60 * (T // 60))
        
    if (T == 0):
        print(A, B, C)
        break;

    if T // 10 >= 1:
        C += T // 10
        T -= (10 * (T // 10))
        
    if (T == 0):
        print(A, B, C)
        break;
        
