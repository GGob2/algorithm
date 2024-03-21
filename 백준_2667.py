import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

def bfs(x, y, area):                # 현재 x, y 좌표, 맵
    queue.append((x, y))            # 현재 위치 추가

    dx = [-1, 0, 1, 0]              # 좌우
    dy = [0, -1, 0, 1]              # 상하

    visit[x][y] = 1                 # 방문 처리

    while(queue):                   # 방문해야할 곳이 남아 있으면
        x, y = queue.popleft()      # 방문

        for _ in range(4):
            ax = x + dx[_]
            ay = y + dy[_]

            if 0 <= ax < n and 0 <= ay < n and area[ax][ay] == area[x][y] and not visit[ax][ay]: # 범위 확인 & 같은 단지 & 방문 안한 집
                visit[ax][ay] = 1                                                                # 방문 처리
                queue.append((ax, ay))
                count += 1                                                                       # 큐에 추가



visit = [[0] * n for k in range(n)] # 방문 확인

queue = deque() # 방문 큐

count = 0 # 집안 세대 수 카운트

count_list = [] # 결과 저장할 리스트 

land = [] # 땅 입력 받기

for i in range(n):
    land.append(list(input().rstrip()))

