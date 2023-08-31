import sys

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    case = int(input())
    num = {}
    times = 1
    
    
    for j in range(case):
    
        name, wear = input().split()

        if wear in num.keys():
            num[wear] += 1
        else:
            num[wear] = 1
        
    for i in num.values():
        times = times * (i+1)

    print(times-1)
        
    

    # 투명 모자, 상의, 하의 고려 (3, 2 2) 인 경우 (4, 3, 3 -1)