n = int(input())
result = []

for i in range(n):
    start, end = map(int, input().split())
    result.append([start, end])

# lambda 함수를 이용해 리스트의 첫 번째 항목으로 정렬 후 
# lambda 함수를 이용해 리스트의 두 번째 항목으로 정렬
result.sort(key=lambda x: x[0])
result.sort(key=lambda x: x[1])

count = 1
end_time = result[0][1]

for j in range(1, n):
    if result[j][0] >= end_time:
        count += 1
        end_time = result[j][1]

print(count)