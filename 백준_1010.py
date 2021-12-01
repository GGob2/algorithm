import math

a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    print(math.factorial(c) // (math.factorial(b) * math.factorial(c-b)))
