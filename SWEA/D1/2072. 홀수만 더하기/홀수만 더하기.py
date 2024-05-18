num = int(input())
result = []
for i in range(num):
    num_list = list(map(int, input().split()))
    temp = 0
    for j in num_list:
        if j % 2 != 0:
            temp += j

    result.append(temp)

for k in range(len(result)):
    print("#" + str(k+1), result[k])
