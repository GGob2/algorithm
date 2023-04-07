import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for i in range(n):
    coins.append(int(input()))

coin = [0] * (k+1)
coin[0] = 1

for i in coins:
    for k in range(i, k+1):
        coin[k] += coin[k-i]

print(coin[k])
