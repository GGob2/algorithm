import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for i in range(n)]
result = []
def answer(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                answer(x, y, N//2)
                answer(x, y+N//2, N//2)
                answer(x+N//2, y, N//2)
                answer(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

answer(0, 0 , n)
print(result.count(0))
print(result.count(1))
