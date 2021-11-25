board = list(input())
result = list()
result_v2 = list()
is_point = False
error = False

X_len = 0
point_len = 0

for i in range(len(board)):
    if i == len(board) -1 and board[i] != ".":
        result.append(X_len+1) 
    
    elif i == len(board) -1 and board[i] == ".":
        result.append(X_len+1) 
     
    elif board[i] != ".":
        is_point = False
        X_len += 1

    elif board[i] == "." and is_point == False:
        result.append([(i - X_len), X_len])
        X_len = 0
        is_point = True

    else:
        continue


# for k in result:
#     if k % 2 != 0:
#          error = True

#     if k & 4 == 0:
#         element = "AAAA" * (len(i) // 4)
#         result_v2.append(element)
#         element = ""
    
#     if k % 4 == 2:
#         element = "AAAA" * ((len(i)-2) // 4)
#         element += "BB"
#         result_v2.append(element)
#         element = ""

#     if k == 2:
#         element = "BB"
#         result_v2.append(element)
#         element = ""


# if error == True:
#     print(-1)
# else:
#     for j in result_v2:
#         if len(result_v2) == j:
#             print(j)
#         else:
#             print(j, end=".")
        
