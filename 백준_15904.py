n = input()

letter = ["U", "C", "P", "C"]
cnt = 0 
for a in letter:
    if a in n:
        cnt += 1
        n = n[n.index(a) +1:]
    else:
        print("I hate UCPC")
        break
if cnt == 4:
    print("I love UCPC")

