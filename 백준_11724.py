import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
count = 0
def dfs(v): 
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, n + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)

