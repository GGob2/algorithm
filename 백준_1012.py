import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(graph, a, b):    
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):              # 상하좌우 좌표 할당
            nx, ny = dx[i] + x, dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:                         
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return

for i in range(T):
    count = 0
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for k in range(n):
        for l in range(m):
            if graph[k][l] == 1:
                bfs(graph, k, l)
                count += 1
    print(count)




    


