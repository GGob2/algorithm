i = 1
while True:
        a, b, c = map(int, input().split())
        
        if a == 0 and b == 0 and c == 0:
            break
        
        result = (a * (c // b)) 
        result += min((c % b), a)  
        print("Case", str(i)+ ":", result)

        i += 1
    
    

        
