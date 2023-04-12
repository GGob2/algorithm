import sys
sys.setrecursionlimit(10**6)                        # Recursion Error 방지
input = sys.stdin.readline

def dfs(node):
    visit[node] = True                              # 노드 방문 처리 (재방문 안하기 위해)

    for i in vil[node]:                             # 간선이 존재하는 모든 노드에 대해
        if not visit[i]:                            # 방문 안했으면 dfs 수행
            dfs(i)
            dp[node][0] += max(dp[i][0], dp[i][1])  # dp[node][0] : dp[node]가 우수마을이 아닌 경우, 자식 상태 중 큰 값 추가 
            dp[node][1] += dp[i][0]                 # dp[node][1] : dp[node]가 우수마을인 경우, 자식이 우수가 아닌 상태의 값 추가

n = int(input())

visit = [0 for _ in range(n+1)]                     # 방문 여부 배열
vil = [[] for _ in range(n+1)]                      # 인접 마을 배열

population = [0] + list(map(int, input().split()))  # 인구수를 받기 위한 배열, 계산 편의를 위해 [0]을 추가
dp = [[0, population[_]] for _ in range(n+1)]       # [우수마을이 아닌 경우, 우수마을인 경우]를 위한 dp 배열   


for i in range(n-1):                                
    a, b = map(int, input().split())
    vil[a].append(b)                                # 인접 마을 추가
    vil[b].append(a)

dfs(1)
print((lambda a, b : max(a, b))(dp[1][1], dp[1][0]))                      # dp[1]을 수행했으니, dp중 큰 값 출력 




                  

