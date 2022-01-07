n = int(input())

for i in range(n):
    sentence = input()
    result = 0
    temp = 0
    before_O = False
    for j in range(len(sentence)):
        if sentence[j] == "O" and before_O == True:
            temp += 1
            result += temp
        elif sentence[j] == "O" and before_O == False:
            temp = 1
            result += temp
            before_O = True
        else:
            before_O = False
            continue
    print(result)