n = int(input())

result = []

for i in range(n):
    word = input()
    if word in result:
        continue
    else: 
        result.append(word)

result.sort(key=lambda x: (len(x), x))


print("\n".join(result[:]))
