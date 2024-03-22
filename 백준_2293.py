import sys

input = sys.stdin.readline

n, k = map(int, input().split())    # 동전의 수와 동전의 가치를 입력 받는다.

coins = []                          # DP 배열 선언

for i in range(n):                  # 동전의 수만큼, 리스트에 추가
    coins.append(int(input()))      # 리스트에 동전 넣기

coin = [0] * (k+1)                  # k원을 만드는 데 필요한 동전의 경우의 수 저장을 위한 배열
coin[0] = 1                         # 1원을 만드는데는 1원 1개 필요 

for i in coins:                     # 모든 코인에 대해
    for k in range(i, k+1):         # 가능한 모든 경우의 수 추가
        coin[k] += coin[k-i]        # 경우의 수 더하기

print(coin[k])
