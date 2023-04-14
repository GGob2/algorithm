def solution(priorities, location):
    answer=[]
    
    result = [0 for _ in range(len(priorities))]
    result[location] = 1
    i = 0

    while True:
        if priorities[0] == max(priorities):
            i += 1
            
            if result[0] != 1:
                priorities.pop(0)
                result.pop(0)
            else:
                answer = i
                break
        else:
            priorities.append(priorities[0])
            result.append(result[0])
            priorities.pop(0)
            result.pop(0)
            
    return answer 
solution([2,1,3,2], 2)