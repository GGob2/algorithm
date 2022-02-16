from tabnanny import check


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    num_list = list(map(int, input().split()))
    rank = 0
    check_list = [0 for i in range(a)]
    check_list[b] = 1

    while True:
        if  num_list[0] == max(num_list):
            rank += 1

            if check_list[0] != 1:
                del num_list[0]
                del check_list[0]
            else:
                print(rank)
                break
        else:
            num_list.append(num_list[0])
            check_list.append(check_list[0])
            del num_list[0]
            del check_list[0]

    
        

        
    
