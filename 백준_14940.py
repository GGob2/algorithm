import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

land = []
queue = deque()
visit = [[False] * m for _ in range(n)]
result = [[-1] * m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    land.append(row)
    
    if 2 in row:
        queue.append([i, row.index(2)])  # 목표 지점 탐색
        visit[i][row.index(2)] = True
        result[i][row.index(2)] = 0
    
    for j in range(m):
        if row[j] == 0:
            result[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while(queue):
    y, x = queue.popleft()     

    for _ in range(4):
        ay = y+dy[_]
        ax = x+dx[_]
        
        if 0 <= ax < m and 0 <= ay < n: 
            if not visit[ay][ax] and land[ay][ax] == 1:        
                queue.append([ay, ax])
                visit[ay][ax] = True
                result[ay][ax] = result[y][x] + 1

for i in result:
    for j in i:
        print(j, end =' ')
    print()