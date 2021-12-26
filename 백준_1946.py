import sys

n = int(input())

for i in range(n):

    k = int(input())
    num_list = []
    result = 1
    
    for j in range(k):
        paper, interview = map(int, sys.stdin.readline().split())
        num_list.append([paper, interview])

    num_list.sort()
    tmp = num_list[0][1]

    for l in range(1, k):
        if tmp > num_list[l][1]:
            result += 1
            tmp = num_list[l][1]

    print(result)

