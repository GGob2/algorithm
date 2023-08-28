import sys

input = sys.stdin.readline

n, m = map(int, input().split())

land = []
visit = []
for i in range(n):
    row = list(map(int, input().split()))
    land.append(row)
    if 2 in row:
        visit.append([i, row.index(2)])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

while(visit):
    x, y = visit.pop()
    
    if land[x][y] == 0:
        continue

    land[x][y] = cnt
    cnt += 1

    for _ in range(4):
        ax = x+dx[_]
        ay = y+dy[_]
        if [ax, ay] not in visit:
            if 0 <= ax <= n and 0 <= ay <= m:
                visit.append([ax, ay])
                


