n, k = map(int, input().split())

sum_min = 0

for i in range(k):
    sum_min += int(input())

sum_max = sum_min

sum_min += (n-k) * -3
sum_max += (n-k) * 3

if sum_min / n  

print(round((sum_min / n), 1 ), round((sum_max / n ), 1))