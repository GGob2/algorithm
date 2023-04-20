import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())

num_list = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    for j in combinations(num_list, i):
        if sum(j) == s:
            count += 1

print(count) 
