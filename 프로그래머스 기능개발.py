def solution(progresses, speeds):
    answer = []
    
    dates = [0 for _ in range(len(progresses))]
    
    for i in range(len(progresses)):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            dates[i] += 1
    
    
    while dates:
        value = dates.pop(0)
        count = 1
        
        if dates and value >= dates[0]:
            dates.pop(0)
            count += 1
        
        answer.append(count)
        
    return answer
