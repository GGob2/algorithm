b, c, d = map(int, input().split())

origin_price = 0
discount_price = 0

burger = list(map(int, input().split()))
side = list(map(int, input().split()))
beverage = list(map(int, input().split()))

origin_price += sum(burger) + sum(side) + sum(beverage)

burger.sort(reverse=True)
side.sort(reverse=True)
beverage.sort(reverse=True)    

set_index = min(len(burger), min(len(side), len(beverage)))

for m in range(set_index):
    discount_price += (burger[0] + side[0] + beverage[0]) * 0.9

    

for n in range(len(burger)):
    discount_price += burger[n]

for l in range(len(side)):
    discount_price += side[n]

for x in range(len(beverage)):
    discount_price += beverage[n]

print(origin_price)
print(int(discount_price))

