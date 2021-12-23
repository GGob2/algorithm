n = int(input())

num_list = list(map(int, input().split()))

num_list.sort(reverse=True)
score = 0
while len(num_list) > 1:
    a = num_list.pop(0)
    b = num_list.pop(0)
    score += a * b

    num_list.append(a+b)

print(score)