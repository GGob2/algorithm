def solution(s):
    answer = False
    
    stack = []
    
    for i in range(len(s)): 
        
        if s[i] == "(":
            stack.append("(")
        else:
            try:
                stack.pop()
            except:
                answer = False
                return answer
        
    if len(stack) == 0:
        answer = True
        
    return answer