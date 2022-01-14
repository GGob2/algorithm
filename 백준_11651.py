import sys
n = int(sys.stdin.readline())
result = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result.append([a, b])

result.sort(key=lambda x: (x[1], x[0]))



for j in range(n):
    print(result[j][0], result[j][1])