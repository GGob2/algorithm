import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

def bfs(x, y, area):        # x, y 좌표 및 맵
    queue.append((x, y))    # 방문점 설정
    
    dx = [-1, 0, 1, 0]      # 좌-우
    dy = [0, 1, 0, -1]      # 상-하
    
    visit[x][y] = 1         # 방문 처리

    while queue:            # 방문해야할 곳이 남아 있는 경우
        x, y = queue.popleft()  # 방문

        for j in range(4):      # 상하좌우 확인
            ax = x + dx[j]
            ay = y + dy[j]

            if 0 <= ax < n and 0 <= ay < n and area[ax][ay] == area[x][y] and not visit[ax][ay]:        # 범위, 색깔, 방문 여부 확인
                 visit[ax][ay] = 1  # 방문 처리
                 queue.append((ax, ay)) # 방문해야하는 곳 추가

map = []
map_v2 = []

for i in range(n):
    line = input().rstrip()
    map.append(list(line))
    map_v2.append(list(line.replace("G", "R")))         # 맵 

queue = deque()

# 일반인

visit = [[0] * n for _ in range(n)]                     # 방문 처리를 위한 큐
count1 = 0                                              # 다른 영역 확인시 +1

for i in range(n):
    for k in range(n):
        if not visit[i][k]:

            bfs(i, k, map)                              # bfs 수행. 모든 영역을 확인해야 하므로, 2중 for문 사용
            count1 += 1

# 적록색약
visit = [[0] * n for _ in range(n)]                     
count2 = 0

for i in range(n):
    for k in range(n):
        if not visit[i][k]:
            bfs(i, k, map_v2)
            count2 += 1

print(count1, count2)
