sentence = input().split('-')
number = []

for i in sentence:
    temp = 0
    t = i.split('+')
    for j in t:
        temp += int(j)
    number.append(temp)

first_value = number[0]

for k in range(1, len(number)):
    first_value -= number[k]

print(first_value)
