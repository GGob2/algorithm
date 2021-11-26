num = int(input())
max_value = 0
result = 0 

while True:
    max_value += 1
    result += max_value
    if result > num:
        break

print(max_value - 1)
