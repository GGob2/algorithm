import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

m = int(input())
find_list = list(map(int, sys.stdin.readline().split()))

def binary_search(target_num):
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == target_num:
            return True
        
        if target_num < num_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

for i in find_list:
    if binary_search(i):
        print(1)
    else:
        print(0)