t = int(input())
count_original = 0
count_reverse = 0

for i in range(t):
    num = int(input())
    if num == 1:
        count_original += 1
    else:
        count_reverse += 1

if count_original > count_reverse:
    print(count_reverse)
else:
    print(count_original)
