n = int(input())
sentence = input()
result = 0

for i in range(n):
    result += (ord(sentence[i]) -96) * (31 ** i)

print(result % 1234567891)