import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())   # 토마토 농장 크기 입력받기 

storage = [list(map(int, input().split()) )for _ in range(n)]  # 토마토 입력 받기

queue = deque([])   # 큐 생성

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우 구현을 위힌 좌표 생성
count = 0 

for i in range(n):                      # 1인 경우에만 좌표 값을 큐에 담기
    for j in range(m):
        if storage[i][j] == 1:
            queue.append([i,j])

def bfs():                              # bfs 함수 선언
    while queue:                        # 큐가 빌 때 까지
        x, y = queue.popleft()          # 큐 에서 좌표 뽑기

        for i in range(4):              # 상하좌우 좌표 할당
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and storage[nx][ny] == 0:    # 0보다 크면서 최대 n, m이 넘어가지 않고 값이 0이라면
                storage[nx][ny] = storage[x][y] + 1                     # 횟수를 기억하기 위해 1이 아닌 +1을 해서 넣기
                queue.append([nx, ny])                                  # 해당 위치 큐에 넣기
bfs()

for i in storage:                       # 토마토에서
    for j in i:                         
        if j == 0:                      # 안 익은게 있다면
            print(-1)                   # -1 출력
            exit(0)                     # 프로그램 종료 

    count = max(count, max(i))          # 최대값 담기

print(count - 1)
