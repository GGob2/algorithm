
def solution(board):
    answer = 0
    n = len(board)
    row, col = [-1, 0, 1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue
                
            else:
                for r in row:
                    for c in col:
                        try:
                            board[i+r][j+c] = 1
                        except:
                            continue                
    return answer

solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
