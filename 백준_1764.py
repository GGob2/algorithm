a, b = map(int, input().split())

name_list = {}

for i in range(a+b):
    name = input()
    
    if name in name_list:
        name_list[name] += 1
    else:
        name_list[name] = 1

result = []

for key, value in name_list.items():
    if value == 2:
        result.append(key)

result.sort()
print(len(result))
print("\n".join(result[:]))


