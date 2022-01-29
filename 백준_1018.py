n, m = map(int, input().split())
board = []
result = []

for i in range(n):
    board.append(input())

for a in range(n - 7):
    for b in range(m - 7):
        index_a = 0
        index_b = 0

        for c in range(a, a+8):
            for d in range(b, b+8):
                if (c+d) % 2 == 0 :
                    if board[c][d] != "W":
                        index_a += 1
                    if board[c][d] != "B":
                        index_b += 1
                else:
                    if board[c][d] != "B":
                        index_a += 1
                    if board[c][d] != "W":
                        index_b += 1
        result.append(index_a)
        result.append(index_b)

print(min(result))
                    