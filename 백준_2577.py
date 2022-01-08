a = int(input())
b = int(input())
c = int(input())

temp = a * b * c

for i in range(0, 10):
    print(str(temp).count(str(i)))