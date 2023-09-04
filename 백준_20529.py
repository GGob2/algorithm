import sys

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
     
    n = int(input())
    result = 13
    mbti_list = list(map(str, input().split()))
    
    if n > 32:  # n이 32가 넘어가게 되면 동일한 mbti가 최소 3명
        print(0)
    
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    tmp = 0
                    for _ in range(4):
                        if mbti_list[i][_] != mbti_list[j][_]: 
                            tmp += 1
                        if mbti_list[j][_] != mbti_list[k][_]: 
                            tmp += 1
                        if mbti_list[i][_] != mbti_list[k][_]: 
                            tmp += 1
                    result = min(result, tmp)
        print(result)