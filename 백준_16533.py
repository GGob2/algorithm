n = int(input())
card = list(map(int, input().split()))
count = 1

for i in range(len(card)-1):
    if card[i] >= card[i+1]:
        continue
    else:
        count += 1

print(count)