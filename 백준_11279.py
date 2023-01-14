import sys
import heapq

input = sys.stdin.readline

num_list = []

n = int(input())

for i in range(n):
    num = int(input())

    if num != 0:
        heapq.heappush(num_list, (-num, num))
    else:
        try:
            print(heapq.heappop(num_list)[1])
        except:
            print(0)

