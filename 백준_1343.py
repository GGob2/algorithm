board = list(input())
X_len = 0
point = False
error = False
adding = False

if board[-1] != ".":
    board.append(".")
    adding = True

for i in range(len(board)):
    if board[i] != ".":
        point = False
        X_len += 1
    
    elif (board[i] == "." and point == False) or i == len(board):
        if X_len % 4 == 0:
            element = "AAAA" * (X_len // 4)    
        
        elif X_len % 4 == 2:
            element = "AAAA" * (X_len // 4)
            element += "BB"        
        elif X_len % 2 == 0:
            element = "BB"
        else:
            error = True

        if error == False:           
            board[i-X_len: i] = element
            element = ""
            point = True
            X_len = 0
        else:
            break
    else:
        continue

if adding == True:
    board.pop()

if error == True:
    print(-1)
else:
    for j in board:
        print(j, end="")