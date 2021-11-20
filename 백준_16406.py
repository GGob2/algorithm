n = int(input())
my_answer =  input()
friend_answer = input()
same_answer = 0


for i in range(len(my_answer)):
    if my_answer[i] == friend_answer[i]:
        same_answer += 1

print(len(my_answer) - abs((same_answer - n)))