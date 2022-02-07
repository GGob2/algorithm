t = int(input())

for i in range(t):
    a = int(input())
    b = int(input())

    people = [x for x in range(1, b+1)]
                                
    for j in range(a):
        for k in range(1, b):
            people[k] += people[k-1]

    print(people[-1])