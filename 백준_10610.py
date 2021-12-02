n = list(input())
isZero = True 

if n.count("0") == 0:
    isZero = False

sum = 0
for i in n:
    sum += int(i)
    
if sum % 3 == 0 and isZero == True:
    n.sort(reverse=True)
    print("".join(n))
else:
    print(-1)