n = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

result = 0

for i in range(n):
    result += min(A_list) * max(B_list)
    A_list.pop(A_list.index(min(A_list)))
    B_list.pop(B_list.index(max(B_list)))

print(result)

