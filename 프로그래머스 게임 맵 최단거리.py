def solution(maps):
    n, m = len(maps)-1, len(maps[0])-1
    answer = 0
    queue = []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    way = [[0,0]]
    
    while queue:
        x, y = way.pop(0)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx <= n and 0 <= ny <= m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[nx][ny] + 1      # 경로 비용 설정
                queue.append(nx, ny)
    
    dest = maps[n][m]

    if dest == 1:
        answer = -1
    else:
        answer = dest
        
    return answer