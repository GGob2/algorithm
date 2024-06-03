import sys

input = sys.stdin.readline

n, k = map(int, input().split())                    # 동전 수와 목표 값 탐색

coins = []

for i in range(n):
    coins.append(int(input()))                      # 동전 내용 추가

min_coin = [10001] * (k+1)                          # K의 최대에 맞게 10001개 배열 선언
min_coin[0] = 0                                     # 최소 동전 개수 0개 설정

for coin in coins:                                  
    for k in range(coin, k+1):                              # ex) 5원을 만들기 위해 1원 5개 -> 5원 1개로 치환 가능 (k-coin) 
        min_coin[k] = min(min_coin[k], min_coin[k-coin]+1)  # 초기 값을 0으로 설정한 이유, min에 안걸리기 때문에

if min_coin[k] == 10001:                            # 불가능한 경우에는 min_coin[k]의 값이 10001 => -1 출력
    print(-1)                                       
else:
    print(min_coin[k])                              # 불가능하지 않은 경우, min_coin[k] 출력
