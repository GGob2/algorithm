letter = list(input())
result = 1

# ord 함수 사용 안해도 문자열끼리 알아서 비교해줌.
for i in range(len(letter)-1):
    if ord(letter[i]) >= ord(letter[i+1]):
        result += 1

print(result)