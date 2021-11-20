n, l, k = map(int, input().split())

q = list()
result = 0
diff_problem = 0
easy_problem = 0

for i in range(n):
    a, b = map(int, input().split())
    q.append([a, b])

for j in range(n):
    if q[j][1] <= l :
        diff_problem += 1
        

    elif q[j][0] <= l:
        easy_problem += 1

if diff_problem + easy_problem <= k:
    result += (diff_problem * 140) + (easy_problem * 100)
elif diff_problem + easy_problem > k:
    if diff_problem >= k:
        result += k * 140
    else:
        result += (diff_problem * 140) + ((k-diff_problem) * 100)


    
print(result)
