a, b = map(int, input().split())

num_list = list(map(int, input().split()))

while b > 0:
    num_list.sort()
    hap = num_list[0] + num_list[1]
    num_list[0]  = hap
    num_list[1]  = hap
    b -= 1

print(sum(num_list))
