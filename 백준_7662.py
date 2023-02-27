from collections import deque
import sys
import heapq

input = sys.stdin.readline

n = int(input())

for i in range(n):
    T = int(input())

    max_heap, min_heap = [], []    # 최대힙, 최소힙 선언
    visit = [False] * T            # 방문했는지 확인하기 위한 배열 선언

    for j in range(T):
        cmd, num = input().split()

        if cmd == 'I':
            heapq.heappush(min_heap, (int(num), j))       # 최소 힙에 삽입 (인덱스와 함께)
            heapq.heappush(max_heap, ((-1 *int(num), j))) # 최대 힙에 삽입
            visit[j] = True                               # visit[j] 가 True 면 양 쪽 모두 살아 있는 값

        elif cmd == "D" and num == str(-1):
            while min_heap and not visit[min_heap[0][1]]:  # visit[min_heap[0][1]]이 False인 경우 == 해당 노드가 삭제된 경우 (값이 삭제된 경우만 들어감)
                heapq.heappop(min_heap)                    # min_heap 에서도 해당 노드를 삭제
            
            if min_heap:                                   
                visit[min_heap[0][1]] = False              # visit[index] 에서 True를 False로 바꾸고 
                heapq.heappop(min_heap)                    # 최소값 삭제
        else:
            while max_heap and not visit[max_heap[0][1]]:  # visit[max_heap[0][1]]이 False인 경우 
                heapq.heappop(max_heap)                    # 이기 삭제된 값이므로 max_heap 에서도 삭제
            
            if max_heap:
                visit[max_heap[0][1]] = False              # visit[index] 에서 True를 False로 바꾸고
                heapq.heappop(max_heap)                    # 최대값 삭제
    
    while min_heap and not visit[min_heap[0][1]]:          # 결과를 내기 전 한번 다시 검토
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if  min_heap and max_heap:                              # 출력단
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
                                  