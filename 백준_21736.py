import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
campus = []
queue = deque()
result = 0
visit = [[False] * b for _ in range(a)]

for i in range(a):
    line = ''.join(input().split())
    campus.append(line)

    for j in range(b):
        if line[j] == 'I':
            queue.append([i, j])
            visit[i][j] = True

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]


while(queue):
    row, col = queue.popleft()
    
    if campus[row][col] == 'P':
        result += 1

    for _ in range(4):
        arow = row + drow[_]
        acol = col + dcol[_]

        if 0 <= arow < a and 0 <= acol < b:
            if not visit[arow][acol]:
                if campus[arow][acol] == 'X':
                    continue
                else:
                    queue.append([arow, acol])
                    visit[arow][acol] = True

if result > 0:
    print(result)
else:
    print('TT')