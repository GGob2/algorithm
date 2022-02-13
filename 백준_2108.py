from collections import Counter
import sys

n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    numbers.append(int(sys.stdin.readline()))

print(round(sum(numbers)/n))
numbers.sort()
print(numbers[int((n-1) /2)])

count_num = Counter(numbers).most_common()

if len(count_num) > 1 and count_num[0][1] == count_num[1][1]:
    print(count_num[1][0])
else:
    print(count_num[0][0])

print(max(numbers) - min(numbers))