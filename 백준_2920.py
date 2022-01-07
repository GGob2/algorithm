num_list = list(map(int, input().split()))
result = ""
num_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
num_list2 = [8, 7, 6, 5, 4, 3 ,2, 1]

if num_list == num_list1:
    result = "ascending"
elif num_list == num_list2:
    result = "descending"
else:
    result = "mixed"

print(result)