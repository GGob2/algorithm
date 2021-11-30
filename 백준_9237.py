n = int(input())
tree_list = list(map(int, input().split()))

tree_list.sort(reverse=True)

for i in range(n):
    tree_list[i] = tree_list[i] + i + 1

print(max(tree_list) + 1)