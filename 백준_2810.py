T = int(input())
seat = list(input())
holder = 1
l_count = False

for i in range(T):
    if seat[i] == "S":
        holder += 1
    if seat[i] == "L":
        holder += 0.5
        l_count = True

if l_count == False:
    holder -=1

print(int(holder))

