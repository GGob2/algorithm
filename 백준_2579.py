n = int(input())

stairs = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

for k in range(3, n):
    dp[k] = max(dp[k-3] + stairs[k-1] + stairs[k], dp[k-2] + stairs[k])

print(dp[n-1])

