n = int(input())

num_list = []

for i in range(n):
    num_list.append(int(input()))

dp = [0 for _ in range(max(num_list)+1)]

dp[1] = 1
dp[2] = 1
dp[3] = 1

for j in range(4, max(num_list)+1):
    dp[j] = dp[j-2] + dp[j-3]

for k in num_list:
    print(dp[k])


