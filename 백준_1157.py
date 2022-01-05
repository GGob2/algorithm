sentence = input().upper()

sentence_dict = {}

for i in range(len(sentence)):
    if sentence[i] in sentence_dict:
        sentence_dict[sentence[i]] += 1
    else:
        sentence_dict[sentence[i]] = 1

max_value = max(sentence_dict.values())
result = []

for key, value in sentence_dict.items():
    if max_value == value:
        result.append(key)

if len(result) != 1:
    print("?")
else:
    print(result[0])

