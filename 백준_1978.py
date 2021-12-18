n = int(input())
numbers = map(int, input().split())

prime = 0

for i in numbers:
    is_not_prime = False
    
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                is_not_prime = True
        
        if is_not_prime == False:
            prime+=1
print(prime)