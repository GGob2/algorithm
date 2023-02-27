from collections import deque
import sys
import heapq

input = sys.stdin.readline

n = int(input())

for i in range(n):
    T = int(input())

    max_heap, min_heap = [], []
    visit = [False] * T

    for j in range(T):
        cmd, num = input().split()

        if cmd == 'I':
            heapq.heappush(min_heap, (int(num), j))
            heapq.heappush(max_heap, ((-1 *int(num), j)))
            visit[j] = True

        elif cmd == "D" and num == str(-1):
            while min_heap and not visit[min_heap[0][1]]:
                heapq.heappop(min_heap)
            
            if min_heap:
                visit[min_heap[0][1]] = False
                heapq.heappop(min_heap)
        else:
            while max_heap and not visit[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visit[max_heap[0][1]] = False
                heapq.heappop(max_heap)
    
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if  min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
                                  