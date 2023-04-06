import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for i in range(n):
    coins.append(int(input()))

min_coin = [10001] * (k+1)
min_coin[0] = 0

for coin in coins:
    for k in range(coin, k+1):
        min_coin[k] = min(min_coin[k], min_coin[k-coin]+1)

if min_coin[k] == 10001:
    print(0)
else:
    print(min_coin[k])
