import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(graph_dfs, v_dfs, visited_dfs):  # dfs 그래프, 시작점, 방문 확인 파라미터로 넘김
    visited_dfs[v_dfs] = True            # 현재 노드 방문 처리 
    print(v_dfs, end=" ")

    graph_dfs[v_dfs].sort()              # 작은 게 우선
    for k in graph_dfs[v_dfs]:           # 연결된 곳에서
        if not visited_dfs[k]:           # 방문 안한 곳이 있는지 확인
            
            dfs(graph_dfs, k, visited_dfs)  # 방문 안한 곳이 있으면 dfs 돌리기


def bfs(graph_bfs, v_bfs, visited_bfs):  # bfs 그래프, 시작점, 방문 확인 파라미터로 넘김
    
    queue = deque([v_bfs])               # 큐 생성
    visited_bfs = [False] * (n + 1)
    visited_bfs[v_bfs] = True            # 현재 노드 방문 처리
    
    while queue:                         

        v_bfs = queue.popleft()          # 큐에서 하나의 원소를 뽑아 출력
        print(v_bfs, end = ' ')

        for i in graph_bfs[v_bfs]:       # 연결된 노드 중
            if not visited_bfs[i]:       # 방문 하지 않은 곳이 있으면
                queue.append(i)          # 큐에 넣고
                visited_bfs[i] = True    # 방문 표시

n, m, start = map(int, input().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n + 1)]


for i in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

dfs(graph, start, visited)
print()
bfs(graph, start, visited)
