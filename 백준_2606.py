n = int(input())
m = int(input())

s = [[0] * n for i in range(n)] 
v = [0 for i in range(n)]


for i in range(m):
    a, b = map(int, input().split())
    s[a-1][b-1] = 1
    s[b-1][a-1] = 1

def dfs(k):
    v[k] = 1
    for i in range(n):
        if s[k][i] == 1 and v[i] == 0:
            dfs(i)

count = 0
dfs(0)

for j in range(1, n):
    if v[j] == 1:
        count += 1

print(count)


