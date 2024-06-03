# 입력 받기
num = int(input())

result = []

# 문자열 입력 받기
for i in range(num):
    char_list_len = int(input())
    char_list = input()
    cnt = 0
    flag = 0
    
    # 조건을 만족할 때 까지
    while flag == 0:
    
        if 'ab' in char_list or  'ba' in char_list or 'aa' in char_list:
            char_list = char_list.replace('a', '', 1)
            cnt += 1
            continue

        if 'bb' in char_list:
            char_list = char_list.replace('b', '', 1)
            cnt += 1
            continue

        result.append(cnt)
        flag = 1

# 결과 출력
for k in range(len(result)):
    print("#" + str(k+1), result[k])
