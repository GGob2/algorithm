import re

def solution(new_id):
      
    # 1. 대문자 -> 소문자
    answer = new_id.lower()
    
    # 2. 알파벳 소문자, 숫자, -, _, . 제외한 모든 문자 제거
    pattern = r'[^a-z0-9-_.]'
    answer = re.sub(pattern, '', answer)
    
    # 3. 마침표 2번 이상 연속된 부분을 하나의 마침표로 치환
    pattern2 = r'\.{2,}'
    answer = re.sub(pattern2, '.', answer)
            
    # 4. 마침표가 처음이나 끝에 위치한다면 제거
    if len(answer) >= 1 and answer[0] == ".":
        answer = answer[1:]
    
    if len(answer) >= 1 and answer[-1] == ".":
        answer = answer[:-1]

    # 5. 빈 문자열이라면, a를 대입
    if answer == "":
        answer = 'a'
    
    # 6. 길이가 16자 이상이라면, 첫 15개 문자를 제외한 나머지 문자 제거, 
    #    마침표가 끝에 위치한다면 마침표 제거
    if len(answer) >= 16:
        answer = answer[:15]
    
    if answer[-1] == ".":
        answer = answer[:-1]
    
    # 7. 길이가 2자 이하라면, 마지막 문자 복사
    if len(answer) <= 2:
        while(len(answer) < 3):
            answer += answer[-1]
    
    return answer