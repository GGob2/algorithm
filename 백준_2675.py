t = int(input())
for i in range(t):
    a, b = input().split()
    result = ""
    for i in b:
        result += i * int(a)
    print(result)
