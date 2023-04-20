import sys

input = sys.stdin.readline

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

def back(idx, temp_sum):
    global count
    
    if idx >= n:
        return
    
    temp_sum += num_list[idx]

    if temp_sum == s:
        count += 1

    back(idx+1, temp_sum)
    back(idx+1, temp_sum - num_list[idx])

back(0,0)
print(count)