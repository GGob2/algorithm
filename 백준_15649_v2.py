import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

def back(num):				# 백트래킹을 위한 재귀 함수
    if len(result) == m:	# 길이가 m이면 출력
        print(' '.join(map(str, result))) 
        return
    
    for i in range(1, num+1):	# 사용 가능한 자연수 범위 내에서
        if i in result:			# 배열에 문자가 있으면 넘어감
            continue
       
        result.append(i)		# 결과에 넣고 
        back()					# 재귀가 끝나면
        result.pop()			# 다시 빼줌

back(n)