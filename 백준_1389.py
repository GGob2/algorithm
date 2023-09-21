import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

relation = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())

    relation[a].append(b)
    relation[b].append(a)

result = []

for i in range(1, n+1):
    num = [0] * (n+1)
    visit = [i]
    queue = deque()
    queue.append(i)

    while queue:
        idx = queue.popleft()
        for i in relation[idx]:
            if i not in visit:
                num[i] = num[idx] + 1
                visit.append(i)
                queue.append(i)
    result.append(sum(num))

print(result.index(min(result))+1)



                
                



