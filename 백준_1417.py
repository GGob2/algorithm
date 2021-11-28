n = int(input())

candidiate = [] 
result = 0


for i in range(n):
    candidiate.append(int(input()))


while True:
    if candidiate[0] != max(candidiate):
        candidiate[candidiate.index(max(candidiate))] -= 1
        candidiate[0] += 1
        result += 1
    else:
        break

for j in range(1, n):
    if candidiate[0] == candidiate[j]:
        candidiate[0] += 1
        result += 1

print(result)