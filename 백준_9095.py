n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))

dp = [0 for _ in range(max(num_list)+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for k in range(4, max(num_list)+1):
    dp[k] = dp[k-1] + dp[k-2] + dp[k-3]

for j in num_list:
    print(dp[j])



