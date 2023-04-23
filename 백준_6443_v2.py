import sys

input = sys.stdin.readline

n = int(input())
result_list = []
def back(str_list, visit, cnt, result):
    
    if cnt == len(str_list):
        if result in result_list:
            return
        result_list.append(result)
        print(result)

    for i in range(len(str_list)):
        if visit[i] :
            continue
        visit[i] = 1
        back(str_list, visit, cnt + 1, result + str_list[i])
        visit[i] = 0


for i in range(n):
    string = list(input().rstrip())
    string.sort()
    visit = [0 for _ in range(len(string))]     
    back(string, visit, 0, '',)