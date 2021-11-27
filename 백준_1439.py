letter = input()
count = 0

for i in range(len(letter)-1):
    if letter[i] != letter[i+1]:
        count += 1
print((count+1)//2)