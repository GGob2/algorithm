def check(s, t):
    j = 0
    for i in range(len(t)):
        if t[i] == s[j]:
            j += 1
            if j == len(s):
                return "Yes"
    
    return "No"

while True:
    try: 
        s, t = input().split()
        print(check(s ,t))

    except:
        break