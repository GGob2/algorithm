T = int(input())
num = list(map(int, input().split()))
result = 0
next = 0

for i in range(T):
    if num[i] == 0 and next == 0:
        next = 1
        result += 1
    if num[i] == 1 and next == 1:
        next = 2
        result +=1
    if num[i] == 2 and next == 2:
        next = 0
        result += 1

print(result)