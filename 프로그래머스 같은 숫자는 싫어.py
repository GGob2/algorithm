from collections import deque
def solution(arr):
    
    answer = [0]
    answer[0] = arr[0]
    
    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    
    return answer
