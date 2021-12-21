n = int(input())

rope = []

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
result = 0
for j in range(n):
    if rope[j] * (j+1) >= result:
        result = rope[j] * (j+1)
    
print(result)
