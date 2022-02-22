import sys

n, m = map(int, sys.stdin.readline().split())

poketmon = {}

for i in range(1, n + 1):
    poket_name = sys.stdin.readline().strip()
    poketmon[i] = poket_name
    poketmon[poket_name] = i

for j in range(m):
    question = sys.stdin.readline().strip()
    
    try:
        print(poketmon[int(question)])
    except:
        print(poketmon[question])
