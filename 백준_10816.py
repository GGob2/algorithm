import sys
a = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

b = int(input())
num_list_v2 = list(map(int, sys.stdin.readline().split()))

result = {}

for i in num_list:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

print(' '.join(str(result[k]) if k in result else '0' for k in num_list_v2))





