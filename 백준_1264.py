while True:
    a = list(input())
    if len(a) == 1 and a[0] == "#":
        break
    else: 
        count = 0
        for i in range(len(a)):
            if a[i] == "a" or a[i] == "e" or a[i] == "o" or a[i] == "u" or a[i] == "i":
                count += 1
            if a[i] == "A" or a[i] == "E" or a[i] == "O" or a[i] == "U" or a[i] == "I":    
                count += 1
        print(count)