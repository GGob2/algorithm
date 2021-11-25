n, x = map(int, input().split())

result = list(map(int, input().split()))

value = []
for i in result:
    if i < x:
        value.append(i)

for k in value:
    print(k, end=" ")

