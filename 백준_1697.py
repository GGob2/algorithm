import sys
from collections import deque

input = sys.stdin.readline

older, young = map(int, input().split())

visit = [0 for i in range(100001)]

def bfs(a):
    queue = deque([])
    queue.append(a)
    
    while queue:
        loc = queue.popleft()
    
        if loc == young:
            print(visit[loc])
            break 
    
        for move in (loc -1, loc +1, 2*loc): 
            if 0 <= move <= 100000 and not visit[move]:  # not visit[move] = visit[move]에 값이 0인 경우에만, 즉, visit 하지 않은 경우
                visit[move] = visit[loc] + 1
                queue.append(move)
bfs(older)
