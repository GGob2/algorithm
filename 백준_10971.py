import sys
input = sys.stdin.readline

n = int(input())
price_list = []
ans = sys.maxsize
visit = [0 for _ in range(n)]

for i in range(n):
    price_list.append(list(map(int, input().split())))

def back(start, now, value, count):
    global ans

    if count == n:
        if price_list[now][start]:
            value += price_list[now][start]
            if ans > value: 
                ans = value
        return
    
    if value > ans:         # 이미 경로 크기가 커져버린 경우
        return
    
    for i in range(n):
        if not visit[i] and price_list[now][i]:
            visit[i] = 1
            back(start, i, value + price_list[now][i], count+1)
            visit[i] = 0

for i in range(n):
    visit[i] = 1
    back(i, i, 0, 1)
    visit[i] = 0

print(ans)
