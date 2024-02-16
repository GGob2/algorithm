import sys

input = sys.stdin.readline

n = int(input())

work = []

for i in range(n):
    time, price = map(int, input().split())

    work.append([time, price])

dp = [0 for i in range(n+1)]

for i in range(n):
    for j in range(i + work[i][0], n+1):
        if dp[j] < dp[i] + work[i][1]:
            dp[j] = dp[i] + work[i][1]

print(dp[-1])