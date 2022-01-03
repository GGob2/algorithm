n = int(input())
result = []
for i in range(n):
    sentence = input()
    
    if len(sentence) % 2 != 0:
        result.append("NO")
        continue
    
    if sentence.count("(") != sentence.count(")"):
        result.append("NO")
        continue

    count = 0

    for j in sentence:
        if j == "(":
            count +=  1
        else:
            count -= 1
        
        if count == -1:
            result.append("NO")
            break
    
    if count == 0:
        result.append("YES")

print("\n".join(result[:]))
