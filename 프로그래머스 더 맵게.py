import heapq
def solution(scoville, K):
    
    heapq.heapify(scoville)
    answer = 0
    
    if scoville[0] >= K: # 최소 값이 7 이상인경우
        return answer    # 리턴

    while scoville[0] < K: # 최소 값이 7 이하인 경우에만
        if len(scoville) <= 1: # 배열의 길이가 짧은 경우 
            return -1          # 리턴
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
    
        heapq.heappush(scoville, first+(second*2)) 
        answer += 1
    
    return answer