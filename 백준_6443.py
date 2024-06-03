import sys
input = sys.stdin.readline

def back(cnt):
    # print(cnt, ans)
    if cnt == len(string):  # 길이가 되었으면
        print("".join(ans)) # 출력
        return
        
    for k in visit:         # 
        if visit[k] :       # 딕셔너리에 값이 있으면
            visit[k] -= 1   # 빼고, ans에 추가
            ans.append(k)
            
            back(cnt+1)     # 재귀
            
            visit[k] += 1   # 같은 글자가 몇 개 있는지 파악하기 위해
            ans.pop()

n = int(input())            # 경우의 수 입력 받기

for i in range(n):          
    string = sorted(list(input().rstrip()))
    visit = {}
    ans = []            # 출력에 필요한 배열

    for i in string:    # 알파벳의 개수를 입력
        if i in visit:
            visit[i] += 1    
        else:
            visit[i] = 1
    
    back(0)                 