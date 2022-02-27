n = int(input())
dP = [0] * (n + 1)	

for i in range(2, n + 1):
    dP[i] = dP[i - 1] + 1
    if i % 3 == 0:
        dP[i] = min(dP[i], dP[i // 3] + 1)	
    if i % 2 == 0:
        dP[i] = min(dP[i], dP[i // 2] + 1)
print(dP[n])