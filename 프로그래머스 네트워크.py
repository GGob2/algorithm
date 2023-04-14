def solution(n, computers):
    answer = 0
    queue = []
    visit = []

    for i in range(n):
        if i not in visit:
            queue.append(i)
            answer += 1
            
            while queue:
                now = queue.pop(0)

                for j in range(n):
                    if computers[now][j] == 1 and j not in visit:
                        visit.append(j)
                        queue.append(j)
    return answer