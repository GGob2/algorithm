import sys
n = int(sys.stdin.readline())

result = [0] * 10001

for i in range(n):
    result[(int(sys.stdin.readline()))] += 1 
     
for j in range(10001):
    if result[j] != 0:
        
        for k in range(result[j]):
            print(j)