n, k = map(int, input().split())
coin_value = []

for i in range(n):
    coin_value.append(int(input()))

diff = k // coin_value[0]
result = 0 

j = len(coin_value) - 1

while k > 0:
    if k // coin_value[j] != 0:
        diff = k // coin_value[j]
        k -= diff * coin_value[j]
        result += diff
    else:
        j = j-1
    if k == 0:
        break

print(result)