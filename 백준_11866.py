from collections import deque

a, b = map(int, input().split())
print('<', end ='')
deq = deque(i + 1 for i in range(a))
result = []

for i in range(a):
    deq.rotate(-b + 1)
    result.append(deq.popleft())

for j in range(len(result)-1):
    print("%d, "%result[j], end="")
print(result[-1], end="")
print('>')