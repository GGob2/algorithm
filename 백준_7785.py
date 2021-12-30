import sys

n = int(input())
p_list = []
for i in range(n):
    name, status = sys.stdin.readline().split()
    if status == "enter":
        p_list.append(name)
    else:
        p_list.pop(p_list.index(name))
    
p_list.sort(reverse=True)
print('\n'.join(p_list[:]))

