n, r = map(int, input().split())

all_people = []
no_people = []

for i in range(n):
    all_people.append(0)

people = list(map(int, input().split()))

if n == r:
    print("*")
else:
    for j in people:
        all_people[j-1] = 1


    for k in range(n):
        if all_people[k] != 1:
            no_people.append(k+1)

    no_people.sort()

    for y in range(len(no_people)):
        print(no_people[y], end=" ")



