n, k = map(int, input().split())

result = 0

while bin(n).count('1') > k:
    temp =  (bin(n)[::-1].index('1'))
    result += 2 ** temp
    n +=  2 ** temp

print(result)    