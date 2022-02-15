n = int(input())

people = []

for i in range(n):
    a, b = map(int, input().split())
    people.append([a, b])

for j in people:
    rank = 1
    for k in people:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank, end=" ")


    

