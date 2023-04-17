import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = []

def back(num):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, num+1):
        if i in result:
            continue
       
        result.append(i)
        back()
        result.pop()

back(n)


