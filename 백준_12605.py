n = int(input())
k = 1
for i in range(n):
    sentence = input().split()
    print("Case #" + str(k)+ ": " +' '.join(sentence[::-1]))
    k += 1
