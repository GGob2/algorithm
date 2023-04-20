import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

result = []
count = 0
visit = []

def back(num, result):
    if sum(result) == s and len(result) != 0:
        global count
        count += 1
           
    for i in range(num, n):
        if i in visit:
            continue

        visit.append(i)
        result.append(num_list[i])
        back(i+1, result)
        result.pop()
        visit.pop()
          
back(0, result)
print(count)