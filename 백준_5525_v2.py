import sys

input = sys.stdin.readline

def makeTable(pattern):
    table = [0 for i in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        while(j>0 and pattern[i] != pattern[j]):
            j = table[j-1]

        if pattern[i] == pattern[j]:
            table[i] = j+1
            j += 1
    return table

def KMP(parent, pattern):
    table = makeTable(pattern)

    j = 0
    result = 0

    for i in range(len(parent)):                    # 전체 길이를 돌며
        while(j>0 and parent[i] != pattern[j]):     # 하나씩 비교
            j = table[j-1]                          # 
        
        if parent[i] == pattern[j]:                 # 글자가 일치하는 경우
            if j == len(pattern) - 1:               # 마지막 인덱스
                result += 1                         # 결과 +1
                j = table[j]                        
            else:
                j+= 1                               # 마지막 인덱스가 아닌 경우
    return result 

n = int(input())
m = int(input())
parent = input().rstrip()

pattern = n * "IO" + "I"

result = KMP(parent, pattern)
print(result)