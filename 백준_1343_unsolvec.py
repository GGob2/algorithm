board = list(input())
result = list()
result_v2 = list()
error = False
trans = 0

for i in board:
    if i == "." and trans != 0:
        result.append(trans)
        trans = 0
    elif i == ".":
        continue
    else:
        trans += 1
        

for k in result:
    if k % 2 != 0:
         error = True

    if k & 4 == 0:
        element = "AAAA" * (len(i) // 4)
        result_v2.append(element)
        element = ""
    
    if k % 4 == 2:
        element = "AAAA" * ((len(i)-2) // 4)
        element += "BB"
        result_v2.append(element)
        element = ""

    if k == 2:
        element = "BB"
        result_v2.append(element)
        element = ""


if error == True:
    print(-1)
else:
    for j in result_v2:
        if len(result_v2) == j:
            print(j)
        else:
            print(j, end=".")
        
