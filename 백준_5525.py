import sys

input = sys.stdin.readline

n = int(input())
m = int(input())


s = input().rstrip()

find = n * "IO" + "I"

result = 0

for i in range(0, len(s)-2):
    
    if s[i] == "I":
        if s[i:i+len(find)] == find:
            result += 1
    else:
        continue

print(result)
