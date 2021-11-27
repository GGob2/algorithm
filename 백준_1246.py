n, m = map(int, input().split())
customer_price = []
result = 0
count = 0
customer_len = 0
for i in range(m):
    customer_price.append(int(input()))

customer_price.sort()

for j in range(m):
    customer_len = min(m-j, n)
    
    if count < customer_price[j] * customer_len:
        
        result = customer_price[j]
        count = customer_price[j] * customer_len


print(result, count) 
        
