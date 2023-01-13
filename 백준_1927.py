import heapq
import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num = int(sys.stdin.readline())
    
    if num != 0:
        heapq.heappush(num_list, num)
    else:
        try:
            print(heapq.heappop(num_list))
        except:
            print(0)
    
    
