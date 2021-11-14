n = int(input())
distance = list(map(int, input().split()))
distance.sort()


print(sum(distance[:n-1]))