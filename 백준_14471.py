n, m = map(int, input().split())
result = 0
check_list = []
min_money = []

for i in range(m):
    a, b = map(int, input().split())
    check_list.append([a, b])

    if check_list[i][0] >= n:
        result += 1
    else:
        min_money.append(check_list[i][1] - n)
        
min_money = sorted(min_money)

if result >= m-1:
    print(0)
else:
    print(sum(min_money[:m-result-1]))