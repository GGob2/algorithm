a, b = map(int, input().split())
c = int(input())
basket = []

for i in range(c):
    basket.append(int(input()))

m = 0
end = b
start = 1

for _ in range(c):
    if end >= basket[_] and start <= basket[_]:
        continue
    elif end < basket[_]:
        m += basket[_] - end
        end = basket[_]
        start = basket[_] - (b - 1)
    
    elif start > basket[_]:
        m += start - basket[_]
        start = basket[_]
        end = basket[_] + (b - 1)

print(m)
