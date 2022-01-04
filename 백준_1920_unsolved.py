import sys

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

m = int(input())

find_list = list(map(int, sys.stdin.readline().split()))

result = []

for i in find_list:
    if num_list.count(i) == 0:
        result.append("0")
    else:
        result.append("1")

print("\n".join(result[:]))