import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

def bfs(x, y, area):
    queue.append((x, y))
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    visit[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for j in range(4):
            ax = x + dx[j]
            ay = y + dy[j]

            if 0 <= ax < n and 0 <= ay < n and area[ax][ay] == area[x][y] and not visit[ax][ay]:
                 visit[ax][ay] = 1
                 queue.append((ax, ay))

map = []
map_v2 = []

for i in range(n):
    line = input().rstrip()
    map.append(list(line))
    map_v2.append(list(line.replace("G", "R")))

queue = deque()

# 일반인

visit = [[0] * n for _ in range(n)]
count1 = 0

for i in range(n):
    for k in range(n):
        if not visit[i][k]:
            bfs(i, k, map)
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
