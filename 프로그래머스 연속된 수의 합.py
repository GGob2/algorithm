def solution(num, total):
    answer = []
    
    temp = int(total / num) 
    
    if num % 2 == 1:
        for i in range(temp-(int(num/2)), temp+(int(num/2))+1):
            answer.append(i)        
    
    else:
        for j in range(temp-(int(num/2)-1), temp+(int(num/2))+1):
            answer.append(j)
            
    answer.sort()    
    return answer