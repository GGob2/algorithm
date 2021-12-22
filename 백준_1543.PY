origin_sentence = input()

find_sentence = input()

result = 0

while True:
    index = origin_sentence.find(find_sentence)
    if index == -1:
        break

    result += 1
    origin_sentence = origin_sentence[index+len(find_sentence):]
    


print(result)

