def solution(numbers, target):
    answer = 0
    leaves = [0] # 배열선언 
    
    for num in numbers:
        tmp = []
        
        for parent in leaves:   
            tmp.append(parent + num)    # bfs 가능한 모든 경우의 수 추가
            tmp.append(parent - num)
        leaves = tmp                    # 각 단계마다 가능한 경우의 수 갱신
    answer = leaves.count(target)
    
    return answer