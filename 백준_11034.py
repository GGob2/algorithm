while True:
    try:
        A, B, C = input().split()
        A_B  = int(B) - int(A)
        B_C = int(C) - int(B)
        
        if A_B >= B_C :
            print((A_B -1))
        else:
            print((B_C -1))
    except: 
        break    

