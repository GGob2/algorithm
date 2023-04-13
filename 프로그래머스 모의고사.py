def solution(answers):
    student_one = [1,2,3,4,5]
    student_two = [2,1,2,3,2,4,2,5]
    student_three = [3,3,1,1,2,2,4,4,5,5]
    
    student_score = [0, 0, 0] 
    
    for i in range(len(answers)):
        if answers[i] == student_one[i%5]:
            student_score[0] += 1

        if answers[i] == student_two[i%8]:
            student_score[1] += 1

        if answers[i] == student_three[i%10]:
            student_score[2] += 1
    
    print(student_score)
    answer = 0
    return answer
solution([1,3,2,4,2])